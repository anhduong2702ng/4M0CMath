const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const PNG = require('pngjs').PNG;

(async () => {
  const { default: pixelmatch } = await import('pixelmatch');
  const args = process.argv.slice(2);
  const htmlPath = args[0] ? path.resolve(args[0]) : path.resolve('../hybrid_export/presentation.html');

  if (!fs.existsSync(htmlPath)) {
      console.error(`HTML file not found: ${htmlPath}`);
      process.exit(1);
  }

  const browser = await chromium.launch();
  const page = await browser.newPage({
    viewport: { width: 960, height: 540 },
    deviceScaleFactor: 1
  });

  async function snapSlide(slideIdx, basename) {
      await page.goto(`file://${htmlPath}`);
      
      const maxStep = await page.evaluate((idx) => {
          currentSlideIdx = idx;
          const slide = slides[idx];
          return parseInt(slide.getAttribute('data-max-step') || 0);
      }, slideIdx);
      
      for (let step = 0; step <= maxStep; step++) {
          await page.evaluate((s) => {
              currentStep = s;
              updateView();
          }, step);
          
          await page.waitForTimeout(500);
          
          const suffix = maxStep > 0 ? `_step${step}` : '';
          const snapName = `${basename}${suffix}.png`;
          const currentImgPath = path.join(__dirname, 'current_' + snapName);
          const trueImgPath = path.join(__dirname, 'true_' + snapName);
          
          await page.screenshot({ path: currentImgPath });
          console.log(`Saved snapshot: ${currentImgPath}`);
          
          // Visual Regression Test
          if (fs.existsSync(trueImgPath)) {
              const img1 = PNG.sync.read(fs.readFileSync(trueImgPath));
              const img2 = PNG.sync.read(fs.readFileSync(currentImgPath));
              
              if (img1.width === img2.width && img1.height === img2.height) {
                  const diff = new PNG({ width: img1.width, height: img1.height });
                  const numDiffPixels = pixelmatch(img1.data, img2.data, diff.data, img1.width, img1.height, {threshold: 0.1});
                  
                  if (numDiffPixels > 0) {
                      const diffPath = path.join(__dirname, 'diff_' + snapName);
                      fs.writeFileSync(diffPath, PNG.sync.write(diff));
                      console.error(`[FAIL] ${snapName}: ${numDiffPixels} pixels differ. Diff saved to ${diffPath}`);
                  } else {
                      console.log(`[PASS] ${snapName} matches baseline.`);
                  }
              } else {
                  console.error(`[ERROR] Size mismatch for ${snapName}`);
              }
          } else {
              console.log(`[INFO] No baseline found for ${snapName}, setting current as baseline.`);
              fs.copyFileSync(currentImgPath, trueImgPath);
          }
      }
  }

  // Map of slide index (0-based) to name
  const testSlides = {
      3: 'slide_4',
      6: 'slide_7',
      7: 'slide_8',
      8: 'slide_9',
      11: 'slide_12',
      12: 'slide_13',
      22: 'slide_23'
  };

  for (const [idx, name] of Object.entries(testSlides)) {
      await snapSlide(parseInt(idx), name);
  }

  await browser.close();
})();

import fitz
import os
import shutil

PDFS = [
    ("inputdata/05092026/4M0. BTVN 05-09.pdf", "outputdata/05092026/images_btvn"),
    ("inputdata/05092026/4M0.NDBH 05-09 (2).pdf", "outputdata/05092026/images_ndbh_05"),
    ("inputdata/12092026/4M0. NDBH 12-09.pdf", "outputdata/12092026/images_ndbh_12"),
    ("inputdata/12092026/4M0.BTVN 12-09.pdf", "outputdata/12092026/images_btvn_12")
]

def extract_pdf(pdf_path, output_dir):
    print(f"Extracting {pdf_path} to {output_dir}...")
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir, exist_ok=True)
    
    doc = fitz.open(pdf_path)
    # zoom = 3 for high-res
    mat = fitz.Matrix(3, 3)
    
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap(matrix=mat)
        output_file = os.path.join(output_dir, f"page_{page_num + 1:02d}.png")
        pix.save(output_file)
        print(f"  Saved {output_file}")
    
    print("Done.\n")

if __name__ == "__main__":
    for pdf, out_dir in PDFS:
        extract_pdf(pdf, out_dir)

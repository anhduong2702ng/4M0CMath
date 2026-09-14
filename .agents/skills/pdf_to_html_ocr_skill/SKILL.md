---
name: PDF to HTML OCR (Data-driven)
description: Extract pages from a PDF to images, perform AI vision OCR to transcribe the text, and synthesize the results into an HTML file using a Python-based data-driven template approach to save tokens. Ensures responsive layout and sharp typography.
---

# PDF to HTML OCR Skill (Data-Driven Architecture)

When the user asks to convert a PDF or images into an HTML file using OCR, follow these steps to ensure structural consistency, avoid layout breaks ("vỡ font"), maintain sharp text, and guarantee mobile responsiveness:

1. **Extract/Prepare Images**
   - Check if `PyMuPDF` (fitz) is installed. If not, use the `run_command` tool to run `pip install pymupdf`.
   - Write and execute a short Python script via the `run_command` tool to extract the required pages from the target PDF as images (if starting from a PDF). Ensure extraction at high DPI (e.g., zoom=2 or 3) if possible to retain quality.

2. **Data-Driven Architecture Setup**
   - **Do not** write raw HTML for each page directly, as duplicating HTML boilerplate and inline CSS consumes excessive tokens and increases the risk of layout breakage.
   - Instead, create a central Python script (e.g., `manual_generator.py`).
   - Define a single global HTML `TEMPLATE` inside the script. 

3. **Mandatory CSS Rules (Responsiveness & Sharpness)**
   - To ensure text is sharp and clear, add the following to the `body` or `:root` CSS:
     ```css
     -webkit-font-smoothing: antialiased;
     -moz-osx-font-smoothing: grayscale;
     text-rendering: optimizeLegibility;
     ```
   - Use container query units (`cqw`) or viewport width (`vw`) combined with a fixed `aspect-ratio: 16 / 9` container for the desktop view, ensuring absolute visual fidelity to the original slides.
   - **Must be responsive**: Implement `@media (max-width: 768px)` to handle mobile displays. In this block, disable fixed aspect ratios (`aspect-ratio: auto; min-height: 100vh;`), convert grid layouts to a single column (`grid-template-columns: 1fr;`), and adjust padding and typography accordingly.

4. **Transcribe Images (OCR) & Semantic Layout**
   - Use the `view_file` tool to visually inspect each extracted image.
   - For each image, transcribe the text and layout logic as an HTML string literal and append it to an array/list in your Python script.
   - Formatting Rules:
     - Apply exact colors and font hierarchies as seen in the image.
     - Isolate components into reusable CSS classes defined in the global template.
     - **Important**: Do not skip or omit complex diagrams or background images that convey meaning. Reconstruct them using CSS Grid/Flexbox or embed the original image snippet precisely.

5. **Generation**
   - Run the Python script to map the data array into the global `TEMPLATE` and output a single `.html` file.
   - If using `utf-8` text from files, explicitly open files with `encoding='utf-8'` in Python to prevent `UnicodeEncodeError`.

6. **QA Verification (Mandatory Protocol)**
   Thay vì review cảm tính, bạn PHẢI thực hiện rà soát theo 4 bước chuẩn hóa sau đối với từng slide:

   *   **Bước 1: Visual Region Mapping (Lập bản đồ khu vực)**
       *   Chia slide gốc thành các khối thị giác (Khối tiêu đề, Khối nội dung trái, Khối nội dung phải, Footer...). Đếm số lượng khối.
       *   Đảm bảo HTML sinh ra có chính xác số lượng container tương ứng.
   *   **Bước 2: Data Completeness Check (Rà soát chống mất chữ - Chống Data Loss)**
       *   Lỗi phổ biến nhất của AI Vision là bỏ sót text nằm trong các hình hộp màu nền đậm (như thẻ màu đen/xanh).
       *   Lỗi phổ biến thứ hai là **rút gọn/diễn giải lại** (paraphrase) thay vì chép nguyên văn. Ví dụ: gốc viết "Cần ít chữ số nhất có thể, ưu tiên đưa các chữ số lớn (như 9) về hàng thấp" nhưng AI tự rút thành "Ít chữ số nhất, đưa chữ số lớn (9) về hàng thấp" — đúng ý nhưng mất từ ngữ gốc.
       *   *Hành động:* Quét mắt đọc từng câu trong ảnh gốc và đối chiếu 1-1 với HTML. Không được phép sót một câu nào dù là text siêu nhỏ. Phải giữ **nguyên văn** — không rút gọn, không diễn giải lại, không bỏ bớt từ.
   *   **Bước 3: Layout & Chart Fidelity (Chống Ảo giác Bố cục & Biểu đồ)**
       *   *Case Study (Lỗi Slide 04):* AI biến biểu đồ thanh ngang (Horizontal Bar Chart) thành một cái bảng 3 cột (grid-3), làm hỏng hoàn toàn ý nghĩa hình ảnh.
       *   *Hành động:* TUYỆT ĐỐI KHÔNG dùng text grid/table để thay thế cho biểu đồ (charts) hoặc sơ đồ (diagrams). Bạn phải dùng HTML/CSS (`width: %`, `flex`) để vẽ lại đúng hình dáng thanh biểu đồ, hoặc cắt ảnh gốc chèn vào nếu sơ đồ quá phức tạp.
   *   **Bước 4: Overflow & Fit Check (Chống tràn)**
       *   *Case Study (Lỗi Slide 08):* Nếu ảnh gốc có layout xếp chồng 4 cột trên 3 cột, đừng đoán mò tự gộp thành 2x2.
       *   Sử dụng Flexbox cho footer (`margin-top: auto`) và thu phóng `cqw` nội bộ để nhét vừa slide dày đặc vào container 16:9 mà không đẩy footer ra ngoài.
   
   Nếu phát hiện bất kỳ sự sai lệch nào, phải lập tức cập nhật lại script Python (data/template) và chạy lại.

7. **Reference Example**
   - Trong thư mục skill này có cung cấp sẵn thư mục `examples/` chứa file `manual_results.html`. Đây là file mẫu (Golden template) cho cấu trúc CSS `cqw`, grid, và typography đã được chuẩn hoá để tham khảo khi render PDF sang HTML.

8. **Cleanup & Delivery**
   - Provide the user with a clickable link to the final HTML file.

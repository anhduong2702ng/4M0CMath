import os
import json

TEMPLATE = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{TITLE}</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet">
    <style>
        :root {{
            /* Colors */
            --bg-body: #f8fafc;
            --bg-slide: #ffffff;
            
            --text-main: #334155;
            --text-dark: #0f172a;
            --text-blue: #2563eb;
            --text-orange: #ea580c;
            --text-gray: #64748b;
            --text-red: #ef4444;
            --text-green: #16a34a;
            
            /* Typography */
            --font-sans: 'Inter', sans-serif;
            --font-serif: 'Playfair Display', serif;
            
            /* Sizing via cqw */
            --padding-slide: 4cqw;
        }}

        body {{
            background-color: var(--bg-body);
            margin: 0;
            padding: 2vw;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 4vw;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
            text-rendering: optimizeLegibility;
        }}

        .slide {{
            width: 100%;
            max-width: 1400px;
            aspect-ratio: 16 / 9;
            container-type: inline-size;
            background-color: var(--bg-slide);
            box-shadow: 0 1cqw 3cqw rgba(0,0,0,0.1);
            position: relative;
            box-sizing: border-box;
            padding: var(--padding-slide);
            font-family: var(--font-sans);
            color: var(--text-main);
            overflow: hidden;
            display: flex;
            flex-direction: column;
            border-radius: 1cqw;
        }}

        /* Header Area */
        .slide-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 2cqw;
            border-bottom: 0.2cqw solid #e2e8f0;
            padding-bottom: 1cqw;
        }}
        .header-title {{
            font-size: 2cqw;
            font-weight: 700;
            color: var(--text-blue);
        }}
        .header-badge {{
            background-color: var(--text-blue);
            color: white;
            padding: 0.5cqw 1.5cqw;
            border-radius: 2cqw;
            font-size: 1.2cqw;
            font-weight: 600;
        }}

        /* Content Areas */
        .content-full {{
            flex: 1;
            display: flex;
            flex-direction: column;
        }}
        
        .grid-2-col {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 3cqw;
            flex: 1;
        }}

        .grid-3-col {{
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 2cqw;
            flex: 1;
        }}

        /* Typography */
        h1, h2, h3, h4, h5, h6 {{ margin: 0; color: var(--text-dark); }}
        
        .title-main {{
            font-size: 4cqw;
            font-weight: 800;
            margin-bottom: 2cqw;
            color: var(--text-dark);
            text-align: center;
        }}

        .text-lg {{ font-size: 2.5cqw; line-height: 1.4; }}
        .text-md {{ font-size: 1.8cqw; line-height: 1.5; }}
        .text-sm {{ font-size: 1.2cqw; line-height: 1.6; }}
        
        .text-center {{ text-align: center; }}
        
        .box-highlight {{
            background: #f1f5f9;
            border: 0.2cqw solid #cbd5e1;
            border-radius: 1cqw;
            padding: 2cqw;
        }}

        .box-blue {{ background: #eff6ff; border: 0.2cqw solid #bfdbfe; border-radius: 1cqw; padding: 2cqw; }}
        .box-orange {{ background: #fff7ed; border: 0.2cqw solid #fed7aa; border-radius: 1cqw; padding: 2cqw; }}
        .box-green {{ background: #f0fdf4; border: 0.2cqw solid #bbf7d0; border-radius: 1cqw; padding: 2cqw; }}
        
        .bold-blue {{ color: var(--text-blue); font-weight: bold; }}
        .bold-orange {{ color: var(--text-orange); font-weight: bold; }}
        .bold-green {{ color: var(--text-green); font-weight: bold; }}
        .bold-red {{ color: var(--text-red); font-weight: bold; }}

        /* Footer */
        .slide-footer {{
            margin-top: auto;
            padding-top: 1cqw;
            display: flex;
            justify-content: space-between;
            font-size: 1cqw;
            color: var(--text-gray);
            border-top: 0.1cqw solid #e2e8f0;
        }}

        /* Responsive Mobile Styles */
        @media (max-width: 768px) {{
            .slide {{
                aspect-ratio: auto;
                height: auto;
                min-height: 100vh;
                padding: 6vw;
                gap: 4vw;
                border-radius: 0;
            }}
            .grid-2-col, .grid-3-col {{ grid-template-columns: 1fr; gap: 4vw; }}
            .header-title {{ font-size: 5vw; }}
            .header-badge {{ font-size: 3.5vw; padding: 1.5vw 4vw; }}
            .title-main {{ font-size: 8vw; margin-bottom: 4vw; }}
            .text-lg {{ font-size: 6vw; }}
            .text-md {{ font-size: 5vw; }}
            .text-sm {{ font-size: 4vw; }}
            .slide-header {{ margin-bottom: 4vw; padding-bottom: 2vw; }}
            .box-highlight, .box-blue, .box-orange, .box-green {{ padding: 4vw; border-radius: 2vw; }}
            .slide-footer {{ font-size: 3vw; padding-top: 4vw; margin-top: 6vw; flex-direction: column; gap: 2vw; align-items: center; }}
            div[style*="font-size:"] {{ font-size: 5vw !important; line-height: 1.5 !important; }}
        }}
    </style>
</head>
<body>
{CONTENT}
</body>
</html>
"""

DATA = {
    "4M0_BTVN_05-09": {
        "title": "4M0. BTVN 05-09",
        "out_file": "outputdata/05092026/4M0_BTVN_05-09.html",
        "slides": [
            """
<div class="slide">
    <div class="slide-header">
        <div class="header-title">4M0. BTVN 05-09</div>
        <div class="header-badge">Trang 5</div>
    </div>
    <div class="content-full">
        <div class="title-main text-lg" style="text-align: left; margin-bottom: 1cqw;">C. Bài tập về nhà</div>
        <div class="title-main text-md" style="text-align: left;">I. Điền đáp án</div>
        <table style="width: 100%; border-collapse: collapse; margin-top: 2cqw; font-size: 1.5cqw;">
            <thead>
                <tr>
                    <th style="border: 1px solid #333; padding: 1cqw; text-align: center; background: #f1f5f9; width: 75%;">Đề bài</th>
                    <th style="border: 1px solid #333; padding: 1cqw; text-align: center; background: #f1f5f9; width: 25%;">TRẢ LỜI</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style="border: 1px solid #333; padding: 1cqw;"><b>Câu 1.</b> Nêu giá trị của chữ số 5 trong số sau: 5 689 903</td>
                    <td style="border: 1px solid #333; padding: 1cqw; text-align: center; color: var(--text-red); font-family: cursive;">5 000 000</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #333; padding: 1cqw;"><b>Câu 2.</b> Số lớn nhất trong dãy số 1904094; 193409670; 93023406; 9312901 là:</td>
                    <td style="border: 1px solid #333; padding: 1cqw; text-align: center; color: var(--text-red); font-family: cursive;">193 409 670</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #333; padding: 1cqw;"><b>Câu 3.</b> Số nhỏ nhất trong dãy số 1198491; 1198409; 119842994; 1192130 là:</td>
                    <td style="border: 1px solid #333; padding: 1cqw; text-align: center; color: var(--text-red); font-family: cursive;">1192 130</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #333; padding: 1cqw;"><b>Câu 4.</b> Một số tự nhiên có chữ số hàng cao nhất thuộc hàng chục triệu. Hỏi số tự nhiên đó có bao nhiêu chữ số?</td>
                    <td style="border: 1px solid #333; padding: 1cqw; text-align: center; color: var(--text-red); font-family: cursive;">8 chữ số</td>
                </tr>
            </tbody>
        </table>
    </div>
    <div class="slide-footer">
        <span>Câu lạc bộ Toán học Muôn màu</span>
        <span>Trang 5</span>
    </div>
</div>
            """,
            """
<div class="slide">
    <div class="slide-header">
        <div class="header-title">4M0. BTVN 05-09</div>
        <div class="header-badge">Trang 6</div>
    </div>
    <div class="content-full">
        <table style="width: 100%; border-collapse: collapse; font-size: 1.2cqw;">
            <tbody>
                <tr>
                    <td style="border: 1px solid #333; padding: 1cqw;"><b>Câu 5.</b> Viết số gồm: 3 triệu, 5 chục nghìn, 5 trăm, 2 chục và 7 đơn vị.</td>
                    <td style="border: 1px solid #333; padding: 1cqw; text-align: center; color: var(--text-red); font-family: cursive; width: 25%;">3 050 527</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #333; padding: 1cqw;"><b>Câu 6.</b> Nam nói: "số 165 gồm 15 chục và 15 đơn vị". Nam nói đúng hay sai?</td>
                    <td style="border: 1px solid #333; padding: 1cqw; text-align: center; color: var(--text-red); font-family: cursive;">Đúng</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #333; padding: 1cqw;"><b>Câu 7.</b> Số liền sau số nhỏ nhất có 7 chữ số là số nào?</td>
                    <td style="border: 1px solid #333; padding: 1cqw; text-align: center; color: var(--text-red); font-family: cursive;">1 000 001</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #333; padding: 1cqw;"><b>Câu 8.</b> Số tự nhiên X là số nào, biết:<br>X = 5 x 100 000 + 8 x 100 + 9</td>
                    <td style="border: 1px solid #333; padding: 1cqw; text-align: center; color: var(--text-red); font-family: cursive;">500 809</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #333; padding: 1cqw;"><b>Câu 9.</b> Điền dấu >, <, = thích hợp vào chỗ chấm:<br>
                    a) 120 432 .... 99 423 &nbsp;&nbsp;&nbsp;&nbsp; b) 233 646 .... 233 746 &nbsp;&nbsp;&nbsp;&nbsp; c) 678 897 ..... 678 889</td>
                    <td style="border: 1px solid #333; padding: 1cqw; text-align: center; color: var(--text-red); font-family: cursive;">a) > <br> b) < <br> c) ></td>
                </tr>
                <tr>
                    <td style="border: 1px solid #333; padding: 1cqw;"><b>Câu 10.</b> Viết chữ số thích hợp vào chỗ chấm:<br>
                    a) 948 ...68 < 948 167 &nbsp;&nbsp;&nbsp;&nbsp; b) 2 608 608 < 2 60... 000 + 608</td>
                    <td style="border: 1px solid #333; padding: 1cqw; text-align: center; color: var(--text-red); font-family: cursive;">a) 0 <br> b) 9</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #333; padding: 1cqw;"><b>Câu 11.</b> Số "Hai trăm linh năm tỉ" được viết là:</td>
                    <td style="border: 1px solid #333; padding: 1cqw; text-align: center; color: var(--text-red); font-family: cursive;">205.000.000.000</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #333; padding: 1cqw;"><b>Câu 12.</b> Dưới đây là ước tính dân số của các thành phố lớn nhất thế giới. Sắp xếp thứ tự các thành phố theo dân số giảm dần (người).<br>
                    <div style="display: flex; gap: 2cqw;">
                        <div>Mexico: 22 843 550<br>New York: 22 310 740<br>Shanghai: 16 708 510<br>London: 12 412 330</div>
                        <div>Cairo: 15 837 460<br>Mumbai: 19 463 950<br>Tokyo: 35 521 740</div>
                    </div>
                    </td>
                    <td style="border: 1px solid #333; padding: 1cqw; text-align: center; color: var(--text-red); font-family: cursive;">Tokyo<br>Mexico<br>New York<br>Mumbai<br>Shanghai<br>Cairo<br>London</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #333; padding: 1cqw;"><b>Câu 13.</b> Viết các số tự nhiên chẵn thoả mãn:<br>
                    a. Lớn nhất và có chữ 5 số.<br>
                    b. Lớn nhất và có 4 chữ số khác nhau.<br>
                    c. Bé nhất và có năm chữ số.<br>
                    d. Bé nhất và có năm chữ số khác nhau.</td>
                    <td style="border: 1px solid #333; padding: 1cqw; text-align: center; color: var(--text-red); font-family: cursive;">a) 99998<br>b) 9876<br>c) 10000<br>d) 10234</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #333; padding: 1cqw;"><b>Câu 13.</b> Viết số tự nhiên lớn nhất có bốn chữ số và tổng các chữ số là 18.</td>
                    <td style="border: 1px solid #333; padding: 1cqw; text-align: center; color: var(--text-red); font-family: cursive;">9900</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #333; padding: 1cqw;"><b>Câu 14.</b> Cho số 205 316 795. Xóa đi năm chữ số, giữ nguyên thứ tự các chữ số còn lại để được số tự nhiên:<br>
                    a. Bé nhất. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; b. Lớn nhất.</td>
                    <td style="border: 1px solid #333; padding: 1cqw; text-align: center; color: var(--text-red); font-family: cursive;">a) 01675<br>b) 6795</td>
                </tr>
            </tbody>
        </table>
    </div>
    <div class="slide-footer">
        <span>Câu lạc bộ Toán học Muôn màu</span>
        <span>Trang 6</span>
    </div>
</div>
            """,
            """
<div class="slide">
    <div class="slide-header">
        <div class="header-title">4M0. BTVN 05-09</div>
        <div class="header-badge">Trang 7</div>
    </div>
    <div class="content-full">
        <div class="title-main text-lg" style="text-align: left; margin-bottom: 1cqw;">II. Tự luận</div>
        <div class="text-md" style="margin-bottom: 1cqw;"><b>Bài 15.</b> Điền số thích hợp vào chỗ chấm:</div>
        
        <table style="width: 100%; border-collapse: collapse; font-size: 1.2cqw; text-align: center; margin-bottom: 2cqw;">
            <thead>
                <tr>
                    <th rowspan="2" style="border: 1px solid #333; padding: 0.5cqw;">Số</th>
                    <th colspan="3" style="border: 1px solid #333; padding: 0.5cqw;">Lớp triệu</th>
                    <th colspan="3" style="border: 1px solid #333; padding: 0.5cqw;">Lớp nghìn</th>
                    <th colspan="3" style="border: 1px solid #333; padding: 0.5cqw;">Lớp đơn vị</th>
                </tr>
                <tr>
                    <th style="border: 1px solid #333; padding: 0.5cqw;">Hàng trăm triệu</th>
                    <th style="border: 1px solid #333; padding: 0.5cqw;">Hàng chục triệu</th>
                    <th style="border: 1px solid #333; padding: 0.5cqw;">Hàng triệu</th>
                    <th style="border: 1px solid #333; padding: 0.5cqw;">Hàng trăm nghìn</th>
                    <th style="border: 1px solid #333; padding: 0.5cqw;">Hàng chục nghìn</th>
                    <th style="border: 1px solid #333; padding: 0.5cqw;">Hàng nghìn</th>
                    <th style="border: 1px solid #333; padding: 0.5cqw;">Hàng trăm</th>
                    <th style="border: 1px solid #333; padding: 0.5cqw;">Hàng chục</th>
                    <th style="border: 1px solid #333; padding: 0.5cqw;">Hàng đơn vị</th>
                </tr>
            </thead>
            <tbody style="color: var(--text-red); font-family: cursive;">
                <tr>
                    <td style="border: 1px solid #333; padding: 0.5cqw; color: #333; font-family: sans-serif;">58 956</td>
                    <td style="border: 1px solid #333;">0</td><td style="border: 1px solid #333;">0</td><td style="border: 1px solid #333;">0</td>
                    <td style="border: 1px solid #333;">0</td><td style="border: 1px solid #333;">5</td><td style="border: 1px solid #333;">8</td>
                    <td style="border: 1px solid #333;">9</td><td style="border: 1px solid #333;">5</td><td style="border: 1px solid #333;">6</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #333; padding: 0.5cqw; color: #333; font-family: sans-serif;">466 714</td>
                    <td style="border: 1px solid #333;">0</td><td style="border: 1px solid #333;">0</td><td style="border: 1px solid #333;">0</td>
                    <td style="border: 1px solid #333;">4</td><td style="border: 1px solid #333;">6</td><td style="border: 1px solid #333;">6</td>
                    <td style="border: 1px solid #333;">7</td><td style="border: 1px solid #333;">1</td><td style="border: 1px solid #333;">4</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #333; padding: 0.5cqw; color: #333; font-family: sans-serif;">3 548 726</td>
                    <td style="border: 1px solid #333;">0</td><td style="border: 1px solid #333;">0</td><td style="border: 1px solid #333;">3</td>
                    <td style="border: 1px solid #333;">5</td><td style="border: 1px solid #333;">4</td><td style="border: 1px solid #333;">8</td>
                    <td style="border: 1px solid #333;">7</td><td style="border: 1px solid #333;">2</td><td style="border: 1px solid #333;">6</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #333; padding: 0.5cqw; color: #333; font-family: sans-serif;">65 736 981</td>
                    <td style="border: 1px solid #333;">0</td><td style="border: 1px solid #333;">6</td><td style="border: 1px solid #333;">5</td>
                    <td style="border: 1px solid #333;">7</td><td style="border: 1px solid #333;">3</td><td style="border: 1px solid #333;">6</td>
                    <td style="border: 1px solid #333;">9</td><td style="border: 1px solid #333;">8</td><td style="border: 1px solid #333;">1</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #333; padding: 0.5cqw; color: #333; font-family: sans-serif;">729 674 543</td>
                    <td style="border: 1px solid #333;">7</td><td style="border: 1px solid #333;">2</td><td style="border: 1px solid #333;">9</td>
                    <td style="border: 1px solid #333;">6</td><td style="border: 1px solid #333;">7</td><td style="border: 1px solid #333;">4</td>
                    <td style="border: 1px solid #333;">5</td><td style="border: 1px solid #333;">4</td><td style="border: 1px solid #333;">3</td>
                </tr>
            </tbody>
        </table>

        <div class="text-md" style="margin-bottom: 1cqw;"><b>Bài 16.</b> Cho biết: Một nghìn triệu gọi là một tỉ. Viết vào chỗ trống.</div>
        <table style="width: 100%; border-collapse: collapse; font-size: 1.4cqw; text-align: center; margin-bottom: 2cqw;">
            <thead>
                <tr>
                    <th style="border: 1px solid #333; padding: 1cqw; background: #f1f5f9; width: 30%;">Viết</th>
                    <th style="border: 1px solid #333; padding: 1cqw; background: #f1f5f9; width: 70%;">Đọc</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style="border: 1px solid #333; padding: 1cqw;">2 000 000 000</td>
                    <td style="border: 1px solid #333; padding: 1cqw;">Hai tỉ</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #333; padding: 1cqw;">5 000 000 000</td>
                    <td style="border: 1px solid #333; padding: 1cqw; color: var(--text-red); font-family: cursive;">Năm tỉ</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #333; padding: 1cqw;">425 000 000 000</td>
                    <td style="border: 1px solid #333; padding: 1cqw; color: var(--text-red); font-family: cursive;">Bốn trăm hai mươi lăm tỉ</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #333; padding: 1cqw; color: var(--text-red); font-family: cursive;">790.000.000.000</td>
                    <td style="border: 1px solid #333; padding: 1cqw;">Bảy trăm chín mươi tỉ</td>
                </tr>
            </tbody>
        </table>
        
        <div class="text-md" style="margin-bottom: 1cqw;"><b>Bài 17.</b> Trong số 738 926:</div>
        <ul style="font-size: 1.4cqw; line-height: 1.6;">
            <li>Chữ số 7 ở hàng <span style="color: var(--text-red); font-family: cursive;">trăm nghìn</span>, có giá trị là <span style="color: var(--text-red); font-family: cursive;">700 000</span> và thuộc lớp <span style="color: var(--text-red); font-family: cursive;">nghìn</span></li>
            <li>Chữ số 9 ở hàng <span style="color: var(--text-red); font-family: cursive;">trăm</span>, có giá trị là <span style="color: var(--text-red); font-family: cursive;">900</span> và thuộc lớp <span style="color: var(--text-red); font-family: cursive;">đơn vị</span></li>
        </ul>
        
        <div class="text-md" style="margin-top: 2cqw;"><b>Bài 18.</b> Viết các số sau:</div>
        <ul style="font-size: 1.4cqw; line-height: 1.6; list-style-type: none; padding-left: 0;">
            <li>a. Chín triệu một trăm chín mươi hai nghìn ba trăm: <span style="color: var(--text-red); font-family: cursive;">9 192 300</span></li>
            <li>b. Bảy mươi tám triệu chín trăm mười bảy nghìn không trăm linh sáu: <span style="color: var(--text-red); font-family: cursive;">78 917 006</span></li>
        </ul>
    </div>
    <div class="slide-footer">
        <span>Câu lạc bộ Toán học Muôn màu</span>
        <span>Trang 7</span>
    </div>
</div>
            """,
            """
<div class="slide">
    <div class="slide-header">
        <div class="header-title">4M0. BTVN 05-09</div>
        <div class="header-badge">Trang 8</div>
    </div>
    <div class="content-full">
        <ul style="font-size: 1.4cqw; line-height: 1.6; list-style-type: none; padding-left: 0; margin-bottom: 2cqw;">
            <li>c. Năm mươi chín triệu bảy trăm tám mươi hai nghìn chín trăm linh năm: <span style="color: var(--text-red); font-family: cursive;">59 782 905</span></li>
            <li>d. Chín trăm triệu không trăm linh ba nghìn tám trăm bốn mươi hai: <span style="color: var(--text-red); font-family: cursive;">900 003 842</span></li>
        </ul>

        <div class="text-md" style="margin-bottom: 1cqw;"><b>Bài 19.</b> Viết số, biết số đó gồm:</div>
        <ul style="font-size: 1.4cqw; line-height: 1.6; list-style-type: none; padding-left: 1cqw;">
            <li>a. 9 triệu, 6 trăm nghìn, 3 chục nghìn, 5 trăm, 9 chục và 9 đơn vị: <span style="color: var(--text-red); font-family: cursive;">9 630 599</span></li>
            <li>b. 6 trăm triệu, 7 triệu, 3 trăm nghìn, 2 nghìn và 17 đơn vị: <span style="color: var(--text-red); font-family: cursive;">607 302 017</span></li>
        </ul>

        <div class="text-md" style="margin-top: 2cqw; margin-bottom: 1cqw;"><b>Bài 20.</b> Viết các số có hai chữ số, hiệu các chữ số là 5. Tìm hiệu của số lớn nhất và số bé nhất trong các số đó.</div>
        
        <div class="box-highlight" style="font-family: cursive; color: var(--text-red); font-size: 1.6cqw; line-height: 1.8;">
            Các số có hai chữ số mà hiệu các chữ số là 5 là: 16, 27, 38, 49, 50, 61, 72, 83, 94.<br>
            Hiệu của số lớn nhất và số bé nhất là:<br>
            <div style="text-align: center; font-weight: bold;">94 - 16 = 78</div>
        </div>
        
        <div class="text-md" style="margin-top: 3cqw;"><b>Chữa bài sai:</b></div>
        <div style="border-bottom: 1px dotted #999; height: 3cqw; margin-top: 1cqw;"></div>
        <div style="border-bottom: 1px dotted #999; height: 3cqw;"></div>
        <div style="border-bottom: 1px dotted #999; height: 3cqw;"></div>
    </div>
    <div class="slide-footer">
        <span>Câu lạc bộ Toán học Muôn màu</span>
        <span>Trang 8</span>
    </div>
</div>
            """
        ]
    },
    "4M0_NDBH_05-09": {
        "title": "4M0. NDBH 05-09",
        "out_file": "outputdata/05092026/4M0_NDBH_05-09.html",
        "slides": [
            """
<div class="slide">
    <div class="slide-header" style="align-items: flex-start; padding-bottom: 0.5cqw; margin-bottom: 1cqw; border-bottom: none;">
        <div style="text-align: left; font-size: 1.2cqw; line-height: 1.5; color: #000;">
            <div style="font-size: 1.8cqw; font-weight: bold;">ĐỌC, VIẾT SỐ TỰ NHIÊN</div>
            <div><b>Môn:</b> Toán 4 &nbsp;&nbsp; <b>Lớp:</b> 4M0</div>
            <div><b>Ngày học:</b> ngày 5 / tháng 9 / năm 2026</div>
            <div><b>Giáo viên dạy:</b> Đỗ Thị Thủy</div>
        </div>
    </div>
    
    <div style="border-top: 2px solid #333; margin-bottom: 1cqw;"></div>

    <div class="title-main text-lg" style="text-align: left; margin-bottom: 1cqw; font-size: 2cqw;">A. Kiến thức cần nhớ</div>
    
    <div class="content-full">
        <div style="text-align: center; font-size: 2.5cqw; font-weight: bold; margin-bottom: 2cqw; text-transform: uppercase;">Củng cố kiến thức về số tự nhiên</div>
        
        <div class="grid-3-col" style="gap: 1cqw; margin-bottom: 2cqw;">
            <div style="text-align: center;">
                <div style="font-size: 3cqw; font-weight: bold; color: #ef4444; letter-spacing: 0.5cqw;">0 1 2 3 4 5 6 7 8 9</div>
                <div style="font-weight: bold; font-size: 1.4cqw; margin-top: 1cqw;">10 Chữ số "Quyền năng"</div>
                <div style="font-size: 1.1cqw; margin-top: 0.5cqw;">Sử dụng các chữ số từ 0 đến 9 để viết mọi số tự nhiên.</div>
            </div>
            <div style="text-align: center;">
                <div style="font-weight: bold; font-size: 1.4cqw; margin-bottom: 1cqw;">Phân loại Chẵn và Lẻ</div>
                <div style="display: flex; gap: 1cqw; justify-content: center;">
                    <div class="box-blue" style="padding: 1cqw; text-align: center; width: 45%;">
                        <div style="font-weight: bold; font-size: 1.2cqw; background: #bfdbfe; border-radius: 0.5cqw; margin-bottom: 0.5cqw;">0, 2, 4, 6, 8</div>
                        <div style="font-size: 1cqw;">Số chẵn tận cùng là<br>0, 2, 4, 6, 8</div>
                    </div>
                    <div class="box-orange" style="padding: 1cqw; text-align: center; width: 45%;">
                        <div style="font-weight: bold; font-size: 1.2cqw; background: #fed7aa; border-radius: 0.5cqw; margin-bottom: 0.5cqw;">1, 3, 5, 7, 9</div>
                        <div style="font-size: 1cqw;">Số lẻ tận cùng là<br>1, 3, 5, 7, 9</div>
                    </div>
                </div>
            </div>
            <div style="text-align: center;">
                <div style="font-weight: bold; font-size: 1.4cqw; margin-bottom: 1cqw;">Mối quan hệ</div>
                <div style="font-weight: bold; color: #ef4444; font-size: 1.2cqw;">"Liền trước - Liền sau"</div>
                <div style="font-size: 1.1cqw; margin-top: 0.5cqw;">Hai số tự nhiên liên tiếp hơn kém nhau 1 đơn vị; số 0 là số bé nhất.</div>
                <div style="font-size: 1.1cqw; margin-top: 0.5cqw; color: #64748b;">Trong dãy số chẵn/lẻ: hai số liên tiếp nhau hơn kém nhau 2 đơn vị.</div>
            </div>
        </div>

        <div style="text-align: center; font-weight: bold; font-size: 1.6cqw; margin-bottom: 1cqw;">Hàng và Lớp</div>
        <table style="width: 80%; margin: 0 auto; border-collapse: collapse; font-size: 1.1cqw; text-align: center; margin-bottom: 2cqw;">
            <thead>
                <tr>
                    <th style="border: 1px solid #333; padding: 0.5cqw; background: #f1f5f9; width: 10%;">Lớp</th>
                    <th colspan="3" style="border: 1px solid #333; padding: 0.5cqw; background: #eff6ff;">Tỉ</th>
                    <th colspan="3" style="border: 1px solid #333; padding: 0.5cqw; background: #fff7ed;">Triệu</th>
                    <th colspan="3" style="border: 1px solid #333; padding: 0.5cqw; background: #f0fdf4;">Nghìn</th>
                    <th colspan="3" style="border: 1px solid #333; padding: 0.5cqw; background: #fdf2f8;">Đơn vị</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style="border: 1px solid #333; padding: 0.5cqw; font-weight: bold; background: #f1f5f9;">Hàng</td>
                    <!-- Tỉ -->
                    <td style="border: 1px solid #333; writing-mode: vertical-rl; transform: rotate(180deg); padding: 0.5cqw;">Trăm tỉ</td>
                    <td style="border: 1px solid #333; writing-mode: vertical-rl; transform: rotate(180deg); padding: 0.5cqw;">Chục tỉ</td>
                    <td style="border: 1px solid #333; writing-mode: vertical-rl; transform: rotate(180deg); padding: 0.5cqw;">Tỉ</td>
                    <!-- Triệu -->
                    <td style="border: 1px solid #333; writing-mode: vertical-rl; transform: rotate(180deg); padding: 0.5cqw;">Trăm triệu</td>
                    <td style="border: 1px solid #333; writing-mode: vertical-rl; transform: rotate(180deg); padding: 0.5cqw;">Chục triệu</td>
                    <td style="border: 1px solid #333; writing-mode: vertical-rl; transform: rotate(180deg); padding: 0.5cqw;">Triệu</td>
                    <!-- Nghìn -->
                    <td style="border: 1px solid #333; writing-mode: vertical-rl; transform: rotate(180deg); padding: 0.5cqw;">Trăm nghìn</td>
                    <td style="border: 1px solid #333; writing-mode: vertical-rl; transform: rotate(180deg); padding: 0.5cqw;">Chục nghìn</td>
                    <td style="border: 1px solid #333; writing-mode: vertical-rl; transform: rotate(180deg); padding: 0.5cqw;">Nghìn</td>
                    <!-- Đơn vị -->
                    <td style="border: 1px solid #333; writing-mode: vertical-rl; transform: rotate(180deg); padding: 0.5cqw;">Trăm</td>
                    <td style="border: 1px solid #333; writing-mode: vertical-rl; transform: rotate(180deg); padding: 0.5cqw;">Chục</td>
                    <td style="border: 1px solid #333; writing-mode: vertical-rl; transform: rotate(180deg); padding: 0.5cqw;">Đơn vị</td>
                </tr>
            </tbody>
        </table>

        <div style="text-align: center; font-weight: bold; font-size: 1.6cqw; margin-bottom: 1cqw;">Quy Tắc So Sánh & Lập Số Logic</div>
        <div style="display: flex; gap: 1cqw; justify-content: center;">
            <!-- Note 1 -->
            <div style="background: #fef08a; padding: 1cqw; border-radius: 0.5cqw; width: 23%; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); position: relative;">
                <div style="font-weight: bold; font-size: 1.1cqw; text-align: center; margin-bottom: 0.5cqw;">Bí kíp<br>So sánh<br>"Siêu tốc"</div>
                <ul style="font-size: 0.9cqw; padding-left: 1.2cqw; margin: 0;">
                    <li>Số có nhiều chữ số hơn thì lớn hơn, số có ít chữ số hơn thì bé hơn.</li>
                    <li>Nếu số chữ số bằng nhau, so sánh từ trái qua phải.</li>
                </ul>
            </div>
            <!-- Note 2 -->
            <div style="background: #fef08a; padding: 1cqw; border-radius: 0.5cqw; width: 23%; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); text-align: center;">
                <div style="font-weight: bold; font-size: 1.1cqw; margin-bottom: 0.5cqw;">Mẹo tìm<br>Số Bé Nhất</div>
                <div style="font-size: 0.9cqw;">Cần ít chữ số nhất có thể, ưu tiên đưa các chữ số lớn (như 9) về hàng thấp.</div>
            </div>
            <!-- Note 3 -->
            <div style="background: #fef08a; padding: 1cqw; border-radius: 0.5cqw; width: 23%; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); text-align: center;">
                <div style="font-weight: bold; font-size: 1.1cqw; margin-bottom: 0.5cqw;">Mẹo tìm<br>Số Lớn Nhất</div>
                <div style="font-size: 0.9cqw;">Cần nhiều chữ số nhất có thể, ưu tiên chữ số lớn ở hàng cao nhất.</div>
            </div>
            <!-- Note 4 -->
            <div style="background: #fef08a; padding: 1cqw; border-radius: 0.5cqw; width: 23%; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); text-align: center;">
                <div style="font-weight: bold; font-size: 1.1cqw; margin-bottom: 0.5cqw;">Bài toán<br>xóa chữ số</div>
                <div style="font-size: 0.9cqw;">Để số còn lại lớn nhất, hãy giữ chữ số lớn nhất ở hàng cao nhất.</div>
            </div>
        </div>

    </div>
    
    <div class="slide-footer" style="margin-top: auto;">
        <span style="font-weight: bold; font-size: 1.2cqw;">1</span>
    </div>
</div>
""",
            """
<div class="slide">
    <div class="slide-header" style="border-bottom: none; margin-bottom: 0;">
        <div class="header-title"></div>
        <div class="header-badge">Trang 2</div>
    </div>
    <div class="content-full">
        <div class="title-main text-lg" style="text-align: left; margin-bottom: 1cqw;">B. Bài tập thực hành</div>
        <div class="text-md" style="margin-bottom: 1cqw;"><b>Bài 1.</b> Điền số thích hợp vào chỗ chấm:</div>
        
        <table style="width: 100%; border-collapse: collapse; font-size: 1.2cqw; text-align: center; margin-bottom: 2cqw;">
            <thead>
                <tr>
                    <th rowspan="2" style="border: 1px solid #333; padding: 0.5cqw;">Số</th>
                    <th colspan="3" style="border: 1px solid #333; padding: 0.5cqw;">Lớp triệu</th>
                    <th colspan="3" style="border: 1px solid #333; padding: 0.5cqw;">Lớp nghìn</th>
                    <th colspan="3" style="border: 1px solid #333; padding: 0.5cqw;">Lớp đơn vị</th>
                </tr>
                <tr>
                    <th style="border: 1px solid #333; padding: 0.5cqw;">Hàng trăm triệu</th>
                    <th style="border: 1px solid #333; padding: 0.5cqw;">Hàng chục triệu</th>
                    <th style="border: 1px solid #333; padding: 0.5cqw;">Hàng triệu</th>
                    <th style="border: 1px solid #333; padding: 0.5cqw;">Hàng trăm nghìn</th>
                    <th style="border: 1px solid #333; padding: 0.5cqw;">Hàng chục nghìn</th>
                    <th style="border: 1px solid #333; padding: 0.5cqw;">Hàng nghìn</th>
                    <th style="border: 1px solid #333; padding: 0.5cqw;">Hàng trăm</th>
                    <th style="border: 1px solid #333; padding: 0.5cqw;">Hàng chục</th>
                    <th style="border: 1px solid #333; padding: 0.5cqw;">Hàng đơn vị</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style="border: 1px solid #333; padding: 0.5cqw;">678 956</td>
                    <td style="border: 1px solid #333;">......</td><td style="border: 1px solid #333;">......</td><td style="border: 1px solid #333;">......</td>
                    <td style="border: 1px solid #333; color: var(--text-red); font-family: cursive;">6</td><td style="border: 1px solid #333; color: var(--text-red); font-family: cursive;">7</td><td style="border: 1px solid #333; color: var(--text-red); font-family: cursive;">8</td>
                    <td style="border: 1px solid #333; color: var(--text-red); font-family: cursive;">9</td><td style="border: 1px solid #333; color: var(--text-red); font-family: cursive;">5</td><td style="border: 1px solid #333; color: var(--text-red); font-family: cursive;">6</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #333; padding: 0.5cqw;">3 245 687</td>
                    <td style="border: 1px solid #333;">......</td><td style="border: 1px solid #333;">......</td><td style="border: 1px solid #333;">......</td>
                    <td style="border: 1px solid #333;">......</td><td style="border: 1px solid #333;">......</td><td style="border: 1px solid #333;">......</td>
                    <td style="border: 1px solid #333;">......</td><td style="border: 1px solid #333;">......</td><td style="border: 1px solid #333;">......</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #333; padding: 0.5cqw;">10 006 435</td>
                    <td style="border: 1px solid #333;">......</td><td style="border: 1px solid #333;">......</td><td style="border: 1px solid #333;">......</td>
                    <td style="border: 1px solid #333;">......</td><td style="border: 1px solid #333;">......</td><td style="border: 1px solid #333;">......</td>
                    <td style="border: 1px solid #333;">......</td><td style="border: 1px solid #333;">......</td><td style="border: 1px solid #333;">......</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #333; padding: 0.5cqw;">31 208 000</td>
                    <td style="border: 1px solid #333;">......</td><td style="border: 1px solid #333;">......</td><td style="border: 1px solid #333;">......</td>
                    <td style="border: 1px solid #333;">......</td><td style="border: 1px solid #333;">......</td><td style="border: 1px solid #333;">......</td>
                    <td style="border: 1px solid #333;">......</td><td style="border: 1px solid #333;">......</td><td style="border: 1px solid #333;">......</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #333; padding: 0.5cqw;">523 100 005</td>
                    <td style="border: 1px solid #333;">......</td><td style="border: 1px solid #333;">......</td><td style="border: 1px solid #333;">......</td>
                    <td style="border: 1px solid #333;">......</td><td style="border: 1px solid #333;">......</td><td style="border: 1px solid #333;">......</td>
                    <td style="border: 1px solid #333;">......</td><td style="border: 1px solid #333;">......</td><td style="border: 1px solid #333;">......</td>
                </tr>
            </tbody>
        </table>

        <div class="text-md" style="margin-bottom: 1cqw;"><b>Bài 2.</b> Cho biết: <b>Một nghìn triệu gọi là một tỉ.</b> Viết vào chỗ trống.</div>
        <table style="width: 100%; border-collapse: collapse; font-size: 1.4cqw; text-align: center; margin-bottom: 2cqw;">
            <thead>
                <tr>
                    <th style="border: 1px solid #333; padding: 1cqw; width: 30%;">Viết</th>
                    <th style="border: 1px solid #333; padding: 1cqw; width: 70%;">Đọc</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style="border: 1px solid #333; padding: 1cqw;">1 000 000 000<br><span style="color: var(--text-red); font-family: cursive; font-size: 1cqw;">lớp triệu - lớp nghìn - lớp đơn vị</span></td>
                    <td style="border: 1px solid #333; padding: 1cqw;">Một tỉ</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #333; padding: 1cqw;">5 000 000 000</td>
                    <td style="border: 1px solid #333; padding: 1cqw; color: var(--text-red); font-family: cursive;">Năm tỉ</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #333; padding: 1cqw;">315 000 000 000</td>
                    <td style="border: 1px solid #333; padding: 1cqw; color: var(--text-red); font-family: cursive;">Ba trăm mười lăm tỉ</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #333; padding: 1cqw; color: var(--text-red); font-family: cursive;">550 000 000 000</td>
                    <td style="border: 1px solid #333; padding: 1cqw;">Năm trăm năm mươi tỉ</td>
                </tr>
            </tbody>
        </table>
        
        <div class="text-md" style="margin-bottom: 1cqw;"><b>Bài 3.</b> Điền chữ hoặc số thích hợp vào chỗ chấm</div>
        <div style="font-size: 1.4cqw; line-height: 1.8;">
            a. Trong số 537 129:<br>
            - Chữ số 7 ở hàng <span style="color: var(--text-red); font-family: cursive;">nghìn</span>, có giá trị là <span style="color: var(--text-red); font-family: cursive;">7 000</span> và thuộc lớp <span style="color: var(--text-red); font-family: cursive;">nghìn</span><br>
            - Chữ số 1 ở hàng <span style="color: var(--text-red); font-family: cursive;">trăm</span>, có giá trị là <span style="color: var(--text-red); font-family: cursive;">100</span> và thuộc lớp <span style="color: var(--text-red); font-family: cursive;">đơn vị</span><br>
            <br>
            b. Trong số 2 387 406:<br>
            - Chữ số 3 ở hàng <span style="color: var(--text-red); font-family: cursive;">trăm nghìn</span>, có giá trị là <span style="color: var(--text-red); font-family: cursive;">300 000</span> và thuộc lớp <span style="color: var(--text-red); font-family: cursive;">nghìn</span><br>
            - Chữ số 2 ở hàng <span style="color: var(--text-red); font-family: cursive;">triệu</span>, có giá trị là <span style="color: var(--text-red); font-family: cursive;">2 000 000</span> và thuộc lớp <span style="color: var(--text-red); font-family: cursive;">triệu</span><br>
        </div>

    </div>
    <div class="slide-footer">
        <span>Câu lạc bộ Toán học Muôn màu</span>
        <span>2</span>
    </div>
</div>
""",
            """
<div class="slide">
    <div class="slide-header" style="border-bottom: none; margin-bottom: 0;">
        <div class="header-title"></div>
        <div class="header-badge">Trang 3</div>
    </div>
    <div class="content-full" style="font-size: 1.4cqw; line-height: 1.8;">
        <div class="text-md" style="margin-bottom: 1cqw;"><b>Bài 4.</b> Viết các số sau:</div>
        <div>
            a. Tám triệu không trăm hai mươi lăm nghìn không trăm linh chín: <span style="color: var(--text-red); font-family: cursive;">8 025 009</span><br>
            b. Hai mươi sáu triệu tám trăm linh năm nghìn không trăm linh bảy: <span style="color: var(--text-red); font-family: cursive;">26 805 007</span><br>
            c. Bảy mươi tư triệu không trăm linh năm nghìn sáu trăm linh một: <span style="color: var(--text-red); font-family: cursive;">74 005 601</span><br>
            d. Chín triệu không trăm linh bảy nghìn tám trăm bốn mươi hai: <span style="color: var(--text-red); font-family: cursive;">9 007 842</span><br>
        </div>

        <div class="text-md" style="margin-top: 1cqw; margin-bottom: 1cqw;"><b>Bài 5.</b> Viết số, biết số đó gồm:</div>
        <div>
            a. 7 triệu, 6 trăm nghìn, 6 chục nghìn, 5 trăm, 8 chục và 9 đơn vị: <span style="color: var(--text-red); font-family: cursive;">7 660 589</span><br>
            b. 8 trăm triệu, 4 triệu, 3 trăm nghìn, 8 nghìn, và 15 đơn vị: <span style="color: var(--text-red); font-family: cursive;">804 308 015</span><br>
        </div>

        <div class="text-md" style="margin-top: 1cqw; margin-bottom: 1cqw;"><b>Bài 6.</b> Hãy sắp xếp các dãy số dưới đây theo thứ tự:</div>
        <div>
            a) Từ bé đến lớn.<br>
            7400321; 3912249; 3934007; 569000<br>
            <span style="color: var(--text-red); font-family: cursive; display: inline-block; border-bottom: 1px solid var(--text-red); padding-bottom: 0.2cqw; min-width: 50%;">569000; 3912249; 3934007; 7 400 321</span><br>
            <br>
            b) Từ lớn đến bé.<br>
            3193444; 7129028; 56023450; 689012<br>
            <span style="color: var(--text-red); font-family: cursive; display: inline-block; border-bottom: 1px solid var(--text-red); padding-bottom: 0.2cqw; min-width: 50%;">56023450; 7129028; 3193444; 689012</span><br>
        </div>

        <div class="text-md" style="margin-top: 1cqw; margin-bottom: 1cqw;"><b>Bài 7.</b> Điền dấu &gt;, &lt;, = thích hợp vào chỗ chấm.</div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2cqw;">
            <div>
                2 657 457 <span style="color: var(--text-red); font-family: cursive;">&gt;</span> 267 001<br><br>
                548 289 <span style="color: var(--text-red); font-family: cursive;">&gt;</span> 458 299<br><br>
                4 389 423 <span style="color: var(--text-red); font-family: cursive;">&gt;</span> 4 389 419
            </div>
            <div>
                234 259 <span style="color: var(--text-red); font-family: cursive;">=</span> 200 000 + 34 259<br><br>
                813 456 <span style="color: var(--text-red); font-family: cursive;">&lt;</span> 813 000 + 457<br><br>
                101 101 <span style="color: var(--text-red); font-family: cursive;">&lt;</span> 101 100 + 10 <span style="color: var(--text-red); font-family: cursive; font-size: 1cqw;">(101 110)</span>
            </div>
        </div>

        <div class="text-md" style="margin-top: 1cqw; margin-bottom: 1cqw;"><b>Bài 8.</b> Từ các số 4, 5, 3, 6 hãy viết tất cả các số có 4 chữ số khác nhau mà có chữ số hàng nghìn là 4. Sắp xếp các số đó theo thứ tự từ bé đến lớn.</div>
        <div style="color: var(--text-red); font-family: cursive; border-bottom: 1px solid var(--text-red); padding-bottom: 0.2cqw; min-width: 80%;">
            Có: 4356, 4365, 4536, 4563, 4635, 4653. Các số đã được sắp xếp theo thứ tự từ bé đến lớn.
        </div>
        <div style="border-bottom: 1px solid #333; margin-top: 2cqw;"></div>
    </div>
    <div class="slide-footer">
        <span>Câu lạc bộ Toán học Muôn màu</span>
        <span>3</span>
    </div>
</div>
""",
            """
<div class="slide">
    <div class="slide-header" style="border-bottom: none; margin-bottom: 0;">
        <div class="header-title"></div>
        <div class="header-badge">Trang 4</div>
    </div>
    <div class="content-full">
        
        <table style="width: 100%; border-collapse: collapse; font-size: 1.3cqw; margin-bottom: 1cqw;">
            <tbody>
                <tr>
                    <td style="border: 1px solid #333; padding: 1cqw; width: 75%;">
                        a. Lớn nhất và có bốn chữ số.<br><br>
                        b. Lớn nhất và có bốn chữ số khác nhau.<br><br>
                        c. Bé nhất và có năm chữ số.<br><br>
                        d. Bé nhất và có năm chữ số khác nhau.
                    </td>
                    <td style="border: 1px solid #333; padding: 1cqw; color: var(--text-red); font-family: cursive;">
                        a) 9999<br><br>
                        b) 9875<br><br>
                        c) 10001<br><br>
                        d) 10235
                    </td>
                </tr>
                <tr>
                    <td style="border: 1px solid #333; padding: 1cqw;">
                        <b>Câu 2.</b> Từ các chữ số 0; 2; 5; 6; 8; 9, viết các số tự nhiên thoả mãn điều kiện sau:<br><br>
                        a. Số chẵn lớn nhất có bốn chữ số khác nhau.<br><br>
                        b. Số lẻ bé nhất có ba chữ số khác nhau.
                    </td>
                    <td style="border: 1px solid #333; padding: 1cqw; color: var(--text-red); font-family: cursive;">
                        <br>
                        a) 9862<br><br>
                        b) 205
                    </td>
                </tr>
                <tr>
                    <td style="border: 1px solid #333; padding: 1cqw;">
                        <b>Câu 3.</b> Viết số tự nhiên lớn nhất có bốn chữ số và tổng các chữ số là 29.<br><br>
                        <span style="color: var(--text-red); font-family: cursive;">29 = 9 + 9 + 9 + 2</span>
                    </td>
                    <td style="border: 1px solid #333; padding: 1cqw; color: var(--text-red); font-family: cursive; text-align: center;">
                        <br>9992
                    </td>
                </tr>
                <tr>
                    <td style="border: 1px solid #333; padding: 1cqw;">
                        <b>Câu 4.</b> Viết số tự nhiên bé nhất có các chữ số khác nhau và tổng các chữ số là 29.<br>
                        <span style="color: var(--text-red); font-family: cursive;">
                        Số cần tìm phải ít chữ số nhất<br>
                        -&gt; các chữ số phải lớn nhất.<br>
                        Ta có: 29 = 9 + 8 + 7 + 5
                        </span>
                    </td>
                    <td style="border: 1px solid #333; padding: 1cqw; color: var(--text-red); font-family: cursive; text-align: center;">
                        <br><br>5789
                    </td>
                </tr>
                <tr>
                    <td style="border: 1px solid #333; padding: 1cqw;">
                        <b>Câu 5.</b> Cho số 905 678 725. Xoá đi 5 chữ số, giữ nguyên thứ tự các chữ số còn lại để được số tự nhiên:<br>
                        <div style="display: flex; justify-content: space-between; margin-top: 1cqw;">
                            <span>a. Bé nhất.</span>
                            <span>b. Lớn nhất.</span>
                        </div>
                    </td>
                    <td style="border: 1px solid #333; padding: 1cqw; color: var(--text-red); font-family: cursive;">
                        a) 5625<br><br>
                        b) 9875
                    </td>
                </tr>
            </tbody>
        </table>

        <div class="text-md" style="margin-top: 1cqw; margin-bottom: 1cqw;"><b>Bài 10.</b> Viết các số có hai chữ số, hiệu các chữ số là 4. Tìm hiệu của số lớn nhất và số bé nhất trong các số đó.</div>
        <div style="color: var(--text-red); font-family: cursive; font-size: 1.4cqw; line-height: 1.8;">
            <div style="border-bottom: 1px solid var(--text-red);">Ta có: 4 = 9 - 5 = 8 - 4 = 7 - 3 = 6 - 2 = 5 - 1 = 4 - 0</div>
            <div style="border-bottom: 1px solid var(--text-red);">Vậy các số cần tìm: 95; 59; 84; 48; 73; 37; 62; 26; 51; 15; 40</div>
            <div style="border-bottom: 1px solid var(--text-red);">Hiệu của số lớn nhất và số bé nhất là:</div>
            <div style="border-bottom: 1px solid var(--text-red); text-align: center;">95 - 15 = 80</div>
            <div style="border-bottom: 1px solid var(--text-red); text-align: center;">Đáp số: 80</div>
        </div>

    </div>
    <div class="slide-footer">
        <span>Câu lạc bộ Toán học Muôn màu</span>
        <span>4</span>
    </div>
</div>
"""
        ]
    },
    "4M0_NDBH_12-09": {
        "title": "4M0. NDBH 12-09",
        "out_file": "outputdata/12092026/4M0_NDBH_12-09.html",
        "slides": [
            """
<div class="slide">
    <div class="slide-header" style="align-items: flex-start; padding-bottom: 0.5cqw; margin-bottom: 1cqw; border-bottom: none;">
        <div style="text-align: left; font-size: 1.2cqw; line-height: 1.5; color: #000;">
            <div style="font-size: 1.8cqw; font-weight: bold;">BÀI TOÁN LẬP SỐ</div>
            <div><b>Môn:</b> Toán 4 &nbsp;&nbsp; <b>Lớp:</b> 4M0</div>
            <div><b>Ngày học:</b> ngày 12 / tháng 9 / năm 2026</div>
            <div><b>Giáo viên dạy:</b> Đỗ Thị Thủy</div>
        </div>
    </div>
    
    <div style="border-top: 2px solid #333; margin-bottom: 2cqw;"></div>

    <div class="content-full">
        <div style="text-align: center; color: var(--text-red); font-family: cursive; font-size: 1.6cqw; margin-bottom: 2cqw;">
            <span style="text-decoration: overline;">abcde</span> = a x 10000 + b x 1000 + c x 100 + d x 10 + e
        </div>

        <div class="text-md" style="margin-bottom: 1cqw;"><b>Bài 1.</b> Viết số tự nhiên x, biết:</div>
        <div style="font-size: 1.4cqw; line-height: 2; margin-bottom: 2cqw;">
            <div style="display: flex; justify-content: space-between;">
                <span>a) x = 4 x 1 000 + 2 x 100 + 5 x 10 + 1</span>
                <span>(x = <span style="color: var(--text-red); font-family: cursive;">4 251</span>)</span>
            </div>
            <div style="display: flex; justify-content: space-between;">
                <span>b) x = 7 x 10 000 + 8 x 100 + 9</span>
                <span>(x = <span style="color: var(--text-red); font-family: cursive;">70 809</span>)</span>
            </div>
            <div style="display: flex; justify-content: space-between;">
                <span>c) x = 2 x 1 000 000 + 2 x 1000 + 2</span>
                <span>(x = <span style="color: var(--text-red); font-family: cursive;">2 002 002</span>)</span>
            </div>
        </div>

        <div class="text-md" style="margin-bottom: 1cqw;"><b>Bài 2.</b></div>
        <div style="font-size: 1.4cqw; margin-bottom: 2cqw;">
            <div style="margin-bottom: 0.5cqw;">a) Từ 3 chữ số 6, 7, 8 hãy viết tất cả các <u style="color: var(--text-red);"><span style="color: black;">số có 3 chữ số khác nhau</span></u>. Sắp xếp các số theo thứ tự từ lớn đến bé.</div>
            <div style="color: var(--text-red); font-family: cursive; border-bottom: 1px solid var(--text-red); padding-bottom: 0.2cqw; margin-bottom: 0.5cqw;">Các số lập được là: 678; 687; 786; 768; 867; 876</div>
            <div style="color: var(--text-red); font-family: cursive; border-bottom: 1px solid var(--text-red); padding-bottom: 0.2cqw; margin-bottom: 1cqw;">Các số trên sắp xếp theo thứ tự từ lớn đến bé là: 876; 867; 786; 768; 687; 678.</div>

            <div style="margin-bottom: 0.5cqw; margin-top: 2cqw;">b) Từ 3 chữ số 5, 0, 9 hãy viết tất cả các số có 3 chữ số khác nhau. Sắp xếp các số theo thứ tự từ tăng dần.</div>
            <div style="color: var(--text-red); font-family: cursive; border-bottom: 1px solid var(--text-red); padding-bottom: 0.2cqw; margin-bottom: 0.5cqw;">Các số lập được là: 509; 590; 905; 950</div>
            <div style="color: var(--text-red); font-family: cursive; border-bottom: 1px solid var(--text-red); padding-bottom: 0.2cqw;">Các số trên sắp xếp theo thứ tự tăng dần là: 509; 590; 905; 950</div>
        </div>

        <div class="text-md" style="margin-bottom: 1cqw;"><b>Bài 3.</b> Cho 6 chữ số 0, <span style="color: var(--text-red); text-decoration: line-through;">1</span>, 2, 3, 7, 9. Viết <u style="color: var(--text-red);"><span style="color: black;">số lớn nhất</span></u> và <u style="color: var(--text-red);"><span style="color: black;">nhỏ nhất</span></u> có mặt đủ 6 chữ số trên.</div>
        <div style="font-size: 1.4cqw; line-height: 2;">
            <div>Số lớn nhất: <span style="color: var(--text-red); font-family: cursive;">973 210</span></div>
            <div>Số bé nhất: <span style="color: var(--text-red); font-family: cursive;">102 379</span></div>
        </div>

    </div>
    
    <div class="slide-footer" style="margin-top: auto;">
        <span></span>
        <span style="font-weight: bold; font-size: 1.2cqw;">1</span>
    </div>
</div>
""",
            """
<div class="slide">
    <div class="slide-header" style="border-bottom: none; margin-bottom: 0;">
        <div class="header-title"></div>
        <div class="header-badge">Trang 2</div>
    </div>
    <div class="content-full">
        
        <div class="text-md" style="margin-bottom: 1cqw;"><b>Bài 4.</b> Viết số tự nhiên theo điều kiện sau:</div>
        <div style="font-size: 1.4cqw; line-height: 2; margin-bottom: 2cqw;">
            <div>a) Lớn nhất có 6 chữ số: <span style="color: var(--text-red); font-family: cursive;">999 999</span></div>
            <div>b) Bé nhất có <u style="color: var(--text-red);"><span style="color: black;">5 chữ số khác nhau</span></u>: <span style="color: var(--text-red); font-family: cursive;">10234</span></div>
            <div>c) Lớn nhất có 6 chữ số mà hàng trăm là 2: <span style="color: var(--text-red); font-family: cursive;">999 299</span></div>
            <div>d) Số lớn nhất có 8 chữ số khác nhau: <span style="color: var(--text-red); font-family: cursive;">987 65432</span></div>
            <div>e) Số <div style="display: inline-block; border: 2px solid var(--text-red); border-radius: 50%; padding: 0 0.2cqw; line-height: 1;">lẻ</div> lớn nhất có 6 chữ số khác nhau: <span style="color: var(--text-red); font-family: cursive;">987 653</span></div>
            <div>g) Số chẵn <u style="color: var(--text-red);"><span style="color: black;">bé nhất</span></u> có 5 chữ số <u style="color: var(--text-red);"><span style="color: black;">khác nhau</span></u>: <span style="color: var(--text-red); font-family: cursive;">10234</span></div>
            <div>h) Số bé nhất có 7 chữ số khác nhau bắt đầu bởi chữ số 8: <span style="color: var(--text-red); font-family: cursive;">8 012 345</span></div>
        </div>

        <div class="text-md" style="margin-bottom: 1cqw;"><b>Bài 5.</b> Viết: <span style="color: var(--text-red); font-family: cursive;">Có 10 cs: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9</span></div>
        <div style="font-size: 1.4cqw; line-height: 2; margin-bottom: 2cqw;">
            <div style="margin-bottom: 1cqw;">
                a) Số tự nhiên <u style="color: var(--text-red);"><span style="color: black;">bé nhất</span></u> có 5 chữ số được viết <u style="color: var(--text-red);"><span style="color: black;">từ ba chữ số khác nhau</span></u>: <span style="color: blue; font-family: cursive; font-size: 1.2cqw; margin-left: 1cqw;">0, 1, 2</span><br>
                <span style="color: var(--text-red); font-family: cursive;">10002</span>
            </div>
            <div>
                b) Số tự nhiên <u style="color: var(--text-red);"><span style="color: black;">lớn nhất</span></u> có 5 chữ số được viết từ <u style="color: var(--text-red);"><span style="color: black;">ba chữ số khác nhau</span></u>.<br>
                <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                    <span style="color: var(--text-red); font-family: cursive;">99987</span>
                    <span style="color: blue; font-family: cursive; font-size: 1.4cqw; margin-right: 15cqw;">9, 8, 7</span>
                </div>
            </div>
        </div>

        <div class="text-md" style="margin-bottom: 1cqw;"><b>Bài 6.</b> Điền số thích hợp vào chỗ trống</div>
        <div style="font-size: 1.4cqw; line-height: 1.8;">
            <div>Minh viết liên tiếp 15 số lẻ <u style="color: var(--text-red);"><span style="color: black;">đầu tiên</span></u> để được một số tự nhiên. Hãy <u style="color: var(--text-red);"><span style="color: black;">xóa đi</span></u> 15 chữ số của số tự nhiên vừa nhận được mà vẫn <u style="color: var(--text-red);"><span style="color: black;">giữ nguyên</span></u> thứ tự của các chữ số còn lại. <span style="color: var(--text-red); font-family: cursive;">-&gt; còn 10 chữ số</span></div>
            <div style="margin-top: 1cqw;">Số Minh viết được là: <span style="color: var(--text-red); font-family: cursive; text-decoration: line-through; text-decoration-color: rgba(255,0,0,0.5);">13579111315171</span><span style="color: var(--text-red); font-family: cursive; border-bottom: 2px solid blue;">9</span><span style="color: var(--text-red); font-family: cursive; text-decoration: line-through; text-decoration-color: rgba(255,0,0,0.5);">2</span><span style="color: var(--text-red); font-family: cursive; border-bottom: 2px solid blue;">1</span><span style="color: var(--text-red); font-family: cursive; text-decoration: line-through; text-decoration-color: rgba(255,0,0,0.5);">2</span><span style="color: var(--text-red); font-family: cursive; border-bottom: 2px solid blue;">3252729</span></div>
            <div style="margin-top: 1cqw;">Sau khi xóa 15 chữ số, số <u style="color: var(--text-red);"><span style="color: black;">lớn nhất</span></u> là: <span style="color: var(--text-red); font-family: cursive;">99223252729</span></div>
            <div style="margin-top: 1cqw;">số <u style="color: var(--text-red);"><span style="color: black;">bé nhất</span></u> là: <span style="color: var(--text-red); font-family: cursive;">11111111222</span></div>
        </div>

    </div>
    <div class="slide-footer">
        <span></span>
        <span>2</span>
    </div>
</div>
""",
            """
<div class="slide">
    <div class="slide-header" style="border-bottom: none; margin-bottom: 0;">
        <div class="header-title"></div>
        <div class="header-badge">Trang 3</div>
    </div>
    <div class="content-full">
        <div class="text-md" style="margin-bottom: 1cqw;"><b>Bài 7. Điền đáp án</b></div>
        
        <table style="width: 100%; border-collapse: collapse; font-size: 1.3cqw;">
            <thead>
                <tr>
                    <th style="border: 1px solid #333; padding: 0.5cqw; background: #f1f5f9; text-align: center; width: 75%;">Đề bài</th>
                    <th style="border: 1px solid #333; padding: 0.5cqw; background: #f1f5f9; text-align: center; width: 25%;">Đáp án</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style="border: 1px solid #333; padding: 1cqw;">
                        a) Tìm số tự <u style="color: var(--text-red);"><span style="color: black;">nhiên nhỏ nhất</span></u> có <u style="color: var(--text-red);"><span style="color: black;">tổng các chữ số bằng 12</span></u>.<br>
                        <div style="color: var(--text-red); font-family: cursive; text-align: center; margin-top: 0.5cqw;">&darr;</div>
                        <div style="color: var(--text-red); font-family: cursive; text-align: center;">ít chữ số nhất nhất &rarr; các chữ số lớn nhất</div>
                        <div style="color: var(--text-red); font-family: cursive; margin-top: 0.5cqw;">Ta có: 12 = 9 + 3 &rarr; số cần tìm là 39</div>
                    </td>
                    <td style="border: 1px solid #333; padding: 1cqw; color: var(--text-red); font-family: cursive; text-align: center; font-size: 2cqw;">39</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #333; padding: 1cqw;">
                        b) Tìm số tự nhiên lớn nhất có <u style="color: var(--text-red);"><span style="color: black;">các chữ số khác nhau</span></u> mà <div style="display: inline-block; border: 2px solid var(--text-red); border-radius: 50%; padding: 0 0.2cqw; line-height: 1;">tích</div> các chữ số của số đó bằng 30.<br>
                        <div style="color: var(--text-red); font-family: cursive; margin-top: 0.5cqw;">Ta có: 30 = 10 x 3 x 1 = 5 x 2 x 3 x 1</div>
                        <div style="color: var(--text-red); font-family: cursive; margin-top: 0.5cqw;">&rarr; Số lập được là 5321</div>
                    </td>
                    <td style="border: 1px solid #333; padding: 1cqw; color: var(--text-red); font-family: cursive; text-align: center; font-size: 2cqw;">5321</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #333; padding: 1cqw;">
                        c) Tìm số tự <u style="color: var(--text-red);"><span style="color: black;">nhiên lớn nhất có 3 chữ số khác nhau</span></u> mà <u style="color: var(--text-red);"><span style="color: black;">tổng</span></u> các chữ số bằng 10.<br>
                        <div style="color: var(--text-red); font-family: cursive; margin-top: 0.5cqw; text-align: center;">10 = 9 + 1 + 0</div>
                    </td>
                    <td style="border: 1px solid #333; padding: 1cqw; color: var(--text-red); font-family: cursive; text-align: center; font-size: 2cqw;">910</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #333; padding: 1cqw;">
                        d) Tìm số tự nhiên bé nhất có 3 chữ số khác nhau mà <u style="color: var(--text-red);"><span style="color: black;">tổng</span></u> các chữ số bằng 14.<br>
                        <div style="color: var(--text-red); font-family: cursive; margin-top: 0.5cqw; text-align: center;">14 = 1 + 9 + 4</div>
                    </td>
                    <td style="border: 1px solid #333; padding: 1cqw; color: var(--text-red); font-family: cursive; text-align: center; font-size: 2cqw;">149</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #333; padding: 1cqw;">
                        e) Tìm số tự nhiên <u style="color: var(--text-red);"><span style="color: black;">bé nhất có 4 chữ số khác nhau</span></u> mà <u style="color: var(--text-red);"><span style="color: black;">tổng</span></u> các chữ số bằng 15.<br>
                        <div style="color: var(--text-red); font-family: cursive; margin-top: 0.5cqw; text-align: center;">15 = 1 + 0 + 9 + 5</div>
                    </td>
                    <td style="border: 1px solid #333; padding: 1cqw; color: var(--text-red); font-family: cursive; text-align: center; font-size: 2cqw;">1059</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #333; padding: 1cqw;">
                        f) Tìm số <u style="color: var(--text-red);"><span style="color: black;">tự nhiên bé nhất</span></u> có <u style="color: var(--text-red);"><span style="color: black;">các chữ số khác nhau</span></u> và tổng các chữ số là 29.<br>
                        <div style="color: var(--text-red); font-family: cursive; margin-top: 0.5cqw;">Muốn số bé nhất thì phải ít chữ số nhất</div>
                        <div style="color: var(--text-red); font-family: cursive;">&rarr; các chữ số lớn nhất.</div>
                        <div style="color: var(--text-red); font-family: cursive; margin-top: 0.5cqw;">Ta có 29 = 9 + 8 + 7 + 5</div>
                    </td>
                    <td style="border: 1px solid #333; padding: 1cqw; color: var(--text-red); font-family: cursive; text-align: center; font-size: 2cqw;">5789</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #333; padding: 1cqw;">
                        g) Tìm <u style="color: var(--text-red);"><span style="color: black;">số tự nhiên lớn nhất</span></u> có <u style="color: var(--text-red);"><span style="color: black;">các chữ số khác nhau</span></u> và tổng các chữ số là 15.<br>
                        <div style="color: var(--text-red); font-family: cursive; margin-top: 0.5cqw;">Muốn số lớn nhất thì phải nhiều chữ số nhất</div>
                        <div style="color: var(--text-red); font-family: cursive;">&rarr; Các chữ số phải bé nhất</div>
                        <div style="color: var(--text-red); font-family: cursive; margin-top: 0.5cqw;">Ta có: 15 = 0 + 1 + 2 + 3 + 4 + 5</div>
                    </td>
                    <td style="border: 1px solid #333; padding: 1cqw; color: var(--text-red); font-family: cursive; text-align: center; font-size: 2cqw;">543210</td>
                </tr>
            </tbody>
        </table>

    </div>
    <div class="slide-footer">
        <span></span>
        <span>3</span>
    </div>
</div>
"""
        ]
    }
}

def generate_all():
    for key, doc in DATA.items():
        if not doc["slides"]:
            print(f"Skipping {key}, no slides data yet.")
            continue
            
        content = "\\n\\n".join(doc["slides"])
        html = TEMPLATE.format(TITLE=doc["title"], CONTENT=content)
        
        with open(doc["out_file"], "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated {doc['out_file']}")

if __name__ == "__main__":
    generate_all()

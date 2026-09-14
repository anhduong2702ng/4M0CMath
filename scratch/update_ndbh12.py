import os
import sys

file_path = "f:/DigiIn/lab/AI/Gemini/4GE/CMath/scripts/generate_html.py"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

slides_12 = [
r'''
<div class="slide">
    <div class="slide-header" style="align-items: flex-start; padding-bottom: 0.5cqw; margin-bottom: 1cqw; border-bottom: none;">
        <div style="display: flex; gap: 1cqw; align-items: center;">
            <div style="font-size: 2.5cqw; font-weight: 800; color: #facc15;">CMATH</div>
            <div style="font-size: 1.2cqw; font-weight: bold; color: #64748b; letter-spacing: 0.2cqw;">EDUCATION</div>
        </div>
        <div style="text-align: right; font-size: 1.2cqw; line-height: 1.5; color: #000;">
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
''',
r'''
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
''',
r'''
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
'''
]

new_slides_str = ",\n            ".join([f'"""{s}"""' for s in slides_12])

target = '''    "4M0_NDBH_12-09": {
        "title": "4M0. NDBH 12-09",
        "out_file": "outputdata/12092026/4M0_NDBH_12-09.html",
        "slides": []
    }'''
replacement = f'''    "4M0_NDBH_12-09": {{
        "title": "4M0. NDBH 12-09",
        "out_file": "outputdata/12092026/4M0_NDBH_12-09.html",
        "slides": [
            {new_slides_str}
        ]
    }}'''

content = content.replace(target, replacement)
with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated successfully")

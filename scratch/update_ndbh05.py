import os
import sys

file_path = "f:/DigiIn/lab/AI/Gemini/4GE/CMath/scripts/generate_html.py"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

slides_05 = [
r'''
<div class="slide">
    <div class="slide-header" style="align-items: flex-start; padding-bottom: 0.5cqw; margin-bottom: 1cqw; border-bottom: none;">
        <div style="display: flex; gap: 1cqw; align-items: center;">
            <div style="font-size: 2.5cqw; font-weight: 800; color: #facc15;">CMATH</div>
            <div style="font-size: 1.2cqw; font-weight: bold; color: #64748b; letter-spacing: 0.2cqw;">EDUCATION</div>
        </div>
        <div style="text-align: right; font-size: 1.2cqw; line-height: 1.5; color: #000;">
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
''',
r'''
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
''',
r'''
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
''',
r'''
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
'''
]

new_slides_str = ",\n            ".join([f'"""{s}"""' for s in slides_05])

target = '''    "4M0_NDBH_05-09": {
        "title": "4M0. NDBH 05-09",
        "out_file": "outputdata/05092026/4M0_NDBH_05-09.html",
        "slides": []
    },'''
replacement = f'''    "4M0_NDBH_05-09": {{
        "title": "4M0. NDBH 05-09",
        "out_file": "outputdata/05092026/4M0_NDBH_05-09.html",
        "slides": [
            {new_slides_str}
        ]
    }},'''

content = content.replace(target, replacement)
with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated successfully")

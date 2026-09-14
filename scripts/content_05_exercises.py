"""Exercises content for lesson 05-09. Uses .answer/.blank classes."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from generate_v2 import hdr, foot, A, Ablk, gen_debai, gen_btvn

def ac(text):
    """Answer in a table cell."""
    return f'<td class="answer-cell"><span class="answer">{text}</span><span class="blank">......</span></td>'

PRACTICE = hdr("BÀI TẬP – ĐỌC, VIẾT SỐ TỰ NHIÊN", "05/09/2026")

# ---- Bài tập thực hành (from NDBH pages 2-4) ----
PRACTICE += '''
    <div class="section-title">B. Bài tập thực hành</div>

    <p><b>Bài 1.</b> Điền số thích hợp vào chỗ chấm:</p>
    <table style="text-align:center; font-size:0.9rem;">
        <thead>
            <tr>
                <th rowspan="2">Số</th>
                <th colspan="3">Lớp triệu</th>
                <th colspan="3">Lớp nghìn</th>
                <th colspan="3">Lớp đơn vị</th>
            </tr>
            <tr>
                <th>Trăm triệu</th><th>Chục triệu</th><th>Triệu</th>
                <th>Trăm nghìn</th><th>Chục nghìn</th><th>Nghìn</th>
                <th>Trăm</th><th>Chục</th><th>Đơn vị</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>678 956</td>
                <td>''' + A("0") + '''</td><td>''' + A("0") + '''</td><td>''' + A("0") + '''</td>
                <td>''' + A("6") + '''</td><td>''' + A("7") + '''</td><td>''' + A("8") + '''</td>
                <td>''' + A("9") + '''</td><td>''' + A("5") + '''</td><td>''' + A("6") + '''</td>
            </tr>
            <tr>
                <td>3 245 687</td>
                <td>''' + A("0") + '''</td><td>''' + A("0") + '''</td><td>''' + A("3") + '''</td>
                <td>''' + A("2") + '''</td><td>''' + A("4") + '''</td><td>''' + A("5") + '''</td>
                <td>''' + A("6") + '''</td><td>''' + A("8") + '''</td><td>''' + A("7") + '''</td>
            </tr>
            <tr>
                <td>10 006 435</td>
                <td>''' + A("0") + '''</td><td>''' + A("1") + '''</td><td>''' + A("0") + '''</td>
                <td>''' + A("0") + '''</td><td>''' + A("0") + '''</td><td>''' + A("6") + '''</td>
                <td>''' + A("4") + '''</td><td>''' + A("3") + '''</td><td>''' + A("5") + '''</td>
            </tr>
            <tr>
                <td>31 208 000</td>
                <td>''' + A("0") + '''</td><td>''' + A("3") + '''</td><td>''' + A("1") + '''</td>
                <td>''' + A("2") + '''</td><td>''' + A("0") + '''</td><td>''' + A("8") + '''</td>
                <td>''' + A("0") + '''</td><td>''' + A("0") + '''</td><td>''' + A("0") + '''</td>
            </tr>
            <tr>
                <td>523 100 005</td>
                <td>''' + A("5") + '''</td><td>''' + A("2") + '''</td><td>''' + A("3") + '''</td>
                <td>''' + A("1") + '''</td><td>''' + A("0") + '''</td><td>''' + A("0") + '''</td>
                <td>''' + A("0") + '''</td><td>''' + A("0") + '''</td><td>''' + A("5") + '''</td>
            </tr>
        </tbody>
    </table>

    <p><b>Bài 2.</b> Cho biết: <b>Một nghìn triệu gọi là một tỉ.</b> Viết vào chỗ trống.</p>
    <table>
        <thead><tr><th style="width:35%;">Viết</th><th>Đọc</th></tr></thead>
        <tbody>
            <tr><td style="text-align:center;">1 000 000 000</td><td style="text-align:center;">Một tỉ</td></tr>
            <tr><td style="text-align:center;">5 000 000 000</td><td style="text-align:center;">''' + A("Năm tỉ") + '''</td></tr>
            <tr><td style="text-align:center;">315 000 000 000</td><td style="text-align:center;">''' + A("Ba trăm mười lăm tỉ") + '''</td></tr>
            <tr><td style="text-align:center;">''' + A("550 000 000 000") + '''</td><td style="text-align:center;">Năm trăm năm mươi tỉ</td></tr>
        </tbody>
    </table>

    <p><b>Bài 3.</b> Điền chữ hoặc số thích hợp vào chỗ chấm</p>
    <div class="content-area" style="padding-left:1rem;">
        <p>a. Trong số 537 129:<br>
        - Chữ số 7 ở hàng ''' + A("nghìn") + ''', có giá trị là ''' + A("7 000") + ''' và thuộc lớp ''' + A("nghìn") + '''<br>
        - Chữ số 1 ở hàng ''' + A("trăm") + ''', có giá trị là ''' + A("100") + ''' và thuộc lớp ''' + A("đơn vị") + '''</p>
        <p>b. Trong số 2 387 406:<br>
        - Chữ số 3 ở hàng ''' + A("trăm nghìn") + ''', có giá trị là ''' + A("300 000") + ''' và thuộc lớp ''' + A("nghìn") + '''<br>
        - Chữ số 2 ở hàng ''' + A("triệu") + ''', có giá trị là ''' + A("2 000 000") + ''' và thuộc lớp ''' + A("triệu") + '''</p>
    </div>

    <p><b>Bài 4.</b> Viết các số sau:</p>
    <div class="content-area" style="padding-left:1rem;">
        <p>a. Tám triệu không trăm hai mươi lăm nghìn không trăm linh chín: ''' + A("8 025 009") + '''<br>
        b. Hai mươi sáu triệu tám trăm linh năm nghìn không trăm linh bảy: ''' + A("26 805 007") + '''<br>
        c. Bảy mươi tư triệu không trăm linh năm nghìn sáu trăm linh một: ''' + A("74 005 601") + '''<br>
        d. Chín triệu không trăm linh bảy nghìn tám trăm bốn mươi hai: ''' + A("9 007 842") + '''</p>
    </div>

    <p><b>Bài 5.</b> Viết số, biết số đó gồm:</p>
    <div class="content-area" style="padding-left:1rem;">
        <p>a. 7 triệu, 6 trăm nghìn, 6 chục nghìn, 5 trăm, 8 chục và 9 đơn vị: ''' + A("7 660 589") + '''<br>
        b. 8 trăm triệu, 4 triệu, 3 trăm nghìn, 8 nghìn, và 15 đơn vị: ''' + A("804 308 015") + '''</p>
    </div>

    <p><b>Bài 6.</b> Sắp xếp theo thứ tự:</p>
    <div class="content-area" style="padding-left:1rem;">
        <p>a) Từ bé đến lớn: 7400321; 3912249; 3934007; 569000<br>
        ''' + Ablk("569 000; 3 912 249; 3 934 007; 7 400 321") + '''</p>
        <p>b) Từ lớn đến bé: 3193444; 7129028; 56023450; 689012<br>
        ''' + Ablk("56 023 450; 7 129 028; 3 193 444; 689 012") + '''</p>
    </div>

    <p><b>Bài 7.</b> Điền dấu &gt;, &lt;, = thích hợp</p>
    <div class="grid-2" style="padding-left:1rem;">
        <div>
            <p>2 657 457 ''' + A("&gt;") + ''' 267 001</p>
            <p>548 289 ''' + A("&gt;") + ''' 458 299</p>
            <p>4 389 423 ''' + A("&gt;") + ''' 4 389 419</p>
        </div>
        <div>
            <p>234 259 ''' + A("=") + ''' 200 000 + 34 259</p>
            <p>813 456 ''' + A("&lt;") + ''' 813 000 + 457</p>
            <p>101 101 ''' + A("&lt;") + ''' 101 100 + 10</p>
        </div>
    </div>

    <p><b>Bài 8.</b> Từ các số 4, 5, 3, 6 viết tất cả các số có 4 chữ số khác nhau mà chữ số hàng nghìn là 4. Sắp xếp từ bé đến lớn.</p>
    ''' + Ablk("4356, 4365, 4536, 4563, 4635, 4653 — đã sắp xếp từ bé đến lớn.") + '''

    <p><b>Bài 9.</b> Viết số thoả mãn:</p>
    <table>
        <tbody>
            <tr>
                <td>a. Lớn nhất có bốn chữ số.</td>
                ''' + ac("9999") + '''
            </tr>
            <tr>
                <td>b. Lớn nhất có bốn chữ số khác nhau.</td>
                ''' + ac("9875") + '''
            </tr>
            <tr>
                <td>c. Bé nhất có năm chữ số.</td>
                ''' + ac("10001") + '''
            </tr>
            <tr>
                <td>d. Bé nhất có năm chữ số khác nhau.</td>
                ''' + ac("10235") + '''
            </tr>
        </tbody>
    </table>

    <p><b>Câu 2.</b> Từ các chữ số 0; 2; 5; 6; 8; 9, viết:</p>
    <table>
        <tbody>
            <tr><td>a. Số chẵn lớn nhất có bốn chữ số khác nhau.</td>''' + ac("9862") + '''</tr>
            <tr><td>b. Số lẻ bé nhất có ba chữ số khác nhau.</td>''' + ac("205") + '''</tr>
        </tbody>
    </table>

    <p><b>Câu 3.</b> Số tự nhiên lớn nhất có bốn chữ số, tổng các chữ số là 29.</p>
    ''' + Ablk("29 = 9 + 9 + 9 + 2 → Số cần tìm: <b>9992</b>") + '''

    <p><b>Câu 4.</b> Số tự nhiên bé nhất có các chữ số khác nhau, tổng các chữ số là 29.</p>
    ''' + Ablk("Ít chữ số nhất → chữ số lớn nhất. 29 = 9 + 8 + 7 + 5 → Số cần tìm: <b>5789</b>") + '''

    <p><b>Câu 5.</b> Cho số 905 678 725. Xoá đi 5 chữ số, giữ nguyên thứ tự:</p>
    <table>
        <tbody>
            <tr><td>a. Bé nhất.</td>''' + ac("5625") + '''</tr>
            <tr><td>b. Lớn nhất.</td>''' + ac("9875") + '''</tr>
        </tbody>
    </table>

    <p><b>Bài 10.</b> Viết các số có hai chữ số, hiệu các chữ số là 4. Tìm hiệu của số lớn nhất và bé nhất.</p>
    ''' + Ablk("4 = 9-5 = 8-4 = 7-3 = 6-2 = 5-1 = 4-0<br>Các số: 95; 59; 84; 48; 73; 37; 62; 26; 51; 15; 40<br>Hiệu: 95 - 15 = <b>80</b>") + '''
''' + foot("Trang 2-4")

# ---- BTVN (from original pages 5-8) ----
HOMEWORK = hdr("BÀI TẬP VỀ NHÀ – ĐỌC, VIẾT SỐ TỰ NHIÊN", "05/09/2026") + '''
    <div class="section-title">C. Bài tập về nhà</div>
    <div class="sub-title">I. Điền đáp án</div>
    <table>
        <thead><tr><th style="width:75%;">Đề bài</th><th>Trả lời</th></tr></thead>
        <tbody>
            <tr><td><b>Câu 1.</b> Nêu giá trị của chữ số 5 trong số: 5 689 903</td>''' + ac("5 000 000") + '''</tr>
            <tr><td><b>Câu 2.</b> Số lớn nhất trong dãy: 1904094; 193409670; 93023406; 9312901</td>''' + ac("193 409 670") + '''</tr>
            <tr><td><b>Câu 3.</b> Số nhỏ nhất trong dãy: 1198491; 1198409; 119842994; 1192130</td>''' + ac("1 192 130") + '''</tr>
            <tr><td><b>Câu 4.</b> Số tự nhiên có chữ số hàng cao nhất thuộc hàng chục triệu. Hỏi số đó có bao nhiêu chữ số?</td>''' + ac("8 chữ số") + '''</tr>
            <tr><td><b>Câu 5.</b> Viết số gồm: 3 triệu, 5 chục nghìn, 5 trăm, 2 chục và 7 đơn vị.</td>''' + ac("3 050 527") + '''</tr>
            <tr><td><b>Câu 6.</b> Nam nói: "số 165 gồm 15 chục và 15 đơn vị". Nam nói đúng hay sai?</td>''' + ac("Đúng") + '''</tr>
            <tr><td><b>Câu 7.</b> Số liền sau số nhỏ nhất có 7 chữ số là số nào?</td>''' + ac("1 000 001") + '''</tr>
            <tr><td><b>Câu 8.</b> X = 5 × 100 000 + 8 × 100 + 9. X = ?</td>''' + ac("500 809") + '''</tr>
            <tr><td><b>Câu 9.</b> Điền dấu &gt;, &lt;, =:<br>a) 120 432 .... 99 423 &nbsp; b) 233 646 .... 233 746 &nbsp; c) 678 897 .... 678 889</td>''' + ac("a) &gt; &nbsp; b) &lt; &nbsp; c) &gt;") + '''</tr>
            <tr><td><b>Câu 10.</b> Viết chữ số thích hợp:<br>a) 948 ...68 &lt; 948 167 &nbsp; b) 2 608 608 &lt; 2 60... 000 + 608</td>''' + ac("a) 0 &nbsp; b) 9") + '''</tr>
            <tr><td><b>Câu 11.</b> Số "Hai trăm linh năm tỉ" được viết là:</td>''' + ac("205 000 000 000") + '''</tr>
        </tbody>
    </table>

    <p><b>Câu 12.</b> Dân số các thành phố (người). Sắp xếp giảm dần:</p>
    <div class="grid-2" style="margin-bottom:0.5rem; font-size:0.9rem;">
        <div>Mexico: 22 843 550<br>New York: 22 310 740<br>Shanghai: 16 708 510<br>London: 12 412 330</div>
        <div>Cairo: 15 837 460<br>Mumbai: 19 463 950<br>Tokyo: 35 521 740</div>
    </div>
    ''' + Ablk("Tokyo, Mexico, New York, Mumbai, Shanghai, Cairo, London") + '''

    <div class="sub-title">II. Tự luận</div>

    <p><b>Bài 13.</b> Viết các số tự nhiên chẵn thoả mãn:</p>
    <table>
        <tbody>
            <tr><td>a. Lớn nhất có 5 chữ số.</td>''' + ac("99998") + '''</tr>
            <tr><td>b. Lớn nhất có 4 chữ số khác nhau.</td>''' + ac("9876") + '''</tr>
            <tr><td>c. Bé nhất có 5 chữ số.</td>''' + ac("10000") + '''</tr>
            <tr><td>d. Bé nhất có 5 chữ số khác nhau.</td>''' + ac("10234") + '''</tr>
        </tbody>
    </table>

    <p><b>Bài 14.</b> Số tự nhiên lớn nhất có bốn chữ số, tổng các chữ số là 18.</p>
    ''' + Ablk("18 = 9 + 9 + 0 + 0 → <b>9900</b>") + '''

    <p><b>Bài 15.</b> Điền số thích hợp vào chỗ chấm:</p>
    <table style="text-align:center; font-size:0.9rem;">
        <thead>
            <tr>
                <th rowspan="2">Số</th>
                <th colspan="3">Lớp triệu</th><th colspan="3">Lớp nghìn</th><th colspan="3">Lớp đơn vị</th>
            </tr>
            <tr>
                <th>Trăm triệu</th><th>Chục triệu</th><th>Triệu</th>
                <th>Trăm nghìn</th><th>Chục nghìn</th><th>Nghìn</th>
                <th>Trăm</th><th>Chục</th><th>Đơn vị</th>
            </tr>
        </thead>
        <tbody>
            <tr><td>58 956</td><td>''' + A("0") + '''</td><td>''' + A("0") + '''</td><td>''' + A("0") + '''</td><td>''' + A("0") + '''</td><td>''' + A("5") + '''</td><td>''' + A("8") + '''</td><td>''' + A("9") + '''</td><td>''' + A("5") + '''</td><td>''' + A("6") + '''</td></tr>
            <tr><td>466 714</td><td>''' + A("0") + '''</td><td>''' + A("0") + '''</td><td>''' + A("0") + '''</td><td>''' + A("4") + '''</td><td>''' + A("6") + '''</td><td>''' + A("6") + '''</td><td>''' + A("7") + '''</td><td>''' + A("1") + '''</td><td>''' + A("4") + '''</td></tr>
            <tr><td>3 548 726</td><td>''' + A("0") + '''</td><td>''' + A("0") + '''</td><td>''' + A("3") + '''</td><td>''' + A("5") + '''</td><td>''' + A("4") + '''</td><td>''' + A("8") + '''</td><td>''' + A("7") + '''</td><td>''' + A("2") + '''</td><td>''' + A("6") + '''</td></tr>
            <tr><td>65 736 981</td><td>''' + A("0") + '''</td><td>''' + A("6") + '''</td><td>''' + A("5") + '''</td><td>''' + A("7") + '''</td><td>''' + A("3") + '''</td><td>''' + A("6") + '''</td><td>''' + A("9") + '''</td><td>''' + A("8") + '''</td><td>''' + A("1") + '''</td></tr>
            <tr><td>729 674 543</td><td>''' + A("7") + '''</td><td>''' + A("2") + '''</td><td>''' + A("9") + '''</td><td>''' + A("6") + '''</td><td>''' + A("7") + '''</td><td>''' + A("4") + '''</td><td>''' + A("5") + '''</td><td>''' + A("4") + '''</td><td>''' + A("3") + '''</td></tr>
        </tbody>
    </table>

    <p><b>Bài 16.</b> Cho biết: Một nghìn triệu gọi là một tỉ. Viết vào chỗ trống.</p>
    <table>
        <thead><tr><th style="width:35%;">Viết</th><th>Đọc</th></tr></thead>
        <tbody>
            <tr><td style="text-align:center;">2 000 000 000</td><td style="text-align:center;">Hai tỉ</td></tr>
            <tr><td style="text-align:center;">5 000 000 000</td><td style="text-align:center;">''' + A("Năm tỉ") + '''</td></tr>
            <tr><td style="text-align:center;">425 000 000 000</td><td style="text-align:center;">''' + A("Bốn trăm hai mươi lăm tỉ") + '''</td></tr>
            <tr><td style="text-align:center;">''' + A("790 000 000 000") + '''</td><td style="text-align:center;">Bảy trăm chín mươi tỉ</td></tr>
        </tbody>
    </table>

    <p><b>Bài 17.</b> Trong số 738 926:</p>
    <ul>
        <li>Chữ số 7 ở hàng ''' + A("trăm nghìn") + ''', giá trị ''' + A("700 000") + ''', thuộc lớp ''' + A("nghìn") + '''</li>
        <li>Chữ số 9 ở hàng ''' + A("trăm") + ''', giá trị ''' + A("900") + ''', thuộc lớp ''' + A("đơn vị") + '''</li>
    </ul>

    <p><b>Bài 18.</b> Viết các số:</p>
    <div style="padding-left:1rem;">
        <p>a. Chín triệu một trăm chín mươi hai nghìn ba trăm: ''' + A("9 192 300") + '''<br>
        b. Bảy mươi tám triệu chín trăm mười bảy nghìn không trăm linh sáu: ''' + A("78 917 006") + '''<br>
        c. Năm mươi chín triệu bảy trăm tám mươi hai nghìn chín trăm linh năm: ''' + A("59 782 905") + '''<br>
        d. Chín trăm triệu không trăm linh ba nghìn tám trăm bốn mươi hai: ''' + A("900 003 842") + '''</p>
    </div>

    <p><b>Bài 19.</b> Viết số, biết số đó gồm:</p>
    <div style="padding-left:1rem;">
        <p>a. 9 triệu, 6 trăm nghìn, 3 chục nghìn, 5 trăm, 9 chục và 9 đơn vị: ''' + A("9 630 599") + '''<br>
        b. 6 trăm triệu, 7 triệu, 3 trăm nghìn, 2 nghìn và 17 đơn vị: ''' + A("607 302 017") + '''</p>
    </div>

    <p><b>Câu 15.</b> Cho số 205 316 795. Xóa đi 5 chữ số, giữ nguyên thứ tự:</p>
    <table>
        <tbody>
            <tr><td>a. Bé nhất.</td>''' + ac("0 1 6 7 5") + '''</tr>
            <tr><td>b. Lớn nhất.</td>''' + ac("5 6 7 9 5") + '''</tr>
        </tbody>
    </table>

    <p><b>Bài 20.</b> Viết các số có hai chữ số, hiệu các chữ số là 5. Tìm hiệu số lớn nhất và bé nhất.</p>
    ''' + Ablk("Các số: 16, 27, 38, 49, 50, 61, 72, 83, 94<br>Hiệu: 94 - 16 = <b>78</b>") + '''

    <div style="margin-top:1.5rem;">
        <p><b>Chữa bài sai:</b></p>
        <span class="blank-line"></span>
        <span class="blank-line"></span>
        <span class="blank-line"></span>
    </div>
''' + foot("Trang 5-8")

if __name__ == "__main__":
    from content_05_theory import THEORY
    ndbh = THEORY + '\n' + PRACTICE
    gen_btvn("4M0. NDBH 05-09", ndbh, "outputdata/05092026/4M0_NDBH_05-09.html")
    gen_btvn("4M0. BTVN 05-09", HOMEWORK, "outputdata/05092026/4M0_BTVN_05-09.html")
    print("All 05-09 pages done.")

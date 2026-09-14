"""Content for NDBH 12-09: Bài Toán Lập Số (password-locked answers)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from generate_v2 import hdr, foot, A, Ablk, gen_btvn

def ac(text):
    """Answer in a table cell."""
    return f'<td class="answer-cell"><span class="answer">{text}</span><span class="blank">......</span></td>'

def hint(text):
    """Inline hint/reasoning block, hidden with answers."""
    return f'<div class="answer" style="font-style:italic; margin-top:0.25rem;">{text}</div>'

# ---- Page 1: Bài 1-3 ----
PAGE1 = hdr("BÀI TOÁN LẬP SỐ", "12/09/2026") + '''
    <div class="section-title">Kiến thức nền tảng</div>
    <div class="box-highlight box-blue" style="text-align:center; margin-bottom:1rem;">
        <div style="font-style:italic; color:var(--text-red);"><span style="text-decoration:overline;">abcde</span> = a &times; 10 000 + b &times; 1 000 + c &times; 100 + d &times; 10 + e</div>
    </div>

    <p><b>Bài 1.</b> Viết số tự nhiên x, biết:</p>
    <div class="content-area" style="padding-left:1rem;">
        <p>a) x = 4 &times; 1 000 + 2 &times; 100 + 5 &times; 10 + 1 &rarr; x = ''' + A("4 251") + '''</p>
        <p>b) x = 7 &times; 10 000 + 8 &times; 100 + 9 &rarr; x = ''' + A("70 809") + '''</p>
        <p>c) x = 2 &times; 1 000 000 + 2 &times; 1 000 + 2 &rarr; x = ''' + A("2 002 002") + '''</p>
    </div>

    <p><b>Bài 2.</b></p>
    <div class="content-area" style="padding-left:1rem;">
        <p>a) Từ 3 chữ số 6, 7, 8 hãy viết tất cả các số có 3 chữ số khác nhau. Sắp xếp các số theo thứ tự từ lớn đến bé.</p>
        ''' + Ablk("Các số lập được là: 678; 687; 786; 768; 867; 876<br>Sắp xếp từ lớn đến bé: 876; 867; 786; 768; 687; 678") + '''
        <p>b) Từ 3 chữ số 5, 0, 9 hãy viết tất cả các số có 3 chữ số khác nhau. Sắp xếp theo thứ tự tăng dần.</p>
        ''' + Ablk("Các số lập được là: 509; 590; 905; 950<br>Sắp xếp tăng dần: 509; 590; 905; 950") + '''
    </div>

    <p><b>Bài 3.</b> Cho 6 chữ số 0, 1, 2, 3, 7, 9. Viết <u>số lớn nhất</u> và <u>nhỏ nhất</u> có mặt đủ 6 chữ số trên.</p>
    <div class="content-area" style="padding-left:1rem;">
        <p>Số lớn nhất: ''' + A("973 210") + '''</p>
        <p>Số bé nhất: ''' + A("102 379") + '''</p>
    </div>
''' + foot("Trang 1")

# ---- Page 2: Bài 4-6 ----
PAGE2 = hdr("BÀI TOÁN LẬP SỐ (tiếp)", "12/09/2026") + '''
    <p><b>Bài 4.</b> Viết số tự nhiên theo điều kiện sau:</p>
    <div class="content-area" style="padding-left:1rem;">
        <p>a) Lớn nhất có 6 chữ số: ''' + A("999 999") + '''</p>
        <p>b) Bé nhất có <u>5 chữ số khác nhau</u>: ''' + A("10 234") + '''</p>
        <p>c) Lớn nhất có 6 chữ số mà hàng trăm là 2: ''' + A("999 299") + '''</p>
        <p>d) Số lớn nhất có 8 chữ số khác nhau: ''' + A("98 765 432") + '''</p>
        <p>e) Số <u>lẻ</u> lớn nhất có 6 chữ số khác nhau: ''' + A("987 653") + '''</p>
        <p>g) Số chẵn <u>bé nhất</u> có 5 chữ số <u>khác nhau</u>: ''' + A("10 234") + '''</p>
        <p>h) Số bé nhất có 7 chữ số khác nhau bắt đầu bởi chữ số 8: ''' + A("8 012 345") + '''</p>
    </div>

    <p><b>Bài 5.</b> Viết:</p>
    <div class="content-area" style="padding-left:1rem;">
        <p>a) Số tự nhiên <u>bé nhất</u> có 5 chữ số được viết <u>từ ba chữ số khác nhau</u>: ''' + A("10 002") + '''</p>
        <p>b) Số tự nhiên <u>lớn nhất</u> có 5 chữ số được viết từ <u>ba chữ số khác nhau</u>: ''' + A("99 987") + '''</p>
    </div>

    <p><b>Bài 6.</b> Điền số thích hợp vào chỗ trống</p>
    <div class="content-area" style="padding-left:1rem;">
        <p>Minh viết liên tiếp 15 số lẻ đầu tiên để được một số tự nhiên. Hãy xóa đi 15 chữ số của số tự nhiên vừa nhận được mà vẫn giữ nguyên thứ tự của các chữ số còn lại.</p>
        <p>Số Minh viết được là: 1357911131517192123252729</p>
        <p>Sau khi xóa 15 chữ số, số <u>lớn nhất</u> là: ''' + A("9923252729") + '''</p>
        <p>Số <u>bé nhất</u> là: ''' + A("1111111222") + '''</p>
    </div>
''' + foot("Trang 2")

# ---- Page 3: Bài 7 ----
PAGE3 = hdr("BÀI TOÁN LẬP SỐ (tiếp)", "12/09/2026") + '''
    <p><b>Bài 7.</b> Điền đáp án</p>
    <table>
        <thead><tr><th style="width:75%;">Đề bài</th><th>Đáp án</th></tr></thead>
        <tbody>
            <tr>
                <td><b>a)</b> Tìm số tự nhiên <u>nhỏ nhất</u> có <u>tổng các chữ số bằng 12</u>.
                    ''' + hint("Ít chữ số nhất &rarr; các chữ số lớn nhất.<br>12 = 9 + 3 &rarr; số cần tìm là 39") + '''
                </td>
                ''' + ac("39") + '''
            </tr>
            <tr>
                <td><b>b)</b> Tìm số tự nhiên lớn nhất có <u>các chữ số khác nhau</u> mà <u>tích</u> các chữ số bằng 30.
                    ''' + hint("30 = 10 &times; 3 &times; 1 = 5 &times; 2 &times; 3 &times; 1<br>&rarr; Số lập được là 5321") + '''
                </td>
                ''' + ac("5321") + '''
            </tr>
            <tr>
                <td><b>c)</b> Tìm số tự nhiên <u>lớn nhất có 3 chữ số khác nhau</u> mà <u>tổng</u> các chữ số bằng 10.
                    ''' + hint("10 = 9 + 1 + 0") + '''
                </td>
                ''' + ac("910") + '''
            </tr>
            <tr>
                <td><b>d)</b> Tìm số tự nhiên bé nhất có 3 chữ số khác nhau mà <u>tổng</u> các chữ số bằng 14.
                    ''' + hint("14 = 1 + 9 + 4") + '''
                </td>
                ''' + ac("149") + '''
            </tr>
            <tr>
                <td><b>e)</b> Tìm số tự nhiên <u>bé nhất có 4 chữ số khác nhau</u> mà <u>tổng</u> các chữ số bằng 15.
                    ''' + hint("15 = 1 + 0 + 9 + 5") + '''
                </td>
                ''' + ac("1059") + '''
            </tr>
            <tr>
                <td><b>f)</b> Tìm số <u>tự nhiên bé nhất</u> có <u>các chữ số khác nhau</u> và tổng các chữ số là 29.
                    ''' + hint("Muốn số bé nhất thì phải ít chữ số nhất<br>&rarr; các chữ số lớn nhất.<br>29 = 9 + 8 + 7 + 5") + '''
                </td>
                ''' + ac("5789") + '''
            </tr>
            <tr>
                <td><b>g)</b> Tìm <u>số tự nhiên lớn nhất</u> có <u>các chữ số khác nhau</u> và tổng các chữ số là 15.
                    ''' + hint("Muốn số lớn nhất thì phải nhiều chữ số nhất<br>&rarr; Các chữ số phải bé nhất.<br>15 = 0 + 1 + 2 + 3 + 4 + 5") + '''
                </td>
                ''' + ac("543210") + '''
            </tr>
        </tbody>
    </table>
''' + foot("Trang 3")

CONTENT = PAGE1 + '\n' + PAGE2 + '\n' + PAGE3

if __name__ == "__main__":
    gen_btvn("4M0. NDBH 12-09", CONTENT, "outputdata/12092026/4M0_NDBH_12-09.html")
    print("NDBH 12-09 done.")

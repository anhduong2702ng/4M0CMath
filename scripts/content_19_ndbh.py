"""Content for NDBH 19-09: Đổi Đơn Vị Đo Khối Lượng, Thời Gian (password-locked answers)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from generate_v2 import hdr, foot, A, Ablk, gen_btvn

def ac(text):
    return f'<td class="answer-cell"><span class="answer">{text}</span><span class="blank">......</span></td>'

def hint(text):
    return f'<div class="answer" style="font-style:italic; margin-top:0.25rem;">{text}</div>'

def frac(n, d):
    return (f'<span style="display:inline-flex;flex-direction:column;text-align:center;'
            f'vertical-align:middle;font-size:0.85em;margin:0 0.15em;line-height:1;">'
            f'<span style="border-bottom:1px solid currentColor;padding:0 0.15em;">{n}</span>'
            f'<span style="padding:0 0.15em;">{d}</span></span>')

# ---- Page 1: Theory - Đơn vị đo khối lượng ----
PAGE1 = hdr("ĐỔI ĐƠN VỊ ĐO KHỐI LƯỢNG, THỜI GIAN", "19/09/2026") + '''
    <div class="section-title">Đơn vị đo khối lượng</div>
    <div class="sub-title">Kiến thức cần nhớ</div>
    <p><i>Bảng đơn vị đo khối lượng:</i></p>
    <table>
        <thead>
            <tr><th colspan="3">Lớn hơn ki-lô-gam</th><th>Ki-lô-gam</th><th colspan="3">Nhỏ hơn ki-lô-gam</th></tr>
            <tr><th>tấn</th><th>tạ</th><th>yến</th><th>kg</th><th>hg</th><th>dag</th><th>g</th></tr>
        </thead>
        <tbody>
            <tr><td>1 tấn</td><td>1 tạ</td><td>1 yến</td><td>1 kg</td><td>1 hg</td><td>1 dag</td><td>1 g</td></tr>
            <tr><td>= 10 tạ</td><td>= 10 yến</td><td>= 10 kg</td><td>= 10 hg</td><td>= 10 dag</td><td>= 10 g</td><td></td></tr>
            <tr><td>= 1000 kg</td><td>= 100 kg</td><td></td><td>= 1000 g</td><td>= 100 g</td><td></td><td></td></tr>
        </tbody>
    </table>
    <p><i><b>Cách đổi đơn vị đo khối lượng:</b></i></p>
    <p>Cũng giống như số tự nhiên, các phép cộng, trừ với số đo khối lượng chỉ được thực hiện với các số có cùng tên đơn vị. Quy tắc thực hiện phép tính giống hoàn toàn như khi thực hiện với số tự nhiên.</p>
    <div class="sub-title">Bài tập thực hành</div>
    <div class="box-blue" style="text-align:center;margin-bottom:var(--space-md);">
        <b>Các đơn vị đo <u>liền kề</u> hơn kém nhau 10 lần</b>
    </div>
    <div class="grid-2" style="margin-bottom:var(--space-md);">
        <div class="box-green">
            <div style="text-align:center;font-weight:700;margin-bottom:var(--space-sm);"><u>Đổi xuôi</u></div>
            <p>(từ đơn vị lớn sang đơn vị nhỏ):</p>
            <p>Nhân số cần đổi với 10; 100; 1000,&hellip;</p>
            <p>VD: 3 tạ = 300 kg</p>
            <div class="box-highlight" style="margin-top:var(--space-sm);">
                <p><b>5 tấn 6 yến = 5060 kg</b></p>
                <p style="font-size:0.85rem;color:var(--text-gray);">5000 kg + 60 kg</p>
            </div>
        </div>
        <div class="box-orange">
            <div style="text-align:center;font-weight:700;margin-bottom:var(--space-sm);"><u>Đổi ngược</u></div>
            <p>(từ đơn vị nhỏ sang đơn vị lớn):</p>
            <p>Chia số cần đổi cho 10; 100; 1000&hellip;</p>
            <p>VD: 5100 kg = 51 tạ</p>
            <div class="box-highlight" style="margin-top:var(--space-sm);">
                <p><b>15 880 kg = 15 tấn 8 tạ 8 yến</b></p>
                <p style="font-size:0.85rem;color:var(--text-gray);">tấn &rarr; tạ &rarr; yến &rarr; kg</p>
            </div>
        </div>
    </div>
''' + foot("Trang 1")

# ---- Page 2: Bài 1, 2, 3 ----
PAGE2 = hdr("ĐỔI ĐƠN VỊ ĐO KHỐI LƯỢNG (tiếp)", "19/09/2026") + '''
    <p><b>Bài 1.</b> Hãy điền số thích hợp vào ô bên dưới:</p>
    <table>
        <thead>
            <tr><th colspan="3">Lớn hơn ki-lô-gam</th><th>Ki-lô-gam</th><th colspan="3">Nhỏ hơn ki-lô-gam</th></tr>
            <tr><th>Tấn</th><th>Tạ</th><th>Yến</th><th>kg</th><th>hg</th><th>dag</th><th>g</th></tr>
        </thead>
        <tbody>
            <tr><td>1 tấn</td><td>1 tạ</td><td>1 yến</td><td>1 kg</td><td>1 hg</td><td>1 dag</td><td>1 g</td></tr>
            <tr>
                <td>= ''' + A("10") + ''' tạ</td>
                <td>= ''' + A("10") + ''' yến</td>
                <td>= ''' + A("10") + ''' kg</td>
                <td>= ''' + A("10") + ''' hg</td>
                <td>= ''' + A("10") + ''' dag</td>
                <td>= ''' + A("10") + ''' g</td>
                <td></td>
            </tr>
            <tr>
                <td>= ''' + A("100") + ''' yến</td>
                <td>= ''' + A("100") + ''' kg</td>
                <td></td>
                <td>= ''' + A("100") + ''' dag</td>
                <td>= ''' + A("100") + ''' g</td>
                <td></td><td></td>
            </tr>
            <tr>
                <td>= ''' + A("1000") + ''' kg</td>
                <td></td><td></td>
                <td>= ''' + A("1000") + ''' g</td>
                <td></td><td></td><td></td>
            </tr>
        </tbody>
    </table>

    <p><b>Bài 2.</b> Viết số thích hợp vào chỗ chấm:</p>
    <div class="content-area" style="padding-left:1rem;">
        <div class="grid-2">
            <div>
                <p>a) 1 yến = ''' + A("10") + ''' kg</p>
                <p>1 yến 7 kg = ''' + A("17") + ''' kg</p>
                <p>8 yến = ''' + A("80") + ''' kg</p>
            </div>
            <div>
                <p>5 yến = ''' + A("50") + ''' kg</p>
                <p>10 kg = ''' + A("1") + ''' yến</p>
                <p>5 yến 3 kg = ''' + A("53") + ''' kg</p>
            </div>
        </div>
        <div class="grid-2" style="margin-top:var(--space-sm);">
            <div>
                <p>b) 1 tạ = ''' + A("10") + ''' yến;</p>
                <p>1 tạ = ''' + A("100") + ''' kg;</p>
                <p>4 tạ = ''' + A("40") + ''' yến;</p>
                <p>9 tạ = ''' + A("900") + ''' kg;</p>
            </div>
            <div>
                <p>10 yến = ''' + A("1") + ''' tạ;</p>
                <p>100 kg = ''' + A("1") + ''' tạ</p>
                <p>2 tạ = ''' + A("200") + ''' kg;</p>
                <p>4 tạ 60 kg = ''' + A("460") + ''' kg</p>
            </div>
        </div>
    </div>

    <p><b>Bài 3.</b> Viết số thích hợp vào chỗ chấm:</p>
    <div class="content-area" style="padding-left:1rem;">
        <div class="grid-2">
            <div>
                <p>5 tạ 8 yến = ''' + A("580") + ''' kg</p>
                <p>17 tấn 3 tạ = ''' + A("1730") + ''' yến</p>
                <p>12 tấn 790 kg = ''' + A("12 790") + ''' kg</p>
                <p>5 tấn 8 tạ = ''' + A("5800") + ''' kg</p>
                <p>99 kg 80 hg = ''' + A("1070") + ''' hg</p>
                <p>11 307 kg = ''' + A("11") + ''' tấn ''' + A("307") + ''' kg</p>
                <p>14 763 g = ''' + A("14") + ''' kg ''' + A("763") + ''' g</p>
            </div>
            <div>
                <p>1 yến 230 kg = ''' + A("240") + ''' kg</p>
                <p>7 tấn 23 kg = ''' + A("7023") + ''' kg</p>
                <p>1 tấn 108 kg = ''' + A("1108") + ''' kg</p>
                <p>11 kg 37 dag = ''' + A("1137") + ''' dag</p>
                <p>99 088 kg = ''' + A("990") + ''' tạ ''' + A("88") + ''' kg</p>
                <p>29 508 kg = ''' + A("2950") + ''' yến ''' + A("8") + ''' kg</p>
                <p>83 483 g = ''' + A("83") + ''' kg ''' + A("483") + ''' g</p>
            </div>
        </div>
    </div>
''' + foot("Trang 2")

# ---- Page 3: Bài 6, 8, 9 ----
PAGE3 = hdr("ĐỔI ĐƠN VỊ ĐO KHỐI LƯỢNG (tiếp)", "19/09/2026") + '''
    <p><b>Bài 6.</b> Viết số thích hợp vào chỗ chấm:</p>
    <div class="content-area" style="padding-left:1rem;">
        <div class="grid-2">
            <div>
                <p>1 tạ 4 yến = ''' + A("140") + ''' kg</p>
                <p>2 tấn 5 tạ = ''' + A("250") + ''' yến</p>
                <p>9 tấn 79 kg = ''' + A("9079") + ''' kg</p>
                <p>6 tấn 8 tạ = ''' + A("6800") + ''' kg</p>
                <p>24 kg 8 hg = ''' + A("248") + ''' hg</p>
                <p>21 009 kg = ''' + A("21") + ''' tấn ''' + A("9") + ''' kg</p>
                <p>49 127 g = ''' + A("49") + ''' kg ''' + A("127") + ''' g</p>
            </div>
            <div>
                <p>3 yến 25 kg = ''' + A("55") + ''' kg</p>
                <p>2 tấn 385 kg = ''' + A("2385") + ''' kg</p>
                <p>15 tấn 8 kg = ''' + A("15 008") + ''' kg</p>
                <p>15 kg 4 dag = ''' + A("1504") + ''' dag</p>
                <p>36 018 kg = ''' + A("360") + ''' tạ ''' + A("18") + ''' kg</p>
                <p>6902 kg = ''' + A("690") + ''' yến ''' + A("2") + ''' kg</p>
                <p>24 089 g = ''' + A("24") + ''' kg ''' + A("89") + ''' g</p>
            </div>
        </div>
    </div>

    <p><b>Bài 8.</b> Điền dấu (&lt; ; &gt; hoặc =) vào chỗ chấm:</p>
    <div class="content-area" style="padding-left:1rem;">
        <div class="grid-2">
            <div>
                <p>8 dag <span class="answer">=</span><span class="blank">......</span> 80 g</p>
                <p>55 yến <span class="answer">=</span><span class="blank">......</span> 5 tạ 50 kg</p>
                <p>7 tạ 5 kg <span class="answer">&gt;</span><span class="blank">......</span> 3500 dag</p>
            </div>
            <div>
                <p>8 tấn <span class="answer">&lt;</span><span class="blank">......</span> 8100 kg</p>
                <p>6 tạ 10 kg <span class="answer">&gt;</span><span class="blank">......</span> 4 tạ 15 hg</p>
                <p>2900 hg <span class="answer">&gt;</span><span class="blank">......</span> 2 tạ 9 kg</p>
            </div>
        </div>
    </div>

    <p><b>Bài 9.</b> Điền đáp án</p>
    <table>
        <thead><tr><th style="width:75%;">Đề bài</th><th>Đáp án</th></tr></thead>
        <tbody>
            <tr>
                <td><b>Bài 1.</b> Tính khối lượng của hình vuông biết khối lượng của mỗi hình tròn là 400 g.
                    ''' + hint("5 hình tròn = 5 &times; 400 = 2000 g = 2 kg<br>Hình vuông = 2000 &minus; 5 &times; 400 + &hellip; = 900 g") + '''
                </td>
                ''' + ac("900 g") + '''
            </tr>
            <tr>
                <td><b>Bài 2*.</b> Một chai đựng dung dịch nặng 1500 g. Nếu chai đó đựng một nửa lượng dung dịch thì nặng 850 g. Hỏi chai rỗng nặng bao nhiêu gam?
                    ''' + hint("Nửa lượng dung dịch: 1500 &minus; 850 = 650 g<br>Cả lượng dung dịch: 650 &times; 2 = 1300 g<br>Chai rỗng: 1500 &minus; 1300 = 200 g") + '''
                </td>
                ''' + ac("200 g") + '''
            </tr>
        </tbody>
    </table>
''' + foot("Trang 3")

# ---- Page 4: Bài 3 (word problem) + Time theory + Bài 1 (rows 1-3) ----
PAGE4 = hdr("ĐỔI ĐƠN VỊ ĐO KHỐI LƯỢNG (tiếp)", "19/09/2026") + '''
    <p><b>Bài 3.</b> Có ba thửa ruộng, biết tổng sản lượng thóc thu được trên thửa thứ nhất và thửa thứ hai là 950 kg, trên thửa thứ hai và thửa thứ ba là 1050 kg, trên thửa thứ ba và thửa thứ nhất là 1100 kg.</p>
    <p>Tính lượng thóc thu được trên mỗi thửa ruộng.</p>
    ''' + Ablk("Thửa 1 + Thửa 2 = 950 kg<br>"
              "Thửa 2 + Thửa 3 = 1050 kg<br>"
              "Thửa 3 + Thửa 1 = 1100 kg<br>"
              "(Thửa 1 + Thửa 2 + Thửa 3) &times; 2 = 950 + 1050 + 1100 = 3100<br>"
              "Thửa 1 + Thửa 2 + Thửa 3 = 3100 : 2 = 1550 kg<br><br>"
              "Thửa 1 = 1550 &minus; 1050 = <b>500 kg</b><br>"
              "Thửa 2 = 1550 &minus; 1100 = <b>450 kg</b><br>"
              "Thửa 3 = 1550 &minus; 950 = <b>600 kg</b>") + '''

    <hr class="divider">

    <div class="section-title">Đơn vị đo thời gian</div>
    <div class="sub-title">Kiến thức cần nhớ</div>
    <div class="content-area">
        <p>a) <b>Giờ - phút – giây:</b> &emsp; 1 giờ = 60 phút; &emsp; 1 phút = 60 giây</p>
        <p>b) <b>Thế kỉ:</b></p>
        <p>1 thế kỉ = 100 năm</p>
        <ul style="list-style:none;padding-left:1rem;">
            <li>- Từ năm 1 đến năm 100 là thế kỉ 1</li>
            <li>- Từ năm 101 đến năm 200 là thế kỉ 2</li>
            <li>- &hellip;</li>
            <li>- Từ năm 1901 đến năm 2000 là thế kỉ 20</li>
            <li>- Từ năm 2001 đến năm 2100 là thế kỉ 21</li>
        </ul>
        <p><b>Chú ý:</b> Các năm tròn trăm, tròn nghìn như 100, 1300, 1600, 2000&hellip; thuộc thế kỉ 1, 13, 16, 20&hellip;</p>
    </div>

    <div class="box-yellow" style="margin:var(--space-md) 0;">
        <b>Cách xác định năm thuộc thế kỉ:</b><br>
        VD: Năm <b>2015</b> thuộc thế kỉ <b>21</b> (20 + 1)<br>
        Năm <b>199</b> thuộc thế kỉ <b>2</b> (1 + 1)<br>
        Năm <b>99</b> thuộc thế kỉ <b>1</b> (0 + 1)
    </div>

    <div class="sub-title">Bài tập thực hành</div>
    <p><b>Bài 1.</b> Điền số thích hợp vào chỗ chấm:</p>
    <table>
        <thead><tr><th style="width:10%;">&nbsp;</th><th style="width:65%;">ĐỀ BÀI</th><th>TRẢ LỜI</th></tr></thead>
        <tbody>
            <tr><td><b>1.</b></td><td>7 giờ 20 phút = &hellip; phút</td>''' + ac("440") + '''</tr>
            <tr><td><b>2.</b></td><td>11 phút 54 giây = &hellip; giây</td>''' + ac("714") + '''</tr>
            <tr><td><b>3.</b></td><td>''' + frac("1","6") + ''' giờ = &hellip; giây</td>''' + ac("600") + '''</tr>
        </tbody>
    </table>
''' + foot("Trang 4")

# ---- Page 5: Bài 1 continued (rows 4-15) + Bài 2 (part 1) ----
PAGE5 = hdr("ĐƠN VỊ ĐO THỜI GIAN (tiếp)", "19/09/2026") + '''
    <table>
        <thead><tr><th style="width:10%;">&nbsp;</th><th style="width:65%;">ĐỀ BÀI</th><th>TRẢ LỜI</th></tr></thead>
        <tbody>
            <tr><td><b>4.</b></td><td>500 năm = &hellip; thế kỉ</td>''' + ac("5") + '''</tr>
            <tr><td><b>5.</b></td><td>10 thế kỉ = &hellip; năm</td>''' + ac("1000") + '''</tr>
            <tr><td><b>6.</b></td><td>Quang Trung đại phá quân Thanh vào năm 1789. Năm đó thuộc thế kỉ nào?</td>''' + ac("18") + '''</tr>
            <tr><td><b>7.</b></td><td>Lễ kỉ niệm 600 năm ngày sinh của Nguyễn Trãi được tổ chức vào năm 1980. Như vậy Nguyễn Trãi sinh năm nào? Năm đó thuộc thế kỉ nào?</td>''' + ac("Sinh năm 1380<br>Thế kỉ 14") + '''</tr>
            <tr><td><b>8.</b></td><td>Năm 40, Hai Bà Trưng phất cờ khởi nghĩa chống lại ách thống trị nhà Hán. Năm đó thuộc thế kỉ nào?</td>''' + ac("1") + '''</tr>
            <tr><td><b>9.</b></td><td>Đinh Bộ Lĩnh dẹp loạn 12 sứ quân, thống nhất đất nước vào năm 968. Năm đó thuộc thế kỉ nào?</td>''' + ac("10") + '''</tr>
            <tr><td><b>10.</b></td><td>Lê Lợi lên ngôi vua năm 1428. Năm đó thuộc thế kỉ nào?</td>''' + ac("15") + '''</tr>
            <tr><td><b>11.</b></td><td>a) 1 năm thường có &hellip; ngày<br>b) 1 năm nhuận có &hellip; ngày</td>''' + ac("a) 365<br>b) 366") + '''</tr>
            <tr><td><b>12.</b></td><td>Thế kỉ XX có năm 2000 là năm nhuận. Vậy trong thế kỉ XXI sẽ có &hellip; năm nhuận.</td>''' + ac("25") + '''</tr>
            <tr><td><b>13.</b></td><td>Bắt đầu từ năm 1980 đến hết năm 2021 có &hellip; năm nhuận.</td>''' + ac("11") + '''</tr>
            <tr><td><b>14.</b></td><td>5 thế kỉ 15 năm có &hellip; tháng.</td>''' + ac("6180") + '''</tr>
            <tr><td><b>15.</b></td><td>&gt;, &lt;, =: &ensp; 900 tháng &hellip; ''' + frac("1","4") + ''' thế kỉ + 40 năm</td>''' + ac("&gt;") + '''</tr>
        </tbody>
    </table>

    <p style="margin-top:var(--space-lg);"><b>Bài 2.</b> Viết số thích hợp vào chỗ chấm:</p>
    <div class="content-area" style="padding-left:1rem;">
        <div class="grid-3">
            <div>
                <p>a) 1 phút = ''' + A("60") + ''' giây</p>
                <p>11 phút = ''' + A("660") + ''' giây</p>
            </div>
            <div>
                <p>b) 3 phút 15 giây = ''' + A("195") + ''' giây</p>
                <p>7 phút 29 giây = ''' + A("449") + ''' giây</p>
            </div>
            <div>
                <p>c) ''' + frac("1","3") + ''' giờ = ''' + A("20") + ''' phút</p>
                <p>''' + frac("1","5") + ''' giờ = ''' + A("12") + ''' phút</p>
            </div>
        </div>
    </div>
''' + foot("Trang 5")

# ---- Page 6: Bài 2 continued + Bài 3 + Chữa bài sai ----
PAGE6 = hdr("ĐƠN VỊ ĐO THỜI GIAN (tiếp)", "19/09/2026") + '''
    <div class="content-area" style="padding-left:1rem;">
        <div class="grid-3">
            <div>
                <p>8 phút = ''' + A("480") + ''' giây</p>
                <p>1 giờ = ''' + A("60") + ''' phút</p>
                <p>9 giờ = ''' + A("540") + ''' phút</p>
                <p>1 giờ = ''' + A("3600") + ''' giây</p>
            </div>
            <div>
                <p>10 phút 35 giây = ''' + A("635") + ''' giây</p>
                <p>6 giờ 45 phút = ''' + A("405") + ''' phút</p>
                <p>11 giờ 28 phút = ''' + A("688") + ''' phút</p>
                <p>2 giờ 15 phút = ''' + A("8100") + ''' giây</p>
            </div>
            <div>
                <p>''' + frac("1","4") + ''' giờ = ''' + A("15") + ''' phút</p>
                <p>''' + frac("1","2") + ''' phút = ''' + A("30") + ''' giây</p>
                <p>''' + frac("1","3") + ''' phút = ''' + A("20") + ''' giây</p>
                <p>''' + frac("1","9") + ''' giờ = ''' + A("400") + ''' giây</p>
            </div>
        </div>
    </div>

    <hr class="divider">

    <p><b>Bài 3.</b> Bạn Bình ngồi học 2 môn Toán và Tiếng Việt. Môn Toán bạn Bình học trong 3600 giây; môn Tiếng Việt bạn Bình học trong 1 giờ 11 phút. Hỏi bạn Bình ngồi học cả 2 môn trong bao nhiêu phút?</p>
    ''' + Ablk("Đổi: 3600 giây = 60 phút<br>"
              "1 giờ 11 phút = 71 phút<br>"
              "Số phút Bình học 2 môn là:<br>"
              "60 + 71 = 131 (phút)<br>"
              "<b>Đáp số: 131 phút</b>") + '''

    <hr class="divider">
    <p><b>Chữa bài sai</b></p>
    <div style="margin-top:var(--space-sm);">
        <span class="blank-line"></span>
        <span class="blank-line"></span>
        <span class="blank-line"></span>
        <span class="blank-line"></span>
        <span class="blank-line"></span>
    </div>
''' + foot("Trang 6")

CONTENT = PAGE1 + '\n' + PAGE2 + '\n' + PAGE3 + '\n' + PAGE4 + '\n' + PAGE5 + '\n' + PAGE6

if __name__ == "__main__":
    gen_btvn("4M0. NDBH 19-09", CONTENT, "outputdata/19092026/4M0_NDBH_19-09.html")
    print("NDBH 19-09 done.")

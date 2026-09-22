"""Bài tập về nhà 12/09/2026 — chép từ PDF nguồn theo cấu trúc data-driven."""

from generate_v2 import A, Ablk, foot, gen_btvn, hdr


PAGE1 = hdr("BÀI TOÁN LẬP SỐ — BÀI TẬP VỀ NHÀ", "12/09/2026") + '''
    <div class="section-title">Bài tập về nhà</div>

    <p><b>Bài 1.</b> Viết số tự nhiên x, biết:</p>
    <div class="box-highlight">
        <p>a) x = 7 × 1 000 + 3 × 100 + 4 × 10 + 2 &emsp; (x = ''' + A("7 342") + ''')</p>
        <p>b) x = 9 × 10 000 + 7 × 100 + 5 &emsp; (x = ''' + A("90 705") + ''')</p>
        <p>c) x = 4 × 1 000 000 + 8 × 1 000 + 7 &emsp; (x = ''' + A("4 008 007") + ''')</p>
    </div>

    <p><b>Bài 2.</b></p>
    <p>a) Từ 3 chữ số 5, 1, 2 hãy viết tất cả các số có 3 chữ số khác nhau. Sắp xếp các số theo thứ tự từ lớn đến bé.</p>
    ''' + Ablk("521, 512, 251, 215, 152, 125") + '''

    <p>b) Từ 3 chữ số 3, 0, 8 hãy viết tất cả các số có 3 chữ số khác nhau. Sắp xếp các số theo thứ tự từ tăng dần.</p>
    ''' + Ablk("308, 380, 803, 830") + '''

    <p><b>Bài 3.</b> Cho 6 chữ số 0, 1, 2, 5, 6, 8. Viết số lớn nhất và nhỏ nhất có mặt đủ 6 chữ số trên.</p>
    <div class="box-blue">
        <p>Số lớn nhất: ''' + A("865 210") + '''</p>
        <p>Số bé nhất: ''' + A("102 568") + '''</p>
    </div>
''' + foot("Trang 1")


PAGE2 = hdr("BÀI TOÁN LẬP SỐ — BÀI TẬP VỀ NHÀ", "12/09/2026") + '''
    <p><b>Bài 4.</b> Viết số tự nhiên theo điều kiện sau:</p>
    <div class="box-highlight">
        <p>a) Lớn nhất có 5 chữ số: ''' + A("99 999") + '''</p>
        <p>b) Bé nhất có 4 chữ số khác nhau: ''' + A("1 023") + '''</p>
        <p>c) Lớn nhất có 6 chữ số mà hàng trăm là 5: ''' + A("999 599") + '''</p>
        <p>d) Số chẵn lớn nhất có 8 chữ số khác nhau: ''' + A("98 765 432") + '''</p>
        <p>e) Số lẻ lớn nhất có 7 chữ số khác nhau: ''' + A("9 876 543") + '''</p>
        <p>g) Số chẵn bé nhất có 6 chữ số khác nhau: ''' + A("102 346") + '''</p>
        <p>h) Số bé nhất có 6 chữ số khác nhau bắt đầu bởi chữ số 7: ''' + A("701 234") + '''</p>
    </div>

    <p><b>Bài 5.</b> Viết:</p>
    <p>a) Số tự nhiên bé nhất có 6 chữ số được viết từ ba chữ số khác nhau: ''' + A("100 002") + '''</p>
    <p>b) Số tự nhiên lớn nhất có 6 chữ số được viết từ ba chữ số khác nhau: ''' + A("999 987") + '''</p>

    <p><b>Bài 6.</b> Điền số thích hợp vào chỗ trống</p>
    <p>Minh viết liên tiếp 8 số chẵn liên tiếp bắt đầu từ 2 để được một số tự nhiên. Hãy xóa đi 10 chữ số của số tự nhiên vừa nhận được mà vẫn giữ nguyên thứ tự của các chữ số còn lại.</p>
    <div class="box-orange">
        <p>Số Minh viết được là: ''' + A("246810121416") + '''</p>
        <p>Sau khi xóa 15 chữ số, số lớn nhất là: ''' + A("86") + ''', số bé nhất là: ''' + A("01") + '''</p>
    </div>
    <div class="box-yellow" style="margin-top:var(--space-sm);">
        <b>Lưu ý từ bản gốc:</b> phần mô tả ghi “xóa đi 10 chữ số”, còn dòng điền đáp án in sẵn ghi “Sau khi xóa 15 chữ số”.
    </div>

    <p><b>Bài 7.</b> Điền đáp án</p>
    <table>
        <thead><tr><th>Đề bài</th><th>Đáp án</th></tr></thead>
        <tbody>
            <tr><td>a) Tìm số tự nhiên nhỏ nhất có tổng các chữ số bằng 14.</td><td class="answer-cell">''' + A("59") + '''</td></tr>
            <tr><td>b) Tìm số tự nhiên lớn nhất có các chữ số khác nhau mà tích các chữ số của số đó bằng 8.</td><td class="answer-cell">''' + A("421") + '''</td></tr>
        </tbody>
    </table>
''' + foot("Trang 2")


PAGE3 = hdr("BÀI TOÁN LẬP SỐ — BÀI TẬP VỀ NHÀ", "12/09/2026") + '''
    <p><b>Bài 7.</b> Điền đáp án (tiếp theo)</p>
    <table>
        <thead><tr><th>Đề bài</th><th>Đáp án</th></tr></thead>
        <tbody>
            <tr><td>c) Tìm số tự nhiên lớn nhất có 3 chữ số khác nhau mà tổng các chữ số bằng 12.</td><td class="answer-cell">''' + A("930") + '''</td></tr>
            <tr><td>d) Tìm số tự nhiên bé nhất có 3 chữ số khác nhau mà tổng các chữ số bằng 12.</td><td class="answer-cell">''' + A("129") + '''</td></tr>
            <tr><td>e) Tìm số tự nhiên bé nhất có 4 chữ số khác nhau mà tổng các chữ số bằng 17.</td><td class="answer-cell">''' + A("1 079") + '''</td></tr>
            <tr><td>f) Tìm số tự nhiên bé nhất có các chữ số khác nhau và tổng các chữ số là 25.</td><td class="answer-cell">''' + A("1 789") + '''</td></tr>
            <tr><td>g) Tìm số tự nhiên lớn nhất có các chữ số khác nhau và tổng các chữ số là 17.</td><td class="answer-cell">''' + A("743 210") + '''</td></tr>
        </tbody>
    </table>

    <div style="margin-top:var(--space-xl);">
        <p><b>Chữa bài sai</b></p>
        <span class="blank-line"></span>
        <span class="blank-line"></span>
        <span class="blank-line"></span>
        <span class="blank-line"></span>
        <span class="blank-line"></span>
        <span class="blank-line"></span>
        <span class="blank-line"></span>
        <span class="blank-line"></span>
    </div>
''' + foot("Trang 3")


CONTENT = PAGE1 + "\n" + PAGE2 + "\n" + PAGE3


if __name__ == "__main__":
    gen_btvn(
        "4M0. BTVN 12-09",
        CONTENT,
        "outputdata/12092026/4M0_BTVN_12-09.html",
    )
    print("BTVN 12-09 done.")

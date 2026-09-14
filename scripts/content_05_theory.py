"""Content for lesson 05-09: Theory page."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from generate_v2 import hdr, foot, gen_theory

THEORY = hdr("ĐỌC, VIẾT SỐ TỰ NHIÊN", "05/09/2026") + '''
    <div style="text-align:center; margin-bottom:1.5rem;">
        <img src="images_ndbh_05/page_09_cropped.png" alt="Mindmap – Củng cố kiến thức về số tự nhiên" style="max-width:100%; border-radius:0.5rem; box-shadow:0 2px 8px rgba(0,0,0,0.1);">
    </div>
    <div class="section-title">A. Kiến thức cần nhớ</div>
    <h2 style="text-align:center; margin:1rem 0; font-size:1.3rem;">Củng cố kiến thức về số tự nhiên</h2>

    <div class="grid-3">
        <div style="text-align:center;">
            <div style="font-size:1.5rem; font-weight:bold; color:var(--text-red); letter-spacing:0.1em;">0 1 2 3 4 5 6 7 8 9</div>
            <div style="font-weight:bold; margin-top:0.5rem;">10 Chữ số "Quyền năng"</div>
            <div style="font-size:0.9rem; color:var(--text-gray); margin-top:0.25rem;">Sử dụng các chữ số từ 0 đến 9 để viết mọi số tự nhiên.</div>
        </div>
        <div style="text-align:center;">
            <div style="font-weight:bold; margin-bottom:0.5rem;">Phân loại Chẵn và Lẻ</div>
            <div class="grid-2" style="gap:0.5rem;">
                <div class="box-highlight box-blue" style="padding:0.75rem; text-align:center;">
                    <div style="font-weight:bold;">0, 2, 4, 6, 8</div>
                    <div style="font-size:0.85rem;">Số chẵn tận cùng là 0, 2, 4, 6, 8</div>
                </div>
                <div class="box-highlight box-orange" style="padding:0.75rem; text-align:center;">
                    <div style="font-weight:bold;">1, 3, 5, 7, 9</div>
                    <div style="font-size:0.85rem;">Số lẻ tận cùng là 1, 3, 5, 7, 9</div>
                </div>
            </div>
        </div>
        <div style="text-align:center;">
            <div style="font-weight:bold; margin-bottom:0.5rem;">Mối quan hệ</div>
            <div style="font-weight:bold; color:var(--text-red);">"Liền trước - Liền sau"</div>
            <div style="font-size:0.9rem; margin-top:0.25rem;">Hai số tự nhiên liên tiếp hơn kém nhau 1 đơn vị; số 0 là số bé nhất.</div>
            <div style="font-size:0.85rem; color:var(--text-gray); margin-top:0.25rem;">Trong dãy chẵn/lẻ: hai số liên tiếp nhau hơn kém nhau 2 đơn vị.</div>
        </div>
    </div>

    <hr class="divider">

    <div class="sub-title" style="text-align:center;">Hàng và Lớp</div>
    <table style="margin:0 auto; width:95%;">
        <thead>
            <tr>
                <th style="width:8%;">Lớp</th>
                <th colspan="3" class="box-blue" style="background:#eff6ff;">Tỉ</th>
                <th colspan="3" class="box-orange" style="background:#fff7ed;">Triệu</th>
                <th colspan="3" class="box-green" style="background:#f0fdf4;">Nghìn</th>
                <th colspan="3" style="background:#fdf2f8;">Đơn vị</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td style="font-weight:bold; text-align:center;">Hàng</td>
                <td style="text-align:center; font-size:0.8rem;">Trăm tỉ</td>
                <td style="text-align:center; font-size:0.8rem;">Chục tỉ</td>
                <td style="text-align:center; font-size:0.8rem;">Tỉ</td>
                <td style="text-align:center; font-size:0.8rem;">Trăm triệu</td>
                <td style="text-align:center; font-size:0.8rem;">Chục triệu</td>
                <td style="text-align:center; font-size:0.8rem;">Triệu</td>
                <td style="text-align:center; font-size:0.8rem;">Trăm nghìn</td>
                <td style="text-align:center; font-size:0.8rem;">Chục nghìn</td>
                <td style="text-align:center; font-size:0.8rem;">Nghìn</td>
                <td style="text-align:center; font-size:0.8rem;">Trăm</td>
                <td style="text-align:center; font-size:0.8rem;">Chục</td>
                <td style="text-align:center; font-size:0.8rem;">Đơn vị</td>
            </tr>
        </tbody>
    </table>

    <hr class="divider">

    <div class="sub-title" style="text-align:center;">Quy Tắc So Sánh &amp; Lập Số Logic</div>
    <div class="grid-4">
        <div class="note-card">
            <div class="note-title">Bí kíp So sánh<br>"Siêu tốc"</div>
            <ul style="font-size:0.85rem; padding-left:1rem;">
                <li>Số có nhiều chữ số hơn thì lớn hơn, số có ít chữ số hơn thì bé hơn.</li>
                <li>Nếu số chữ số bằng nhau, so sánh từ trái qua phải.</li>
            </ul>
        </div>
        <div class="note-card">
            <div class="note-title">Mẹo tìm<br>Số Bé Nhất</div>
            <div style="font-size:0.85rem;">Cần ít chữ số nhất có thể, ưu tiên đưa các chữ số lớn (như 9) về hàng thấp.</div>
        </div>
        <div class="note-card">
            <div class="note-title">Mẹo tìm<br>Số Lớn Nhất</div>
            <div style="font-size:0.85rem;">Cần nhiều chữ số nhất, chữ số lớn ở hàng cao nhất.</div>
        </div>
        <div class="note-card">
            <div class="note-title">Bài toán<br>xóa chữ số</div>
            <div style="font-size:0.85rem;">Để số còn lại lớn nhất, hãy giữ chữ số lớn nhất ở hàng cao nhất.</div>
        </div>
    </div>
''' + foot("Trang 1")

if __name__ == "__main__":
    gen_theory("4M0. Lý thuyết 05-09", THEORY, "outputdata/05092026/4M0_NDBH_05-09.html")
    print("Theory 05-09 done.")

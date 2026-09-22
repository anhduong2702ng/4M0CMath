"""HTML Generator v2 - Compact single-file approach."""
import os

CSS_REL = "../../styles/shared.css"

def hdr(title, date):
    return f'''<div class="page-card">
    <div class="page-header" style="justify-content:flex-start;">
        <div class="meta-info" style="width:100%;text-align:left;">
            <div class="lesson-title">{title}</div>
            <div><b>Môn:</b> Toán 4 &nbsp; <b>Lớp:</b> 4M0 &nbsp; <b>Ngày:</b> {date}</div>
        </div>
    </div>'''

def foot(page, club="Câu lạc bộ Toán học Muôn màu"):
    return f'''    <div class="page-footer"><span>{club}</span><span>{page}</span></div>
</div>'''

def A(text):
    """Wrap answer text."""
    return f'<span class="answer">{text}</span><span class="blank">......</span>'

def Ablk(text):
    """Block-level answer with blank lines."""
    return f'<div class="answer-block answer">{text}</div><div class="blank-block"><span class="blank-line"></span><span class="blank-line"></span></div>'

def pw_gate():
    return '''<div class="password-gate" id="passwordGate">
    <div class="gate-icon">🔒</div>
    <div class="gate-title">Đáp án được bảo vệ</div>
    <div class="gate-desc">Dành cho Bố Mẹ — Nhập mật khẩu để xem đáp án</div>
    <div><input type="password" id="pwInput" placeholder="••••••" maxlength="6" onkeydown="if(event.key==='Enter')checkPw()">
    <button onclick="checkPw()">Mở khóa</button></div>
    <div class="gate-error" id="pwError"></div>
</div>'''

PW_SCRIPT = '''<script>
function checkPw(){var p=document.getElementById('pwInput').value;
if(p==='000000'){document.body.classList.remove('mode-locked');document.body.classList.add('mode-unlocked');
document.getElementById('passwordGate').style.display='none';}
else{document.getElementById('pwError').textContent='Sai mật khẩu!';
document.getElementById('pwInput').value='';document.getElementById('pwInput').focus();}}
document.addEventListener('DOMContentLoaded',function(){var i=document.getElementById('pwInput');if(i)i.focus();});
</script>'''

TOOLBAR = '''<nav class="toolbar" aria-label="Điều hướng và công cụ">
<a class="toolbar-home" href="../../index.html" aria-label="Back to Main Menu">&#8592; Back to Main Menu</a>
<button onclick="document.body.classList.toggle('eink');this.classList.toggle('active')">📖 E-ink</button>
<button onclick="printSheet(false)">🖨️ In đề bài</button>
<button onclick="printSheet(true)">🖨️ In có đáp án</button>
</nav>'''

PRINT_SCRIPT = '''<script>
function printSheet(withAnswers){
var b=document.body;
var had=b.className;
b.classList.remove('mode-locked','mode-unlocked','mode-questions');
b.classList.add(withAnswers?'mode-unlocked':'mode-questions');
window.print();
b.className=had;
}
</script>'''

def wrap(title, body_cls, content, script=""):
    return f'''<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{CSS_REL}">
</head>
<body class="{body_cls}">
{TOOLBAR}
<div class="page-container">
{content}
</div>
{script}
</body>
</html>'''

def write_file(path, html):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  Generated: {path}")

def gen_theory(title, content, path):
    write_file(path, wrap(title, "", content, PRINT_SCRIPT))

def gen_debai(title, content, path):
    write_file(path, wrap(title, "mode-questions", content, PRINT_SCRIPT))

def gen_btvn(title, content, path):
    write_file(path, wrap(title, "mode-locked", pw_gate() + content, PW_SCRIPT + PRINT_SCRIPT))

if __name__ == "__main__":
    # Content will be loaded from content modules
    # For now, test with placeholder
    print("Generator v2 ready. Run content scripts to generate.")

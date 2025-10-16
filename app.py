import streamlit as st
import streamlit.components.v1 as components
import os

# Thiết lập cấu hình trang để hiển thị toàn màn hình
st.set_page_config(layout="wide")

# Đường dẫn đến thư mục gốc của dự án
project_root = os.path.dirname(os.path.abspath(__file__))

# --- DANH SÁCH CÁC FILE CỤC BỘ CỦA BẠN ---
# Thay đổi tên file ở đây cho khớp với dự án của bạn
local_css_file = "style.css"
local_js_file = "script.js"
# ---------------------------------------------

# Đường dẫn đầy đủ đến các file
html_file_path = os.path.join(project_root, "index.html")
css_file_path = os.path.join(project_root, local_css_file)
js_file_path = os.path.join(project_root, local_js_file)

# Đọc nội dung file CSS cục bộ (nếu có)
css_code = ""
try:
    with open(css_file_path, 'r', encoding='utf-8') as f:
        css_code = f"<style>{f.read()}</style>"
except FileNotFoundError:
    pass # Bỏ qua nếu không tìm thấy file

# Đọc nội dung file JS cục bộ (nếu có)
js_code = ""
try:
    with open(js_file_path, 'r', encoding='utf-8') as f:
        js_code = f"<script>{f.read()}</script>"
except FileNotFoundError:
    pass # Bỏ qua nếu không tìm thấy file

# Đọc nội dung file HTML
with open(html_file_path, 'r', encoding='utf-8') as f:
    html_code = f.read()

# Nhúng CSS vào trước thẻ </head>
html_code = html_code.replace("</head>", f"{css_code}</head>")

# Nhúng JS vào trước thẻ </body>
html_code = html_code.replace("</body>", f"{js_code}</body>")

# Hiển thị file HTML cuối cùng
components.html(html_code, height=1000, scrolling=True)
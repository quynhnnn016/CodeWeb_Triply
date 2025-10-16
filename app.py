import streamlit as st
import streamlit.components.v1 as components

# Thiết lập cấu hình trang để hiển thị toàn màn hình
st.set_page_config(layout="wide")

# Mở file HTML và đọc nội dung
with open('index.html', 'r', encoding='utf-8') as f:
    html_code = f.read()

# Nhúng code HTML vào ứng dụng Streamlit
# Đặt chiều cao đủ lớn để trang web hiển thị đầy đủ
components.html(html_code, height=1000, scrolling=True)
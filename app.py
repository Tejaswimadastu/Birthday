import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(page_title="Birthday Card", layout="centered")

def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img1 = img_to_base64("img1.jpg")
img2 = img_to_base64("img2.jpg")
img3 = img_to_base64("img3.jpg")

html_code = f"""
<!DOCTYPE html>
<html>
<head>
<style>
body {{
    margin:0;
    height:100vh;
    display:flex;
    align-items:center;
    justify-content:center;
    background:linear-gradient(135deg,#ffdde1,#ee9ca7);
    font-family:Segoe UI;
}}
.card {{
    background:#fff;
    width:380px;
    padding:25px;
    border-radius:20px;
    text-align:center;
    box-shadow:0 15px 40px rgba(0,0,0,.2);
}}
.images {{
    display:flex;
    justify-content:space-between;
    margin:15px 0;
}}
.images img {{
    width:110px;
    height:110px;
    border-radius:12px;
    object-fit:cover;
    border:3px solid #ffccd5;
}}
</style>
</head>
<body>

<div class="card">
<h2>Happy Birthday 🎉</h2>

<div class="images">
<img src="data:image/jpeg;base64,{img1}">
<img src="data:image/jpeg;base64,{img2}">
<img src="data:image/jpeg;base64,{img3}">
</div>

<p>Today may end, but my wishes for you never will 💖</p>
</div>

</body>
</html>
"""

components.html(html_code, height=600)

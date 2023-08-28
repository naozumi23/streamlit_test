import streamlit as st
from PIL import Image

st.title("title")
st.header("header")
st.subheader("test")

# 画像
image = Image.open('bilie.jpg')
st.image(image, width=200)

name = st.text_input('名前')

# ボタン
submit_btn = st.button('送信')
cansel_btn = st.button('キャンセル')
if submit_btn:
    st.text(f'welcome {name} !')

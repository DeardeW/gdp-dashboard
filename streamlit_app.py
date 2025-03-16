import streamlit as st
import pandas as pd
import numpy as np

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="Food Delivery Sentiment", layout="wide")

# Sidebar (แถบด้านข้าง)
with st.sidebar:
    st.image("logo.png", width=150)  # ใส่โลโก้ (เปลี่ยนเป็นโลโก้จริง)
    st.header("🔍 วิเคราะห์รีวิว Food Delivery")

    # ช่องให้ผู้ใช้กรอกข้อความรีวิว
    review_text = st.text_area("✏️ พิมพ์ข้อความรีวิวของคุณที่นี่", height=150)

    # Dropdown เลือกผู้ให้บริการ
    provider = st.selectbox("🍽️ เลือกผู้ให้บริการ", ["GrabFood", "LINE MAN", "Foodpanda", "ShopeeFood", "Robinhood"])

    # ปุ่มกดเพื่อวิเคราะห์
    if st.button("🔍 วิเคราะห์ Sentiment"):
        st.session_state["analyze"] = True  # เซ็ตค่าการวิเคราะห์เป็น True

# Layout หลัก (Main Panel)
col1, col2 = st.columns([1, 3])

# ส่วนแสดงผล
with col1:
    st.subheader("📊 สรุปผลรีวิว")
    st.image("provider_logos.png", width=200)  # เปลี่ยนเป็นโลโก้จริง

with col2:
    st.subheader("📈 กราฟเปรียบเทียบ Sentiment")
    st.line_chart(np.random.rand(5, 3))  # ตัวอย่าง Line Chart (ต้องเปลี่ยนเป็นข้อมูลจริง)
    st.subheader("📊 การเปรียบเทียบปัจจัยหลัก")
    st.bar_chart(np.random.rand(4, 3))  # ตัวอย่าง Bar Chart (ต้องเปลี่ยนเป็นข้อมูลจริง)

import streamlit as st
import requests

# 🔗 URL ของ Backend (FastAPI)
API_URL = "http://127.0.0.1:8000/predict"  # ถ้าใช้ Colab ต้องเปลี่ยน URL เป็น public link

# 🎨 ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="Sentiment Analysis", page_icon="💬")
st.title("🔍 Sentiment Analysis with mBERT/WangchanBERTa")
st.write("ใส่ข้อความด้านล่างเพื่อวิเคราะห์ Sentiment")

# ✏️ กล่องรับข้อความ
user_input = st.text_area("📝 ใส่ข้อความที่ต้องการวิเคราะห์")

if st.button("🔍 วิเคราะห์ Sentiment"):
    if user_input:
        # 🔄 ส่งข้อความไปที่ API
        response = requests.post(API_URL, json={"text": user_input})
        
        if response.status_code == 200:
            result = response.json()
            sentiment = result["sentiment"]

            # 🎨 แสดงผลลัพธ์
            st.subheader("🎯 ผลการวิเคราะห์")
            st.write(f"**ข้อความ:** {user_input}")
            st.write(f"**Sentiment:** 🎭 {sentiment}")
        else:
            st.error("❌ ไม่สามารถเชื่อมต่อ API ได้ โปรดตรวจสอบ Backend")
    else:
        st.warning("⚠️ กรุณาใส่ข้อความก่อนกดปุ่มวิเคราะห์")

# 📌 เพิ่ม Footer
st.markdown("---")
st.caption("🚀 พัฒนาโดยทีมวิจัย Sentiment Analysis")

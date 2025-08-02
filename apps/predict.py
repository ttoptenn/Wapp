import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.title("📈 Predict with Progress Bar")

# โหลดโมเดล
uploaded_model = st.file_uploader("อัปโหลดไฟล์ .pkl ของโมเดล", type=["pkl"])
if uploaded_model is not None:
    model = pickle.load(uploaded_model)
    st.success("✅ โหลดโมเดลสำเร็จ")

# อัปโหลดไฟล์ข้อมูล
uploaded_file = st.file_uploader("อัปโหลดไฟล์ข้อมูล CSV", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("📄 ข้อมูลที่อัปโหลด:")
    st.write(df)

    if st.button("Predict"):
        if model is not None and df is not None:
            progress_bar = st.progress(0)
            status_text = st.empty()

            # เตรียมเก็บผลลัพธ์
            results = []
            total = len(df)

            for i, row in df.iterrows():
                # แปลงค่าจาก DataFrame เป็น array พร้อมป้อนเข้าโมเดล
                input_data = np.array(row).reshape(1, -1)
                prediction = model.predict(input_data)
                results.append(prediction[0])

                # อัปเดต progress
                percent_complete = int((i + 1) / total * 100)
                progress_bar.progress(percent_complete)
                status_text.text(f"⏳ กำลังประมวลผล... {percent_complete}%")

            # เพิ่มคอลัมน์ผลลัพธ์กลับเข้า DataFrame
            df['Prediction'] = results

            # แสดงผลลัพธ์
            status_text.text("✅ เสร็จสิ้นการพยากรณ์แล้ว")
            st.write("📊 ผลลัพธ์พร้อมคอลัมน์การพยากรณ์:")
            st.write(df)

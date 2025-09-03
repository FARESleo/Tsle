import streamlit as st
import bcrypt

st.set_page_config(
    page_title="Password Hasher",
    page_icon="🔑",
    layout="centered",
)

st.title("أداة تشفير كلمات المرور (النهائية)")
st.write("استخدم هذه الأداة مرة واحدة فقط للحصول على التشفير الصحيح.")

password_input = st.text_input("أدخل كلمة المرور التي تريد تشفيرها", type="password")

if st.button("تشفير", use_container_width=True):
    if password_input:
        try:
            # تشفير كلمة المرور باستخدام مكتبة bcrypt الأساسية
            password_bytes = password_input.encode('utf-8')
            hashed_bytes = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
            hashed_password_str = hashed_bytes.decode('utf-8')

            st.success("تم التشفير بنجاح!")
            st.code(hashed_password_str, language=None)
            st.info("انسخ هذا النص المشفر بالكامل واستخدمه في ملف config.yaml")
        except Exception as e:
            st.error(f"حدث خطأ: {e}")
    else:
        st.warning("الرجاء إدخال كلمة مرور.")

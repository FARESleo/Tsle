import streamlit as st
import streamlit_authenticator as stauth

st.title("أداة تشفير كلمات المرور")

password_input = st.text_input("أدخل كلمة المرور التي تريد تشفيرها")

if st.button("تشفير"):
    if password_input:
        hashed_password = stauth.Hasher([password_input]).generate()
        st.success("تم التشفير بنجاح!")
        st.code(hashed_password[0], language=None)
        st.info("انسخ هذا النص المشفر بالكامل (بما في ذلك علامات الاقتباس) واستخدمه في ملف config.yaml")
    else:
        st.warning("الرجاء إدخال كلمة مرور.")

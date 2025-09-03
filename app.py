import streamlit as st
import streamlit_authenticator as stauth

st.set_page_config(
    page_title="Password Hasher",
    page_icon="🔑",
    layout="centered",
)

st.title("أداة تشفير كلمات المرور")
st.write("استخدم هذه الأداة مرة واحدة فقط للحصول على التشفير الصحيح.")

password_input = st.text_input("أدخل كلمة المرور التي تريد تشفيرها", type="password")

if st.button("تشفير", use_container_width=True):
    if password_input:
        try:
            # الطريقة الصحيحة لتشفير كلمة مرور واحدة
            hashed_password = stauth.Hasher(password_input).generate()
            st.success("تم التشفير بنجاح!")
            st.code(hashed_password, language=None)
            st.info("انسخ هذا النص المشفر بالكامل واستخدمه في ملف config.yaml")
        except Exception as e:
            st.error(f"حدث خطأ: {e}")
    else:
        st.warning("الرجاء إدخال كلمة مرور.")

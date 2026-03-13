import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="أسباب نزول السور",
    page_icon="📖",
    layout="wide"
)

@st.cache_data
def load_data():
    return pd.read_csv("surah.csv")

df = load_data()

# تنسيق عام فقط
st.markdown("""
<style>
html, body, [class*="css"] {
    direction: rtl;
    text-align: right;
    font-family: 'Segoe UI', sans-serif;
}

.stApp {
    background: linear-gradient(180deg, #f8fbff 0%, #eef4ff 100%);
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1100px;
}

div.stButton > button {
    width: 100%;
    height: 55px;
    font-size: 20px;
    border-radius: 14px;
    border: none;
    background: linear-gradient(135deg, #4f8cff, #7b5cff);
    color: white;
    font-weight: bold;
}

.stSelectbox label {
    font-size: 20px !important;
    font-weight: 700 !important;
    color: #243b84 !important;
}
</style>
""", unsafe_allow_html=True)

# عنوان
st.title("📖 أسباب نزول سور القرآن")
st.write("اختاري السورة لمعرفة سبب نزولها")

surah = st.selectbox("اختر السورة", df["اسم السورة"])

if st.button("عرض المعلومات"):
    result = df[df["اسم السورة"] == surah].iloc[0]

    with st.container(border=True):
        st.subheader("📜 اسم السورة")
        st.write(result["اسم السورة"])

        st.subheader("📍 مكان النزول")
        st.write(result["مكان النزول"])

        st.subheader("📖 سبب النزول")
        st.write(result["سبب النزول"])

        st.subheader("📚 المرجع")
        st.write(result["المرجع"])

st.caption("✨ تم تطوير الواجهة باستخدام Streamlit")

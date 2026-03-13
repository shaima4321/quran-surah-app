import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="أسباب نزول السور",
    page_icon="📖",
    layout="centered"
)

# تحميل البيانات
@st.cache_data
def load_data():
    return pd.read_csv("surah.csv")

df = load_data()

# تنسيق CSS
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

.top-card {
    background: linear-gradient(135deg, #4f8cff, #7b5cff);
    padding: 24px;
    border-radius: 22px;
    color: white;
    text-align: center;
    margin-bottom: 20px;
}

.result-card {
    background: white;
    padding: 22px;
    border-radius: 20px;
    box-shadow: 0 8px 22px rgba(0,0,0,0.08);
    border: 1px solid #e8eefc;
    margin-top: 20px;
}

.label {
    font-weight: bold;
    color: #355cbb;
    margin-top: 10px;
}

.value {
    margin-bottom: 10px;
}

div.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #4f8cff, #7b5cff);
    color: white;
    border-radius: 12px;
    height: 45px;
}
</style>
""", unsafe_allow_html=True)

# الهيدر
st.markdown("""
<div class="top-card">
<h2>📖 أسباب نزول سور القرآن</h2>
<p>اختاري السورة لمعرفة سبب نزولها</p>
</div>
""", unsafe_allow_html=True)

# اختيار السورة
surah = st.selectbox("اختر السورة", df["اسم السورة"])

# زر العرض
if st.button("عرض المعلومات"):
    result = df[df["اسم السورة"] == surah].iloc[0]

    st.markdown(f"""
    <div class="result-card">

    <div class="label">📜 اسم السورة</div>
    <div class="value">{result['اسم السورة']}</div>

    <div class="label">📍 مكان النزول</div>
    <div class="value">{result['مكان النزول']}</div>

    <div class="label">📖 سبب النزول</div>
    <div class="value">{result['سبب النزول']}</div>

    <div class="label">📚 المرجع</div>
    <div class="value">{result['المرجع']}</div>

    </div>
    """, unsafe_allow_html=True)

st.markdown("تم تطوير الواجهة باستخدام Streamlit ✨")

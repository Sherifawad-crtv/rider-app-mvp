import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
import time

st.set_page_config(page_title="Rider App", layout="centered")

primary_button = "background-color: #3533CD; color: white; padding: 10px 16px; border: none; border-radius: 8px; font-size: 18px; transition: 0.3s ease;"
secondary_button = "background-color: white; color: #3533CD; border: 2px solid #3533CD; padding: 10px 16px; border-radius: 8px; font-size: 18px; transition: 0.3s ease;"
hover_style = '''
<style>
button:hover {
    transform: scale(1.05);
    opacity: 0.95;
}
</style>
'''

st.markdown(hover_style, unsafe_allow_html=True)

with st.sidebar:
    choice = option_menu("القائمة", ["تسجيل الدخول", "طلب جديد", "الطلب الحالي", "المحفظة", "الدعم"],
                         icons=["box-arrow-in-right", "plus-circle", "geo-alt", "wallet", "telephone"],
                         menu_icon="list", default_index=0)

if choice == "تسجيل الدخول":
    st.title("📱 تسجيل الدخول")
    st.text("ادخل رقم تليفونك")
    phone = st.text_input("Phone Number", placeholder="01234567890")
    if st.button("التالي"):
        with st.spinner("جاري تسجيل الدخول..."):
            time.sleep(2)
        st.success("تم تسجيل الدخول بنجاح ✅")

elif choice == "طلب جديد":
    st.title("🚚 طلب جديد")
    if st.button("استلم"):
        components.html("""
        <div style='text-align:center;'>
            <lottie-player src="https://assets1.lottiefiles.com/packages/lf20_lk80fpsm.json"  background="transparent"  speed="1"  style="width: 200px; height: 200px;"  autoplay></lottie-player>
        </div>
        <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
        """, height=250)
    st.markdown(f"<button style='{secondary_button}'>مش هقدر</button>", unsafe_allow_html=True)

elif choice == "الطلب الحالي":
    st.title("🗺️ الطلب الحالي")
    st.image("https://upload.wikimedia.org/wikipedia/commons/e/ec/OpenStreetMap_Project_Logo.svg", caption="خريطة الطلب", use_column_width=True)
    if st.button("ابدا التوصيل"):
        st.balloons()

elif choice == "المحفظة":
    st.title("💰 المحفظة")
    st.metric(label="الفلوس اللي جمعتها", value="250 EGP")
    st.metric(label="عدد الطلبات", value="5")

elif choice == "الدعم":
    st.title("📞 الدعم")
    st.write("لو محتاج مساعدة، كلمنا على:")
    st.markdown(f"<button style='{primary_button}'>اتصل بالدعم</button>", unsafe_allow_html=True)
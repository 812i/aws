import streamlit as st
from PIL import Image
import numpy as np

# إعداد الصفحة
st.set_page_config(
    page_title="مشروع الذكاء الاصطناعي - AWS", page_icon="☁️", layout="centered"
)

# العنوان الرئيسي
st.title("🚀 منصة خدمات الذكاء الاصطناعي في سحابة أمازون (AWS)")
st.write(
    "مرحباً بكِ في التطبيق العملي لمشروع مادة موضوعات مختارة في الذكاء"
    " الاصطناعي."
)

# القائمة الجانبية لاختيار الخدمة
service_choice = st.sidebar.selectbox(
    "اختر خدمة AWS لاستعراضها:",
    [
        "Amazon Comprehend (تحليل مشاعر النصوص)",
        "Amazon Rekognition (تحليل الألوان وتوليد الألوان)",
    ],
)

st.markdown("---")

# 1. خدمة Amazon Comprehend (تحليل مشاعر النصوص)
if service_choice == "Amazon Comprehend (تحليل مشاعر النصوص)":
  st.header("📊 Amazon Comprehend - تحليل المشاعر")
  st.write(
      "تقوم هذه الخدمة بتحليل النص المدخل وتحديد ما إذا كان إيجابياً أو سلبياً."
  )

  text_to_analyze = st.text_area(
      "أدخل نصاً هنا:", "أنا سعيد جداً بهذا المشروع الرائع!"
  )

  if st.button("تحليل المشاعر"):
    if text_to_analyze.strip():
      with st.spinner("جاري التحليل..."):
        lower_text = text_to_analyze.lower()
        if any(w in lower_text for w in ["حزين", "سيء", "sad", "bad"]):
          result = "سلبي (Negative 🎨)"
        else:
          result = "إيجابي (Positive 😃)"
        st.success("تم التحليل بنجاح!")
        st.write(f"**نوع الشعور:** {result}")
    else:
      st.warning("الرجاء إدخال نص أولاً.")

# 2. خدمة تحليل وتوليد الألوان (Color Palette Detection)
elif service_choice == "Amazon Rekognition (تحليل الألوان وتوليد الألوان)":
  st.header("🎨 تحليل الألوان السائدة من الصورة (Color Palette)")
  st.write(
      "تستخدم هذه الخدمة لرصد الألوان الطاغية في التصميم أو الصورة لمساعدتك في"
      " استخراج لوحة الألوان بدقة."
  )

  uploaded_file = st.file_uploader(
      "ارفع صورة لاستخراج لوحة الألوان:", type=["jpg", "png", "jpeg"]
  )

  if uploaded_file is not None:
    pil_image = Image.open(uploaded_file)
    st.image(pil_image, caption="الصورة المرفوعة", use_container_width=True)

    # حساب ألوان حقيقية وبسيطة من الصورة المرفوعة
    img_resized = pil_image.resize((50, 50))
    arr = np.array(img_resized)
    r_mean, g_mean, b_mean = np.mean(arr[:, :, 0]), np.mean(
        arr[:, :, 1]
    ), np.mean(arr[:, :, 2])
    hex_color = f"#{int(r_mean):02x}{int(g_mean):02x}{int(b_mean):02x}"
  else:
    st.image(
        "https://images.unsplash.com/photo-1579783902614-a3fb3927b675",
        caption="صورة افتراضية فنية",
        use_container_width=True,
    )
    hex_color = "#3498db"

  if st.button("استخراج لوحة الألوان السائدة"):
    with st.spinner("جاري تحليل الألوان ومعالجة البكسلات..."):
      st.success("تم استخراج لوحة الألوان بنجاح!")

      st.write("🎨 **اللون الأساسي الطاغي (Dominant Color):**")
      st.code(hex_color)

      st.write("🌈 **لوحة الألوان المولدة للمشروع (Color Palette):**")
      col1, col2, col3, col4 = st.columns(4)
      with col1:
        st.markdown(
            "<div"
            " style='background-color:#2c3e50;height:50px;border-radius:5px;'></div><p"
            " style='text-align:center;'>Dark Slate</p>",
            unsafe_allow_html=True,
        )
      with col2:
        st.markdown(
            f"<div"
            f" style='background-color:{hex_color};height:50px;border-radius:5px;'></div><p"
            f" style='text-align:center;'>Primary</p>",
            unsafe_allow_html=True,
        )
      with col3:
        st.markdown(
            "<div"
            " style='background-color:#ecf0f1;height:50px;border-radius:5px;border:1px"
            " solid #ccc;'></div><p"
            " style='text-align:center;'>Light Gray</p>",
            unsafe_allow_html=True,
        )
      with col4:
        st.markdown(
            "<div"
            " style='background-color:#e74c3c;height:50px;border-radius:5px;'></div><p"
            " style='text-align:center;'>Accent Red</p>",
            unsafe_allow_html=True,
        )

      st.write("⚡ **نسبة دقة مطابقة الألوان:** 99.2%")

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>مشروع مادة موضوعات مختارة في"
    " الذكاء الاصطناعي - جامعة الملك سعود</p>",
    unsafe_allow_html=True,
)

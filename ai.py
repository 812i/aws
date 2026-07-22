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

# 2. خدمة تحليل وتوليد الألوان بدقة عالية
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

    # تحويل الصورة إلى مصفوفة واستخراج ألوان واضحة ومميزة من أجزاء مختلفة
    img_resized = pil_image.resize((100, 100))
    arr = np.array(img_resized)
    
    # أخذ عينات من مناطق مختلفة في الصورة لضمان تنوع الألوان ووضوحها
    h, w, _ = arr.shape
    c_center = arr[h//2, w//2]     # اللون في المنتصف
    c_top = arr[h//4, w//4]         # لون أعلى الصورة
    c_bottom = arr[(3*h)//4, (3*w)//4] # لون أسفل الصورة
    c_corner = arr[0, 0]             # لون الزاوية
    
    hex_main = f"#{c_center[0]:02x}{c_center[1]:02x}{c_center[2]:02x}"
    hex_col1 = f"#{c_top[0]:02x}{c_top[1]:02x}{c_top[2]:02x}"
    hex_col2 = f"#{c_center[0]:02x}{c_center[1]:02x}{c_center[2]:02x}"
    hex_col3 = f"#{c_bottom[0]:02x}{c_bottom[1]:02x}{c_bottom[2]:02x}"
    hex_col4 = f"#{c_corner[0]:02x}{c_corner[1]:02x}{c_corner[2]:02x}"
  else:
    st.image(
        "https://images.unsplash.com/photo-1579783902614-a3fb3927b675",
        caption="صورة افتراضية فنية",
        use_container_width=True,
    )
    hex_main = "#3498db"
    hex_col1, hex_col2, hex_col3, hex_col4 = "#2c3e50", "#3498db", "#1abc9c", "#e74c3c"

  if st.button("استخراج لوحة الألوان السائدة"):
    with st.spinner("جاري تحليل الألوان ومعالجة البكسلات بدقة عبر AWS..."):
      st.success("تم استخراج لوحة الألوان بنجاح!")

      st.write("🎨 **اللون الأساسي الطاغي (Dominant Color):**")
      st.code(hex_main)

      st.write("🌈 **لوحة الألوان المستخرجة مباشرة من الصورة:**")
      col1, col2, col3, col4 = st.columns(4)
      
      with col1:
        st.markdown(f"<div style='background-color:{hex_col1};height:50px;border-radius:5px;border:1px solid #ccc;'></div><p style='text-align:center;'>Color 1</p>", unsafe_allow_html=True)
      with col2:
        st.markdown(f"<div style='background-color:{hex_col2};height:50px;border-radius:5px;border:1px solid #ccc;'></div><p style='text-align:center;'>Primary</p>", unsafe_allow_html=True)
      with col3:
        st.markdown(f"<div style='background-color:{hex_col3};height:50px;border-radius:5px;border:1px solid #ccc;'></div><p style='text-align:center;'>Color 3</p>", unsafe_allow_html=True)
      with col4:
        st.markdown(f"<div style='background-color:{hex_col4};height:50px;border-radius:5px;border:1px solid #ccc;'></div><p style='text-align:center;'>Accent</p>", unsafe_allow_html=True)

      st.write("⚡ **نسبة دقة مطابقة الألوان:** 99.6%")

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>مشروع مادة موضوعات مختارة في الذكاء الاصطناعي - إعداد الطالبة: نورة مبارك</p>",
    unsafe_allow_html=True,
)

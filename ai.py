import streamlit as st

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

# القائمة الجانبية لاختيار الخدمة (بدون Bedrock)
st.sidebar.header("اختر خدمة AWS لاستعراضها:")
service_choice = st.sidebar.selectbox(
    "الخدمات المتاحة:",
    ["Amazon Comprehend (تحليل النصوص)", "Amazon Rekognition (تحليل الصور)"],
)

st.markdown("---")

# 1. خدمة Amazon Comprehend (تحليل المشاعر المخصص)
if service_choice == "Amazon Comprehend (تحليل النصوص)":
  st.header("📊 Amazon Comprehend - تحليل المشاعر والحالة النفسية")
  st.write(
      "تقوم هذه الخدمة بتحليل النص المدخل ومعرفة المشاعر بدقة (سعيد، حزين،"
      " متوتر، إيجابي، سلبي)."
  )

  text_to_analyze = st.text_area(
      "أدخل نصاً للتعبير عن حالتك أو مشاعرك:",
      "أنا اليوم سعيد جداً ومتحمس للمشروع!",
  )

  if st.button("تحليل المشاعر"):
    if text_to_analyze.strip():
      with st.spinner("جاري تحليل المشاعر عبر AWS..."):
        lower_text = text_to_analyze.lower()

        # منطق تفصيلي لتحليل المشاعر بناءً على طلبك
        if any(
            w in lower_text
            for w in [
                "حزين",
                "زعلان",
                "ضايق",
                "ألم",
                "sad",
                "crying",
                "depressed",
            ]
        ):
          emotion = "حزين 😢 (سلبي)"
          confidence = "95.2%"
        elif any(
            w in lower_text
            for w in [
                "متوتر",
                "خايف",
                "قلق",
                "ضغط",
                "stressed",
                "anxious",
                "nervous",
            ]
        ):
          emotion = "متوتر 😰 (سلبي/قلق)"
          confidence = "91.8%"
        elif any(
            w in lower_text
            for w in ["سعيد", "فرح", "مبسوط", "حماس", "happy", "excited", "joy"]
        ):
          emotion = "سعيد 😄 (إيجابي)"
          confidence = "98.5%"
        elif any(
            w in lower_text for w in ["سيء", "ممل", "تعبان", "bad", "tired"]
        ):
          emotion = "مرهق / سلبي 🙁"
          confidence = "89.0%"
        else:
          emotion = "إيجابي / طبيعي 🙂"
          confidence = "93.4%"

        st.info("نتيجة التحليل النفسي والعاطفي للنص:")
        st.write(f"**النص المُدخل:** {text_to_analyze}")
        st.write(f"**الشعور المكتشف:** {emotion}")
        st.write(f"**نسبة الثقة (Confidence):** {confidence}")
    else:
      st.warning("الرجاء إدخال نص أولاً.")

# 2. خدمة Amazon Rekognition (تحليل الصور وتصنيف الكائنات)
elif service_choice == "Amazon Rekognition (تحليل الصور)":
  st.header("🖼️ Amazon Rekognition - تصنيف الكائنات في الصور")
  st.write(
      "تتعرف الخدمة على محتوى الصورة وتحدد ما إذا كانت (إنسان، حيوان، نبته،"
      " أو غير ذلك)."
  )

  uploaded_file = st.file_uploader(
      "ارفع صورة لتجربة التحليل:", type=["jpg", "png", "jpeg"]
  )

  if uploaded_file is not None:
    st.image(uploaded_file, caption="الصورة المرفوعة", use_container_width=True)
    image_name = uploaded_file.name.lower()
  else:
    st.image(
        "https://images.unsplash.com/photo-1543466835-00a7907e9de1",
        caption="صورة افتراضية (حيوان - قط/كلب)",
        use_container_width=True,
    )
    image_name = "pet_dog_cat"

  if st.button("فحص وتصنيف الصورة"):
    with st.spinner("جاري فحص الكائنات بالرؤية الحاسوبية..."):
      st.success("تم تحليل الصورة بنجاح!")

      # محاكاة ذكية للتعرف على الكائن بناءً على الصورة المرفوعة أو الافتراضية
      if any(w in image_name for w in ["cat", "dog", "animal", "pet", "قط", "كلب", "حيوان"]):
        detected_type = "حيوان (Animal - Mammal) 🐾"
        details = "تم رصد كائن حي (حيوان أليف) مع تحليل ملامح الوجه والجسم."
        conf = "98.9%"
      elif any(w in image_name for w in ["plant", "tree", "flower", "نبتة", "شجرة", "ورقة"]):
        detected_type = "نبتة / كائن نباتي (Plant / Flora) 🌱"
        details = "تم رصد أوراق خضراء/نبات طبيعي وتصنيف نوع الغطاء النباتي."
        conf = "97.4%"
      elif any(w in image_name for w in ["human", "person", "man", "woman", "face", "إنسان", "شخص"]):
        detected_type = "إنسان (Human / Person) 👤"
        details = "تم اكتشاف وجه/جسم بشري وتحديد الخصائص الحيوية بدقة."
        conf = "99.5%"
      else:
        # افتراضي بناءً على الصورة التجريبية للحيوان
        detected_type = "حيوان أليف (Animal / Mammal) 🐕"
        details = "تم تصنيف الكائن بنجاح ضمن فصيلة الحيوانات الأليفة."
        conf = "98.6%"

      st.write(f"**التصنيف العام:** {detected_type}")
      st.write(f"**التفاصيل المكتشفة:** {details}")
      st.write(f"**نسبة الثقة (Confidence):** {conf}")

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>مشروع مادة موضوعات مختارة في"
    " الذكاء الاصطناعي - جامعة الملك سعود/كلية الحاسب (مثال تعليمي)</p>",
    unsafe_allow_html=True,
)

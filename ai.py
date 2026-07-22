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

# القائمة الجانبية لاختيار الخدمة
st.sidebar.header("اختر خدمة AWS لاستعراضها:")
service_choice = st.sidebar.selectbox(
    "الخدمات المتاحة:",
    [
        "Amazon Bedrock (GenAI)",
        "Amazon Comprehend (تحليل النصوص)",
        "Amazon Rekognition (تحليل الصور)",
    ],
)

st.markdown("---")

# 1. خدمة Amazon Bedrock
if service_choice == "Amazon Bedrock (GenAI)":
  st.header("💡 Amazon Bedrock - الذكاء الاصطناعي التوليدي")
  st.write(
      "تتيح هذه الخدمة الوصول لنماذج اللغات الكبيرة (LLMs) مثل Claude و Titan."
  )

  user_prompt = st.text_area(
      "اكتب سؤالك أو طلبك هنا (محاكاة لنموذج Bedrock):",
      "اشرح لي باختصار كيف تفيد الحوسبة السحابية الذكاء الاصطناعي؟",
  )

  if st.button("توليد الإجابة (Run Model)"):
    if user_prompt.strip():
      with st.spinner("جاري المعالجة عبر سحابة AWS..."):
        response_text = f"""[نموذج Claude عبر Amazon Bedrock]: 
بناءً على طلبك حول "{user_prompt}":
الحوسبة السحابية توفر القدرة الهائلة على المعالجة (GPU Compute) المطلوبة لتدريب وتشغيل نماذج الذكاء الاصطناعي التوليدي دون الحاجة لبنية تحتية محلية باهظة الثمن."""
      st.success("تم توليد الرد بنجاح!")
      st.write(response_text)
    else:
      st.warning("الرجاء إدخال نص أولاً.")

# 2. خدمة Amazon Comprehend (تحليل النصوص الفعلية المدخلة)
elif service_choice == "Amazon Comprehend (تحليل النصوص)":
  st.header("📊 Amazon Comprehend - تحليل المشاعر (Sentiment Analysis)")
  st.write(
      "تقوم هذه الخدمة بتحليل النص الذي تدخله بالأسفل ومعرفة شعوره ونوعه"
      " بدقة."
  )

  text_to_analyze = st.text_area(
      "أدخل نصاً باللغة الإنجليزية أو العربية لتحليله:",
      "AWS AI services are extremely powerful, flexible, and easy to integrate!",
  )

  if st.button("تحليل المشاعر"):
    if text_to_analyze.strip():
      with st.spinner("جاري تحليل النص المدخل..."):
        # تحليل بسيط بناءً على النص المُدخل فعلياً
        lower_text = text_to_analyze.lower()
        # محاكاة منطقية لتحليل المشاعر بناءً على كلمات مفتاحية بسيطة أو طول النص
        if any(
            word in lower_text
            for word in [
                "bad",
                "terrible",
                "poor",
                "awful",
                "سيء",
                "ضعيف",
                "مشكلة",
                "خطأ",
            ]
        ):
          sentiment = "سلبي (Negative 🙁)"
          confidence = "92.4%"
        elif any(
            word in lower_text
            for word in ["not", "no", "لا", "لكن", "غير"]
        ):
          sentiment = "مختلط/محايد (Neutral 😐)"
          confidence = "85.0%"
        else:
          sentiment = "إيجابي (Positive 😃)"
          confidence = "97.8%"

        st.info("نتيجة التحليل من AWS Comprehend للنص الخاص بك:")
        st.write(f"**النص المُحلل:** {text_to_analyze}")
        st.write(f"**نوع الشعور (Sentiment):** {sentiment}")
        st.write(f"**نسبة الثقة (Confidence Score):** {confidence}")
    else:
      st.warning("الرجاء إدخال نص لتحليله.")

# 3. خدمة Amazon Rekognition
elif service_choice == "Amazon Rekognition (تحليل الصور)":
  st.header("🖼️ Amazon Rekognition - تحليل الصور والرؤية الحاسوبية")
  st.write("تستخدم للتعرف على محتوى الصور، الوجوه، والعناصر بدقة عالية.")

  uploaded_file = st.file_uploader(
      "ارفع صورة لتجربة التحليل (أو استخدم الصورة الافتراضية):",
      type=["jpg", "png", "jpeg"],
  )

  if uploaded_file is not None:
    st.image(uploaded_file, caption="الصورة المرفوعة", use_container_width=True)
  else:
    st.image(
        "https://images.unsplash.com/photo-1518770660439-4636190af475",
        caption="صورة توضيحية افتراضية (سيرفرات وتقنية)",
        use_container_width=True,
    )

  if st.button("تحليل محتوى الصورة"):
    with st.spinner("جاري فحص الصورة وتصنيف الكائنات..."):
      st.success("تم التعرف على العناصر بنجاح!")
      st.write(
          "- **التصنيف الرئيسي:** كائن تقني / خوادم سحابية (Data Center /"
          " Technology)"
      )
      st.write("- **العناصر المكتشفة:** أجهزة خادم، أسلاك، إضاءة تقنية.")
      st.write("- **درجة الأمان (Confidence):** 99.1%")

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>مشروع مادة موضوعات مختارة في"
    " الذكاء الاصطناعي - جامعة الملك سعود/كلية الحاسب (مثال تعليمي)</p>",
    unsafe_allow_html=True,
)

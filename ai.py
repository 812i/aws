import streamlit as st 

# إعداد الصفحة
st.set_page_config(
    page_title="مجوهرات مشروع الذكاء الاصطناعي - AWS",
    page_icon="☁️",
    layout="centered"
)

# العنوان الرئيسي
st.title("🚀 منصة خدمات الذكاء الاصطناعي في سحابة أمازون (AWS)")
st.write("مرحباً بكِ في التطبيق العملي لمشروع مادة موضوعات مختارة في الذكاء الاصطناعي.")

# القائمة الجانبية لاختيار الخدمة
st.sidebar.header("اختر خدمة AWS لاستعراضها:")
service_choice = st.sidebar.selectbox(
    "الخدمات المتاحة:",
    [
        "Amazon Bedrock (GenAI)",
        "Amazon Comprehend (تحليل النصوص)",
        "Amazon Rekognition (تحليل الصور)",
    ]
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
                # محاكاة لرد النموذج (يمكنك ربطه لاحقاً بـ Boto3 الحقيقي)
                response_text = f"""[نموذج Claude عبر Amazon Bedrock]: 
بناءً على طلبك حول "{user_prompt}":
الحوسبة السحابية توفر القدرة الهائلة على المعالجة (GPU Compute) المطلوبة لتدريب وتشغيل نماذج الذكاء الاصطناعي التوليدي دون الحاجة لبنية تحتية محلية باهظة الثمن."""
            st.success("تم توليد الرد بنجاح!")
            st.write(response_text)
        else:
            st.warning("الرجاء إدخال نص أولاً.")

# 2. خدمة Amazon Comprehend
elif service_choice == "Amazon Comprehend (تحليل النصوص)":
    st.header("📊 Amazon Comprehend - تحليل المشاعر (Sentiment Analysis)")
    st.write("تقوم هذه الخدمة بتحليل النصوص ومعرفة ما إذا كانت إيجابية أم سلبية.")

    text_to_analyze = st.text_area(
        "أدخل نصاً باللغة الإنجليزية أو العربية لتحليله:",
        "AWS AI services are extremely powerful, flexible, and easy to integrate!",
    )

    if st.button("تحليل المشاعر"):
        with st.spinner("جاري التحليل..."):
            st.info("نتيجة التحليل من AWS Comprehend:")
            st.write("**نوع الشعور (Sentiment):** Positive (إيجابي 😃)")
            st.write(
                "**نسبة الثقة (Confidence Score):** 98.5% باستخدام خوارزميات NLP"
            )

# 3. خدمة Amazon Rekognition
elif service_choice == "Amazon Rekognition (تحليل الصور)":
    st.header("🖼️ Amazon Rekognition - تحليل الصور والرؤية الحاسوبية")
    st.write("تستخدم للتعرف على محتوى الصور، الوجوه، والعناصر بدقة عالية.")

    uploaded_file = st.file_uploader(
        "ارفع صورة لتجربة التحليل (أو استخدم الصورة الافتراضية):",
        type=["jpg", "png", "jpeg"],
    )

    if uploaded_file is not None:
        st.image(
            uploaded_file, caption="الصورة المرفوعة", use_container_width=True
        )
    else:
        st.image(
            "https://images.unsplash.com/photo-1518770660439-4636190af475",
            caption="صورة توضيحية افتراضية (سيرفرات وتقنية)",
            use_container_width=True,
        )

    if st.button("تحليل محتوى الصورة"):
        with st.spinner("جاري فحص الصورة..."):
            st.success("تم التعرف على العناصر بنجاح!")
            st.write(
                "- **العناصر المكتشفة:** سحابة رقمية، معالجات، أضواء مركز بيانات (Data Center)."
            )
            st.write("- **درجة الأمان:** 99.1%")

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>مشروع مادة موضوعات مختارة في الذكاء الاصطناعي - جامعة الملك سعود/كلية الحاسب (مثال تعليمي)</p>",
    unsafe_allow_html=True,
)

import streamlit as st
from PIL import Image
import base64
from io import BytesIO

st.set_page_config(page_title="Diabetes", layout="wide", page_icon="⚕️")

st.markdown("""
    <style>
        .block-container {
            padding-top: 0rem !important; /* delete default spacing between all content and top padding */
        }
        .header {
            padding-top: 10px; /* spacing between header and top padding */
            display: flex; /* place child divs in horizontal */
            justify-content: center;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
        }
        .main-content {
            padding-top: 30px; /* spacing between main content and header */
        }
        .footer { 
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #f0f2f6;
            color: #333;
            text-align: center;
            padding: 10px;
            font-size: 14px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="header">
        <h1 style="font-size: 80px; font-weight: 800; color: #e74c3c; margin: 0;">GlucoMate</h1>
        <h1 style="font-size: 40px; font-weight: 600; color: #1e81b0; margin: 0;">AI-based Diabetes Support System</h1>
    </div>

    <div class="main-content"></div>
""", unsafe_allow_html=True)

st.markdown("""### 1. Introduction""")
st.markdown("""
Diabetes Mellitus is a common chronic metabolic disorder worldwide, characterized by hyperglycemia due to impaired insulin secretion or insulin resistance. 
This article summarizes theoretical knowledge about diabetes, including classification, causes, clinical symptoms, 
complications, treatment methods, as well as current research advances. 
Understanding the pathogenesis and risk factors will help improve the effectiveness of treatment and management of diabetic patients, 
and contribute to disease prevention in the community.

Diabetes is one of the fastest growing non-communicable diseases today. 
According to the International Diabetes Federation (IDF), in 2023, there were approximately 537 million adults living with diabetes, 
and this number is expected to increase to 643 million by 2030 without effective intervention.
""")

st.markdown("""### 2. Pathogenesis""")
st.markdown("""
Diabetes occurs when the body loses its ability to produce or use insulin effectively.
Insulin is a hormone secreted by the beta cells of the pancreas that helps transport glucose from the blood into the cells.
Insulin deficiency or insulin resistance leads to a state of prolonged hyperglycemia, causing damage to many organs and systems in the body.
""")

def image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()
image1 = Image.open("../images/pathogenesis_of_diabetes.jpg")
st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="data:image/png;base64,{image_to_base64(image1)}" alt="DS vs AI" style="max-width: 100%; height: auto;">
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("""### 3. Types of Diabetes""")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ##### a. Type 1 Diabetes Mellitus
    Type 1 diabetes is an autoimmune disease in which the immune system destroys pancreatic beta cells, causing the body to lose its ability to produce insulin with the main features:
    - Early onset: usually occurs in children, adolescents or young adults, although it can also occur in adults (LADA - Latent Autoimmune Diabetes in Adults).
    - Clear acute symptoms: rapid onset, rapid weight loss, severe fatigue, and easily leading to ketoacidosis if not treated promptly.
    - Genetic factors: related to the HLA-DR3, DR4 genes, which are associated with autoimmune conditions, but they account for only part of the total risk.
    - Diagnosis: can detect autoantibodies (anti-GAD, anti-IA2, anti-ZnT8...) in the blood. These biomarkers help confirm autoimmune destruction of beta cells
    - Compulsory insulin treatment: requires lifelong subcutaneous insulin injections, as blood sugar cannot be controlled by oral medications alone.
    """)

with col2:
    st.markdown("""
    ##### b. Type 2 Diabetes Mellitus
    This is the most common form, accounting for about 90–95% of cases. Type 2 is related to two main mechanisms:
    - Insulin resistance: tissues (liver, muscle, fat) do not respond well to insulin.
    - Decreased insulin secretion: the pancreas does not produce enough insulin to compensate.
    
    **Clinical features:**
    - Silent onset, vague symptoms
    - Can last for many years before being diagnosed
    - Many cases are detected late when complications have occurred
    - Main risk factors: age ≥ 45, BMI > 25, low physical activity, genetics, hypertension, dyslipidemia
    - Often associated with obesity and metabolic syndrome
    """)

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    ##### c. Gestational Diabetes Mellitus - GDM
    This is a condition of hyperglycemia that occurs during pregnancy, usually detected by the oral glucose tolerance test (OGTT) at week 24–28.
    
    **Mechanism:**
    - Due to placental hormones reducing insulin sensitivity → causing temporary insulin resistance.
    - Pregnant women must produce more insulin; if the pancreas can't keep up, GDM develops.

    **Effects:**
    - Increased risk of preeclampsia, polyhydramnios, premature birth, large fetus, cesarean section.
    - Newborns are susceptible to hypoglycemia, jaundice, obesity and diabetes later.
    - Postpartum mothers have a high risk of developing type 2 within 5–10 years.
    """)

with col4:
    st.markdown("""
    ##### d. Secondary & Monogenic Diabetes
    Monogenic Diabetes due to single gene mutations, the most common is MODY (Maturity Onset Diabetes of the Young).
    Early diagnosis is important to choose the right medication (many forms of MODY respond well to sulfonylureas instead of insulin).
    Inherited in a dominant manner, usually appearing in young people with no obesity, no insulin resistance.

    **Diabetes due to pancreatic disease:**
    - Chronic pancreatitis, cystic fibrosis, pancreatic trauma, pancreatectomy...
    - Loss of both insulin and glucagon → easy to fluctuate blood sugar.

    **Diabetes due to drugs or chemicals:**
    - Glucocorticoids, immunosuppressants, HIV treatment drugs...
    - Some toxins destroy the pancreas (eg streptozotocin in preclinical studies)
    """)

st.markdown("### 4. Summary")

tab1, tab2 = st.tabs(["Clinical Symptoms & Complications", "Diagnose & Treatment"])

with tab1:
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("##### Clinical Symptoms")
        st.markdown("""
        - Excessive thirst  
        - Frequent urination  
        - Excessive hunger but weight loss  
        - Fatigue  
        - Skin infections, slow wound healing  
        - Blurred vision  
        """)

    with col2:
        st.markdown("##### Complications")
        st.markdown("""
        - Hyperglycemic coma  
        - Eyes: Retinopathy → blindness  
        - Kidneys: Diabetic nephropathy → dialysis  
        - Cardiovascular: Myocardial infarction, stroke  
        - Nerves: Numbness, muscle weakness, leg ulcers  
        - Legs: Slow-healing ulcers, amputation  
        """)

with tab2:
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("##### Diagnose")
        st.markdown("""
        - FPG (Fasting Plasma Glucose) ≥ 130 mg/dL
        - HbA1c (Hemoglobin A1c) ≥ 7%  
        - OGTT (Oral Glucose Tolerance Test) after 2 hours ≥ 200 mg/dL  
        - Random plasma glucose ≥ 200 mg/dL with symptoms of hyperglycemia
        - BMI ≥ 25 or ≥ 23 if Asian  
        - Hypertension, dyslipidemia  
        """)

    with col2:
        st.markdown("##### Treatment")
        st.markdown("""
        - Healthy eating: Reduce starch quickly, increase fiber  
        - Exercise regularly, lose weight if overweight  
        - Oral medications: metformin, sulfonylureas, DPP-4i, SGLT2i...  
        - Insulin injections: required in type 1, may be used in severe type 2  
        - Self-measurement of blood glucose, measure HbA1c periodically  
        - Regular check-up for complications  
        """)


st.markdown("""<div class="footer">© 2025 Nguyễn Đức Tây | All rights reserved.</div>""", unsafe_allow_html=True)
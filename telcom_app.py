import streamlit as st
import pandas as pd
import pickle

# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(
    page_title="Telecom Churn AI",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================================================
# LOAD MODEL
# ======================================================

model = pickle.load(open('best_churn_model.pkl', 'rb'))

selected_features = pickle.load(
    open('selected_features.pkl', 'rb')
)

# ======================================================
# CUSTOM CSS
# ======================================================

st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #0F172A;
    color: white;
}

/* Remove default padding */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
    border-right: 1px solid #1F2937;
}

/* Hero section */
.hero {
    background: linear-gradient(
        135deg,
        #1E3A8A,
        #2563EB
    );
    padding: 2rem;
    border-radius: 20px;
    color: white;
    margin-bottom: 2rem;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.4);
}

/* Cards */
.metric-card {
    background: #1E293B;
    padding: 25px;
    border-radius: 18px;
    text-align: center;
    color: white;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
    transition: 0.3s;
}

.metric-card:hover {
    transform: translateY(-5px);
}

/* Input containers */
.input-box {
    background-color: #1E293B;
    padding: 20px;
    border-radius: 18px;
    margin-bottom: 1rem;
}

/* Prediction box */
.prediction-box {
    padding: 30px;
    border-radius: 18px;
    text-align: center;
    font-size: 28px;
    font-weight: bold;
    margin-top: 20px;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(
        90deg,
        #2563EB,
        #3B82F6
    );
    color: white;
    border: none;
    border-radius: 12px;
    height: 3.5em;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.02);
    background: linear-gradient(
        90deg,
        #1D4ED8,
        #2563EB
    );
}

/* Progress bar */
.stProgress > div > div > div > div {
    background-color: #2563EB;
}

/* Selectbox + Inputs */
.stSelectbox, .stSlider, .stNumberInput {
    background-color: #1E293B;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# ======================================================
# SIDEBAR
# ======================================================

st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/3059/3059518.png",
    width=80
)

st.sidebar.title("Telecom AI Dashboard")

st.sidebar.markdown("""
### Intelligent Customer Analytics

Predict telecom customer churn risk using
Machine Learning and behavioral analytics.
""")

st.sidebar.markdown("---")

st.sidebar.success("Model Status: Active")

st.sidebar.markdown("""
### Technologies
- Streamlit
- Scikit-Learn
- Random Forest
- SMOTE
- Python
""")

# ======================================================
# HERO SECTION
# ======================================================

st.markdown("""
<div class="hero">

# 📡 Telecom Customer Churn Prediction

### AI-Powered Customer Retention Intelligence Platform

Analyze customer behavior and predict churn
risk using Machine Learning.

</div>
""", unsafe_allow_html=True)

# ======================================================
# KPI SECTION
# ======================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
    <h3>Accuracy</h3>
    <h1>77%</h1>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
    <h3>Recall</h3>
    <h1>56%</h1>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
    <h3>ROC-AUC</h3>
    <h1>Good</h1>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
    <h3>Model</h3>
    <h1>RF</h1>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ======================================================
# TABS
# ======================================================

tab1, tab2 = st.tabs([
    "Prediction Dashboard",
    "Customer Insights"
])

# ======================================================
# TAB 1
# ======================================================

with tab1:

    st.subheader("Customer Information")

    left_col, right_col = st.columns(2)

    with left_col:

        tenure = st.slider(
            "Tenure (Months)",
            0,
            72,
            12
        )

        monthly_charges = st.slider(
            "Monthly Charges",
            0.0,
            200.0,
            70.0
        )

        total_charges = st.number_input(
            "Total Charges",
            0.0,
            10000.0,
            1000.0
        )

        gender_male = st.selectbox(
            "Gender",
            ["Female", "Male"]
        )

        partner_yes = st.selectbox(
            "Partner",
            ["No", "Yes"]
        )

    with right_col:

        dependents_yes = st.selectbox(
            "Dependents",
            ["No", "Yes"]
        )

        paperless_billing = st.selectbox(
            "Paperless Billing",
            ["No", "Yes"]
        )

        internet_service = st.selectbox(
            "Internet Service",
            ["DSL", "Fiber optic", "No"]
        )

        contract = st.selectbox(
            "Contract Type",
            ["Month-to-month", "One year", "Two year"]
        )

        payment_method = st.selectbox(
            "Payment Method",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer",
                "Credit card"
            ]
        )

    # ======================================================
    # INPUT DATA
    # ======================================================

    input_data = {
        'tenure': tenure,
        'TotalCharges': total_charges,
        'MonthlyCharges': monthly_charges,

        'PaymentMethod_Electronic check':
            1 if payment_method == "Electronic check" else 0,

        'InternetService_Fiber optic':
            1 if internet_service == "Fiber optic" else 0,

        'PaperlessBilling_Yes':
            1 if paperless_billing == "Yes" else 0,

        'Contract_Two year':
            1 if contract == "Two year" else 0,

        'MultipleLines_Yes': 0,

        'gender_Male':
            1 if gender_male == "Male" else 0,

        'Contract_One year':
            1 if contract == "One year" else 0
    }

    input_df = pd.DataFrame([input_data])

    input_df = input_df.reindex(
        columns=selected_features,
        fill_value=0
    )

    # ======================================================
    # PREDICTION
    # ======================================================

    if st.button("Predict Customer Churn"):

        prediction = model.predict(input_df)[0]

        probability = model.predict_proba(
            input_df
        )[0][1]

        st.markdown("## Prediction Analysis")

        if prediction == 1:

            st.markdown(f"""
            <div class="prediction-box"
            style="
            background-color:#7F1D1D;
            color:white;
            ">

            ⚠️ HIGH CHURN RISK

            <br><br>

            Probability:
            {probability:.2%}

            </div>
            """, unsafe_allow_html=True)

        else:

            st.markdown(f"""
            <div class="prediction-box"
            style="
            background-color:#064E3B;
            color:white;
            ">

            ✅ LOW CHURN RISK

            <br><br>

            Probability:
            {probability:.2%}

            </div>
            """, unsafe_allow_html=True)

        st.markdown("### Churn Probability")

        st.progress(float(probability))

# ======================================================
# TAB 2
# ======================================================

with tab2:

    st.subheader("Key Churn Insights")

    st.info("""
    Customers with shorter tenure and higher
    monthly charges are more likely to churn.
    """)

    st.warning("""
    Month-to-month contract customers show
    significantly higher churn rates.
    """)

    st.success("""
    Long-term contracts strongly improve
    customer retention.
    """)

    st.markdown("### Top Drivers of Churn")

    churn_factors = pd.DataFrame({
        "Feature": [
            "Tenure",
            "Monthly Charges",
            "Total Charges",
            "Contract Type",
            "Fiber Optic Service"
        ],
        "Impact": [
            0.17,
            0.14,
            0.17,
            0.10,
            0.07
        ]
    })

    st.dataframe(
        churn_factors,
        use_container_width=True
    )

# ======================================================
# FOOTER
# ======================================================

st.markdown("---")

st.caption(
    "Telecom AI Retention System | Built with Streamlit"
)
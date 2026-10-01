import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Loan Default Risk Analyzer", page_icon="📊", layout="wide"
)


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------


@st.cache_data
def load_data():
    return pd.read_csv("data/loan_data.csv")


df = load_data()


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("📊 Loan Default Risk Analyzer")

st.markdown("""
    **Loan Repayment & Risk Analytics Dashboard**

    Explore loan characteristics, repayment outcomes,
    borrower risk indicators, and machine-learning insights.
    """)


# --------------------------------------------------
# KEY METRICS
# --------------------------------------------------

total_loans = len(df)

fully_paid = (df["not.fully.paid"] == 0).sum()

not_fully_paid = (df["not.fully.paid"] == 1).sum()

non_repayment_rate = (not_fully_paid / total_loans) * 100


col1, col2, col3, col4 = st.columns(4)


col1.metric("Total Loans", f"{total_loans:,}")

col2.metric("Fully Paid", f"{fully_paid:,}")

col3.metric("Not Fully Paid", f"{not_fully_paid:,}")

col4.metric("Non-Repayment Rate", f"{non_repayment_rate:.2f}%")


st.divider()


# --------------------------------------------------
# LOAN PURPOSE ANALYSIS
# --------------------------------------------------

st.subheader("Loan Distribution by Purpose")


purpose_counts = df["purpose"].value_counts().sort_values()


fig, ax = plt.subplots(figsize=(10, 5))

ax.barh(purpose_counts.index, purpose_counts.values)

ax.set_xlabel("Number of Loans")
ax.set_ylabel("Loan Purpose")
ax.set_title("Loan Distribution by Purpose")

st.pyplot(fig)


# --------------------------------------------------
# NON-REPAYMENT BY PURPOSE
# --------------------------------------------------

st.subheader("Non-Repayment Rate by Loan Purpose")


purpose_rate = df.groupby("purpose")["not.fully.paid"].mean().sort_values() * 100


fig, ax = plt.subplots(figsize=(10, 5))

ax.barh(purpose_rate.index, purpose_rate.values)

ax.set_xlabel("Non-Repayment Rate (%)")
ax.set_ylabel("Loan Purpose")
ax.set_title("Non-Repayment Rate by Purpose")

st.pyplot(fig)


# --------------------------------------------------
# FICO ANALYSIS
# --------------------------------------------------

st.subheader("FICO Score by Repayment Outcome")


fig, ax = plt.subplots(figsize=(8, 5))

df.boxplot(column="fico", by="not.fully.paid", ax=ax)

ax.set_title("FICO Score by Repayment Outcome")
ax.set_xlabel("Not Fully Paid")
ax.set_ylabel("FICO Score")

fig.suptitle("")

st.pyplot(fig)


# --------------------------------------------------
# DTI ANALYSIS
# --------------------------------------------------

st.subheader("Debt-to-Income Ratio by Repayment Outcome")


fig, ax = plt.subplots(figsize=(8, 5))

df.boxplot(column="dti", by="not.fully.paid", ax=ax)

ax.set_title("DTI by Repayment Outcome")
ax.set_xlabel("Not Fully Paid")
ax.set_ylabel("DTI")

fig.suptitle("")

st.pyplot(fig)


# --------------------------------------------------
# RISK SEGMENTATION
# --------------------------------------------------

st.subheader("Risk Segmentation")


def classify_risk(row):

    if row["fico"] < 650 and row["dti"] > 20:
        return "High Risk"

    elif row["fico"] < 700 or row["dti"] > 20:
        return "Moderate Risk"

    else:
        return "Lower Risk"


df["risk_group"] = df.apply(classify_risk, axis=1)


risk_analysis = (
    df.groupby("risk_group")
    .agg(
        total_loans=("not.fully.paid", "count"),
        unpaid_loans=("not.fully.paid", "sum"),
        non_repayment_rate=("not.fully.paid", "mean"),
    )
    .reset_index()
)


risk_analysis["non_repayment_rate"] *= 100


st.dataframe(risk_analysis, use_container_width=True)


# --------------------------------------------------
# MACHINE LEARNING RESULTS
# --------------------------------------------------

st.subheader("Machine Learning Model Performance")


try:

    model_comparison = pd.read_csv("data/model_comparison.csv")

    st.dataframe(model_comparison, use_container_width=True)

except FileNotFoundError:

    st.info("Model comparison file not found.")


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "Loan Default Risk Analyzer | " "Python • Pandas • SQL • Scikit-learn • Streamlit"
)

# Loan Default Risk Analyzer

An end-to-end data analytics and beginner machine learning project
analyzing loan repayment patterns and borrower risk indicators.

## Project Overview

The objective of this project is to analyze historical loan data,
identify patterns associated with loans that were not fully repaid,
and build machine learning models to predict repayment outcomes.

The project combines:

- Exploratory Data Analysis
- SQL Business Analysis
- Feature Engineering
- Machine Learning
- Data Visualization
- Interactive Dashboard

## Business Questions

This project investigates questions such as:

- What percentage of loans were not fully repaid?
- Which loan purposes have the highest observed non-repayment rates?
- How does FICO score differ across repayment outcomes?
- How does debt-to-income ratio relate to repayment outcomes?
- How do interest rates differ across loan purposes and repayment outcomes?
- Can borrower characteristics be used to predict repayment outcomes?

## Dataset

The dataset contains 9,578 loan records and 14 variables.

The target variable is:

`not.fully.paid`

Where:

- `0` = Fully Paid
- `1` = Not Fully Paid

Important features include:

- FICO score
- Debt-to-income ratio
- Interest rate
- Installment
- Annual income
- Credit inquiries
- Public records
- Loan purpose
- Revolving credit utilization

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- SQL / SQLite
- Scikit-learn
- Streamlit
- Jupyter Notebook

## Project Workflow

```text
Raw Dataset
     ↓
Data Understanding
     ↓
Data Cleaning & EDA
     ↓
SQL Business Analysis
     ↓
Feature Engineering
     ↓
Machine Learning
     ↓
Model Evaluation
     ↓
Interactive Dashboard

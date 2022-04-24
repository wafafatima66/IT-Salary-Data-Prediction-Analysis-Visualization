import streamlit as st
from report import show_report_page
from predict import show_predict_page
from analysis import show_analysis_page

st.header('')
page = st.sidebar.selectbox("Prediction , Report & Analysis",("Predict","Reports","Analysis"))

if page == "Predict":
    show_predict_page()
elif page == "Reports":
    show_report_page()
else :
    show_analysis_page()
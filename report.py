import streamlit as st
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from my_function import shorten_categories
from my_function import clean_experience
from my_function import clean_education
from my_function import clean_country_name
from my_function import clean_experience_2018

@st.cache
def load_data(year):
    
    df = pd.read_csv("./data/"+year+".csv")

    if year == '2021':
        df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedCompYearly"]]
        df = df[df["ConvertedCompYearly"].notnull()]
        # df= df.rename({"ConvertedCompYearly": "Salary"}, axis=1)

    elif year == '2020' or year == '2019':
        df = df[["Country","Employment", "ConvertedComp", "EdLevel", "YearsCodePro"]]
        df = df[df["ConvertedComp"].notnull()]
        df= df.rename({"ConvertedComp": "ConvertedCompYearly"}, axis=1)

    elif year == '2018' :
        df = df[["Country","Employment", "ConvertedSalary","YearsCodingProf","FormalEducation"]]
        df = df[df["ConvertedSalary"].notnull()]
        df = df[df["YearsCodingProf"].notnull()]
        df= df.rename({"ConvertedSalary": "ConvertedCompYearly"}, axis=1)
        df["YearsCodingProf"] = df["YearsCodingProf"].apply(clean_experience_2018)
        df= df.rename({"YearsCodingProf": "YearsCodePro"}, axis=1)
        df= df.rename({"FormalEducation": "EdLevel"}, axis=1)

    df = df.dropna()
    df = df[df["Employment"] == "Employed full-time"]
    df = df.drop("Employment", axis=1)

    df['Country'] = df['Country'].apply(clean_country_name)
    country_map = shorten_categories(df.Country.value_counts(), 1000)
    df["Country"] = df["Country"].map(country_map)
    df = df[df["ConvertedCompYearly"] <= 250000]
    df = df[df["ConvertedCompYearly"] >= 10000]
    df = df[df["Country"] != "Other"]
    

    df["YearsCodePro"] = df["YearsCodePro"].apply(clean_experience)
    df["EdLevel"] = df["EdLevel"].apply(clean_education)
    df= df.rename({"ConvertedCompYearly": "Salary"}, axis=1)

    return df


def show_report_page():

    col1, col2 = st.columns([4, 2])

    col2.write("""#### """)
    col2.write("""#### """)
    col2.write("""#### """)
    col2.write("""#### """)
    col2.write("""#### """)

    expander = col2.expander("Select Year")
    year = expander.selectbox(
        "",
        ('2021', '2020', '2018','2019'))

    # col2.write(year)
    df = load_data(year)
   
    col1.title('Report of {}'.format(year))

    data = df["Country"].value_counts()

    
    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    col1.write("""#### Number of Data from different countries""")
    col1.pyplot(fig1)

    col1.write("""#### Mean Salary Based On Country """ )

    data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    col1.bar_chart(data, height=500)

    col1.write("""#### Mean Salary Based On Experience""")

    data = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
    # data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    # st.write(data)
    col1.line_chart(data, height=500)


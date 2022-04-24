import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
from my_function import clean_country_name
from my_function import shorten_categories

@st.cache
def load_data_years():
    # 2018
    df_18 = pd.read_csv("./data/2018.csv")
    df_18 = df_18[["Country","Employment", "ConvertedSalary"]]
    df_18 = df_18.rename({"ConvertedSalary": "2018"}, axis=1)
    df_18 = df_18[df_18["2018"].notnull()]
    df_18 = df_18[df_18["2018"] <= 250000]
    df_18 = df_18[df_18["2018"] >= 10000]
    df_18 = df_18[df_18["Employment"] == "Employed full-time"]
    df_18 = df_18.drop("Employment", axis=1)

    #2019
    df_19 = pd.read_csv("./data/2019.csv")
    df_19 = df_19[["Country","Employment", "ConvertedComp"]]
    df_19 = df_19.rename({"ConvertedComp": "2019"}, axis=1)
    df_19 = df_19[df_19["2019"].notnull()]
    df_19 = df_19[df_19["2019"] <= 250000]
    df_19 = df_19[df_19["2019"] >= 10000]
    df_19 = df_19[df_19["Employment"] == "Employed full-time"]
    df_19 = df_19.drop("Employment", axis=1)

    #2020
    df_20 = pd.read_csv("./data/2020.csv")
    df_20 = df_20[["Country","Employment", "ConvertedComp"]]
    df_20 = df_20.rename({"ConvertedComp": "2020"}, axis=1)
    df_20 = df_20[df_20["2020"].notnull()]
    df_20 = df_20[df_20["2020"] <= 250000]
    df_20 = df_20[df_20["2020"] >= 10000]
    df_20 = df_20[df_20["Employment"] == "Employed full-time"]
    df_20 = df_20.drop("Employment", axis=1)

    # 2021
    df_21 = pd.read_csv("./data/2021.csv")
    df_21 = df_21[["Country","Employment", "ConvertedCompYearly"]]
    df_21 = df_21.rename({"ConvertedCompYearly": "2021"}, axis=1)
    df_21 = df_21[df_21["2021"].notnull()]
    df_21 = df_21[df_21["2021"] <= 250000]
    df_21 = df_21[df_21["2021"] >= 10000]
    df_21 = df_21[df_21["Employment"] == "Employed full-time"]
    df_21 = df_21.drop("Employment", axis=1)

    # concat
    df_list = [df_18,df_19,df_20 , df_21]
    df = pd.concat(df_list)
    df['Country'] = df['Country'].apply(clean_country_name)
    country_map = shorten_categories(df.Country.value_counts(), 2000)
    df['Country'] = df['Country'].map(country_map)
    df = df[df["Country"] != "Other"]

    return df

    # df = pd.read_csv("./data/year.csv")
    # return df

@st.cache
def load_data_era():

    # BEFORE CORONA

    #2018
    df_18 = pd.read_csv("./data/2018.csv")
    df_18 = df_18[["Country","Employment", "ConvertedSalary"]]
    df_18 = df_18.rename({"ConvertedSalary": "Before"}, axis=1)
    # df_18 = df_18[df_18["2018"].notnull()]
    # df_18 = df_18[df_18["2018"] <= 250000]
    # df_18 = df_18[df_18["2018"] >= 10000]
    # df_18 = df_18[df_18["Employment"] == "Employed full-time"]
    # df_18 = df_18.drop("Employment", axis=1)

    #2019
    df_19 = pd.read_csv("./data/2019.csv")
    df_19 = df_19[["Country","Employment", "ConvertedComp"]]
    df_19 = df_19.rename({"ConvertedComp": "Before"}, axis=1)
    # df_19 = df_19[df_19["2019"].notnull()]
    # df_19 = df_19[df_19["2019"] <= 250000]
    # df_19 = df_19[df_19["2019"] >= 10000]
    # df_19 = df_19[df_19["Employment"] == "Employed full-time"]
    # df_19 = df_19.drop("Employment", axis=1)

    #CONCAT BEFORE CORONA ERA

    df_list_bf = [df_18,df_19]
    df_bf = pd.concat(df_list_bf)
    # df_bf['Country'] = df_bf['Country'].apply(clean_country_name)
    # country_map = shorten_categories(df_bf.Country.value_counts(), 2000)
    # df_bf['Country'] = df_bf['Country'].map(country_map)
    # df_bf = df_bf[df_bf["Country"] != "Other"]
    df_bf = df_bf[df_bf["Before"].notnull()]
    df_bf = df_bf[df_bf["Before"] <= 250000]
    df_bf = df_bf[df_bf["Before"] >= 10000]
    df_bf = df_bf[df_bf["Employment"] == "Employed full-time"]
    df_bf = df_bf.drop("Employment", axis=1)

    #AFTER CORONA ERA 
    #2020
    df_20 = pd.read_csv("./data/2020.csv")
    df_20 = df_20[["Country","Employment", "ConvertedComp"]]
    df_20 = df_20.rename({"ConvertedComp": "After"}, axis=1)
    # df_20 = df_20[df_20["2020"].notnull()]
    # df_20 = df_20[df_20["2020"] <= 250000]
    # df_20 = df_20[df_20["2020"] >= 10000]
    # df_20 = df_20[df_20["Employment"] == "Employed full-time"]
    # df_20 = df_20.drop("Employment", axis=1)

    # 2021
    df_21 = pd.read_csv("./data/2021.csv")
    df_21 = df_21[["Country","Employment", "ConvertedCompYearly"]]
    df_21 = df_21.rename({"ConvertedCompYearly": "After"}, axis=1)
    # df_21 = df_21[df_21["2021"].notnull()]
    # df_21 = df_21[df_21["2021"] <= 250000]
    # df_21 = df_21[df_21["2021"] >= 10000]
    # df_21 = df_21[df_21["Employment"] == "Employed full-time"]
    # df_21 = df_21.drop("Employment", axis=1)

    # CONCAT AFTER CORONA ERA
    df_list_af = [df_20 , df_21]
    df_af = pd.concat(df_list_af)
    # df_af['Country'] = df_af['Country'].apply(clean_country_name)
    # country_map = shorten_categories(df_af.Country.value_counts(), 2000)
    # df_af['Country'] = df_af['Country'].map(country_map)
    # df_af = df_af[df_af["Country"] != "Other"]
    df_af = df_af[df_af["After"].notnull()]
    df_af = df_af[df_af["After"] <= 250000]
    df_af = df_af[df_af["After"] >= 10000]
    df_af = df_af[df_af["Employment"] == "Employed full-time"]
    df_af = df_af.drop("Employment", axis=1)

    # FINAL CONCAT
    df_list = [df_af,df_bf]
    df = pd.concat(df_list)
    df['Country'] = df['Country'].apply(clean_country_name)
    country_map = shorten_categories(df.Country.value_counts(), 2000)
    df['Country'] = df['Country'].map(country_map)
    df = df[df["Country"] != "Other"]

    return df

# main page
def show_analysis_page():
    col1, col2 = st.columns([4, 2])

    col2.write("""#### """)
    col2.write("""#### """)
    col2.write("""#### """)
    col2.write("""#### """)
    col2.write("""#### """)
    

    col1.title('Analysis')

    
    expander = col2.expander("Analysis Through Years")
    years = ('2021' , '2020' ,'2019' ,'2018')
    dropdown = expander.multiselect('Pick a year', years , default='2021')


    expander = col2.expander("Analysis Through Corona Era")
    eras = ('Before' , 'After' )
    era = expander.multiselect('Pick a year', eras , default='After')
    
    if len(dropdown) > 0:
        df=load_data_years()
        data = df.groupby(["Country"])[dropdown].mean()
        col1.write("""#### Mean Salary Based On Year """ )
        col1.subheader('Analysis of Years -  {}'.format(dropdown))
        col1.line_chart(data , height=500)
        # data = df.groupby(["Country"]).mean()

    elif len(era) > 0 :
        df=load_data_era()
        data = df.groupby(["Country"])[era].mean()
        col1.write("""#### Mean Salary Based On Corona Era """ )
        col1.subheader('Analysis of Corona Era -  {}'.format(era))
        col1.line_chart(data , height=500)

    
    
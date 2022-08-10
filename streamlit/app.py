import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import os
import sys
import matplotlib.pyplot as plt
import warnings
import seaborn as sns
from sklearn import preprocessing
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
warnings.filterwarnings("ignore")

# adding scripts to path
sys.path.append(os.path.abspath("../scripts/python"))

# loading scripts
from connection_manager import Manager
from modeling_utils import Modeling_Utils
man = Manager()
util = Modeling_Utils()

["width", "site_name", "platform_os",	"device_type", "browser", "startdate", "volume_agreed", "agency_fee"]

connection, cursor = man.connect_to_server(host="localhost", port=5432, user="warehouse", password="warehouse", dbName="warehouse")
data = man.fetch_data(conn=connection, limit=10000)
def train():
    
    
    plt.figure(figsize=(15, 7))
    sns.set(style="ticks")
    sns.set(font_scale = 2)
    sns.set_style("white")
    sns.set_style("whitegrid")
    sns.despine()
    ax = sns.lineplot(x=df[df.columns[0]], y=df[df.columns[1]])
    ax.spines['left'].set_linewidth(5)
    ax.spines['bottom'].set_linewidth(5)
    ax.spines['left'].set_color('black')
    ax.spines['bottom'].set_color('black')
    plt.title(title)
    plt.savefig("temp_image.png")
    st.image("temp_image.png")

def app():

    st.title("Predict Likilihood")
    st.subheader("This model will predict the sales and number of customers on a specified date")
    Width= st.number_input("width", min_value=0, max_value=3115)
    site_name = st.text_input("site_name", "site_name")
    platform_os = st.text_input("platform_os", "platform_os")
    device_type = st.text_input("device_type", "device_type")
    browser = st.text_input("browser", "browser")
    startdate = st.text_input("startdate", "startdate")
    volume_agreed = st.text_input("volume_agreed", "volume_agreed")
    agency_fee = st.text_input("agency_fee", "agency_fee")


    calculate = st.button('Calculate')
    if ((uploaded_file is not None) and (calculate)):
        input = pd.read_csv(uploaded_file)
        new_df = input[select_list]
        new_df.insert(1, 'Assortment', Assortment)
        new_df.insert(2, 'StoreType', StoreType)
        new_df.insert(7, "Store", Store)
        new_df.insert(8, "CompDist", dist)
        new_df.insert(0, "Sales", 0)
        new_df[:] = scaler.transform(new_df[:])
        new_df.pop("Sales")
        prediction = model.predict(new_df)
        new_df.insert(0, "Sales", prediction)
        
        new_df[:] = scaler.inverse_transform(new_df[:])
        
        st.subheader("The calculated sales:")
        st.write(new_df)
        
        aggr_m = new_df[["Month", "Sales"]].groupby(["Month"]).agg({"Sales": "mean"}).reset_index()
        aggr_w = new_df[["WeekOfYear", "Sales"]].groupby(["WeekOfYear"]).agg({"Sales": "mean"}).reset_index()
        aggr_wd = new_df[["DayOfWeek", "Sales"]].groupby(["DayOfWeek"]).agg({"Sales": "mean"}).reset_index()
        aggr_md = new_df[["DayOfMonth", "Sales"]].groupby(["DayOfMonth"]).agg({"Sales": "mean"}).reset_index()

        plot(aggr_m, "Average Sales Accross Months")
        st.markdown("""---""")
        plot(aggr_w, "Average Sales Across Weeks")
        st.markdown("""---""")
        plot(aggr_wd, "Average Sales Across Days of the Week")
        st.markdown("""---""")
        plot(aggr_md, "Average Sales Across Days of the Month")
       

if __name__ == "main":
    pass
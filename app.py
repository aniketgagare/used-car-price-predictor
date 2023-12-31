import streamlit as st
import pickle
import numpy as np
import pandas as pd


st.markdown("<center><b><h1>Welcome_to_car_price_predictor<h1><b/><center/>",unsafe_allow_html=True)

pipe=pickle.load(open("pipe.pkl","rb"))

df=pickle.load(open("dataframe.pkl","rb"))
df=df.dropna()

# Taking input from user

company=st.selectbox("brand",sorted(df["company"].unique()))

year_of_purchase=int(st.number_input("year_of_purchase", value=0, step=1))

transmission_type=st.selectbox("Transmission Type",sorted(df["transmission_type"].unique()))

km_driven =float(st.number_input("Kilometers Driven"))

fuel_type=st.selectbox("Fuel Type",sorted(df["fuel_type"].unique()))

no_of_seats=float(st.number_input("no_of_seats", value=0, step=1))


if st.button("predict_price"):

    data=[[company,year_of_purchase,km_driven,fuel_type,transmission_type,no_of_seats]]


    one_df=pd.DataFrame(data,columns=df.columns[:-1])

    price=pipe.predict(one_df)[0]

    if price<0:
        st.text("not going to take car")

    else:
        st.text(f"price of car is {price} INR ")

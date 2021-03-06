#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 23:38:47 2021

@author: cindy
"""

import streamlit as st
import pandas as pd
import numpy as np

st.title('HHA 507: Deployment of E2E Data Process with Streamlit')
st.write('Cindy Mei :collision:') 

hospital_df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_hospital_2.csv')
inpatient_df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_inpatient_2.csv')
outpatient_df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_outpatient_2.csv')

@st.cache
def load_hospitals():
    hospital_df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_hospital_2.csv')
    return hospital_df

@st.cache
def load_inpatient():
    inpatient_df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_inpatient_2.csv')
    return inpatient_df

@st.cache
def load_outpatient():
    outpatient_df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_outpatient_2.csv')
    return outpatient_df


st.header('All Hospital Data')
st.dataframe(hospital_df)

st.header('All Inpatient Data Preview')
st.dataframe(inpatient_df)

st.header('All Outpatient Data')
st.dataframe(outpatient_df)

st.header('Stony Brook Hospital Inpatient Data')
SB_inpatient = inpatient_df[inpatient_df['provider_id']== 330393]
st.dataframe(SB_inpatient)

st.header('Stony Brook Hospital Outpatient Data')
SB_outpatient = outpatient_df[outpatient_df['provider_id'] == 330393]
st.dataframe(SB_outpatient)

st.header('Hospitals in NY Excluding Stony Brook')
NY_notSB = hospital_df[hospital_df['provider_id'] != 330393]
NY_notSB = hospital_df[hospital_df['state'] == 'NY']
st.dataframe(NY_notSB)


st.header('Question 1. What are the most expensive inpatient DRGs at Stony Brook?')
st.markdown('Answer: The most expensive SB inpatient DRG is 003 - ECMO OR TRACH W MV >96 HRS OR PDX EXC FACE, MOUTH & NECK W MAJ O.R., averaging $216,636.88')
st.markdown('The pivot table below shows the average total payments of SB inpatient DRGs in descending order.')
SB_inpatientDRGs_pivot = SB_inpatient.pivot_table(index=['provider_id','drg_definition'],values=['average_total_payments'])
SB_inpatientDRGs_order = SB_inpatientDRGs_pivot.sort_values(['average_total_payments'], ascending=False)
st.dataframe(SB_inpatientDRGs_order)


st.header('Question 2. What is the most common type of hospital in the U.S.?')
st.markdown('Answer: The bar chart shows that the most common hospital type is acute care, followed by critical access hospitals.')
type_bar = hospital_df['hospital_type'].value_counts().reset_index()
st.bar_chart(data=type_bar, width=0, height=0, use_container_width=True)


st.header('Question 3. Which state has the most hospitals?')
st.markdown('Answer: The bar chart shows that the majority of hospitals are located in TX (449), followed by CA (378).')
state_bar = hospital_df['state'].value_counts().reset_index()
st.bar_chart(data=state_bar, width=0, height=0, use_container_width=True)


st.header('Question 4. What are the most common categories of hospital ownership within NY?')
st.markdown('Answer: The area chart shows that the majority of NY hospitals are voluntary nonprofit.')
NY_ownership = NY_notSB['hospital_ownership'].value_counts().reset_index()
st.area_chart(data=NY_ownership, width=0, height=0, use_container_width=True)


st.header('Question 5. Which county in NY has the most hospitals?')
st.markdown('Answer: Schoharie (56) and Cayuga (55) are NY counties with the most hospitals.')
city_bar = NY_notSB['county_name'].value_counts().reset_index()
st.bar_chart(data=city_bar, width=0, height=0, use_container_width=True)


st.header('Question 6. Which state has the most outpatient providers?')
st.markdown('Answer: Texas has the most outpatient providers (2205), followed by California (2113).')
outpatient_bar = outpatient_df['provider_state'].value_counts().reset_index()
st.bar_chart(data=outpatient_bar, width=0, height=0, use_container_width=True)







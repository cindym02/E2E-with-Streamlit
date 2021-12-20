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
st.write('Shuwen Tan :smiley:') 

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


st.header('Hospital Data')
st.dataframe(hospital_df)

st.header('Inpatient Data Preview')
st.dataframe(inpatient_df)

st.header('Outpatient Data')
st.dataframe(outpatient_df)

st.header('Hospitals in NY Excluding Stony Brook')
NY = hospital_df[hospital_df['state'] == 'NY']
NY = hospital_df[hospital_df['state'] != 'NY']



st.header('Question 1. How does Stony Brook compare to the rest of NY?')

st.header('Question 2. What are the most expensive inpatient DRGs at Stony Brook?')

st.header('Question 3. What are the most expensive outpatient DRGs at Stony Brook?')



st.write('')

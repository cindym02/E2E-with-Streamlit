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
st.write('Cindy Mei :smiley:') 

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


st.header('Question 1. How does Stony Brook compare to the rest of NY?')


st.header('Question 2. What are the most expensive inpatient DRGs at Stony Brook?')
SB_inpatientDRGs_pivot = SB_inpatient.pivot_table(index=['provider_id','drg_definition'],values=['average_total_payments'])
SB_inpatientDRGs_order = SB_inpatientDRGs_pivot.sort_values(['average_total_payments'], ascending=False)
st.dataframe(SB_inpatientDRGs_order)

st.header('Question 3. What are the most expensive outpatient DRGs at Stony Brook?')


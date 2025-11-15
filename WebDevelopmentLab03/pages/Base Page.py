import streamlit as st
import requests as requests
import pandas as pd
def mostPopulated(region, num):
    adict = {}
    bdict = {}
    res = requests.get(f'https://restcountries.com/v3.1/region/{region}')
    variable = res.json()
    for country in variable:
        adict[country['name']['common']] = country['population']
    for i in range(num):
        maxpop = 0
        maxcon = ''
        for key, value in adict.items():
            if value > maxpop:
                maxpop = value
                maxcon = key
        bdict[maxcon] = maxpop
        adict.pop(maxcon)
    return bdict

slid1 = st.slider('Adjust the slider to the x highest number of populations in a region', 1, 14, step=1, key='one')
inp1 = st.selectbox('What region would you like to see from the list below?', options =['Europe', 'Asia', 'Americas', 'Oceania', 'Africa', 'South America'], key = 'two')

if 'two' not in st.session_state:
    st.session_state.two = inp1

if 'one' not in st.session_state:
    st.session_state.one = slid1

a = mostPopulated(inp1, slid1)
st.write(a)
st.bar_chart(a, y = 'value')



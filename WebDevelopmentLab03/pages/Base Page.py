import streamlit as st
import requests as requests
st.write('Hi')
def languageCapitals(language):
    alist = []
    res = requests.get(f'https://restcountries.com/v3.1/lang/{language}')
    if res.status_code == 200:
        print('Success!')
    variable = res.json()
    for i in range(len(variable)):
        if variable[i]['area'] > 1000000:
            alist.append(variable[i]['capital'][0])
    return sorted(alist)
st.write(languageCapitals('English'))


import streamlit as st
from datetime import date

amount=350000   #Spending up to 16/02/2024
extra = 16822 #Spending up to 27/02/2024

st.header('Project E', divider='rainbow')
today = date.today()
st.write(f'Spending as of {today}')
amount_p = '₹' + str(amount)
st.write(amount_p)
st.write('Extra Spending')
extra_amount = '₹' + str(extra)
st.write(extra_amount)
spent = (amount/350000)*100
#print(spent)
result = st.slider('Amount Spent Percentage', 0, 100, round(spent))

Details1 = '[Spending Details (Current)](https://docs.google.com/spreadsheets/d/12Yan1dsOCCYXrkRDGmZ4CXrQY-sZP-vB/edit?usp=sharing&ouid=102403513019249144512&rtpof=true&sd=true)'
st.markdown(Details1, unsafe_allow_html=True)

Details2 = '[Spending Details (Old)](https://docs.google.com/spreadsheets/d/1uYHIpqs-cm0l-PMWME5GUpxgSNCa3NNt/edit?usp=drive_link&ouid=102403513019249144512&rtpof=true&sd=true)'
st.markdown(Details2, unsafe_allow_html=True)

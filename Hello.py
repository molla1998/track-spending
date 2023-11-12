import streamlit as st
from datetime import date

amount=100000 #Update Here

today = date.today()
st.write(f'Spending as of {today}')
amount_p = '₹' + str(amount)
st.write(amount_p)
spent = (amount/350000)*100
#print(spent)
result = st.slider('Amount Spent Percentage', 0, 100, round(spent))
Details = '[Spending Details](https://docs.google.com/spreadsheets/d/1uYHIpqs-cm0l-PMWME5GUpxgSNCa3NNt/edit?usp=drive_link&ouid=102403513019249144512&rtpof=true&sd=true)'
st.markdown(Details, unsafe_allow_html=True)

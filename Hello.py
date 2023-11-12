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

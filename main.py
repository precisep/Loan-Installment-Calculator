"""
    Streamlit Financial Calculator.

    Author: Thabang P Mokoena
    Date: 2023/01/07
    Description: This file is used to launch a minimal streamlit web 
	application. A financial calculator that estimates the monthly installment that will be paid 
    for covering the a personal loan.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

    To get a background of the application , see:

    https://rcs.co.za/lifestyle/articles/loan-payment-formula-for-financial-planning-2022

"""

#Streamlit depends 
import streamlit as st
from calculator import monthly_installment


#SEO configuration
st.set_page_config (page_title = 'Fincial Calculator:  Monthly Installment Estimation ',
                    page_icon ='📱', 
                    layout ='centered'
)



def main ():
    st.title("Financial Calculator")
    

    principal = st.number_input('ENTER LOAN AMOUNT R')
    period = st.slider('LOAN TERM IN YEARS',1,20)
    interest_rate = st.slider('ARIABLE INTEREST RATE %', 7.75, 0.25, 25.75)

    if st.button('Calculate Monthly Installment'):
        st.write('Your Monthly Installment for the loan of R'+str(principal)+ ' is R' +str(monthly_installment(principal,period,interest_rate)))
    
        

    

if __name__ =='__main__':
    main()
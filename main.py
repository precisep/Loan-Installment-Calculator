"""
    Streamlit Financial Calculator.

    Author: Thabang P Mokoena
    Company Name: Immensity Holdings (pty) ltd
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
import streamlit as st #  pip install streamlit
from calculator import monthly_installment
import base64 #pip install base64

#SEO configuration
st.set_page_config (page_title = 'Fincial Calculator:  Monthly Installment Estimation ',
                    page_icon ='', 
                    layout ='centered'
)

# modify app display
hide_menu = """
<style>
#MainMenu {
    visibility: hidden;
    }

footer {
    visibility: visible;
}
footer:before{
    content:'Copyright (c) 2023: Immensity Holdings';
    display:block;
    position:relative;
    color:#D33639;
}
<style>
"""

def main ():

    """### gif from local file"""
    file_ = open("./assests/animated_og.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    image = f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">'
    st.markdown( f"<h1 style='text-align: center'>{image}</h1>",
        unsafe_allow_html=True,
        )

    st.markdown(hide_menu,unsafe_allow_html=True)
    st.title("Financial Calculator")
    
    with st.form('data_form', clear_on_submit=False):
        principal = st.number_input('ENTER LOAN AMOUNT R')
        period = st.slider('LOAN TERM IN YEARS',1,20)
        interest_rate = st.slider('VARIABLE INTEREST RATE %', 7.75, 0.25, 25.75)

        if st.form_submit_button('Calculate Monthly Installment'):
            st.write('Your Monthly Installment for the loan of R'+str(principal)+ ' is R' +str(monthly_installment(principal,period,interest_rate)))
    

if __name__ =='__main__':
    main()
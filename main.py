import streamlit as st
import streamlit.components.v1 as components
import json 

from supabase import create_client, Client

st.title("Health Portal")   

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

supabase = init_connection()

def login_otp(email):   
    response = supabase.auth.sign_in_with_otp({"email": email})
    st.write("Check your email address for your token code")

def verify_otp(email, token_code, type):
    response = supabase.auth.verify_otp({"email": email, "token_code": token_code, "type": type})
    if response.user:   
      st.session_state.user = response.user
      st.success("welcome")
    else:
        st.warning("Token expired or Invalid token.")
  

col1, col2 = st.columns(2)
    with col1:
        with st.expander('Generate Token to Login'):
            email = st.text_input('Email', key='enter email address')
            generate_btn = st.button('Login', on_click=login_otp, args=(email)
    with col2:
        with st.expander('Verify Token'):
            email = st.text_input('Email', key='email address')
            password = st.text_input('Token', key='Token')
            type = st.text_input('Type', key='Type')
            verify_btn = st.button('Verify Token', on_click=verify_otp, args=(email, token, type))

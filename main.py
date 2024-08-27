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
        st.warning("Login failed. check your credentials.")
  


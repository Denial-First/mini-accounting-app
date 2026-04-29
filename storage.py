import streamlit as st


def get_data():
    if "transactions" not in st.session_state:
        st.session_state.transactions = []
    if "postings" not in st.session_state:
        st.session_state.postings = []

    return st.session_state.transactions, st.session_state.postings
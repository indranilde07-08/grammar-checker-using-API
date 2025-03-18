import streamlit as st
from backend import check_grammar,convert_to_formal,convert_to_casual

st.markdown(
    """
     <style>
    div.stButton > button:first-child {
        background-color: #4CAF50; /* Green */
        color: white;
        border-radius: 10px;
        font-size: 16px;
        padding: 10px 24px;
    }
    </style>
    """,
    unsafe_allow_html=True
)





st.header("Checking Grammar")


text = st.text_input("Enter the sentence")

if st.button("check grammar"):
    st.info(check_grammar(text))

if st.button("convert formal"):
    st.info(convert_to_formal(text))
if st.button("convert casual"):
    st.info(convert_to_casual(text))
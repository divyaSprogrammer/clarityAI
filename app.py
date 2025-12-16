import streamlit as st

st.title("🛡️ SafeRoute AI")
st.write("Intelligent Women’s Safety Navigation & Emergency Response System")

st.header("🚨 Emergency")
if st.button("SOS"):
    st.warning("Emergency Alert Sent!")


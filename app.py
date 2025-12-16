import streamlit as st

# App Title
st.title("🛡️ SafeRoute AI")
st.write("Intelligent Women’s Safety Navigation & Emergency Response System")

st.markdown("---")

# Emergency Section
st.header("🚨 Emergency")
if st.button("SOS"):
    st.error("🚨 Emergency Alert Sent! Help is on the way.")

st.markdown("---")

# Location Input
st.header("📍 Enter Your Location")

latitude = st.number_input("Enter Latitude", value=12.9716)
longitude = st.number_input("Enter Longitude", value=77.5946)

st.write("📌 Your Location:")
st.write("Latitude:", latitude)
st.write("Longitude:", longitude)

st.markdown("---")

# Safety Check
st.header("🧠 Safety Check")

time = st.selectbox("Select Time", ["Day", "Night"])

if time == "Night":
    st.warning("⚠️ Be Careful! Night time travel is risky.")
else:
    st.success("✅ Day time travel is safer.")

st.markdown("---")
st.info("Future: AI-based safety prediction, live GPS, police alerts")


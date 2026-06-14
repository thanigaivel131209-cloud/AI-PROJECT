import streamlit as st
from chatbot import chatbot_response

st.set_page_config(
    page_title="Renewable Energy Output Predictor",
    page_icon="🌱"
)

st.title("🌱 Renewable Energy Output Predictor")

page = st.sidebar.selectbox(
    "Navigation",
    ["Home", "Solar", "Wind", "Analytics", "Chatbot"]
)

if page == "Home":
    st.header("🏠 Home")

    st.write("""
    Welcome to the Renewable Energy Output Predictor.

    Features:
    • Solar Energy Prediction
    • Wind Energy Prediction
    • Analytics Dashboard
    • Renewable Energy Chatbot
    """)

elif page == "Solar":
    st.header("☀ Solar Energy Prediction")

    temperature = st.slider("Temperature (°C)", 0, 50, 25)

    if st.button("Predict Solar Output"):
        st.success("Predicted Output: 85 kWh (Demo Value)")

elif page == "Wind":
    st.header("🌬 Wind Energy Prediction")

    wind_speed = st.slider("Wind Speed (km/h)", 0, 100, 30)

    if st.button("Predict Wind Output"):
        st.success("Predicted Output: 120 kWh (Demo Value)")

elif page == "Analytics":
    st.header("📊 Analytics Dashboard")

    st.metric("Solar Output", "85 kWh")
    st.metric("Wind Output", "120 kWh")

    st.line_chart([10, 20, 15, 30, 25])

elif page == "Chatbot":
    st.header("🤖 Renewable Energy Chatbot")

    user_input = st.text_input("Ask a question")

    if user_input:
        st.write(chatbot_response(user_input))
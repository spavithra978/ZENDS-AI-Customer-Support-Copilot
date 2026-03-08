# app.py

import streamlit as st
from copilot import zends_ai_copilot

st.set_page_config(page_title="ZENDS AI Copilot", layout="wide")

st.title("📡 ZENDS AI Customer Support Copilot")

st.write("Enter a customer query to analyze intent, sentiment, and retrieve relevant company policy.")

# Input box
user_query = st.text_area("Enter Customer Query")

# Button
if st.button("Analyze Query"):

    if user_query.strip() == "":
        st.warning("Please enter a query.")
    else:

        intent, sentiment, policy, response = zends_ai_copilot(user_query)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📊 Prediction Results")
            st.write("Intent:", intent)
            st.write("Sentiment:", sentiment)

        with col2:
            st.subheader("📚 Retrieved Policy")
            st.write(policy)

        st.subheader("🤖 AI Recommended Response")
        st.write(response)
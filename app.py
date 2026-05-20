import streamlit as st
from copilot import zends_ai_copilot

# Page config
st.set_page_config(
    page_title="ZENDS AI Copilot",
    page_icon="📡",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

.stTextArea textarea {
    background-color: #1E1E1E;
    color: white;
    border-radius: 10px;
}

div.stButton > button {
    background: linear-gradient(90deg,#00C6FF,#0072FF);
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
}

.result-box {
    background-color: #1E1E1E;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.5);
}

.header-title {
    font-size: 42px;
    font-weight: bold;
    color: #00C6FF;
}

.sub-text {
    font-size: 18px;
    color: #CCCCCC;
}

</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/1041/1041916.png",
    width=100
)

st.sidebar.title("📡 ZENDS AI")
st.sidebar.markdown("### Telecom Customer Support Copilot")

st.sidebar.info("""
This AI system can:

✅ Predict customer intent  
✅ Detect sentiment  
✅ Retrieve telecom policies  
✅ Recommend support responses
""")

# Main Title
st.markdown(
    '<p class="header-title">📡 ZENDS AI Customer Support Copilot</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-text">AI-powered telecom customer query analysis dashboard</p>',
    unsafe_allow_html=True
)

st.divider()

# Input
user_query = st.text_area(
    "💬 Enter Customer Query",
    placeholder="Example: My recharge failed but amount got deducted..."
)

# Button
if st.button("🚀 Analyze Query"):

    intent, sentiment, policy, response = zends_ai_copilot(user_query)

    st.divider()

    col1, col2 = st.columns(2)

    # Prediction Box
    with col1:
        st.markdown("""
        <div class="result-box">
        <h2>📊 Prediction Results</h2>
        """, unsafe_allow_html=True)

        st.metric("Intent", intent)
        st.metric("Sentiment", sentiment)

        st.markdown("</div>", unsafe_allow_html=True)

    # Policy Box
    with col2:
        st.markdown("""
        <div class="result-box">
        <h2>📚 Retrieved Policy</h2>
        """, unsafe_allow_html=True)

        st.write(policy)

        st.markdown("</div>", unsafe_allow_html=True)

    # AI Response
    st.markdown("""
    <div class="result-box">
    <h2>🤖 AI Recommended Response</h2>
    """, unsafe_allow_html=True)

    st.write(response)

    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.divider()

st.caption("🚀 Developed using Streamlit | Transformers | NLP | RAG")
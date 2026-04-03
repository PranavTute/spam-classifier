import streamlit as st
import pickle

# Page config
st.set_page_config(page_title="Spam Detector", page_icon="📩", layout="centered")

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Custom CSS
st.markdown("""
    <style>
    body {
        background-color: #0f172a;
    }
    .main {
        background-color: #0f172a;
        color: white;
    }
    .stTextArea textarea {
        border-radius: 10px;
        border: 2px solid #6366f1;
        padding: 10px;
    }
    .stButton>button {
        background-color: #6366f1;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center;'>📩 Spam Message Detector</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>AI-powered spam detection system</p>", unsafe_allow_html=True)

# Input box
message = st.text_area("✍️ Enter your message here:")

# Button
if st.button("🔍 Analyze Message"):
    if message.strip() == "":
        st.warning("⚠️ Please enter a message first")
    else:
        data = vectorizer.transform([message])
        prediction = model.predict(data)

        st.markdown("---")

        if prediction[0] == 1:
            st.error("🚨 This is a SPAM message!")
        else:
            st.success("✅ This is NOT a spam message")

# Footer
st.markdown("---")
st.markdown("<p style='text-align:center; font-size:12px;'>Built with ❤️ using Machine Learning</p>", unsafe_allow_html=True)
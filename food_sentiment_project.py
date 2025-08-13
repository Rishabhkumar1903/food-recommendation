import streamlit as st
import joblib
import pandas as pd

model=joblib.load("food_review_sentiment.pkl")

st.set_page_config(page_title="food sentiment", layout="wide") 

import streamlit as st
import base64

# Encode your local image to base64
def set_bg_local(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# 👇 Put your local image filename here (must be in same folder as app)
set_bg_local("E:\ML Images\Sentiment-Analysis.jpg")

st.markdown("""
    <div style="background-color:brown;border-radius:10px;text-align:center;">
        <h1 style="color:burlywood;">🍔FOOD SENTIMENT PREDICTION</h1>
    </div>
""", unsafe_allow_html=True)

# Add CSS for scrollable sidebar
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        overflow-y: auto;
        height: 100vh; /* Full height */
    }
    </style>
""", unsafe_allow_html=True)

# CSS for sidebar background color
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background-color: #f5d7b5; /* Light brown - change to any color */
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar content
with st.sidebar:
    st.sidebar.image("E:\ML Images\Fast-food.jpg")
    st.sidebar.text("Let food be thy medicine and medicine be the food." )
    st.sidebar.header("💬CONTACT US")
    st.sidebar.text("📞8809972414")
    st.sidebar.text("✉️rishabhverma190388099@gmail.com")

    st.sidebar.header("👥About US")
    st.sidebar.text("We are a group of ML engineers working on food sentiment")

st.markdown("""
    <style>
    .stTextInput input {
        width: 100%;
        padding: 20px;
        font-size: 16px;
        font-weight: bold;
        text-align:left;
        border-radius: 10px;
        border: none;
        background: linear-gradient(90deg, #FF5733, #FFC300);
        color: white;
        text-shadow: 1px 1px 3px #000;
    }
    .stTextInput input::placeholder {
        color: black;
        opacity: 0.7;
    }
    </style>
""", unsafe_allow_html=True)
msg = st.text_input("Your review is important for us...", placeholder="💬Enter your review here...")

if st.button("predict"):
    resp = model.predict([msg])
    if resp[0] == 0:
        st.markdown("<h2 style='color:red;'>👎 Dislike</h2>", unsafe_allow_html=True)
    else:
        st.markdown("<h2 style='color:green;'>👍 Like</h2>", unsafe_allow_html=True)
        st.balloons()

left_col, right_col = st.columns([6, 1])  # Wider left column to push uploader to extreme left

with left_col:
    st.markdown("📄 **Upload CSV or TXT file**")
    path = st.file_uploader(" ", type=['csv', 'txt'])  # empty label for cleaner look

with right_col:
    predict_clicked = st.button("Predict", key="predict_btn")

# If file is uploaded
if path is not None:
    df = pd.read_csv(path, names=["Msg"])
    
    # Layout for side-by-side DataFrames
    df_col1, df_col2 = st.columns([1, 1])

    with df_col1:
        st.markdown("### 📥 Uploaded Data")
        st.dataframe(df, width=500)

    with df_col2:
        if predict_clicked:
            # Add your actual model prediction here
            df["Sentiment"] = model.predict(df.Msg)
            df["Sentiment"] = df["Sentiment"].map({0: "👎 Dislike", 1: "👍 Like"})

            st.markdown("### 🤖 Predicted Sentiment")
            st.dataframe(df, width=500)
        else:
            st.markdown("### 🤖 Predicted Sentiment")
            st.info("Click **Predict** to analyze sentiment.")
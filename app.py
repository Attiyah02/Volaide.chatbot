import streamlit as st

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="My Beautiful Frontend",
    page_icon="✨",
    layout="wide",   # "centered" or "wide"
    initial_sidebar_state="expanded"
)

# ---- CUSTOM STYLING ----
st.markdown("""
    <style>
        .big-font {
            font-size:30px !important;
            font-weight: bold;
            color: #4CAF50;
        }
        .subtitle {
            font-size:18px !important;
            color: #555;
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            border-radius: 12px;
            height: 3em;
            width: 100%;
        }
    </style>
""", unsafe_allow_html=True)

# ---- HEADER ----
st.markdown("<p class='big-font'>🌸 Welcome to My App</p>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>A modern Streamlit frontend with style 🚀</p>", unsafe_allow_html=True)

st.write("---")

# ---- LAYOUT (COLUMNS) ----
col1, col2 = st.columns([2,1])

with col1:
    st.subheader("📊 Dashboard")
    st.line_chart({"Sales": [10, 30, 20, 50, 40, 70]})
    st.bar_chart({"Visitors": [100, 200, 150, 300, 250]})

with col2:
    st.subheader("⚙️ Controls")
    name = st.text_input("Enter your name")
    option = st.selectbox("Choose an option", ["Option A", "Option B", "Option C"])
    btn = st.button("Submit")

    if btn:
        st.success(f"✅ Hello {name}, you picked **{option}**!")

# ---- SIDEBAR ----
st.sidebar.header("Navigation")
st.sidebar.write("👉 Select a section")
st.sidebar.radio("Go to", ["Home", "Dashboard", "Settings"])
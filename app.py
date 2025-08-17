import streamlit as st

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
st.sidebar.title("🤖 Chatbot Settings")
bot_name = st.sidebar.text_input("Bot Name", "HelperBot")

st.title(f"💬 Chat with {bot_name}")

# Display chat messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div style='text-align:right; background:#DCF8C6; padding:8px; border-radius:10px; margin:5px 0'>{msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='text-align:left; background:#EEE; padding:8px; border-radius:10px; margin:5px 0'>{msg['content']}</div>", unsafe_allow_html=True)

# User input
user_input = st.text_input("Type your message:", key="input")

if st.button("Send") and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Simple bot response (replace with API call)
    bot_response = f"Echo: {user_input}"
    st.session_state.messages.append({"role": "bot", "content": bot_response})
    
    st.experimental_rerun()
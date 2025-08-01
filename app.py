import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

from ai_utils import generate_full_response
from sample_data import sample_user_data
from users import users

st.set_page_config("💰 Finance Chatbot Login", layout="centered")

# --- Session Handling ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

def login(username, password):
    if username in users and users[username] == password:
        st.session_state.authenticated = True
        st.session_state.username = username
    else:
        st.session_state.authenticated = False
        st.warning("❌ Invalid username or password.")

# --- Login UI ---
if not st.session_state.authenticated:
    st.title("🔐 Login to Finance Chatbot")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")
        if submitted:
            login(username, password)
else:
    st.title("💬 AI Finance Chatbot with Visual Insights")
    st.caption(f"Welcome, **{st.session_state.username}** 👋")

    user_input = st.text_area("🧠 Type your financial concern:", "")

    if user_input:
        result = generate_full_response(user_input)

        st.subheader("🧠 What I Understood")
        st.info(result["ai_thinking"])

        st.subheader("🎯 Detected Area of Concern")
        st.code(result["intent"])

        st.subheader("✅ Solution")
        st.success(result["solution"])

        st.subheader("📌 Why This Solution?")
        st.info(result["reasoning"])

        st.subheader("⚠️ Escape Plan")
        st.warning(result["escape_plan"])

        st.subheader("📈 Catch-Up Strategy")
        st.info(result["catch_up"])

        # Charts
        st.subheader("📊 Expenses Breakdown")
        expenses = sample_user_data["expenses"]
        df_expenses = pd.DataFrame(list(expenses.items()), columns=["Category", "Amount"])
        fig1, ax1 = plt.subplots()
        ax1.pie(df_expenses["Amount"], labels=df_expenses["Category"], autopct="%1.1f%%")
        ax1.set_title("Your Expenses Overview")
        st.pyplot(fig1)

        st.subheader("💳 Outstanding Loans")
        loans = sample_user_data["loans"]
        df_loans = pd.DataFrame(list(loans.items()), columns=["Type", "Outstanding"])
        st.bar_chart(df_loans.set_index("Type"))

    st.sidebar.success(f"🔓 Logged in as: {st.session_state.username}")
    if st.sidebar.button("Logout"):
        st.session_state.authenticated = False
        st.experimental_rerun()

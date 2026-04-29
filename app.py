import streamlit as st
from accounting import *
from storage import get_data
import pandas as pd

st.set_page_config(page_title="Mini Accounting", layout="wide")

transactions, postings = get_data()

st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    [
        "Create Transaction",
        "Receive Payment",
        "Pay Vendor",
        "Transactions",
        "Partner Ledger",
        "Statistics",
    ]
)

# --- NEW TRANSACTION ---
if page == "Create Transaction":
    st.title("Create Transaction")

    t_type = st.selectbox("Type", ["Receive", "Send"])
    amount = st.number_input("Amount", min_value=0.0)
    partner = st.text_input("Partner")

    if st.button("Submit"):
        if amount <= 0:
            st.warning("Amount must be > 0")
        else:
            if t_type == "Receive":
                new_postings = create_sale(amount, partner)
            else:
                new_postings = create_expense(amount, partner)

            transactions.append({
                "type": t_type + ' transaction',
                "amount": amount,
                "partner": partner
            })

            postings.extend(new_postings)

            st.success("Transaction added!")


# --- TRANSACTIONS ---
elif page == "Transactions":
    st.title("Transactions")

    for t in transactions:
        st.write(t)

    st.subheader("Postings")
    for p in postings:
        st.write(vars(p))


# --- P&L ---
elif page == "Statistics":
    st.title("Statistics")

    stats = calculate_stats(postings)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Revenue", stats['revenue'])
        st.metric("Expenses", stats['expenses'])
    with col2:
        st.metric('Waiting to receive', stats['receive'])
        st.metric('Waiting to pay', stats['pay'])
    with col3:
        st.write("Profit")
        if stats['profit'] < 0:
            st.error(stats['profit'])
        elif stats['profit'] > 0:
            st.success(stats['profit'])
        else:
            st.write(stats['profit'])

    st.metric('Cash',
              sum(stats['cash']),
              chart_type='line',
              chart_data=stats['cash'],
              width=200,
              delta=stats['cash'][-1] if stats['cash'] else 0,
              border=True)


# --- PARTNER LEDGER ---
elif page == "Partner Ledger":
    st.title("Partner Ledger")

    ledger = partner_ledger(postings)

    for partner, balance in ledger.items():
        st.write(f"{partner}: {balance}")

elif page == "Receive Payment":
    st.title("Receive Payment")

    amount = st.number_input("Amount", min_value=0.0)
    partner = st.text_input("Customer")

    if st.button("Receive"):
        postings.extend(receive_payment(amount, partner))

        transactions.append({
            "type": "Receive",
            "amount": amount,
            "partner": partner
        })

        st.success("Payment received!")

elif page == "Pay Vendor":
    st.title("Pay Vendor")

    amount = st.number_input("Amount", min_value=0.0)
    partner = st.text_input("Vendor")

    if st.button("Pay"):
        postings.extend(pay_vendor(amount, partner))

        transactions.append({
            "type": "Pay",
            "amount": amount,
            "partner": partner
        })

        st.success("Payment sent!")
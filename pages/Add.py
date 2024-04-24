import streamlit as st
import csv


st.title("Add a New Investment")
st.write("This is where you can add a new investment to your portfolio.")

# Add a form to the page
investment_name = st.text_input("Investment Name")
investment_type = st.selectbox("Investment Type", ["Stock", "Crypto", "ETF", "Mutual Fund"])
investment_price = st.number_input("Price ($)", step=0.01)
investment_quantity = st.number_input("Quantity", step=1)
investment_date = st.date_input("Date of Purchase")

# Add a button to submit the form
# On submit, add the data to investments.csv
if st.button("Add Investment"):
    st.write("Investment added successfully!")
    
    # Open the file in append mode
    with open("investments.csv", "a") as file:
        writer = csv.writer(file)
        
        # Write the data to the file
        # Format: Name,Type,Date,Qty,BoughtAt,CurrentPrice,CurrentValue,Profit/Loss
        writer.writerow([investment_name, investment_type, investment_date, investment_quantity, investment_price, investment_price, investment_price * investment_quantity, 0])
import streamlit as st
import csv
import pandas as pd
import requests


def update():
    # Open the file in read mode
    with open("investments.csv", "r") as file:
        reader = csv.reader(file)
        
        # Read the data from the file
        data = list(reader)

    # Get current prices for each investment
    for stock in data[1:]:
        symbol = stock[0]
        url = f"https://financialmodelingprep.com/api/v3/profile/{symbol}?apikey=XzSZA5ApPyZ9adxqJpkA7BWDlauaNUjC"
        res = requests.get(url).json()
        current_price = res[0]["price"]
        stock[5] = current_price
        stock[6] = round(current_price * float(stock[3]), 3)
        stock[7] = round(stock[6] - float(stock[4]) * float(stock[3]), 3)

    # Write the updated data to the file
    with open("investments.csv", "w") as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)


st.title("Welcome to Your Portfolio")
st.write("This is where you can view all of your investments.")

update()

# Open the file in read mode
with open("investments.csv", "r") as file:
    reader = csv.reader(file)
    
    # Read the data from the file
    data = list(reader)

df = pd.DataFrame(data[1:], columns=data[0])
df.index = [i + 1 for i in df.index]

st.write(df)
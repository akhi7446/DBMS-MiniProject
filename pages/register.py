import streamlit as st
import mysql.connector
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.switch_page_button import switch_page


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="dbname"
)


mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255), email VARCHAR(255))")


st.title("Registration")
username = st.text_input("Username")
password = st.text_input("Password", type="password")
email = st.text_input("Email")
    # Check if the user has submitted the form
if st.button("Register"):
        # Insert the user's data into the database
        sql = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
        val = (username, password, email)
        mycursor.execute(sql, val)
        mydb.commit()
        switch_page("home")
        # Show a confirmation message
        st.success("You have successfully registered!")

import streamlit as st
import mysql.connector
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.switch_page_button import switch_page

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="dbname"
)

st.set_page_config(
    page_title="Login App",
    page_icon="👋",
    initial_sidebar_state="collapsed"
)
col11, col12 = st.columns((2,10))

st.text('''
 █████╗ ██╗██████╗ ██╗     ██╗███╗   ██╗███████╗███████╗
██╔══██╗██║██╔══██╗██║     ██║████╗  ██║██╔════╝██╔════╝
███████║██║██████╔╝██║     ██║██╔██╗ ██║█████╗  ███████╗
██╔══██║██║██╔══██╗██║     ██║██║╚██╗██║██╔══╝  ╚════██║
██║  ██║██║██║  ██║███████╗██║██║ ╚████║███████╗███████║
╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝                                                       

''')
# st.title("Air Traffic Control System")
# Create a new table to store user accounts
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255), email VARCHAR(255))")

# st.title("Login")
username = st.text_input("Username")
password = st.text_input("Password", type="password")

col3, col4 = st.columns((2,10))

# Check if the user has submitted the form
if col3.button("Login"):
        # Retrieve the user's data from the database
        sql = "SELECT * FROM users WHERE username = %s AND password = %s"
        val = (username, password)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()

        # Check if the login credentials are correct
        if result:
            st.success("You have successfully logged in!")
            switch_page("load")
            
        else:
            st.error("Invalid username or password")
    
if col4.button("Register"):
        switch_page("register")

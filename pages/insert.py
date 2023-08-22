import streamlit as st
import mysql.connector
import pandas as pd
from streamlit_extras.switch_page_button import switch_page


# # Connect to the MySQL database
cnx = mysql.connector.connect(user='root', password='password',
                              host='localhost', database='dbname')
cursor = cnx.cursor()
create_table_query = '''CREATE TABLE IF NOT EXISTS flight_info (
                            flight_id INT NOT NULL AUTO_INCREMENT,
                            flight_number VARCHAR(10) NOT NULL,
                            airline VARCHAR(50) NOT NULL,
                            origin VARCHAR(50) NOT NULL,
                            destination VARCHAR(50) NOT NULL,
                            departure_time DATETIME NOT NULL,
                            eta DATETIME NOT NULL,
                            ata DATETIME NOT NULL,
                            altitude INT NOT NULL,
                            speed INT NOT NULL,
                            aircraft_type VARCHAR(50) NOT NULL,
                            heading INT NOT NULL,
                            departure_gate VARCHAR(10) NOT NULL,
                            arrival_gate VARCHAR(10) NOT NULL,
                            status VARCHAR(50) NOT NULL,
                            runway_number VARCHAR(10) NOT NULL,
                            controller_id INT NOT NULL,
                            controller_name VARCHAR(50) NOT NULL,
                            sector VARCHAR(50) NOT NULL,
                            PRIMARY KEY (flight_id)
                        )'''
cursor.execute(create_table_query)
cnx.commit()


col1, col2 = st.columns(2)
col3, col4 = st.columns((2,10))
col5, col6 = st.columns((2,10))


# Add input fields to each column
with col1:
    flight_id = st.text_input("Flight ID")

with col2:
    flight_number = st.text_input("Flight Number")

with col1:
    airline = st.text_input("Airline")

with col2:
    origin = st.text_input("Origin")

with col1:
    destination = st.text_input("Destination")

with col2:
    departure_time = st.text_input("Departure Time")

with col1:
    eta = st.text_input("Estimated Time of Arrival")

with col2:
    ata = st.text_input("Actual Time of Arrival")

with col1:
    altitude = st.text_input("Altitude")

with col2:
    speed = st.text_input("Speed")

with col1:
    aircraft_type = st.text_input("Aircraft Type")

with col2:
    heading = st.text_input("Heading")

with col1:
    departure_gate = st.text_input("Departure Gate")

with col2:
    arrival_gate = st.text_input("Arrival Gate")

with col1:
    status = st.text_input("Status")

with col2:
    runway_number = st.text_input("Runway Number")

with col1:
    controller_id = st.text_input("Air Traffic Controller ID")

with col2:
    controller_name = st.text_input("Air Traffic Controller Name")

with col1:
    sector = st.text_input("Sector")


cursor=cnx.cursor()
# When the user clicks the "Submit" button, create a dictionary with the flight information

with col3:
    if st.button("Submit"):
        sql = "INSERT INTO flight_info (flight_number, airline, origin, destination, departure_time, eta, ata, altitude, speed, aircraft_type, heading, departure_gate, arrival_gate, status, runway_number, controller_id, controller_name, sector) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (flight_number, airline, origin, destination, departure_time, eta, ata, altitude, speed, aircraft_type, heading, departure_gate, arrival_gate, status, runway_number, controller_id, controller_name, sector)
        cursor.execute(sql, values)
        cnx.commit()
        st.success("Data successfully inserted into table.")
        data = {
            'Flight ID': [flight_id],
            'Flight Number': [flight_number],
            'Airline': [airline],
            'Origin': [origin],
            'Destination': [destination],
            'Departure Time': [departure_time],
            'Estimated Time of Arrival': [eta],
            'Actual Time of Arrival': [ata],
            'Altitude': [altitude],
            'Speed': [speed],
            'Aircraft Type': [aircraft_type],
            'Heading': [heading],
            'Departure Gate': [departure_gate],
            'Arrival Gate': [arrival_gate],
            'Status': [status],
            'Runway Number': [runway_number],
            'Air Traffic Controller ID': [controller_id],
            'Air Traffic Controller Name': [controller_name],
            'Sector': [sector]
        }
        # Create a Pandas DataFrame from the dictionary and display it as a table
        df = pd.DataFrame(data)
        pd.set_option('display.max_rows', 1000)
        pd.set_option('display.max_columns', 1000)
        st.dataframe(df)
    if col4.button('Show'):
        switch_page("show")

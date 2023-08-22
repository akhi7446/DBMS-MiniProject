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
select_query = "SELECT flight_id, flight_number, airline, origin, destination,departure_time, eta, ata, altitude, speed, aircraft_type, heading, departure_gate, arrival_gate, status, runway_number, controller_id, controller_name, sector FROM flight_info"
cursor.execute(select_query)
data = cursor.fetchall()
for row in data:
    with st.expander(row[2]):
      with st.form(f'ID-{row[0]}'):
        flight_id = st.text_input("Flight ID",row[0])
        flight_number = st.text_input("Flight Number",row[1])
        airline = st.text_input("Airline",row[2])
        origin = st.text_input("Origin",row[3])
        destination = st.text_input("Destination",row[4])
        departure_time = st.text_input("Departure Time",row[5])
        eta = st.text_input("Estimated Time of Arrival",row[6])
        ata = st.text_input("Actual Time of Arrival",row[7])
        altitude = st.text_input("Altitude",row[8])
        speed = st.text_input("Speed",row[9])
        aircraft_type = st.text_input("Aircraft Type",row[10])
        heading = st.text_input("Heading",row[11])
        departure_gate = st.text_input("Departure Gate",row[12])
        arrival_gate = st.text_input("Arrival Gate",row[13])
        status = st.text_input("Status",row[14])
        runway_number = st.text_input("Runway Number",row[15])
        controller_id = st.text_input("Air Traffic Controller ID",row[16])
        controller_name = st.text_input("Air Traffic Controller Name",row[17])
        sector = st.text_input("Sector",row[18])
        if st.form_submit_button('Save'):
            update_query = "UPDATE flight_info SET flight_number=%s, airline=%s, origin=%s, destination=%s, departure_time=%s, eta=%s, ata=%s, altitude=%s, speed=%s, aircraft_type=%s, heading=%s, departure_gate=%s, arrival_gate=%s, status=%s, runway_number=%s, controller_id=%s, controller_name=%s, sector=%s WHERE flight_id=%s"
            cursor.execute(update_query, (flight_number, airline, origin, destination, departure_time, eta, ata, altitude, speed, aircraft_type, heading, departure_gate, arrival_gate, status, runway_number, controller_id, controller_name, sector, flight_id))
            cnx.commit()

        if st.form_submit_button('Delete'):
            cursor.execute(f'DELETE FROM flight_info WHERE flight_id ="{row[0]}";')
            cnx.commit()
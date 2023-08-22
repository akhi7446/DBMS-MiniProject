import streamlit as st
import mysql.connector
import pandas as pd
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.switch_page_button import switch_page

cnx = mysql.connector.connect(user='root', password='password',
                              host='localhost', database='dbname')
cursor=cnx.cursor()

select_query = "SELECT flight_id, flight_number, airline, origin, destination,departure_time, eta, ata, altitude, speed, aircraft_type, heading, departure_gate, arrival_gate, status, runway_number, controller_id, controller_name, sector FROM flight_info"
cursor.execute(select_query)
data = cursor.fetchall()
st.write("Data Entries")
if len(data) > 0:
    cols = ['Flight_Id', 'Flight_Number', 'Airline', 'Origin', 'Destination','Departure_Time', 'ETA', 'ATA', 'Altitude', 'Speed', 'Aircraft_Type', 'Heading', 'Departure_Gate', 'Arrival_Gate', 'Status', 'Runaway_Number', 'Controller_Id', 'Controller_Name', 'Sector']
    df = pd.DataFrame(data, columns=cols)
    st.dataframe(df)
else:
    st.warning('No data entries found.')

if st.button('↩'):
    switch_page('load')
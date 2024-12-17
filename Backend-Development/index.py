"""
REST API - Total Life Test

Requirements:
1. Design a clinician, patient, and an appointments table.
   --> Try to select a few fields that might be useful in the context.
   --> Setup relevant relationships between the two resources.

2. Implement endpoints to create, read, update, and delete for all resources.

3. Use an SQLlite database to store the data.

4. Validate incoming request data - DO NOT KNOW HOW TO DO THIS.

5. Be sure to include an NPI number in the clinician table.
   --> An NPI number is a unique identification number for covered health care
       providers in the US.
   --> When a new clinician is added onto the system, we will want to validate the NPI
       number, and check the clinicians first and last name, as well as their state using
       the https://npiregistry.cms.hhs.gov/api-page API.

Author: James Rota

Date Created: Dec 16th, 2024
Last Modified: Dec 16th, 2024

"""
# Step one and four 
#
# 1. Design a clinician, patient, and an appointments table.
#    --> Try to select a few fields that might be useful in the context.
#    --> Setup relevant relationships between the two resources.
# Reference: https://www.youtube.com/watch?v=29_AuYCrqjU 
# I used this video as a reference on how to create a database using python
# 
#
# 4. Use an SQLlite database to store the data.
#

import sqlite3

# Create the connection
connection = sqlite3.connect("REST.db")

# Make foreign keys possible to create relationships
connection.execute("PRAGMA foreign_keys = ON")

# Create a cursor
cursor = connection.cursor()

#Create the tables

#Clinician table - (NPI (Primary Key), clinician name, specialty (Anixety, Depression, etc))
cursor.execute("""
CREATE TABLE IF NOT EXISTS clinician (
    NPI_NUM INTEGER PRIMARY KEY, 
    name TEXT, 
    specialty TEXT
)
""")

# Patient table - (id (Primary Key), patient name, 
#                  clinician_id (forign key from clinician table),
#                  trouble (Why the patient is seeking therapy))
cursor.execute("""
CREATE TABLE IF NOT EXISTS patient (
    id INTEGER PRIMARY KEY,
    name TEXT, 
    clinician_id INTEGER, 
    trouble TEXT,
    FOREIGN KEY (clinician_id) REFERENCES clinician(NPI_NUM) ON DELETE CASCADE
)
""")

# Appointment table - (id (Primary Key), clinician_id (foreign key),
#                      patient_id (foreign key), 
#                      appointment_time (Time the appointment takes place) )
#

cursor.execute("""
CREATE TABLE IF NOT EXISTS appointment (
    id INTEGER PRIMARY KEY,
    clinician_id INTEGER, 
    patient_id INTEGER, 
    appointment_time TEXT,
    FOREIGN KEY (clinician_id) REFERENCES clinician(NPI_NUM) ON DELETE CASCADE,
    FOREIGN KEY (patient_id) REFERENCES patient(id) ON DELETE CASCADE
)
""")

#Inserting sample data
cursor.execute("INSERT INTO clinician VALUES(?, ?, ?)", (1, "John", "Anxiety"))
cursor.execute("INSERT INTO patient VALUES(?, ?, ?, ?)", (1, "Karen", 1, "Depression"))
cursor.execute("INSERT INTO appointment VALUES(?, ?, ?, ?)", (1, 1, 1, "12:30"))

connection.commit() # commit changes
connection.close() # close the connection

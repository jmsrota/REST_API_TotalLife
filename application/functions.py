"""
    This functions.py file is a place to implement create, read, update, and delete statements

    All my functions for the webpage are stored here. 

    Author: James Rota

    Date Created: Dec 16, 2024
    Last Modified: Dec 16, 2024

"""
import sqlite3

# Step Two
# Implement endpoints to create, read, update, and delete for all resources.

# Create the connection
connection = sqlite3.connect("REST.db")

# Allow foreign keys
connection.execute("PRAGMA foreign_keys = ON")

# Create cursor
cursor = connection.cursor()

# ------ Create Statements -------

def Create_new_clinician(NPI_NUM, name, specialty):
    cursor.execute("INSERT OR IGNORE INTO clinician VALUES(?, ?, ?)", (NPI_NUM, name, specialty)) # added the IGNORE TO AVOID DUPLICATES

def Create_new_patient(patient_id, name, clinician_id, specialty):
    cursor.execute("INSERT OR IGNORE INTO patient VALUES(?, ?, ?, ?)", (patient_id, name, clinician_id, specialty))

def Create_new_appointment(app_id, clinician_id, patient_id,  appointment_time):
    cursor.execute("INSERT OR IGNORE INTO appointment VALUES(?, ?, ?, ?)", (app_id, clinician_id, patient_id,  appointment_time))

# ------- Read Statements -------

# Get patient name from appointments table to display on the webpage

def get_appointments_info_patient_name():
    # Create the connection
    connection = sqlite3.connect("REST.db")

    cursor = connection.cursor()

    patient_name = cursor.execute("""
                   SELECT patient.name AS patient_name
                   FROM appointment
                   JOIN patient ON appointment.patient_id = patient.id
                   """).fetchall()
    
    connection.close()

    return patient_name

# Get clinician name from appointments table to display on the webpage

def get_appointments_info_clinician_name():
    # Create the connection
    connection = sqlite3.connect("REST.db")

    cursor = connection.cursor()

    clinician_name = cursor.execute("""
                   SELECT clinician.name AS clinician_name
                   FROM appointment
                   JOIN clinician ON appointment.clinician_id = clinician.NPI_NUM
                   """).fetchall()
    
    connection.close()

    return clinician_name

# Get appointment time from appointments table to display on the webpage

def get_appointments_info_appointment_time():
    # Create the connection
    connection = sqlite3.connect("REST.db")

    cursor = connection.cursor()

    appointment_time = cursor.execute("""
                   SELECT appointment_time
                   FROM appointment
                   """).fetchall()
    
    connection.close()

    return appointment_time

# ------ Update Statements ------ 

# Helper function to be used in updating patient's clinician, have to make sure the clinician exists
def check_if_clinician_exists(clinician_id):

    cursor.execute("SELECT COUNT(*) FROM clinician WHERE NPI_NUM = ?", (clinician_id,))
    
    # Fetch the result
    count = cursor.fetchone()[0]
    
    # Return True if the ID exists, otherwise False
    
    if count > 0:
        return True
    
    return False

# Update patient's clinician 

def update_patients_clinician(clinician_id, patient_id):

    query = """
            UPDATE patient
            SET clinician_id = ?
            WHERE id = ?;

            """
    
    if check_if_clinician_exists(clinician_id) == True:
        cursor.execute(query, (clinician_id, patient_id))
    else:
        print("Sorry, the process cannot be done, clinician does not exist")


# ------ Delete statements ------

# Delete patient

def remove_patient(patient_name):

    query = """
            DELETE FROM patient
            WHERE name = ?;
            
            """
    
    cursor.execute(query, (patient_name))

# Delete clinician

def remove_clinician(clinician_name):

    query = """
            DELETE FROM clinician
            WHERE name = ?;

            """
    cursor.execute(query, (clinician_name))

# Delete appointment

def remove_appointment(app_num):

    query = """
            DELETE FROM appointment
            WHERE id = ?;

            """
    cursor.execute(query, (app_num))


connection.close()


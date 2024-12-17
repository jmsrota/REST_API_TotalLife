"""
    This Create.py file is a place to implement create, read, update, and delete statements
    
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

# Create Statements

def Create_new_clinician(NPI_NUM, name, specialty):
    cursor.execute("INSERT OR IGNORE INTO clinician VALUES(?, ?, ?)", (NPI_NUM, name, specialty)) # added the IGNORE TO AVOID DUPLICATES

def Create_new_patient(patient_id, name, clinician_id, specialty):
    cursor.execute("INSERT INTO patient VALUES(?, ?, ?, ?)", (patient_id, name, clinician_id, specialty))

def Create_new_appointment(app_id, clinician_id, patient_id,  appointment_time):
    cursor.execute("INSERT INTO appointment VALUES(?, ?, ?, ?)", (app_id, clinician_id, patient_id,  appointment_time))

# Read Statements

def get_appointments_info():
    appointment_info = cursor.execute("""
                   SELECT appointment.appointment_time, clinician.name AS clinician_name, patient.name AS patient_name
                   FROM appointment
                   JOIN clinician ON appointment.clinician_id = clinician.NPI_NUM
                   JOIN patient ON appointment.patient_id = patient.id
                   """).fetchall()
    
    print(f'appointments_info: {appointment_info}')

# Update Statements

# Helper function to be used in updating patient's clinician, have to make sure the clinician exists
def check_if_clinician_exists(clinician_id):

    cursor.execute("SELECT COUNT(*) FROM clinician WHERE NPI_NUM = ?", (clinician_id,))
    
    # Fetch the result
    count = cursor.fetchone()[0]
    
    # Return True if the ID exists, otherwise False
    
    if count > 0:
        return True
    
    return False

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


# TEST 




connection.close()

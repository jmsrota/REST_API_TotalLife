"""
    Part 2:

    Objective: Create a simple frontend web app (ie. React app) that fetches and displays a list of
    appointments from the API in part 1.

    Requirements:
    --> Display appointments in a list, showing the patient's name, appointment time, and
        appointment status.
    --> Implement a time range filter.
    --> Style the application using any minimal styling framework (Tailwind CSS etc.)
    --> You must be able to demonstrate a working list by leveraging the backend in part 1a and
        populating it with data.

    Author: James Rota
"""

from flask import Blueprint, render_template, redirect
import sqlite3
from .functions import get_appointments_info_patient_name, get_appointments_info_clinician_name, get_appointments_info_appointment_time

main = Blueprint('main', __name__)

@main.route('/')
def home():
    p_name = get_appointments_info_patient_name() # get patient name
    c_name = get_appointments_info_clinician_name() # get clinician name
    a_time = get_appointments_info_appointment_time() # get appointment times

    # Remove database tuple formatting ie: ('karen'), ('john'), ('12:30')
    p_name = [row[0] for row in p_name]
    c_name = [row[0] for row in c_name]
    a_time = [row[0] for row in a_time]

    # Send database information to the webpage
    return render_template('homepage.html', p_name=p_name, c_name=c_name, a_time=a_time)

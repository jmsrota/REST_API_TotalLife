# Manage webpages, in this case, it is only one page. 

from flask import Blueprint, render_template
import sqlite3
from .functions import get_appointments_info_patient_name, get_appointments_info_clinician_name, get_appointments_info_appointment_time

main = Blueprint('main', __name__)

@main.route('/')
def home():
    p_name = get_appointments_info_patient_name() # get patient name
    c_name = get_appointments_info_clinician_name() # get clinician name
    a_time = get_appointments_info_appointment_time() # get appointment times


    return render_template('homepage.html', p_name=p_name, c_name=c_name, a_time=a_time)

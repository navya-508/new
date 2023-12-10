import sqlite3
from bottle import route, run, template, request, redirect


connection = sqlite3.connect("hospital-appointments.db")
cursor = connection.cursor()

def get_patients_with_appointments():
    cursor.execute("""
        SELECT patients.*, appointments.appointment_date, appointments.appointment_time, appointments.status
        FROM patients
        LEFT JOIN appointments ON patients.patient_id = appointments.patient_id
    """)
    result = cursor.fetchall()
    return result



@route('/')
def index():
    search_term = request.query.get('search', '').strip()

    
    patient_query = """
        SELECT patients.*, appointments.appointment_date, appointments.appointment_time, appointments.status
        FROM patients
        LEFT JOIN appointments ON patients.patient_id = appointments.patient_id
    """
    
    
    if search_term:
        patient_query += f" WHERE patients.patient_name LIKE '%{search_term}%' OR patients.contact_number LIKE '%{search_term}%' OR patients.date_of_birth LIKE '%{search_term}%' OR patients.gender LIKE '%{search_term}%'"

    cursor.execute(patient_query)
    patients_with_appointments = cursor.fetchall()

    
    
    

    return template('index', patients_with_appointments=patients_with_appointments, search_term=search_term)

  
@route('/add_patient')
def add_patient():
    return template('add_patient')

@route('/save_patient', method='POST')
def save_patient():
    patient_name = request.forms.get('patient_name')
    date_of_birth = request.forms.get('date_of_birth')
    gender = request.forms.get('gender')
    contact_number = request.forms.get('contact_number')
    
    appointment_date = request.forms.get('appointment_date')
    appointment_time = request.forms.get('appointment_time')
    appointment_status = request.forms.get('appointment_status')

    
    cursor.execute("""
        INSERT INTO patients (patient_name, date_of_birth, gender, contact_number)
        VALUES (?, ?, ?, ?)
    """, (patient_name, date_of_birth, gender, contact_number))

    
    cursor.execute("SELECT last_insert_rowid()")
    patient_id = cursor.fetchone()[0]

    
    cursor.execute("""
        INSERT INTO appointments (patient_id, appointment_date, appointment_time, status)
        VALUES (?, ?, ?, ?)
    """, (patient_id, appointment_date, appointment_time, appointment_status))

    connection.commit()
    redirect('/')

@route('/edit_patient/<patient_id>')
def edit_patient(patient_id):
    cursor.execute("""
    SELECT patients.*, appointments.appointment_date, appointments.appointment_time, appointments.status
    FROM patients
    LEFT JOIN appointments ON patients.patient_id = appointments.patient_id
    WHERE patients.patient_id=?
       """, (patient_id,))
    patient = cursor.fetchone()
    return template('edit_patient', patient=patient)

@route('/update_patient/<patient_id>', method='POST')
def update_patient(patient_id):
    patient_name = request.forms.get('patient_name')
    date_of_birth = request.forms.get('date_of_birth')
    gender = request.forms.get('gender')
    contact_number = request.forms.get('contact_number')
    
    appointment_date = request.forms.get('appointment_date')
    appointment_time = request.forms.get('appointment_time')
    appointment_status = request.forms.get('appointment_status')

    cursor.execute("""
        UPDATE patients
        SET patient_name=?, date_of_birth=?, gender=?, contact_number=?
        WHERE patient_id=?
    """, (patient_name, date_of_birth, gender, contact_number, patient_id))

    cursor.execute("""
        UPDATE appointments
        SET appointment_date=?, appointment_time=?, status=?
        WHERE patient_id=?
    """, (appointment_date, appointment_time, appointment_status, patient_id))

    connection.commit()
    
    redirect('/')

@route('/delete_patient/<patient_id>')
def delete_patient(patient_id):
    cursor.execute("DELETE FROM patients WHERE patient_id=?", (patient_id,))
    connection.commit()
    
    redirect('/')


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)

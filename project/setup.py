import sqlite3

connection = sqlite3.connect("hospital-appointments.db")
cursor = connection.cursor()


try:
    cursor.execute("DROP TABLE patients")
except sqlite3.OperationalError:
    pass

cursor.execute("""
    CREATE TABLE patients (
        patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_name TEXT,
        date_of_birth DATE,
        gender TEXT,
        contact_number TEXT
    )
""")


patients_data = [
    ('John',  '1980-01-15', 'Male', '555-1234'),
    ('Jane',  '1992-05-20', 'Female', '555-5678'),
    ('Robert',  '1975-09-10', 'Male', '555-9876'),
]

cursor.executemany("INSERT INTO patients (patient_name, date_of_birth, gender, contact_number) VALUES (?, ?, ?, ?)", patients_data)

try:
    cursor.execute("DROP TABLE appointments")
except sqlite3.OperationalError:
    pass

cursor.execute("""
    CREATE TABLE appointments (
        appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER,
        appointment_date DATE,
        appointment_time TIME,
        status TEXT,
        FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
    )
""")


appointments_data = [
    (1, '2023-12-10', '10:00 ', 'Scheduled'),
    (2, '2023-12-12', '02:30 ', 'Completed'),
    (3, '2023-12-15', '11:15 ', 'Scheduled'),
]

cursor.executemany("INSERT INTO appointments (patient_id, appointment_date, appointment_time, status) VALUES (?, ?, ?, ?)", appointments_data)

connection.commit()
connection.close()
print("done.")

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Patient</title>
</head>
<body>
    <h1>Edit Patient</h1>
    <form action="/update_patient/{{ patient[0] }}" method="post">
        <label for="patient_name">Name:</label>
        <input type="text" name="patient_name" value="{{ patient[1] }}" required><br>

        <label for="date_of_birth">Date of Birth:</label>
        <input type="date" name="date_of_birth" value="{{ patient[2] }}" required><br>

        <label for="gender">Gender:</label>
        <select name="gender" required>
            <option value="Male" % if patient[3] == 'Male': selected % end>Male</option>
            <option value="Female" % if patient[3] == 'Female': selected % end>Female</option>
        </select><br>

        <label for="contact_number">Contact Number:</label>
        <input type="text" name="contact_number" value="{{ patient[4] }}" required><br>

        
        <h2>Appointment Details</h2>
        <label for="appointment_date">Appointment Date:</label>
       <input type="date" name="appointment_date" value="{{ patient[5] }}"><br>
       <input type="time" name="appointment_time" value="{{ patient[6] }}"><br>
        <select name="appointment_status">
    <option value="Scheduled" % if patient[7] == 'Scheduled': selected % end>Scheduled</option>
    <option value="Completed" % if patient[7] == 'Completed': selected % end>Completed</option>
    
            
        </select><br>

        <input type="submit" value="Update">
    </form>
    <br>
    <a href="/">Back to Patients</a>
</body>
</html>

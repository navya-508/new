<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add New Patient</title>
</head>
<body>
    <h1>Add New Patient</h1>
    <form action="/save_patient" method="post">
        <label for="patient_name">Name:</label>
        <input type="text" name="patient_name" required><br>

        <label for="date_of_birth">Date of Birth:</label>
        <input type="date" name="date_of_birth" required><br>

        <label for="gender">Gender:</label>
        <select name="gender" required>
            <option value="Male">Male</option>
            <option value="Female">Female</option>
        </select><br>

        <label for="contact_number">Contact Number:</label>
        <input type="text" name="contact_number" required><br>

        
        <h2>Appointment Details</h2>
        <label for="appointment_date">Appointment Date:</label>
        <input type="date" name="appointment_date" required><br>

        <label for="appointment_time">Appointment Time:</label>
        <input type="time" name="appointment_time" required><br>

        <label for="appointment_status">Appointment Status:</label>
        <select name="appointment_status" required>
            <option value="Scheduled">Scheduled</option>
            <option value="Completed">Completed</option>
            <!-- Add more options if needed -->
        </select><br>

        <input type="submit" value="Save">
    </form>
    <br>
    <a href="/">Back to Patients</a>
</body>
</html>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hospital Appointments</title>
</head>
<body>
    <h1>Patients with Appointments</h1>
    
<form action="/" method="get">
    <label for="search">Search:</label>
    <input type="text" name="search" value="{{ search_term }}">
    <input type="submit" value="Search">
</form>
<table border="1">
    <tr>
        <th>Patient ID</th>
        <th>Name</th>
        <th>Date of Birth</th>
        <th>Gender</th>
        <th>Contact Number</th>
        <th>Appointment Date</th>
        <th>Appointment Time</th>
        <th>Status</th>
        <th>Edit</th>
        <th>Delete</th>
    </tr>
    % for row in patients_with_appointments:
        <tr>
            <td>{{ row[0] }}</td>  
            <td>{{ row[1] }}</td>
            <td>{{ row[2] }}</td>
            <td>{{ row[3] }}</td>
            <td>{{ row[4] }}</td>
            <td>{{ row[5] }}</td>
            <td>{{ row[6] }}</td>
            <td>{{ row[7] }}</td>
            <td><a href="/edit_patient/{{ row[0] }}">Edit</a></td>
            <td><a href="/delete_patient/{{ row[0] }}" onclick="return confirm('Are you sure you want to delete this patient?')">Delete</a></td>
        </tr>
    % end
</table>



    <br>
    <a href="/add_patient">Add New Patient</a>
</body>
</html>

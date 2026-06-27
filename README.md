# Student Management System

A simple Python-based console application for managing student records.

## Features

- **Add Student**: Add a new student by entering their ID, Name, and Marks. The grade is automatically calculated based on the marks.
- **Display Students**: View a list of all students currently in the system.
- **Search Student**: Find a specific student by their ID.
- **Update Marks**: Update the marks of an existing student.
- **Delete Student**: Remove a student from the system.
- **Topper**: Find and display the student with the highest marks.
- **Statistics**: View overall statistics, including the total number of students, highest marks, lowest marks, and average marks.
- **Save**: Save the current list of students to a text file (`students.txt`) for persistent storage.

## How to Run

1. Ensure you have Python installed on your system.
2. Clone this repository or download the `student_management.py` file.
3. Run the script using Python:

   ```bash
   python student_management.py
   ```
4. Follow the interactive menu in the console to manage student records.

## File Structure

- `student_management.py`: The main Python script containing the application logic.
- `students.txt`: A text file used to save and persist student data (automatically generated when you save from the app).

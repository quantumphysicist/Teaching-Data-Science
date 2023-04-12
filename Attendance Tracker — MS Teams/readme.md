# Attendance Tracker
This script processes MS Teams attendance data by comparing a list of expected participants against a list of actual participants. It loads two CSV files: one containing the expected participants with their official and informal names, and the other containing the actual participants.

## Requirements
Python 3.7 or higher  
Pandas library

## Usage
1. Replace the Microsoft Teams Meeting Attendance report in this folder with your own report.
2. Create a CSV file named `expected_participants.csv` with the following columns: "Name (Original Name)" and "Official Name". List all the participants that are expected to attend the event in this file. Make sure that the "Name (Original Name)" column matches the name column in the file from MS Teams.
3. Run the script by executing python `check_attendance_teams.py`.
4. The script will generate a CSV file named `attendance.csv` with the attendance information, including the names of the attendees and their attendance status (Present, Absent, or Unknown).

[//]: <> (## Note: The script assumes that the exported participants list from Zoom is saved as `participants_xxxxxxx.csv` in the same directory as the script file.)


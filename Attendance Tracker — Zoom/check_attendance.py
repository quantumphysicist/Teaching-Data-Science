"""
Author: Dr Renju Mathew

Distribution according to BSD 3-Clause License 

This script processes attendance data by comparing a list of expected participants against a list of actual participants.
It loads two CSV files: one containing the expected participants with their official and informal names, and the other containing the actual participants.
The script then replaces the informal names with the official names.
Next, it determines who attended the event, who did not attend, and who is unknown.
Finally, it creates a DataFrame with the attendance information, including the names of the attendees and their attendance status (Present, Absent, or Unknown).
"""

import pandas as pd
import glob

# Load expected participants

# Search for file path that starts with "expected_participants"
file_path = glob.glob('expected_participants*.csv')[0]
expected_participants = pd.read_csv(file_path)
expected_participants_list = set(expected_participants['Official Name'])
expected_participants_dict = dict(zip(expected_participants['Name (Original Name)'], 
                                      expected_participants['Official Name']))


# Load actual participants. Remove unnecessary rows and columns.
actual_participants_file = glob.glob('participant*.csv')[0]  # Get the name of the csv file that begins with "participant"
df = pd.read_csv(actual_participants_file, header=None)

# Find the row where the column header is 'Name (Original Name)'
locations = df.where(df == 'Name (Original Name)').stack().index.tolist()

# Delete all rows before the first location
df = df.drop(df.index[:locations[0][0]])

# Delete all columns except the first one
df = df.drop(df.columns[1:], axis=1)

# Make the first row the header
df.columns = df.iloc[0]
df = df.iloc[1:].reset_index(drop=True)

# Replace the informal name with the official name or keep the informal name if not in the dictionary
actual_participants_list = df['Name (Original Name)'].apply(lambda x: expected_participants_dict.get(x, x)).tolist()

# Determine who attended, who did not attend, and who is unknown
present = set(actual_participants_list).intersection(expected_participants_list)
absent = set(expected_participants_list).difference(actual_participants_list)
unknown = [name for name in actual_participants_list if name not in expected_participants_list]

# Create a dataframe for attendance status
attendance_df = (pd.concat([pd.DataFrame(present, columns=['Name']).assign(Status='Present'),
                            pd.DataFrame(absent, columns=['Name']).assign(Status='Absent')])
                 .sort_values('Name'))

# Add unknown attendees to the dataframe
unknown_df = pd.DataFrame(unknown, columns=['Name']).assign(Status='Present (Unrecognized Name)').reset_index(drop=True)
attendance_df = pd.concat([attendance_df, unknown_df]).reset_index(drop=True)
attendance_df.index += 1

# Create a column with the name Status Code. 1 for present. 0 for absent.
attendance_df['Status Code'] = attendance_df['Status'].apply(lambda x: 1 if x == 'Present' else 0)

# Reorder the columns
attendance_df = attendance_df[['Name', 'Status Code', 'Status']]

attendance_df.to_csv('attendance.csv', index=False)
print(attendance_df)
print()
print("Saved to attendance.csv")
print("-----------------------")
# Wait for user to press a key
input('Press Enter key to exit')

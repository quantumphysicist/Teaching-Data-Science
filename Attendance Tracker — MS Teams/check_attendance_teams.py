"""
Author: Dr Renju Mathew

This script processes attendance data by comparing a list of expected participants against a list of actual participants.
It loads two CSV files: one containing the expected participants with their official and informal names, and the other containing the actual participants.
The script then replaces the informal names with the official names.
Next, it determines who attended the event, who did not attend, and who is unknown.
Finally, it creates a DataFrame with the attendance information, including the names of the attendees and their attendance status (Present, Absent, or Unknown).
This is then saved as a CSV file.
"""

import glob
import pandas as pd

# Find the name of the csv file in the current directory that starts with "Microsoft Teams Meeting"
filename = glob.glob("Microsoft Teams Meeting*.csv")[0]
#print(filename)

# Define the column names (8 columns in total)
column_names = ['col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8']

# Read csv using UTF-16 encoding and the specified column names; delimiter is a tab
df = pd.read_csv(filename, encoding='UTF-16', names=column_names, header=None, delimiter='\t')

# Find the index of the row that contains the string "2. Participants"
participants_index = df[df['col1'].str.contains('2. Participants')].index[0]

# Find the index of the row that contains the string "3. In-Meeting Activities"ArithmeticError
activities_index = df[df['col1'].str.contains('3. In-Meeting Activities')].index[0]

# Keep only the rows between the two indices
df = df.iloc[participants_index+2:activities_index]
df = df.reset_index(drop=True)  
df = df.rename(columns={'col1': 'Name (Original Name)'})
#display(df[['Name (Original Name)']])

# Load expected participants
expected_participants = pd.read_csv('expected_participants.csv')
expected_participants_list = set(expected_participants['Official Name'])
expected_participants_dict = dict(zip(expected_participants['Name (Original Name)'], 
                                      expected_participants['Official Name']))

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
unknown_df = pd.DataFrame(unknown, columns=['Name']).assign(Status='Present (Unrecognized Name)')
attendance_df = pd.concat([attendance_df, unknown_df]).reset_index(drop=True)
attendance_df.index += 1
attendance_df.to_csv('attendance.csv', index=False)
print(attendance_df)

# Press the "Enter" key to exit
input("Press the Enter key to exit...")
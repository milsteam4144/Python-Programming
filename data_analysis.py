# Mallory Milstead

import pandas as pd

# Read the csv file into a variable
df = pd.read_csv("home_school_state.csv")

# Display first few rows in the dataframe
print(df.head(10))

# Put the homeschool_students column into a variable
student_count = df["homeschool_students"]

# Display largest student count
#print(student_count.max())

largest_stud_count = df[df['homeschool_students'] == df['homeschool_students'].max()]
print("Largest number of homeschool students")
print()
print(largest_stud_count)

# Display smallest student count
#print(student_count.min())
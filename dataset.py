import csv

# Data to be written to the CSV file
data = [['Name', 'Age', 'Gender'],
        ['John', 25, 'Male'],
        ['Jane', 30, 'Female'],
        ['Bob', 40, 'Male'],
        ['Alice', 35, 'Female'],
        ['Dave', 45, 'Male']]

# Create the CSV file and write the data to it
with open('example_dataset.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file created successfully!")

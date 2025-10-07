# cmayenga_assignment_6.py 
# Student: Charlestone Mayenga
# Assignment 6: Contact Information Formatter 
# Demonstrates mastery of string methods for data cleaning and formatting

# input collection
contacts = []

print("Enter contact information (format: name|phone|email|address): ")

while True:
    line = input()
    if line.strip().upper() == "DONE":
        break

    parts = line.strip().split("|")
    if len(parts) != 4:
        print("Invalid format. Please enter exactly four fields separated by '|'.")
        continue

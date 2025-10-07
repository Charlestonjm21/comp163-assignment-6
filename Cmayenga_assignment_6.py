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
    
    #format Name
    name_raw = parts[0].strip().split()

        name = " ".join([part.capitalize() for part in name_raw])

    #format Phone
    phone = parts[1]
    digits = "".join(ch for ch in phone if ch.isdigit())
    if len(digits) == 10:
        phone = f"({digits[0:3]}) {digits[3:6]}-{digits[6:]}"
    else:
        phone = phone.strip()
        
    #format Email
    email = parts[2].strip().lower()

    #format Address
    address = ' '.join(word.capitalize() for word in parts[3].strip().split())

    contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }

    contacts.append(contact)

#output directory

print("\n=== CONTACT DIRECTORY ===\n")

for i, contact in enumerate(contacts, 1):
    print(f"CONTACT {i}:")
    print(f"Name:     {contact['name']}")
    print(f"Phone:    {contact['phone']}")
    print(f"Email:    {contact['email']}")
    print(f"Address:  {contact['address']}\n")

#summary
print("\n=== DIRECTORY SUMMARY ===")
print(f"Total contacts processed: {len(contacts)}\n")

#formatting for printing
print("=== FORMATTED FOR PRINTING ===")
for contact in contacts:
    name_parts = contact['name'].split()
    if len(name_parts) >= 2:
        last = name_parts[-1]
        first_middle = ' '.join(name_parts[:-1])
        formatted_name = f"{last}, {first_middle}"
    else:
        formatted_name = contact['name']
    print(f"{formatted_name:<30} {contact['phone']}   {contact['email']}")


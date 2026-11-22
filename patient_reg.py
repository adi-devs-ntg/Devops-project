name = input("Enter patient name: ")
age = input("Enter patient age: ")
gender = input("Enter gender (Male/Female/Other): ")
phone = input("Enter contact number: ")
email = input("Enter email address: ")
address = input("Enter residential address: ")
blood_group = input("Enter blood group: ")
department = input("Enter consulting department: ")
doctor = input("Enter doctor name: ")
app_date = input("Enter appointment date (DD/MM/YYYY): ")

print("\n--- PATIENT APPOINTMENT SLIP ---")
print("Patient Name      :", name)
print("Age               :", age)
print("Gender            :", gender)
print("Contact Number    :", phone)
print("Email Address     :", email)
print("Address           :", address)
print("Blood Group       :", blood_group)
print("Department        :", department)
print("Doctor Assigned   :", doctor)
print("Appointment Date  :", app_date)

# Save to a file
with open("patient_records.txt", "a") as f:
    f.write(f"{name}, {age}, {gender}, {phone}, {email}, {address}, {blood_group}, {department}, {doctor}, {app_date}\n")

print("\nAppointment booked and details saved successfully!")

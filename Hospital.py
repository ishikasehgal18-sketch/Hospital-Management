# import csv
# class InvalidPatientError(Exception):
#      pass

# records={1: {"Simar": 15, "Gender": "Male", "Disease": "Typhoid"},
#          2: {"Neharika": 45, "Gender": "Female", "Disease": "Jaundice"},
#          3: {"Satyakumar": 60, "Gender": "Male", "Disease": "Heart"}
# }
# patient_ids= records.keys() 
# a=list(patient_ids)
# print(patient_ids)

# class Doctor:
#     def__init__(self,name,specialization,fee)
#         self.name=name
#         self.specialization=specialization
#         self.fee=fee
#         self.patients=[]
#     def add_patient(self,patient):
#         self.patients.append(patient)
#         print(f"patient{patient.name} added to Dr. {self.name}'s list.")
#     def get_details(self) 
#         return f"Dr.{self.name}-{self.specialization} (fee:${self.fee})"
# class patient:
#     def__init__(self,name,disease,gendre,age):
#         self.name=name
#         self.disease=disease
#         self.age=age
#         self.gendre=gender
#         self.prescriptions=[]

#     def add_prescriptions(self,medication):
#         self.prescriptions.append(medication)

#     def get_medical_profile(self):
#         return f"patient: {self.name},Age: {self.age}, Disease:{self.disease}"

#      def validate_patient_data(name, age, gender, disease):
#     """Validates patient information before an object is created."""
#     if not name.strip() or not disease.strip():
#         raise InvalidPatientError(" Patient name and disease fields cannot be blank.")
    
#     if age <= 0 or age > 100:
#         raise InvalidAgeError(f" Age ({age}) must be a valid number between 1 and 120.")
#     return True


# def schedule_appointment(patient_obj, doctor_obj, date_str, time_str, appointments_list):
    
#     for appt in appointments_list:
#         if appt["doctor"] == doctor_obj.name and appt["date"] == date_str and appt["time"] == time_str:
#             raise DoctorBusyError(f" Dr. {doctor_obj.name} is already booked at {time_str} on {date_str}.")


#     new_booking = {
#         "patient": patient_obj.name,
#         "doctor": doctor_obj.name,
#         "date": date_str,
#         "time": time_str
#     }
#     appointments_list.append(new_booking)
#     doctor_obj.add_patient(patient_obj)
#     print(f" Appointment confirmed for {patient_obj.name} with Dr. {doctor_obj.name} on {date_str} at {time_str}!")

# with open("patients.csv", "w", newline="") as file:
#     fields = ["Name", "Age", "Gender", "Disease"]
#     writer = csv.DictWriter(file, fieldnames=fields)

#     writer.writeheader() 
#     writer.writerows(patients) 

# with open("patients.csv", "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(dict(row))

import os

class InvalidPatientError(Exception):
    pass

class Patient:
    def __init__(self, patient_id, name, age, gender, disease):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.disease = disease

class Doctor:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

patient_record = {}
patient_ids = []
appointments = []

def add_patient(patient_id, name, age, gender, disease):
    try:
        if age <= 0:
            raise InvalidPatientError("Age cannot be negative or zero")
        if patient_id in patient_ids:
            raise InvalidPatientError("Id already exists")
        
        new_patient = Patient(patient_id, name, age, gender, disease)
        patient_record[patient_id] = new_patient
        patient_ids.append(patient_id)
        print(f"Patient {name} added successfully.")

    except InvalidPatientError as error:
        print(f"Registration Failed: {error}")

def schedule_appointment(p_id, doctor_obj, date):
    if p_id not in patient_ids:
        print("Patient id not found; Can't schedule appointment!")
        return
    patient_obj = patient_record[p_id]

    details = f"Patient: {patient_obj.name} | Doctor: {doctor_obj.name} ({doctor_obj.specialty}) | Date: {date}"
    appointments.append(details)
    print("Appointment scheduled successfully.")

def save_to_file():
    with open("hospital.txt", "w") as file:
        file.write("PATIENTS\n")
        for pid in patient_ids:
            p = patient_record[pid]
            file.write(f"ID: {p.patient_id}, Name: {p.name}, Age: {p.age}, Gender: {p.gender}, Disease: {p.disease}\n")
            
        file.write("\nAPPOINTMENTS\n")
        for app in appointments:
            file.write(app + "\n")
    print("Records saved to 'hospital.txt'.")

doc1 = Doctor("Dr. Smith", "Heart Specialist")

print(" Testing Patient Add ")
add_patient("P1", "A", 25, "Male", "Flu")          
add_patient("P2", "B", -5, "Female", "Cough")          
add_patient("P1", "C", 30, "Male", "Fever")     

print("\n Testing Appointments ")
schedule_appointment("P1", doc1, "2026-06-25") 
schedule_appointment("P9", doc1, "2026-06-25") 

print("\nTesting File Storage")
save_to_file()

        



     

class patient:
    count = 1
    def __init__(self,patient_name,age,disease):
        if not(1<= age <=120):
            raise ValueError("Please enter the correct age of the patient")
        if disease.strip == "":
            raise ValueError("Disease cannot be empty")
        
        self.patient_name = patient_name
        self.age = age
        self.disease = disease
        self.patient_id = f"P(patient.count:03d)"
        patient.count +=1

    def display_details(self):
        print("\n----Patient Details----")
        print(f"patient id : {self.patient_id}")
        print(f"patient name : {self.patient_name}")
        print(f"age : {self.age}")
        print(f"disease : {self.disease}")

    def update_disease(self,new_disease):
        if new_disease.strip() == "":
            self.disease = new_disease
            print("Disease Update Successfully")
            raise ValueError("Disease cannot be empty")
        
class doctor:
    count = 1
    def __init__(self,doctor_name,specialization):
        self.doctor_name = doctor_name
        self.doctor_id =  f"D(doctor.count:03d)"
        self.specialization = specialization
        doctor.count += 1

    def display_details(self):
        print("----Doctor Details----")
        print(f"doctor id : {self.doctor_id}")
        print(f"doctor name : {self.doctor_name}")
        print(f"specialization : {self.specialization}")

class hospital:
    def __init__(self):
        self.patients = {}
        self.doctors = {}

    def add_patient(self,patient):
        if patient.patient_id in self.patients:
            print(f"Conflict error : {patient.patient_id} already exist")
        else :
            self.patients[patient.patient_id] = patient
            print(f"Patient '{patient.patient_name}' ({patient.patient_id}) added successfully.")

    def remove_patient(self, patient_id):
        if patient_id in self.patients:
            patient = self.patients.pop(patient_id)
            print(f"Patient '{patient.patient_name}' ({patient_id}) removed successfully.")
        else:
            print(f"Patient not found: {patient_id}")

    def add_doctor(self, doctor):
        if doctor.doctor_id in self.doctors:
            print(f"Conflict Error: Doctor ID {doctor.doctor_id} already exists.")
        else:
            self.doctors[doctor.doctor_id] = doctor
            print(f"Doctor '{doctor.doctor_name}' ({doctor.doctor_id}) added successfully.")

    def show_all_patients(self):
        if len(self.patients) == 0:
            print("No records found.")
        else:
            print("\n========== All Patients ==========")
            for patient in self.patients.values():
                patient.display_details()

    def show_all_doctors(self):
        if len(self.doctors) == 0:
            print("No records found.")
        else:
            print("\n========== All Doctors ==========")
            for doctor in self.doctors.values():
                doctor.display_details()


hospital = hospital()

# Creating Patients
p1 = patient("Rohit", 21, "Fever")
p2 = patient("Aman", 25, "Diabetes")

# Creating Doctors
d1 = doctor("Dr. Sharma", "Cardiologist")
d2 = doctor("Dr. Mehta", "Surgeon")

# Adding Patients
hospital.add_patient(p1)
hospital.add_patient(p2)

# Adding Doctors
hospital.add_doctor(d1)
hospital.add_doctor(d2)

# Display All Records
hospital.show_all_patients()
hospital.show_all_doctors()

# Update Disease
p1.update_disease("Viral Fever")

# Remove Patient
hospital.remove_patient("P002")

# Attempt to Remove Non-Existing Patient
hospital.remove_patient("P010")

# Display Patients Again
hospital.show_all_patients()
        

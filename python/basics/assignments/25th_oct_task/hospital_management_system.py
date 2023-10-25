class Patient:
    def __init__(self, patient_id, name, age, gender):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender

class HospitalManagementSystem:
    def __init__(self):
        self.patient_records = []

    def add_patient(self, patient_id, name, age, gender):
        patient = Patient(patient_id, name, age, gender)
        self.patient_records.append(patient)

    def display_patients(self):
        if not self.patient_records:
            print("No patient records available.")
        else:
            print("Patient Records:")
            for patient in self.patient_records:
                print(f"ID: {patient.patient_id}, Name: {patient.name}, Age: {patient.age}, Gender: {patient.gender}")

    def search_patient(self, search_id):
        for patient in self.patient_records:
            if patient.patient_id == search_id:
                print("Patient Found:")
                print(f"ID: {patient.patient_id}, Name: {patient.name}, Age: {patient.age}, Gender: {patient.gender}")
                return
        print(f"No patient found with ID: {search_id}")

    def delete_patient(self, delete_id):
        for patient in self.patient_records:
            if patient.patient_id == delete_id:
                self.patient_records.remove(patient)
                print(f"Patient with ID {delete_id} has been deleted.")
                return
        print(f"No patient found with ID: {delete_id}")

    def update_patient(self, update_id, name, age, gender):
        for patient in self.patient_records:
            if patient.patient_id == update_id:
                patient.name = name
                patient.age = age
                patient.gender = gender
                print("Patient details updated successfully.")
                return
        print(f"No patient found with ID: {update_id}")

if __name__ == "__main__":
    hospital_system = HospitalManagementSystem()

    while True:
        print("\nHospital Management System Menu:")
        print("1. Add a new patient")
        print("2. Display all patient details")
        print("3. Search for a patient by ID")
        print("4. Delete a patient by ID")
        print("5. Update patient details by ID")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            patient_id = input("Enter patient ID: ")
            name = input("Enter patient name: ")
            age = input("Enter patient age: ")
            gender = input("Enter patient gender: ")
            hospital_system.add_patient(patient_id, name, age, gender)
        elif choice == "2":
            hospital_system.display_patients()
        elif choice == "3":
            search_id = input("Enter the ID of the patient to search: ")
            hospital_system.search_patient(search_id)
        elif choice == "4":
            delete_id = input("Enter the ID of the patient to delete: ")
            hospital_system.delete_patient(delete_id)
        elif choice == "5":
            update_id = input("Enter the ID of the patient to update: ")
            name = input("Enter new name: ")
            age = input("Enter new age: ")
            gender = input("Enter new gender: ")
            hospital_system.update_patient(update_id, name, age, gender)
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

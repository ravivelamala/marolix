employee_database = {}

def add_employee():
    domain = input("Enter employee domain: ")
    name = input("Enter employee name: ")
    empid = input("Enter employee ID: ")
    email = input("Enter employee email: ")
    
    
    employee_details = {
        "Domain": domain,
        "Name": name,
        "EmpID": empid,
        "Email": email
    }
    
    
    employee_database[empid] = employee_details
    print("Employee added successfully!")


def print_employee_details(empid):
    if empid in employee_database:
        employee_details = employee_database[empid]
        print("\nEmployee Details:")
        for key, value in employee_details.items():
            print(f"{key}: {value}")
    else:
        print("Employee not found in the database.")


while True:
    print("\nMenu:")
    print("1. Add Employee")
    print("2. Print Employee Details")
    print("3. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_employee()
    elif choice == "2":
        empid = input("Enter employee ID to print details: ")
        print_employee_details(empid)
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please choose again.")

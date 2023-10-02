# filter the stored employee details with name and empid and designation and email.
employee_list = []

# Function to add employee details
def add_employee():
    name = input("Enter Name: ")
    emp_id = input("Enter Employee ID: ")
    designation = input("Enter Designation: ")
    email = input("Enter Email: ")

    employee = {
        "Name": name,
        "Employee ID": emp_id,
        "Designation": designation,
        "Email": email
    }

    employee_list.append(employee)
    print("Employee details added successfully!")

# Function to filter employee details by criteria
def filter_employee():
    print("Filter employee details by:")
    print("1. Name")
    print("2. Employee ID")
    print("3. Designation")
    print("4. Email")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        search_name = input("Enter the name to search: ")
        filtered_employees = [emp for emp in employee_list if emp['Name'] == search_name]
    elif choice == '2':
        search_emp_id = input("Enter the Employee ID to search: ")
        filtered_employees = [emp for emp in employee_list if emp['Employee ID'] == search_emp_id]
    elif choice == '3':
        search_designation = input("Enter the designation to search: ")
        filtered_employees = [emp for emp in employee_list if emp['Designation'] == search_designation]
    elif choice == '4':
        search_email = input("Enter the email to search: ")
        filtered_employees = [emp for emp in employee_list if emp['Email'] == search_email]
    else:
        print("Invalid input")
        return

    if filtered_employees:
        print("Filtered Employee Details:")
        for emp in filtered_employees:
            print(f"Employee ID: {emp['Employee ID']}")
            print(f"Name: {emp['Name']}")
            print(f"Designation: {emp['Designation']}")
            print(f"Email: {emp['Email']}")
    else:
        print("No matching records found.")

# Main menu
while True:
    print("\nEmployee Details Management System")
    print("1. Add Employee Details")
    print("2. Filter Employee Details")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        add_employee()
    elif choice == '2':
        filter_employee()
    elif choice == '3':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

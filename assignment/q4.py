# 4) Let the user give multiple data in the following format—
# Company_Name: Employee_Name-Experience*Specialization (for example, Wipro: Amit-14*Java).
# The program should allow the user to enter multiple employee records. The number of records is not
# fixed and should be decided by the user during program execution. It is the user's choice how much data
# he wants to give.
# Make a list using Python that only stores the name, experience, and specialization of each employee as a
# string delimited by spaces so that the HR manager of a company can quickly access them without
# knowing the encoding of the data sort by experience.
# Sample User Input
# Enter the number of employee records: 9
# Enter Record 1: Wipro: Amit-14*Java
# Enter Record 2: Wipro: Riya-5*Python
# Enter Record 3: Wipro: Rahul-15*Data Migration
# Enter Record 4: TCS: Ronil-6*DataScience
# Enter Record 5: TCS: Sohini-18*DBMS
# Enter Record 6: TCS: Abhishek-13*Robotics
# Enter Record 7: Cognizant: Neha-7*Testing
# Enter Record 8: Cognizant: Suman-12*Cloud
# Enter Record 9: Cognizant: Shruti-8*MVC
# Expected Output
# Employee Details (Sorted by Experience)
# Sohini 18 DBMS, Rahul 15 Data Migration, …….So on

n = int(input("Enter the number of employee records: "))

employees = []

for i in range(n):
    record = input(f"Enter Record {i + 1}: ")

    company, details = record.split(":")
    name, details = details.strip().split("-")
    experience, specialization = details.split("*")

    employees.append(name + " " + experience + " " + specialization)

employees.sort(key=lambda x: int(x.split()[1]), reverse=True)

print("\nEmployee Details (Sorted by Experience)")

for employee in employees:
    print(employee)
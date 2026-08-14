#1.Given a list of roll numbers:  [101, 105, 102, 101, 108, 105, 110] . Print all unique roll numbers in the list.


#2) Given employee records in the form of a list of tuples, where each tuple contains:   (Employee ID, Employee Name, Salary)
#Example:[(101, "Alice", 50000), (102, "Bob", 65000), (103, "Charlie", 45000)]  Ask the user to enter an Employee ID and search for it inside the records.


#roll= {101 , 105, 102, 101, 108, 105, 110}
#print(roll)

record=(
    (101, "Alice", 50000),
    (102, "Bob", 65000),
    (103, "Charlie", 45000)
       )

emp_id=int(input("enter your employee id: "))

for employee in record: 
  
  # meaning (101, "Alice", 50000)= 1 tuple  where Python takes each tuple from record one at a time and temporarily calls it employee


  if employee[0]==emp_id:   #jodhi oi 0,1,2 3 khane tuple modhe aktao input match hoi
     
     print(employee)   #akhane employee ta print hoye jaba


# Orlando Harris
# 7 Oct 2026
# P3HW2 Salary Calculator


# request employee information


employee_name = input("Enter employee name: ")
hours_worked = float(input("Enter hours worked: "))
hourly_rate = float(input("Enter hourly pay rate: "))


# Evaluate overtime
if hours_worked > 40:
    # Calculate overtime
    overtime_hours = hours_worked - 40
    # Calculate over pay rate (1.5 times the hourly rate)
    overtime_rate = hourly_rate * 1.5
    # Calculate salary for overtime hours   
    overtime_pay = overtime_hours * overtime_rate
    # Calculate Gross pay
    regular_pay = 40 * hourly_rate
    # Calculate overtime pay
    gross_pay = regular_pay + (overtime_hours * overtime_rate)
    
    
else:
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = hours_worked * hourly_rate
    gross_pay = regular_pay

    # Display results
print("--------------------------------")    
print("Employee Name: " , employee_name)
print(f'{"Hours Worked":<20}{"Pay Rate":<20}{"Overtime Hours":<20}{"Overtime Pay":<20}){"Regular Pay":<20}{"Gross Pay":<20}')
print(f'{hours_worked:<20}{hourly_rate:<20}{overtime_hours:<20}{overtime_pay:<20}{regular_pay:<20}{gross_pay:<20}')
print("--------------------------------")
    
    
    
    
    
    

    


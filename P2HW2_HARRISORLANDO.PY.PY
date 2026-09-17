# Orlando Harris
# 16 September 2026
# P2HW2
# This program uses pseudocode to ask user to enter test grades

# Enter test grades for each Module 1 through Module 6 
module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

# Possible grades for each module
grades = ["F", "D", "C", "B", "A"]

# Grade Equivalents
def grade_equivalent(grade):
    if grade >= 90:
        return grades[4]  # A
    elif grade >= 80:
        return grades[3]  # B
    elif grade >= 70:
        return grades[2]  # C
    elif grade >= 60:
        return grades[1]  # D
    else:
        return grades[0]  # F

    #print the grade equivalents for each module
print(f"Grade for Module 1: {module1:.2f} ({grade_equivalent(module1)})")
print(f"Grade for Module 2: {module2:.2f} ({grade_equivalent(module2)})")
print(f"Grade for Module 3: {module3:.2f} ({grade_equivalent(module3)})")
print(f"Grade for Module 4: {module4:.2f} ({grade_equivalent(module4)})")
print(f"Grade for Module 5: {module5:.2f} ({grade_equivalent(module5)})")
print(f"Grade for Module 6: {module6:.2f} ({grade_equivalent(module6)})")



# Grades List
grades = [module1, module2, module3, module4, module5, module6]


print("--------------Results-----------------")


# Calculate the average grade
lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = sum(grades) / len(grades)

# Display the results

print(f"Lowest Grade: {lowest:.2f} ({grade_equivalent(lowest)})")
print(f"Highest Grade: {highest:.2f} ({grade_equivalent(highest)})")
print(f"Total Grade: {total:.2f}")
print(f"Average: {average:.2f} ({grade_equivalent(average)})")    







    






















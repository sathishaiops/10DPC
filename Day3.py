
#If Else Statement Example: 
score = int(input("Enter your score: "))

if score < 0 or score > 100:
    print("Invalid Score")
elif score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("FAIL")



#Nested If Example:
age = int(input("Enter your age: "))
pro = input("Are you a professional? (yes/no): ").strip().lower()

if age >= 18:
    if pro == 'yes':
        print("You are eligible for the professional membership.")
    else:
        print("You are eligible for the regular membership.")
else:
    print("You are not eligible for membership.")   

# Ternary Operator Example:
status = "Adult" if age >= 18 else "Minor"
print("Status:", status)    
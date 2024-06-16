# Asks the user to input a numerical score 0-100, score is a variable that holds the INTEGER Value.
score = int(input("Enter the score (0-100): "))

# Categorise the scores into grades
if score >= 90:
    grade = "A"
elif score >= 80:  
    grade = "B"  
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"    

print(f"The grade based on your score {score} is {grade}")

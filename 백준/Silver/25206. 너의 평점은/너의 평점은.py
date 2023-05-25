import sys

total_credit = 0.0
total_score = 0.0
for _ in range(20):
    name, credit, score = input().split()
    credit = float(credit)
    if score == "A+":
        score = 4.5
    elif score == "A0":
        score = 4.0
    elif score == "B+":
        score = 3.5
    elif score == "B0":
        score = 3.0
    elif score == "C+":
        score = 2.5
    elif score == "C0":
        score = 2.0
    elif score == "D+":
        score = 1.5
    elif score == "D0":
        score = 1.0
    elif score == "F":
        score = 0
    elif score == "P":
        credit = 0.0
        score = 0
        
    total_credit += credit
    total_score += score*credit
    
print(total_score/total_credit)
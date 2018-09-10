"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = 1
while score > 0:
    score = float(input("Enter score: "))
    if score > 0 and score <= 49:
        print("Fail")
    elif score >= 50 and score <= 89:
        print("Passable")
    elif score >= 90 and score <= 100:
        print("Excellent")
    else:
        print("Invalid Score")
print("Negative Score entered, Goodbye")
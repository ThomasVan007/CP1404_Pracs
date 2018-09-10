"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
def main():
    score = 1
    while score > 0:
        score = float(input("Enter score: "))
        result = score_calc(score)
        print(result)
    print("Negative Score entered, Goodbye")

def score_calc(score):
    if score > 0 and score <= 49:
        return "Fail"
    elif score >= 50 and score <= 89:
        return "Passable"
    elif score >= 90 and score <= 100:
        return "Excellent"
    else:
        return "Invalid Score"
main()
def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)

def get_letter_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "F"

if __name__ == "__main__":
    print("Student Grade Tracker Initialized")
    sample_grades = [85, 90, 78, 92]
    avg = calculate_average(sample_grades)
    letter = get_letter_grade(avg)
    print(f"Sample Average Grade: {avg:.2f} ({letter})")

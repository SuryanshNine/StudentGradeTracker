def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)

if __name__ == "__main__":
    print("Student Grade Tracker Initialized")
    sample_grades = [85, 90, 78, 92]
    avg = calculate_average(sample_grades)
    print(f"Sample Average Grade: {avg}")

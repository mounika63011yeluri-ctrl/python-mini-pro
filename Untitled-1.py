def grade_from_average(average: float) -> str:
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"

if __name__ == "__main__":
    student_name = "mounika"
    roll_number = 63
    marks = [80, 90, 70, 65, 82]  # use a list so we can compute programmatically

    total = sum(marks)
    average = total / len(marks)

    print("student name:", student_name)
    print("roll number:", roll_number)
    for i, m in enumerate(marks, start=1):
        print(f"marks in subject {i}:", m)
    print("sum:", total)
    print("average:", average)
    print("grade:", grade_from_average(average))

    for i, m in enumerate(marks):
        if m < 40:
            print("subject", i + 1, "is failed")

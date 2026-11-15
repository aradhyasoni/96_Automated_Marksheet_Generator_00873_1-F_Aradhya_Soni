import pandas as pd


def calculate_grade(percentage):
    """Return the grade according to the university grading system."""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 40:
        return "E"
    else:
        return "F"


def load_student_data(file_name):
    """Read the CSV file and skip rows containing invalid marks."""
    try:
        data = pd.read_csv(file_name)
    except FileNotFoundError:
        print("Error: marks.csv file not found.")
        return None
    except Exception as error:
        print("Error while reading the CSV file:", error)
        return None

    required_columns = [
        "RollNo", "Name", "Maths", "Physics", "Programming"
    ]

    if not all(column in data.columns for column in required_columns):
        print("Error: CSV file must contain these columns:",
              ", ".join(required_columns))
        return None

    valid_rows = []

    for _, row in data.iterrows():
        try:
            marks = [
                float(row["Maths"]),
                float(row["Physics"]),
                float(row["Programming"])
            ]

            if any(mark < 0 or mark > 100 for mark in marks):
                print(
                    f"Warning: Row for roll {row['RollNo']} skipped - "
                    "marks must be between 0 and 100."
                )
                continue

            if any(mark != int(mark) for mark in marks):
                print(
                    f"Warning: Row for roll {row['RollNo']} skipped - "
                    "marks must be whole numbers."
                )
                continue

            if pd.isna(row["RollNo"]) or pd.isna(row["Name"]):
                print("Warning: A row with missing student details was skipped.")
                continue

            valid_rows.append(row)

        except (ValueError, TypeError, OverflowError):
            print(
                f"Warning: Row for roll {row.get('RollNo', 'unknown')} "
                "skipped - invalid marks."
            )

    if not valid_rows:
        print("No valid student records found.")
        return pd.DataFrame(columns=required_columns)

    return pd.DataFrame(valid_rows)


def print_marksheet(student):
    """Calculate and display one student's marksheet."""
    maths = int(student["Maths"])
    physics = int(student["Physics"])
    programming = int(student["Programming"])

    total = maths + physics + programming
    percentage = total / 300 * 100
    grade = calculate_grade(percentage)

    if maths < 40 or physics < 40 or programming < 40:
        result = "FAIL"
        failed_subjects = []
        if maths < 40:
            failed_subjects.append("Maths")
        if physics < 40:
            failed_subjects.append("Physics")
        if programming < 40:
            failed_subjects.append("Programming")
        result += " (" + ", ".join(failed_subjects) + " below 40)"
    else:
        result = "PASS"

    print("\n" + "=" * 48)
    print("              STUDENT MARKSHEET")
    print("=" * 48)
    print(f"Roll No: {int(student['RollNo'])} | Name: {student['Name']}")
    print("-" * 48)
    print(f"Maths: {maths} | Physics: {physics} | Programming: {programming}")
    print("-" * 48)
    print(f"Total: {total}/300")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
    print(f"Result: {result}")
    print("=" * 48)


def main():
    print("AUTOMATED MARKSHEET GENERATOR")
    print("Reading student records from marks.csv...")

    students = load_student_data("marks.csv")

    if students is None or students.empty:
        return

    print(f"\nValid student records loaded: {len(students)}")
    roll_number = input("\nEnter student roll number: ").strip()

    try:
        roll_number = int(roll_number)
    except ValueError:
        print("Invalid roll number. Please enter a number.")
        return

    student = students[students["RollNo"].astype(int) == roll_number]

    if student.empty:
        print(f"Roll number {roll_number} not found.")
        return

    print_marksheet(student.iloc[0])


if __name__ == "__main__":
    main()

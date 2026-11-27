# SGPA / CGPA calculator for Thapar's 10-point grading scheme

GRADE_POINTS = {
    "A+": 10, "A": 10, "A-": 9, "B": 8, "B-": 7,
    "C": 6, "C-": 5, "E": 2, "F": 0,
}


def calculate_sgpa(subjects):
    """subjects: list of (credits, grade) tuples"""
    total_credits = sum(c for c, _ in subjects)
    total_points = sum(c * GRADE_POINTS[g.upper()] for c, g in subjects)
    return round(total_points / total_credits, 2)


def calculate_cgpa(semesters):
    """semesters: list of (sgpa, credits) tuples"""
    total_credits = sum(c for _, c in semesters)
    weighted = sum(s * c for s, c in semesters)
    return weighted / total_credits


if __name__ == "__main__":
    n = int(input("Number of subjects: "))
    subjects = []
    for i in range(n):
        credits = float(input(f"Subject {i+1} credits: "))
        grade = input(f"Subject {i+1} grade: ")
        subjects.append((credits, grade))
    print("SGPA:", calculate_sgpa(subjects))

from dataclasses import dataclass, field


@dataclass
class Student:
    roll_no: int
    name: str
    internal_marks: list[float] = field(default_factory=list)

    @property
    def total(self):
        return sum(self.internal_marks)


def main():
    students = []
    count = int(input("Enter the Number of Students : "))

    for _ in range(count):
        roll_no, name = input("Enter Roll No and Name: ").split(maxsplit=1)
        marks = []
        for subject in range(1, 6):
            subject_total = 0.0
            for ia in range(1, 4):
                mark = float(input(f"Enter the IA {ia} mark for sub {subject}: "))
                subject_total += mark
            internal_mark = (subject_total / 300) * 20
            marks.append(internal_mark)
        students.append(Student(int(roll_no), name, marks))

    print("\nThe Student Details are")
    for student in students:
        print(f"\nRollNo:{student.roll_no}\nName:{student.name}")
        for i, mark in enumerate(student.internal_marks, 1):
            print(f"Subject{i} - Internal Mark: {mark:.2f}")

if __name__ == "__main__":
    main()

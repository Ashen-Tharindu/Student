import tkinter as tk
from tkinter import messagebox

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"{self.name} is {self.age} years old and is in grade {self.grade}."

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name, age, grade):
        student = Student(name, age, grade)
        self.students.append(student)
        return f"Student {name} added successfully!"

    def print_students(self):
        if not self.students:
            return "No students in the system."
        else:
            return "\n".join([str(student) for student in self.students])

    def search_student(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                return student
        return None

    def delete_student(self, name):
        student = self.search_student(name)
        if student:
            self.students.remove(student)
            return f"Student {name} deleted successfully!"
        else:
            return f"Student {name} not found."

    def edit_student(self, name, new_name=None, new_age=None, new_grade=None):
        student = self.search_student(name)
        if student:
            if new_name:
                student.name = new_name
            if new_age:
                student.age = new_age
            if new_grade:
                student.grade = new_grade
            return f"Student {name} updated successfully!"
        else:
            return f"Student {name} not found."

class StudentManagementSystemUI:
    def __init__(self):
        self.system = StudentManagementSystem()
        self.window = tk.Tk()
        self.window.title("Student Management System")

        # Create frames
        self.frame1 = tk.Frame(self.window)
        self.frame1.pack()
        self.frame2 = tk.Frame(self.window)
        self.frame2.pack()
        self.frame3 = tk.Frame(self.window)
        self.frame3.pack()

        # Create labels and entries
        self.label1 = tk.Label(self.frame1, text="Name:")
        self.label1.pack(side=tk.LEFT)
        self.entry1 = tk.Entry(self.frame1)
        self.entry1.pack(side=tk.LEFT)
        self.label2 = tk.Label(self.frame1, text="Age:")
        self.label2.pack(side=tk.LEFT)
        self.entry2 = tk.Entry(self.frame1)
        self.entry2.pack(side=tk.LEFT)
        self.label3 = tk.Label(self.frame1, text="Grade:")
        self.label3.pack(side=tk.LEFT)
        self.entry3 = tk.Entry(self.frame1)
        self.entry3.pack(side=tk.LEFT)

        # Create buttons
        self.button1 = tk.Button(self.frame2, text="Add Student", command=self.add_student)
        self.button1.pack(side=tk.LEFT)
        self.button2 = tk.Button(self.frame2, text="Print Students", command=self.print_students)
        self.button2.pack(side=tk.LEFT)
        self.button3 = tk.Button(self.frame2, text="Search Student", command=self.search_student)
        self.button3.pack(side=tk.LEFT)
        self.button4 = tk.Button(self.frame2, text="Delete Student", command=self.delete_student)
        self.button4.pack(side=tk.LEFT)
        self.button5 = tk.Button(self.frame2, text="Edit Student", command=self.edit_student)
        self.button5.pack(side=tk.LEFT)

        # Create text area
        self.text_area = tk.Text(self.frame3)
        self.text_area.pack()

    def add_student(self):
        name = self.entry1.get()
        age = self.entry2.get()
        grade = self.entry3.get()
        result = self.system.add_student(name, age, grade)
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, result)

    def print_students(self):
        result = self.system.print_students()
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, result)

    def search_student(self):
        name = self.entry1.get()
        student = self.system.search_student(name)
        if student:
            result = str(student)
        else:
            result = f"Student {name} not found."
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, result)

    def delete_student(self):
        name = self.entry1.get()
        result = self.system.delete_student(name)
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, result)

    def edit_student(self):
        name = self.entry1.get()
        new_name = self.entry2.get()
        new_age = self.entry3.get()
        new_grade = self.entry4.get()
        result = self.system.edit_student(name, new_name, new_age, new_grade)
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, result)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    ui = StudentManagementSystemUI()
    ui.run()
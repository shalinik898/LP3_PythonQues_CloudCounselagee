"""
CODING QUESTIONS:12
Write a Python program to count the number of students of the individual class.
Sample data:
classes = (
('V', 1),
('VI', 1),
('V', 2),
('VI', 2),
('VI', 3),
('VII', 1),
)
Expected Output:
Counter({'VI': 3, ' Example 1: V': 2, 'VII': 1})
"""

from collections import Counter
classes = (
    ('V', 1),
    ('VI', 1),
    ('V', 2),
    ('VI', 2),
    ('VI', 3),
    ('VII', 1),
)
students = Counter(class_name for class_name, no_students in classes)
print(students)

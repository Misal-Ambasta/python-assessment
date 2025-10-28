students = [
    {"name": "Alice", "marks": [80, 75, 90]},
    {"name": "Bob", "marks": [70, 60, 65]},
    {"name": "Charlie", "marks": [95, 85, 100]},
    {"name": "David", "marks": [60, 70, 80]}
]


for i,v in enumerate(students):
    avg = sum(v['marks'])/3
    if avg >= 85:
        v['grade'] = 'A'
    elif avg >= 70 and avg < 85:
        v['grade'] = 'B'
    else:
        v['grade'] = 'C'

for i,v in enumerate(students):
    print(f"Student: {v["name"]} -- Grade: {v['grade']}")    
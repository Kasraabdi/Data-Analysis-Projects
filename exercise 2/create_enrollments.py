import pandas as pd
import numpy as np


students = [f'Student_{i}' for i in range(1, 21)] # 20 students
courses = ['Math', 'Physics', 'Chemistry', 'History', 'Art', 'Literature', 'Programming', 'Economics']

num_records = 50
student_names = np.random.choice(students, num_records)
course_names = np.random.choice(courses, num_records)

df = pd.DataFrame({'student_name': student_names, 'course_name': course_names})

df.drop_duplicates(inplace=True)

try:
    df.to_csv('enrollments.csv', index=False)
    print(f"✅ Successfully created enrollments.csv with {len(df)} unique records.")
except Exception as e:
    print(f"❌ Error creating file: {e}")
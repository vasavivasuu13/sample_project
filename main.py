import pandas as pd

df = pd.read_csv('your_file.csv', delimiter='\t')

def calculate_average_grades(df):
    df['Average Grade'] = df['grades'].apply(lambda x: sum(map(int, x.split(','))) / len(x.split(',')))
    return df[['name', 'Average Grade']]

def classify_students_by_major(df):
    major_groups = df.groupby('major')
    for major, group in major_groups:
        print(f"\nStudents in {major}:\n{group[['name', 'grades']]}")


def find_top_students(df):
    top_students = df.groupby('major').apply(lambda x: x.loc[x['grades'].apply(lambda grades: max(map(int, grades.split(',')))) == max(x['grades'].apply(lambda grades: max(map(int, grades.split(',')))), key=int)][['name', 'grades']])
    return top_students


def identify_failing_students(df):
    failing_students = df[df['grades'].apply(lambda grades: any(int(grade) < 70 for grade in grades.split(',')))]
    return failing_students[['name', 'grades']]

average_grades = calculate_average_grades(df)
print("\nAverage Grades:\n", average_grades)

classify_students_by_major(df)

top_students = find_top_students(df)
print("\nTop Students:\n", top_students)

failing_students = identify_failing_students(df)
print("\nFailing Students:\n", failing_students)

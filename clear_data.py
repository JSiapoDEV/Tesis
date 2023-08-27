import pandas as pd

xls = pd.ExcelFile('original_data.xlsx')
sheets = xls.sheet_names
dataframes_per_sheet = {}

for sheet in sheets:
    df = pd.read_excel(xls, sheet).fillna('')
    dataframes_per_sheet[sheet] = df

students_by_email_per_sheet = {}

for sheet, df in dataframes_per_sheet.items():
    students_by_email = {}
    for index, row in df.iterrows():
        email = row['CORREO']
        student = row['ESTUDIANTE']
        nro = row['Nº EXAM']
        date_exam = row['FECHA']
        career = row['CARRERA']
        score = row['PT']

        if "@" in email:
            if email not in students_by_email:
                students_by_email[email] = []
            students_by_email[email].append((nro, date_exam, career, score, student))

    students_by_email_per_sheet[sheet] = students_by_email

for sheet, students_by_email in students_by_email_per_sheet.items():
    total_exams = 0
    for email, exams in students_by_email.items():
        total_exams += len(exams)
    average_exams = total_exams / len(students_by_email)
    for email, exams in students_by_email.items():
        if len(exams) > average_exams:
            print(f'{sheet} - {email}: {len(exams)} average exams: {average_exams}')
            for exam in exams:
                print(f'exam {exam[0]} date {exam[1]} career {exam[2]} score {exam[3]} student {exam[4]}')


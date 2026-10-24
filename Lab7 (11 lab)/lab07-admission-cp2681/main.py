'''
lab07-admission-cp2681
'''
num_applicants = int(input())

applicants_score = []
for i in range(num_applicants):

    math = float(input())
    science = float(input())
    english =float(input())
    civics =float(input())

    applicants_score.append([math, science, english, civics])

#น้ำหนักแต่ละวิชา
w_math = float(input())
w_science = float(input())
w_english = float(input())
w_civics = float(input())

pass_score = float(input())

pass_applicants = []
for i in range(num_applicants):
    score = applicants_score[i]

    total_score = (score[0] * w_math) + (score[1] * w_science ) + (score[2] * w_english ) + (score[3] * w_civics)

    if total_score >= pass_score:
        pass_applicants.append(i + 1)

if len(pass_applicants) > 0:
    print(pass_applicants)
else:
    print("NO ACCEPTABLE APPLICANT")


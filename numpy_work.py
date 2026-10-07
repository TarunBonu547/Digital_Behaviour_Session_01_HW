import numpy as np
import csv

python = []
aptitude = []
communication = []
sql = []
student = []

#Taking Python score

with open("placement_readiness.csv","r",encoding="utf-8") as file:
    reader = csv.DictReader(file)

    print(reader)

    for data in reader:
        python.append(int(data["Python_Score"]))
        aptitude.append(int(data["Aptitude_Score"]))
        communication.append(int(data["Communication_Score"]))
        sql.append(int(data['SQL_Score']))
        student.append(data["Student_ID"])


python_np = np.array(python)
aptitude_np = np.array(aptitude)
communication_np = np.array(communication)
sql_np = np.array(sql)

python_avg = python_np.mean()

highest_ap = aptitude_np.max()

lowest_ap = aptitude_np.min()

greater = communication_np > 70

count = greater.sum()

print(f"Mean of Python Scores : {python_avg}\nMaximum in aptitude score : {highest_ap}\nMinimum in aptitude score : {lowest_ap}\nNo of students greater than 70 in communication : {count}")

print(f"For every student gap between their worst and best skills : \n")

best = max(python,aptitude,communication,sql)

worst = min(python,aptitude,communication,sql)

for i in range(120):
    print(f"Student ID : {i+1}")
    print(abs(best[i]-worst[i]))

# Searched in Internet there is a method known as np.ptp() which can give the gap between worst and best
import numpy as np
import csv
import matplotlib.pyplot as plt

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

print("Numpy Work\n\n")

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

print("Pandas Work\n\n")

import pandas as pd

df = pd.read_csv("placement_readiness.csv")
print(f"Head :\n {df.head()}\n")
print(f"Shape :\n {df.shape}\n")
print(f"Columns :\n {df.columns}\n")
print(f"Describe :\n {df.describe}\n")

print("Python score greater than 75 : \n\n")
print(df[df["Python_Score"] > 75])
print("\n\n")

print("Sort the values according to the Aptitude Score in descending order : \n\n")

print(df.sort_values(by="Aptitude_Score",ascending=False))

df2 = df.sort_values(by="Python_Score",ascending=False)

print("The Top 10 Students by Python Score : \n\n")
print(df2.head(10))

print("Strong in Python but Weak in communication \n")

print(df[df["Python_Score"] > df["Communication_Score"]])

print("Creating New Knowledge along wth classifications............\n\n")

df["Total_Score"] = df["Communication_Score"] + df["Python_Score"] + df["SQL_Score"] + df["Aptitude_Score"]

df["Average_Score"] = df["Total_Score"]/4

df["Weakest_Score"] = df[["Aptitude_Score","Communication_Score","Python_Score","SQL_Score"]].min(axis=1)

df["Readiness_Score"] = np.minimum((df["Average_Score"] + 2*df["Projects_Completed"] + df["Mock_Interviews_Attended"]),100)

df["Readiness_band"] = "Ready"

df.loc[df["Readiness_Score"] < 60,"Readiness_band"] = "Needs Work"

df.loc[(df["Readiness_Score"] >= 60) & (df["Readiness_Score"] < 75),"Readiness_band"] = "Almost Ready"

print("The DataFrame with new Knowledge amd classifications:\n")

print(df)

print("The count of each band :\n")

print(f"Needs Work : {(df["Readiness_band"] == "Needs Work").sum()}\n")

print(f"Ready : {(df["Readiness_band"] == "Ready").sum()}\n")

print(f"Almost Ready : {(df["Readiness_band"] == "Almost Ready").sum()}\n")

print(f"The maximum of three bands : {np.max([(df["Readiness_band"] == "Needs Work").sum(),(df["Readiness_band"] == "Ready").sum(),(df["Readiness_band"] == "Almost Ready").sum()])}")

print("Creating the new knowledge.......!!!!!")

df.to_csv("placement_results.csv")

#Creating charts

plt.figure(figsize=(12,5))

Average_score = {
    "Python Score" : python_np.mean(),
    "SQL Score" : sql_np.mean(),
    "Communication Score" : communication_np.mean(),
    "Aptitude Score" : aptitude_np.mean()
}

plt.bar(Average_score.keys(),Average_score.values())
plt.xlabel("Subject")
plt.ylabel("Score")
plt.title("Average Score of Each app")
plt.savefig("charts/Average_Score.png",dpi=500)
plt.show()
plt.close()


plt.figure(figsize=(12,5))

Readiness = {
    "Needs Work" : (df["Readiness_band"] == "Needs Work").sum(),
    "Ready" : (df["Readiness_band"] == "Ready").sum(),
    "Almost Ready" : (df["Readiness_band"] == "Almost Ready").sum()
}

plt.bar(Readiness.keys(),Readiness.values())
plt.xlabel("Readiness Type")
plt.ylabel("No of Students")
plt.title("Students in each readiness")
plt.savefig("charts/Students_readiness.png",dpi = 500)
plt.show()
plt.close()

Avg_readiness = {
    "Needs Work" : (df["Readiness_band"] == "Needs Work").mean(),
    "Ready" : (df["Readiness_band"] == "Ready").mean(),
    "Almost Ready" : (df["Readiness_band"] == "Almost Ready").mean()
}
plt.bar(Avg_readiness.keys(),Avg_readiness.values())
plt.xlabel("Branch")
plt.ylabel("Readiness Score")
plt.title("Average readiness score by branch")
plt.savefig("charts/Average_readiness.png",dpi = 500)
plt.show()
plt.close()
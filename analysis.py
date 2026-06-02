import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("students.csv")
print("\nStudent Data")
print(data)
data["Average"] = (
    data["Maths"] +
    data["Science"] +
    data["English"]
) / 3
print("\nAverage Marks")
print(data[["Name", "Average"]])
top_student = data.loc[data["Average"].idxmax()]
print("\nTop Student")
print(top_student)
failed_students = data[data["Average"] < 50]
print("\nFailed Students")
print(failed_students)
plt.bar(data["Name"], data["Average"])
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Student Performance Analysis")
plt.show()
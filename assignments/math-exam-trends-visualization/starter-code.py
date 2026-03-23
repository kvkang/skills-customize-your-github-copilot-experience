# Starter Code: Math Exam Trends Visualization

import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset
df = pd.read_csv("math_scores.csv")

# 2. Display the first 5 rows
print(df.head())

# 3. Show summary statistics for exam columns
exam_columns = ["exam1", "exam2", "exam3", "exam4"]
print(df[exam_columns].describe())

# 4. Calculate class averages
class_averages = df[exam_columns].mean()
print("\nClass averages:")
print(class_averages)

# 5. Create student trend chart
plt.figure(figsize=(10, 6))
for _, row in df.iterrows():
    plt.plot(exam_columns, row[exam_columns], marker="o", alpha=0.6, label=row["student_name"])

plt.title("Student Math Score Trends")
plt.xlabel("Exam")
plt.ylabel("Score")
plt.ylim(0, 100)
plt.grid(True, alpha=0.3)
plt.savefig("student_trends.png")
plt.close()

# 6. Create class average trend chart
plt.figure(figsize=(8, 5))
plt.plot(exam_columns, class_averages.values, marker="o", linewidth=2)
plt.title("Class Average Math Scores by Exam")
plt.xlabel("Exam")
plt.ylabel("Average Score")
plt.ylim(0, 100)
plt.grid(True, alpha=0.3)
plt.savefig("class_average_trend.png")
plt.close()

# 7. Create score distribution chart
plt.figure(figsize=(10, 6))
df[exam_columns].boxplot()
plt.title("Math Score Distribution Across Exams")
plt.xlabel("Exam")
plt.ylabel("Score")
plt.ylim(0, 100)
plt.savefig("score_distribution.png")
plt.close()

print("\nCharts saved successfully.")
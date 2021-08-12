import pandas as pd
import statistics
import csv

df = pd.read_csv("StudentsPerformance.csv")

gender_list = df["gender"].to_list()
race_list = df["race/ethnicity"].to_list()
education_list = df["parental level of education"].to_list()
lunch_list = df["lunch"].to_list()
preparation_course_list = df["test preparation course"].to_list()
math_score = df["math score"].to_list()
reading_score_list = df["reading score"].to_list()
writing_score_list = df["writing score"].to_list()
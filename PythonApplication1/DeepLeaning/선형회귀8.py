
from turtle import title
import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys


if sys.platform == 'win32':  # Windows
    plt.rcParams['font.family'] = 'Malgun Gothic'
elif sys.platform == 'darwin':  # macOS
    plt.rcParams['font.family'] = 'AppleGothic'
else:  # Linux
    plt.rcParams['font.family'] = 'Noto Sans CJK KR'

plt.rcParams['axes.unicode_minus'] = False

print("hello")

# 데이타 

# 1.CSV 를읽어서 1열은 X 2열은 Y 로 넣기
csvpath=r"F:\2025_Portpolio\PythonApplication1\PythonApplication1\DeepLeaning\1.csv"
csvdata = pd.read_csv(csvpath)

X_DATA=np.array([])
Y_DATA=np.array([])

for row in csvdata.itertuples():
    print(row)
    X_DATA = np.append(X_DATA, float(row[1]))
    Y_DATA = np.append(Y_DATA, float(row[2]))

print(X_DATA)
print(Y_DATA)

#배열 크기 최대값 최소값
print("X_DATA max:", np.max(X_DATA), " min:", np.min(X_DATA))

var_val = np.max(X_DATA) - np.min(X_DATA)

print( int(np.min(X_DATA)), int(np.max(X_DATA))+1)

plt.figure(figsize=(int(np.min(X_DATA)),(int(np.max(X_DATA))+1)))

df = pd.DataFrame({
    "Hours_Studied": X_DATA,
    "Exam_Score": Y_DATA
})



기울기 =np.max(Y_DATA)-np.min(Y_DATA)/(Y_DATA.size-1)
절편 =np.min(Y_DATA)-기울기
print("기울기:", 기울기 ,"절편", 절편)

# 예측선 그리기



plt.scatter(df["Hours_Studied"],df["Exam_Score"],color="blue")
plt.title("시간 VS 점수")
plt.xlabel("시간")
plt.ylabel("점수")
plt.grid(True)
plt.show()
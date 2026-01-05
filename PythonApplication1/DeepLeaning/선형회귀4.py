from numpy.random import f
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


print(pd.__version__)
print(np.__version__)

# step 1 -create data
X_data = np.array([1.5,1.8,2.0,2.5,3.3,3.8,4.0,4.9,5.5,5.9,6.0,6.3,7.0,7.2,8.9,9.0,9.5])
Y_data = np.array([50,55,54,58,60,65,69,72,75,79,80,82,84,81,86,89,92])

# step 2 - save to csv
df =pd.DataFrame({'Hours_Studied':X_data, 'Exam_Score':Y_data})
df.to_csv('student_scores.csv', index=False)
print(df)

# Step 2 - Visualize dataㅁ
plt.figure(figsize=(8,6))
plt.scatter(df["Hours_Studied"], df["Exam_Score"], color="blue")  # CSV 도 할수있구나 
plt.title("Hours Studied VS Exam Score")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.grid(True)
plt.show()

# STEP 3 — Loss Function (MSE)  이걸 구해야 한다.
def mean_squared_error(X,Y,m,b):
    predicted_Y = m * X + b
    return np.mean((Y-predicted_Y) ** 2) # 평균 제곱 오차 계산 그냥 고정공식 

# STEP 4 — Gradient Descent 
def gradient_descent(X,Y,m,b,learning_rate):
    N= len(Y)
    predicated_Y = m * X + b  # 그냥 이공식은 무조건 나오는듯 
    error = predicated_Y - Y

    # 기울기 계산    
    gradient_m = (2/N) * np.sum(error * X)  # 편미분 공식)
    gradient_b =(2/N) * np.sum(error)      # 편미분 공식)

    # 매개변수 업데이트
    m -= learning_rate * gradient_m
    b -= learning_rate * gradient_b
    return m,b

# STEP 5 — Training Loop
m= 0.0  # 초기 기울기
b= 0.0  # 초기 절편
learning_rate = 0.01 # 학습률
epochs =500 # 반복 횟수

m_history = [] # 기울기 기록
b_history = []# 절편 기록
loss_history = []# 손실 기록

for epoch in range(epochs):
    m,b = gradient_descent(X_data, Y_data, m, b, learning_rate)
    loss= mean_squared_error(X_data, Y_data, m, b)

    m_history.append(m)
    b_history.append(b)
    loss_history.append(loss)

print(f"학습된 기울기 (m): {m_history}")
print(f"절편기록 (m): {b_history}")
print(f"손실기록 기울기 (m): {loss_history}")


# STEP 6 — Evaluation Metrics
def mean_absolute_error(y_true,y_pred):
        return np.mean(np.abs(y_true - y_pred)) # 절대 오차 평균 np.abs 절대값
"""
[3, 5, 7] - [2, 6, 8]
= [1, -1, -1]
절대값은 [1 ,1,1]
평균은 1 이다  절대값의 평균
"""

def root_mean_squared_error(y_true, y_pred):
    return np.sqrt(np.mean((y_true - y_pred) ** 2))
"""
제곱 오차 평균의 제곱근 루트 
"""

def r2_score(y_true, y_pred):
    ss_total = np.sum((y_true - np.mean(y_true))**2)
    ss_residual = np.sum((y_true - y_pred)**2)
    return 1 - (ss_residual / ss_total)


# Calculate Metrics


# STEP 7 — Visualizations

# Regression Fit


# Loss Curve

# STEP 8 — Compare with sklearn

# STEP 9 — R² Comparison

# STEP 10 — Compare Loss Curve: Scratch vs Sklearn

# Compute constant MSE for sklearn model


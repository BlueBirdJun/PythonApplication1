from numpy.random import f
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

X_data = np.array([1.5,1.8,2.0,2.5,3.3,3.8,4.0,4.9,5.5,5.9,6.0,6.3,7.0,7.2,8.9,9.0,9.5])
Y_data = np.array([50,55,54,58,60,65,69,72,75,79,80,82,84,81,86,89,92])

plt.figure(figsize=(8,6))
plt.scatter(X_data, Y_data, color="blue")  # CSV 도 할수있구나
plt.title("Hours Studied VS Exam Score")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.grid(True)
plt.show()

# MSE 
def mean_squard_error(X,Y,m,b):  # 여기서 X는 입력 Y는 정답입니다. m은 기울기 b는 절편
    predicted_Y = m * X + b
    return np.mean((Y - predicted_Y) ** 2)  # 평균 제곱 오차 계산 그냥 고정공식
# 일종의 검증 기울기랑 절편을 넣어서 오차 를 구하는 공식 
#   predicted_Y = m * X + b  배열 값을 던져서 기울기랑 절편으로 한개의 값을 구하는것 여기서 죽어도 수학이 안나올수가 없다

def gradient_descent(X,Y,m,b, learning_rate):
    N= len(Y)
    predicated_Y = m*X+ b  # X  입력값을 기울기랑 절편으로 예측값을 구한다
    error = predicated_Y - Y # 이걸로 정답이랑 오차를 구한다.

    gradient_m = (2/N) * np.sum(error * X)
    gradient_b = (2/N) * np.sum(error)

    m -= learning_rate * gradient_m
    b -= learning_rate * gradient_b
    return m,b
# 반복학습 

m= 0.0
b= 0.0  # 둘다 0으로 시작
learning_rate = 0.01
epochs =500

m_history = []
b_history = []
loss_history = []

for epoch in range(epochs):
    m,b =gradient_descent(X_data,Y_data,m,b, learning_rate)
    loss = mean_squard_error(X_data, Y_data, m, b)
    print(m,b)
    m_history.append(m)
    b_history.append(b)
    loss_history.append(loss)


print(f"\nFinal Parameters : m={m:.4f}, b={b:.4f}")


# 절대값
def mean_absolute_error(y_true, y_pred):
    return np.mean(np.abs(y_true - y_pred))

# 제곱근 오차
def root_mean_squared_error(y_true, y_pred):
    return np.sqrt(np.mean((y_true - y_pred)**2))

# 결정계수 R²
def r2_score(y_true, y_pred):
    ss_total = np.sum((y_true - np.mean(y_true))**2)
    ss_residual = np.sum((y_true - y_pred)**2)
    return 1 - (ss_residual / ss_total)

final_predicted_Y = m * X_data + b
mae = mean_absolute_error(Y_data, final_predicted_Y)
rmse = root_mean_squared_error(Y_data, final_predicted_Y)
r2_custom = r2_score(Y_data, final_predicted_Y)



# STEP 7 — Visualizations
plt.figure(figsize=(12,5))

# Regression Fit
plt.subplot(1,2,1)
plt.scatter(X_data, Y_data, color="blue")
plt.plot(X_data, final_predicted_Y, color="red", linewidth=2)
plt.title("Linear Regression Fit (Scratch)")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.grid(True)

# Loss Curve
plt.subplot(1,2,2)
plt.plot(loss_history, color="green")
plt.title("MSE Loss vs Epochs")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid(True)

plt.tight_layout()
plt.show()

 

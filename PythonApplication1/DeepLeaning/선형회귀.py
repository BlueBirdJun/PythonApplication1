"""
선형회귀(Linear Regression)는 
통계학과 머신러닝에서 널리 사용되는 기법으로,
독립 변수(입력 변수)와 종속 변수(출력 변수) 간의 
선형 관계를 모델링하는 방법입니다. 선형회귀는 
주로 예측 및 추론에 사용되며, 데이터 분석에서 중요한 역할을 합니다.

기본 공식
y = wx + b
입력 값에 비례해서 결과 값을 예측
x=입력값
y=출력값
a=기울기(가중치)
b=절편(기본값)
x가 커질수록 y도 커짐 숫자로 표현 
"""
from tkinter.ttk import tclobjs_to_py
import matplotlib.pyplot as plt
import torch
import sys

# OS별 한글 폰트 자동 설정
if sys.platform == 'win32':  # Windows
    plt.rcParams['font.family'] = 'Malgun Gothic'
elif sys.platform == 'darwin':  # macOS
    plt.rcParams['font.family'] = 'AppleGothic'
else:  # Linux
    plt.rcParams['font.family'] = 'Noto Sans CJK KR'

plt.rcParams['axes.unicode_minus'] = False
 

 

# 입력 데이타 (x)
# x = [1, 2, 3, 4, 5]
# 정답 데이타(y)
#y = [3, 4, 6, 8, 10]
# 이건  y=2x 공식임 
a = 0
b = 0

#def predict(x):
#    return a*x + b

# 이것 이렇다 공식을 만드는것구나 

x = torch.tensor([[1.], [2.], [3.], [4.], [5.]])
y = torch.tensor([[2.], [4.], [6.], [8.], [10.]])
# 선형 모델
model = torch.nn.Linear(1, 1)

# 손실 함수
loss_fn = torch.nn.MSELoss()

# 최적화 도구 (경사하강법)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

for epoch in range(1000):
    # 예측
    y_pred = model(x)

    # 오차 계산
    loss = loss_fn(y_pred, y)

    # 이전 기울기 제거
    optimizer.zero_grad()

    # 역전파
    loss.backward()

    # 파라미터 업데이트
    optimizer.step()

    if epoch % 100 == 0:
        print(epoch, loss.item())

# 데이터
x = torch.tensor([1, 2, 3, 4, 5], dtype=torch.float32)
y = torch.tensor([2, 4, 6, 8, 10], dtype=torch.float32)

# 학습된 것처럼 가정한 파라미터
a = 2.0
b = 0.0

# 예측
y_pred = a * x + b # x 는 y의 두배니까 b라는 오차를 넣는구나

# 그래프
"""
plt.figure()
plt.scatter(x, y)      # 실제 데이터 입력을 이렇게 한다.
plt.plot(x, y_pred)   # 선형회귀 직선 공식을 넣을수 있구나
plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Regression Visualization")
plt.show()

선형회귀는 선을 찾는것 
"""

x1 =torch.tensor([1,2,3,4,5,6,7,8,9,10,11,12], dtype=torch.float32) #입력데이타를 배열로 할려면 
y2= torch.tensor([2,4,6,8,10,12,14,16,18,20,22,24], dtype=torch.float32)
print(x1)
a1 =2 #기울기
b1 =2 #보강값

y_pred2 = a1*x1 + b1
plt.figure()
plt.scatter(x1, y2)      # 실제 데이터 입력을 이렇게 한다.
plt.plot(x1, y_pred2)   # 선형회귀 직선 공식을 넣을수 있구나
plt.xlabel("x1")
plt.ylabel("y2")
plt.title("선형회귀")
plt.show()

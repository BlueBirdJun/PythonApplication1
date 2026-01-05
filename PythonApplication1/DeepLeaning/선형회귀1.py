import torch
import matplotlib.pyplot as plt

torch.manual_seed(0) # 재현성을 위한 시드 설정 

x1 = torch.linspace(0, 10, 50) # 0~10 50개 균일간격
x2 = torch.linspace(5, 15, 50) # 5~15 50개 균일간격
"""
   .....
   .............
   아 unsqueese 가 뭔지 알겠다
    unsqueeze는 차원을 하나 늘려주는 역할을 한다.
    예를 들어, 1차원 텐서 [10, 20, 30]이 있을 때,
    unsqueeze(1)을 적용하면 2차원 텐서 [[10], [20], [30]]이 된다.
    unsqueeze는 주로 텐서의 차원을 맞춰주기 위해 사용된다.
    예를들면 (50,) 텐서를 (50,1) 로 바꿀때 사용
    unsqueeze(2)  는 2번째 차원에 새로운 차원을 추가한다.
    예를들면 (3,4) 텐서에  unsqueeze(2) 적용하면 (3,4,1) 이 된다.
    unsqueeze(0)  는 0번째 차원에 새로운 차원을 추가한다. 

  
"""
# 일종의 데이타셋 생성
x= torch.stack((x1, x2), dim=1) # 두 변수를 하나의 텐서로 합침 dim=1 열방향으로 합침
#x 의 0.5를 곱해준다.
noise = torch.randn(x.size()) * 0.5 # 정규분포 노이즈 생성  0.5 곱해 노이즈 강도 조절 현실적 
y = 3 * x1 + 2 * x2 + noise[:, 0] # 선형 조합에 노이즈 추가
y=y.unsqueeze(1) # y를 (50,1) 형태로 변경

# ===============================
# 2. 선형회귀 모델 (입력 2 → 출력 1)
# ===============================
model = torch.nn.Linear(2, 1)
loss_fn = torch.nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.001)

# ===============================
# 3. 학습
# ===============================
for epoch in range(3000):
    y_pred = model(x)
    loss = loss_fn(y_pred, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 500 == 0:
        print(epoch, loss.item())

# ===============================
# 4. 결과 확인
# ===============================
w1, w2 = model.weight[0]
b = model.bias.item()

print(f"학습된 w1 (x1): {w1.item():.2f}")
print(f"학습된 w2 (x2): {w2.item():.2f}")
print(f"학습된 b: {b:.2f}")

# ===============================
# 5. 시각화 (x1 기준)
# ===============================
plt.figure()
plt.scatter(x1, y.squeeze(), label="Actual")
plt.plot(x1, (3*x1 + 5*x2 + 2), label="True Line")
plt.plot(x1, y_pred.detach().squeeze(), label="Predicted")
plt.xlabel("x1")
plt.ylabel("y")
plt.title("Multivariable Linear Regression (Practical Case)")
plt.legend()
plt.show()
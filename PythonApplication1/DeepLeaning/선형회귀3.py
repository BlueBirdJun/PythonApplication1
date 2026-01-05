from pickletools import optimize
import sys
import torch
import matplotlib.pyplot as plt

print(torch.__version__)
torch.manual_seed(0) # 그냥 고정값인가보다

# OS별 한글 폰트 자동 설정
if sys.platform == 'win32':  # Windows
    plt.rcParams['font.family'] = 'Malgun Gothic'
elif sys.platform == 'darwin':  # macOS
    plt.rcParams['font.family'] = 'AppleGothic'
else:  # Linux
    plt.rcParams['font.family'] = 'Noto Sans CJK KR'
plt.rcParams['axes.unicode_minus'] = False
 
x1 = torch.linspace(0, 10, 50) # 0~10 50개 균일간격
x2 = torch.linspace(5, 15, 50) # 5~15 50개 균일간격

x=torch.stack((x1, x2), dim=1) # 두 변수를 하나의 텐서로 합침 dim=1 열방향으로 합침
noise = torch.randn(x.size()) * 0.5 # 정규분포 노이즈 생성  0.5 곱해 노이즈 강도 조절 현실적))
y=(3*x1)+(2*x2)+noise[:,0] # 선형 조합에 노이즈 추가
y=y.unsqueeze(1) # y를 (50,1) 형태로 변경

model = torch.nn.Linear(2, 1)# 선형회귀 모델 (입력 2 → 출력 1)
loss_fn =torch.nn.MSELoss() # 손실함수 설정
optimizer = torch.optim.SGD(model.parameters(), lr=0.001) # 학습률 0.001

for epoch  in range(3000):
     y_pred = model(x)
     loss = loss_fn(y_pred, y)
     optimizer.zero_grad()
     loss.backward()
     optimizer.step()

     if epoch % 500 ==0:
            print(epoch, loss.item())

w1, w2 = model.weight[0]
b = model.bias.item()

print(f"학습된 w1 (x1): {w1.item():.2f}")
print(f"학습된 w2 (x2): {w2.item():.2f}")
print(f"학습된 b: {b:.2f}")

plt.figure()
plt.scatter(x1, y.squeeze(), label="Actual")
plt.plot(x1, (3*x1 + 5*x2 + 2), label="True Line")
plt.plot(x1, y_pred.detach().squeeze(), label="Predicted")
plt.xlabel("x1")
plt.ylabel("y")
plt.title("Multivariable Linear Regression (Practical Case)")
plt.legend()
plt.show()
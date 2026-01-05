
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

# 1. 간단한 데이터 생성 (PyTorch 텐서 활용)
x = torch.linspace(0, 10, 100)
y = torch.sin(x)

# 2. 그래프 그리기
plt.figure(figsize=(8, 4))
plt.plot(x.numpy(), y.numpy(), label='Sine Wave')

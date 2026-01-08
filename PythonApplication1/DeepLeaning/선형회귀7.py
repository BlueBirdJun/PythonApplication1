from numpy.random import f
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys


X_data = np.array([1.1,2.3,3.5,4.8,5.8])
Y_data = np.array([43,49,54,62,73])

# OS별 한글 폰트 자동 설정
if sys.platform == 'win32':  # Windows
    plt.rcParams['font.family'] = 'Malgun Gothic'
elif sys.platform == 'darwin':  # macOS
    plt.rcParams['font.family'] = 'AppleGothic'
else:  # Linux
    plt.rcParams['font.family'] = 'Noto Sans CJK KR'

plt.rcParams['axes.unicode_minus'] = False

#Y=WX +B 여기
#서  Y 는 출력값  X는 입력값 W는 가중치 B는 편향
#
print(X_data)
# 배열 크기 알기
print(f"X 배열의 크기: {X_data.shape}")      # (5,)
print(f"X 배열의 요소 개수: {X_data.size}")  # 5
print(f"X 배열의 길이: {len(X_data)}")    
print(f"X 최대값: {np.min(Y_data)}")
print(f"X 최소값: {np.max(Y_data)}")



for i in range(len(X_data)):
    print(f"입력: {X_data[i]}, 출력: {Y_data[i]}")




"""
scatter

"""
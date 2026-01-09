from typing import Literal
from numpy.random import f
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

# OS별 한글 폰트 자동 설정
if sys.platform == 'win32':  # Windows
    plt.rcParams['font.family'] = 'Malgun Gothic'
elif sys.platform == 'darwin':  # macOS
    plt.rcParams['font.family'] = 'AppleGothic'
else:  # Linux
    plt.rcParams['font.family'] = 'Noto Sans CJK KR'

plt.rcParams['axes.unicode_minus'] = False


def  chat_util(kind:Literal["scatter", "plot", "bar"] ,데이타: pd.DataFrame):
   plt.figure(figsize=(8,6))
   plt.title("챠트")
   plt.xlabel("X선")
   plt.ylabel("Y선")
   plt.grid(True)
   plt.tight_layout()
   if kind == "scatter":
    plt.scatter(데이타.iloc[:, 0], 데이타.iloc[:, 1])
   elif kind == "plot":
    plt.plot(데이타.iloc[:, 0], 데이타.iloc[:, 1])
   elif kind == "bar":
    plt.bar(데이타.iloc[:, 0], 데이타.iloc[:, 1])

   return plt
    


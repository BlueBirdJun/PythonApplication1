from numpy.random import f
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import torch

# OS별 한글 폰트 자동 설정
if sys.platform == 'win32':  # Windows
    plt.rcParams['font.family'] = 'Malgun Gothic'
elif sys.platform == 'darwin':  # macOS
    plt.rcParams['font.family'] = 'AppleGothic'
else:  # Linux
    plt.rcParams['font.family'] = 'Noto Sans CJK KR'

plt.rcParams['axes.unicode_minus'] = False
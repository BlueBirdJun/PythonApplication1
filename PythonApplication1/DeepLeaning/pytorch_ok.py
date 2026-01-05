import torch

# 1. 결과가 True로 바뀌어야 합니다.
print(torch.cuda.is_available())

# 2. 결과가 0 이상의 숫자(보통 1)가 나와야 합니다.
print(torch.cuda.device_count())

# 3. 'NVIDIA GeForce RTX 5070'이 출력되는지 확인하세요.
print(torch.cuda.get_device_name(0))
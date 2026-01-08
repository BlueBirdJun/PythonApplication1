import Commons

print("시작")

# 1. 가짜 데이타 만들기
X =2 * Commons.np.random.rand(100,1)
Y= 4 +3 * X + Commons.np.random.randn(100,1)
print("X:", X[:5],"Size",X.size)
print("X:", X[:5])


def predict(x,w,b):
    return w * x + b

#오차  평균 제곱오차 
def mean_squared_error(입력배열, 정답배열,기울기,절편):
    예측값 =절편*입력배열 + 절편
    return Commons.np.mean((정답배열 - 예측값) ** 2) #


w=0.0  #기울기
b=0.0  #절편
learning_rate = 0.01
epoch= 500 


print("최종 w:", w)
print("최종 b:", b)
#경사 하강법 함수





Commons.plt.figure(figsize=(8,6)) #크기설정
Commons.plt.scatter(X,Y) #산점도
Commons.plt.plot(X, predict(Y, w, b), color="red", label="Regression Line")
Commons.plt.xlabel("X")
Commons.plt.ylabel("Y")
Commons.plt.title("Random Data")
Commons.plt.grid(True)
Commons.plt.show()

import Commons

print("시작")

# 1. 더미데이타 만들기
입력데이타 = Commons.np.array([1.5,1.8,2.0,2.5,3.3,3.8,4.0,4.9,5.5,5.9,6.0,6.3,7.0,7.2,8.9,9.0,9.5])
정답데이타 =   Commons.np.array([50,55,54,58,60,65,69,72,75,79,80,82,84,81,86,89,92])

데이타=Commons.pd.DataFrame({
    "입력":입력데이타,
    "정답":정답데이타
    })

plt= Commons.chat_util("scatter", 데이타)
plt.xlabel("입력값")
plt.ylabel("정답값")

#MSE
def mse_get(x,y,m,b):   
   c =x*m +b
   return Commons.np.mean ((y-c) ** 2)
 
#내려가기

def gradient_fun(x,y,m,b,lr):
     n=len(y)
     pred = m*x + b
     err = pred - y
     
     grad_m = (2/n) * Commons.np.sum(err * x)
     grad_b = (2/n) * Commons.np.sum(err)
     
     m -= lr * grad_m
     b -= lr * grad_b
     return m,b

m = 0.0   #기울기
b = 0.0   #절편 
lr = 0.01#0.01  #학습률
eporch =500 #훈련횟수

error_data=[]


for i in range(eporch):
    m,b = gradient_fun(입력데이타,정답데이타,m,b,lr)
    loss = mse_get(입력데이타,정답데이타,m,b)
    error_data.append(loss)

print(m,b)
    
plt.subplot(1,2,1)    
plt.plot(error_data, color="gray", linewidth=2)
plt.subplot(1,1,1)
plt.plot(입력데이타, m*입력데이타 + b, color="red")
plt.show()







plt.show()

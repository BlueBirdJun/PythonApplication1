import Commons

print("시작")

# 1. 가짜 데이타 만들기
#입력배열 =2 * Commons.np.random.rand(100,1)
#정답배열= 4 +3 * 입력배열 + Commons.np.random.randn(100,1)
# Study/1.py  DeepLeaning/선형회귀6.py,Study/1.py

입력배열 = Commons.np.array([1.5,1.8,2.0,2.5,3.3,3.8,4.0,4.9,5.5,5.9,6.0,6.3,7.0,7.2,8.9,9.0,9.5])
정답배열 = Commons.np.array([50,55,54,58,60,65,69,72,75,79,80,82,84,81,86,89,92])


# MSE
def 오류값(입력배열,정답배열,기울기,절편):
   예측값배열=기울기*입력배열+절편
   return Commons.np.mean((정답배열-예측값배열) **2) # 제곱의 평균
# 오류값의 평균을 내준다

def 경사_하강(입력배열,정답배열,기울기,절편,미세조정):
     갯수=len(정답배열)
     예측값 = 기울기*입력배열+절편
     오류값 = 예측값-정답배열
     #편미분 출동 
     경사하강입력= (2/갯수) * Commons.np.sum(오류값*입력배열)
     경사하강 =(2/갯수)*Commons.np.sum(오류값)

     기울기 -=미세조정*경사하강입력
     절편 -=미세조정*경사하강 
     return 기울기,절편


훈련횟수=500 
기울기=0.0
절편=0.0
미세조정=0.01

입력챠트 =Commons.pd.DataFrame({
    "시간":입력배열,
    "점수":정답배열
    })   
plt= Commons.chat_util("scatter",입력챠트)

기울기_기록=[]
절편_기록 =[]
오류_기록 =[]

for 훈련 in range(훈련횟수):
    기울기,절편=경사_하강(입력배열,정답배열,기울기,절편,미세조정)         
    오류 = 오류값(입력배열,정답배열,기울기,절편) 
    
    기울기_기록.append(기울기)
    절편_기록.append(절편)
    오류_기록.append(오류)

print(f"\nFinal Parameters : m={기울기:.4f}, b={오류:.4f}")
 
print(기울기_기록);

# STEP 6 — Evaluation Metrics
def mean_absolute_error(y_true, y_pred):
    return Commons.np.mean(Commons.np.abs(y_true - y_pred))

def root_mean_squared_error(y_true, y_pred):
    return Commons.np.sqrt(Commons.np.mean((y_true - y_pred)**2))

def r2_score(y_true, y_pred):
    ss_total = Commons.np.sum((y_true - Commons.np.mean(y_true))**2)
    ss_residual = Commons.np.sum((y_true - y_pred)**2)
    return 1 - (ss_residual / ss_total)
final_predicted_Y = 기울기 * 입력배열 + 절편
mae = mean_absolute_error(정답배열, final_predicted_Y)
rmse = root_mean_squared_error(정답배열, final_predicted_Y)
r2_custom = r2_score(정답배열, final_predicted_Y)
    

plt.subplot(1,2,1)
plt.plot(입력배열, final_predicted_Y, color="red", linewidth=2)
plt.show()
     
print("완료")
 
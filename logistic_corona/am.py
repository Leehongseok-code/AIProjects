import numpy as np # 넘파이 사용
import matplotlib.pyplot as plt # 맷플롯립사용
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import pandas as pd
from numpy import asarray
from main import c
import math

def sigmoid(x): # 시그모이드 함수 정의
    return 1/(1+np.exp(-x))

def make_xdataset(dat):
    mdata=[]
    temp=[]
    for i in range(0,len(dat)-7):
        for j in range(7):
            temp.append(dat[i+j])
        mdata.append(temp)
        temp=[]
        print(temp)
    return mdata

def make_ydataset(dat):
    mdata=[]
    temp=[]
    for i in range(7,len(dat)):
        temp.append(dat[i])
        mdata.append(temp)
        temp=[]
    return mdata

def maxmin(dat):
    mx=max(dat[0::])
    mn=min(dat[0::])
    dis=mx-mn
    return (dat-mn)/mx#이렇게하면 그래프가 더 비슷하게 나옴


x = np.arange(-5.0, 5.0, 0.1)

exdata=pd.read_csv("./logis.csv")

cdata=exdata["am"]
mx=max(cdata[0::])
mn=min(cdata[0::])
dis=mx-mn
ccdata=maxmin(cdata)#구간의 길이에 대한 상대도수로 표현

#for i in range(15,len(cdata)):
#    cdata[i]=math.log10(math.log10(cdata[i]))
x_data=make_xdataset(ccdata)

print(x_data)
#print(xdata)

print(cdata)
y_data=make_ydataset(ccdata)#x의 코스트를 줄이기 위해 같이 나눔
y_datab=make_ydataset(cdata)#원본
#print(ydata)

x_train = torch.FloatTensor(x_data)
y_train = torch.FloatTensor(y_data)



# 모델 초기화
W = torch.zeros((7, 1), requires_grad=True)
b = torch.zeros(1, requires_grad=True)
# optimizer 설정
optimizer = optim.SGD([W , b], lr=1)

nb_epochs = 50000
for epoch in range(nb_epochs + 1):

    # Cost 계산
    hypothesis = 1 / (1 + torch.exp(-(x_train.matmul(W) + b)))

    cost = -(y_train * torch.log(hypothesis) +
             (1 - y_train) * torch.log(1 - hypothesis)).mean()

    # cost로 H(x) 개선
    optimizer.zero_grad()
    cost.backward()
    optimizer.step()

    # 100번마다 로그 출력
    if epoch % 100 == 0:
        print('Epoch {:4d}/{} Cost: {:.6f}'.format
        (
            epoch, nb_epochs, cost.item()
        ))
#print(cdata[len(cdata)-7:len(cdata)-1:])

x_test=asarray(cdata[len(cdata)-7:len(cdata):])#뒤의 7개데이터를 통해 다음 날 유추
print(x_test)
x_test=list((x_test-mn)/mx)
x_test=[x_test]
x_test=torch.FloatTensor(x_test)


hypothesisbe=torch.sigmoid(x_train[len(x_train)-1].matmul(W) + b)#마지막날을 모델에서는 어떻게 예측했는가!
hypothesis = torch.sigmoid(x_test.matmul(W) + b)#다음날을 모델에서 어떻게 예측했는가!
differ=hypothesis-hypothesisbe

print("train:",x_train[len(x_train)-1])
print("test:",x_test)

'''
x_test=x_test[:1:5]+(hypothesis)
print("a:",x_test)
'''

prediction=[]
'''
for i in range(len(hypothesis)):
    print(hypothesis[i] * mx + mn)
    prediction.append(hypothesis[i]*mx+mn)
'''
print((x_test[len(x_test)-1][len(x_test[0])-1]+differ)*mx+mn)#추가 확진자수를 예측해서 마지막날 확진자수에 더함.(평행이동)
prediction.append((x_test[len(x_test)-1][len(x_test[0])-1]+differ)*mx+mn)
c.am=c.am+round(float(prediction[0]))
#print(prediction)

'''
plt.plot(y_datab)

plt.plot(prediction)
plt.legend(['original','prediction'])
plt.title('Sigmoid Function')
plt.show()
'''
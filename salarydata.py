import pandas as pd
data = pd.read_csv("Salary_Data.csv",encoding="utf-8")
print(data)

x = data["YearsExperience"]
y = data["Salary"]

import matplotlib.pyplot as plt
plt.rc("font",family="Microsoft JhengHei")

def plot_pred(w,b):
    y_pred = w*x + b
    plt.plot(x,y_pred,color="blue",label="預測線")
    plt.scatter(x,y , marker="x",color="red",label="真實數據")
    plt.title("年資-薪水")
    plt.xlabel("年資")
    plt.ylabel("月薪(千)")
    plt.xlim([0,12]) #固定X軸
    plt.ylim([0,140]) #固定Y軸
    plt.legend() #顯示圖例
    plt.savefig('1.png')

plot_pred(10, 30)
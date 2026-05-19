import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#data reading
data=pd.read_csv("Load_Extension - Sheet1.csv")
x=data[["Load (N)"]]
y=data[["Extension (mm)"]]

#graph
plt.scatter(x,y)
plt.show()

#linear regression model
model= LinearRegression()
model.fit(x,y)
m= model.coef_
c= model.intercept_
print("coefficient:", m)
print("intercept:", c)
print(f"Linear Regression Model y= {m}x +{c}")

#for 55N
new_Extension= model.predict([[55]])
print("Predicted Extension for 55 N =", new_Extension ,"mm")

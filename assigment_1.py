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
print("coefficient:", model.coef_)
print("intercept:", model.intercept_)

#for 55N
new_Extension= model.predict([[55]]).item()
print("Predicted Extension for 55 N =", new_Extension ,"mm")
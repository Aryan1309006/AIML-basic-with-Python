from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, mean_absolute_error,mean_squared_error,root_mean_squared_error,accuracy_score
import pandas as pd


df=pd.read_csv('diabetes_prediction_dataset.csv')

x=df[['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']]

y = df[['Outcome']]


#split 

x_train,x_test,y_train,y_test=train_test_split(
    x,y,test_size=0.2,random_state=42
)

model=LogisticRegression()

model.fit(x_train,y_train)

y_pred=model.predict(x_test)

print(mean_absolute_error(y_test, y_pred))
print(mean_squared_error(y_test, y_pred))
print(root_mean_squared_error(y_test, y_pred))

# print("MAE:", mae)
# print("MSE:", mse)
# print("RMSE:", rmse)



Pregnancies = int(input("Enter number of pregnancies: "))
Glucose = float(input("Enter glucose level: "))
BloodPressure = float(input("Enter blood pressure: "))
SkinThickness = float(input("Enter skin thickness: "))
Insulin = float(input("Enter insulin level: "))
BMI = float(input("Enter BMI: "))
DiabetesPedigreeFunction = float(input("Enter diabetes pedigree function: "))
Age = int(input("Enter age: "))


prediction=model.predict([[
Pregnancies,
Glucose,
BloodPressure,
SkinThickness,
Insulin,
BMI_v,
DiabetesPedigreeFunction,
Age,]]
)[[0]]

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

if prediction[0] == 1:
    if Glucose > 180:
        print("Severe Diabetes Risk")
    elif Glucose > 140:
        print("Moderate Diabetes Risk")
    else:
        print("Mild Diabetes Risk")
else:
    print("No Diabetes")
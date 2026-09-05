from sklearn.preprocessing import LabelEncoder,OneHotEncoder
import pandas as pd

df=pd.read_csv('demo.csv')

df_lable=df.copy()

# LabelEncoding
le=LabelEncoder()
df_lable['gender_Encoded']=le.fit_transform(df_lable['Gender'])
print(df_lable[['Name','gender_Encoded']])

# One-Hot incoding

df_encoded=pd.get_dummies(df_lable,columns=['City'])
# get_dummies-text into small binary column
print(df_encoded)

# Import required libraries
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Read CSV file
df = pd.read_csv('demo.csv')

# Create copy of original DataFrame
df_label = df.copy()

# ---------------- Label Encoding ----------------
# Converts text labels into numeric values

le = LabelEncoder()

# Encode Gender column
df_label['gender_Encoded'] = le.fit_transform(df_label['Gender'])

# Display encoded values
print("Label Encoded Data:")
print(df_label[['Name', 'gender_Encoded']])


# ---------------- One-Hot Encoding ----------------
# Converts categorical text into binary columns

df_encoded = pd.get_dummies(df_label, columns=['City'])

# Display updated DataFrame
print("\nOne-Hot Encoded Data:")
print(df_encoded)
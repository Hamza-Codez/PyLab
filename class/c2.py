import pandas as pd

# Load dataset and read the given csv file

data = pd.read_csv("E:/PyLab/class/Big_Black_Money_Dataset.csv")
print("Data load successfully")

# String operations on countries

upperCase = data["Country"].str.upper()
# print(upperCase)

lowerCase = data["Country"].str.lower()
# print(lowerCase) 

# Check if 'Country' contains the substring 'zil'

print("Countries containing 'Zil' in their name")
# print(data["Country"].str.contains("zil"))

# Replace text in 'Country' column
print("The China and Brazil is replaced with C and B respectivey")
print(data["Country"].replace({
  "Brazil": "B",
  "China": "C"
}))

# Check the length of strings in the 'Country' column
print("Length of the dataset strings index is:")
print(data["Country"].str.len())

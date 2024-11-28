
import pandas as pd

# 1. Load the Dataset
# =========================

try: 
  data = pd.read_csv('E:/PyLab/class/Big_Black_Money_Dataset.csv')
  print('The File (Big_Black_Money_Dataset.csv) is loaded successfully!')
except:
  print('The File (Big_Black_Money_Dataset.csv) is not found')  
  exit()

# 2. View Dataset
# =========================
  # print('Data of first 8 rows is given')
  # print(data.head(8))

# 3. ADD new column
# =========================
 
data["(33.3%) of Amount"] = data["Amount (USD)"]/3
# print(data.head(7))

#4. Renaming columns

new_data = data.rename(
  columns={
    "Transaction ID":"ID",
    "Financial Institution": "Banks",
    "(33.3%) of Amount":"1/3rd of Amount"
  }
)
# print("The renamed column dataset is :")
# print(new_data.head(10))

#5. Agression

data_agg = data.agg({
  "Money Laundering Risk Score":["min", "max", "median"],
  "Shell Companies Involved":["min", "max", "median"]
})

data_mode ={
   "Money Laundering Risk Score":data["Money Laundering Risk Score"].mode().iloc[0],
   "Shell Companies Involved":data["Shell Companies Involved"].mode().iloc[0]
}

data_agg.loc["mode"] = [data_mode["Money Laundering Risk Score"], data_mode["Shell Companies Involved"]]
# print("The calculated Agression is:")
# print(data_agg)

# 6: String Operations
print(data.head(6))
print("Countries in upperCase")
print(data["Country"].str.upper())

# 7:Save To a new file
data.to_csv("E:/theans.csv", index=False)
# print("Dataset saved to E:/theans.csv")

data_agg.to_csv("E:/Agression.csv", index=False)
print("Dataset Saved to E file storage")

# 8: Suppose you get a custom data
new_customData = ({
  "name":["Muhammad Hamza Ahmad"],
  "degree":["Bechelor's in Computer Science"],
  "age": [26],
  "Skill": ["Mern and Next Js"]
})

customData = pd.DataFrame(new_customData)
print("new custom Data:")
print(customData)

# 9. String Splitting Example
# =========================
print("Third word from the name:")
print(customData["name"].str.split(" ").str.get(2))

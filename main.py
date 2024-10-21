import pandas as pd


Dev = pd.DataFrame(
  {
    "Name": ["Ali", "Ahmed", "Fazal"],
    "Son Of": ["Afzal Ahmad", "Saleem Iqbal", "Rohail Safiq"],
      "Id": [34, 45, 65],
      "Class": ["Bs Cs", "Bs BI", "BS Data Science" ],
      "Marks": ["78%", "72%", "89%"],
      "Proficencies": ["Java","Rust","Ruby On Rails"]
  }
)


# print(Dev)
# print(Dev.describe())
# print(Dev["Marks"].max())
# print(Dev["Id"].max())

# requires data set file to run csv

# //Python treats string as object

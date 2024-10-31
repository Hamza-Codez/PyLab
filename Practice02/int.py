import pandas as pd
# import matplotlib.pyplot as plt
# #import libaray first
# # complete pandas function
var=pd.read_csv("Big_Black_Money_Dataset.csv")
# #print(var)
# #var["new column"]=var["Transaction ID"]+var["Country"]
# #print(var.head())
# #ar1=var.rename(columns={
# #    "Transaction ID":"ID",
# #    "Country":"COUN", 
# #})
# #var2=var1.rename(columns=str.lower)
# #print(var2)
# #print(var.values)

# #var1= var.agg({
# #    "Money Laundering Risk Score":["min", "max","median", "skew"],
# #    "Shell Companies Involved":["min","max","median","mean"]
# #})

#print(var.head())

#var["new column"]=var["Amount (USD)"]/3
#var1=pd.DataFrame(var)
#var1.to_csv("D:/theans.csv",index=False)
#print("program run successful")


#print(var["Country"].str.split(","))
#print(var["Country"].str.upper())
#print(var["Country"].str.contains())
#print(var["Country"])



# var1={
#     "name":["muhammad waqar younnas"],
#     "gendre":"male",
#     "marks":90,
#     }



# var2=pd.DataFrame(var1)

# print(var2["name"].str.split(" ").str.get(2))



var4={
    "Name": ["Anique", "Ahmad"],
    "Catogery": ["Software Engineer", "DataScientist", ]
}

vari = pd.DataFrame(var4)

print(vari["Catogery"])




# stu={
#     "name":["anique","ahmad"],
#     "class":["cs","it"],
#     }
# stu1=pd.DataFrame(stu)

# print(stu1["name"][1])









# Importing the Pandas library
# Pandas is an open-source data manipulation and analysis library for Python. 
# It provides data structures like Series (1D) and DataFrame (2D) that are 
# highly efficient for handling and analyzing large datasets. With Pandas, 
# we can perform data cleaning, merging, reshaping, and visualization tasks 
# seamlessly. It's widely used in data science, machine learning, and data 
# analysis projects due to its flexibility and powerful functionality.






# Importing the Pandas library
# Pandas is an open-source data manipulation and analysis library for Python, 
# providing powerful tools for handling structured data. Here are some benefits:
#
# 1. Efficient Data Handling: Pandas uses data structures like Series (1D) and 
#    DataFrame (2D) that allow for efficient handling of large datasets.
#
# 2. Data Cleaning & Preprocessing: It offers functions for handling missing 
#    data, duplicates, and transformations, making data preparation easier.
#
# 3. Flexible Data Indexing: Allows custom indexing, multi-level indexes, 
#    and alignment, making complex data manipulation tasks straightforward.
#
# 4. Data Aggregation & Grouping: Provides powerful group-by and aggregation 
#    capabilities for summarizing and analyzing data based on categories.
#
# 5. Integration with Other Libraries: Works well with libraries like NumPy, 
#    Matplotlib, and Scikit-Learn, streamlining the workflow for data analysis 
#    and machine learning tasks.
#
# 6. Read/Write Support for Various Formats: Supports formats like CSV, Excel, 
#    SQL, and JSON, simplifying the process of importing and exporting data.
#
# With its comprehensive feature set, Pandas is an essential tool in data 
# analysis, machine learning, and scientific computing projects.

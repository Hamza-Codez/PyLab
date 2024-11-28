import sklearn as sk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pyplot



from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestRegressor
from sklearn import svm
from sklearn.metrics import mean_squared_error

x,y = load_

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

# //Python treats string as obj

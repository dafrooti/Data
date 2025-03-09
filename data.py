import pandas as pd
import numpy as np

# data = np.array(['a','b','c','d','e'])

# n1 = pd.Series(data)
# print(n1)

# df = pd.DataFrame(['a','b','c','d','e'])
# print(df)

dict = {'name':["Aparna", "Pankaj", "Sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}
df = pd.DataFrame(dict)
# print(df)

name = df[["name", "degree"]]
# print(name)

# make a new list as a column and add to a existing Dataframe
df["age"] = [20, 23, 19, 21]
# print(df)

# make a new DF as a row and add to an existing Dataframe
newrow = pd.DataFrame({'name':"Shruti", "degree": "BSc", "score": 95},index = [0])
df = pd.concat([newrow, df]).reset_index(drop = True)
# print(df.info())

df.drop(["score", "age"], axis = 1, inplace = True)
df.set_index("name", inplace = True)
df.drop(["Shruti"], inplace = True)
print(df)

# df = pd.read_csv("titanic.csv")
# print(df)

# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.describe())

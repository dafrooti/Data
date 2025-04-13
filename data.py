import pandas as pd
import numpy as np

# # data = np.array(['a','b','c','d','e'])

# # n1 = pd.Series(data)
# # print(n1)

# # df = pd.DataFrame(['a','b','c','d','e'])
# # print(df)

# dict = {'name':["Aparna", "Pankaj", "Sudhir", "Geeku"],
#         'degree': ["MBA", "BCA", "M.Tech", "MBA"],
#         'score':[90, 40, 80, 98]}
# df = pd.DataFrame(dict)
# # print(df)

# name = df[["name", "degree"]]
# # print(name)

# # make a new list as a column and add to a existing Dataframe
# df["age"] = [20, 23, 19, 21]
# # print(df)

# # make a new DF as a row and add to an existing Dataframe
# newrow = pd.DataFrame({'name':"Shruti", "degree": "BSc", "score": 95},index = [0])
# df = pd.concat([newrow, df]).reset_index(drop = True)
# # print(df.info())

# df.drop(["score", "age"], axis = 1, inplace = True)
# df.set_index("name", inplace = True)
# df.drop(["Shruti"], inplace = True)
# print(df)

df = pd.read_csv("titanic.csv")
# print(df)

# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.describe())

# selecting and storing one or more columns

# .loc[](Label-based indexing)
# .iloc[](Interger-based indexing) row and column position slicing

# print(df.loc[df["Survived"]==1])
# print(df.loc[df["Sex"]=="female", ["Name", "Age", "Sex"]])

# print(df.iloc[0:100, 2:5]) #rows(Start:End), column(Start:End)

# selecting multiple columns

# df2 = df[["Name", "Age", "Sex", "Fare"]]

# adults = df2[df2["Age"]>18]
# print(adults)

# df3 = df[["Survived", "Pclass", "Name"]]

# firstclass = df3[df3["Pclass"]<2] # or == 1
# print(firstclass)

# df4 = df[["Survived", "Pclass", "Name"]]

# classes = df4[(df4["Pclass"]<2)|(df4["Pclass"]==2)]
# print(classes)

# df5 = df[["Survived", "Pclass", "Name", "Sex"]]

# classes = df5[(df5["Pclass"]<2)&(df5["Sex"]=="male")]
# print(classes.count())
# print(df["Pclass"].value_counts())

# df6 = df[["Survived", "Pclass", "Name", "Sex"]]

# classes = df6[(df6["Pclass"]==1)&(df6["Survived"]==1)]
# print(classes)

# df7 = df[["Survived", "Pclass", "Name", "Sex"]]

# classes = df7[(df7["Pclass"]==2)&(df7["Survived"]==1)]
# print(classes)

# df8 = df[["Survived", "Pclass", "Name", "Sex"]]

# classes = df8[(df8["Pclass"]==3)&(df8["Survived"]==1)]
# print(classes)

# # sorting values
# df = df[["Age", "Name", "Pclass"]]
# df = df.sort_values(by = ["Pclass", "Age"], ascending=True)
# print(df)

# # changing value in the dataset
# df.iloc[1,2] = "Florence Briggs Thayer"
# print(df.iloc[1,2])

# save the data to local to verify changes
# creating a new column in the dataFrame

df["New Fare"] = (df["Fare"]*(1.1)).round(2) #*(df["Pclass"])
print(df)
df.to_csv("newdata.csv")

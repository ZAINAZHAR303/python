import pandas as pd
stu = pd.DataFrame(
    {
        "Name": ["Tom", "nick", "krish", "jack"],
        "Age": [20, 21,9, 18],
        "Marks" : [4,5,5,78],
    }
)

print(stu["Age"].max())

print(stu.describe())

print(stu["Marks"].min())

air = pd.read_csv("air.csv")

print(air.describe()) 


# print(stu["Age"].max())

# print(stu.describe())

# print(stu["Marks"].min())

# air = pd.read_csv("air.csv")

# print(air.describe()) 

# air.agg(
#     {
#     "station_london": ["max","min","skew"]
    
#     }
# )
titanic = pd.read_csv("titanic.csv")
# print(titanic["Name"].str.split("").str.get(1))
print(titanic[titanic["Name"].str.contains("Mr")])

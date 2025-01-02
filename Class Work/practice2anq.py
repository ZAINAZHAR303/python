import pandas as pd


var1=pd.read_csv("Big_Black_Money_Dataset.csv")
#print(var1.head())

#convert into lower case
#print(var1["Country"].str.lower())


#print(var1["Country"].str.contains("zil"))

#replace the text
# print(var1["Country"].replace({
#     "Brazil":"B",
#     "China":"C"
# }))


#check length
print(var1["Country"].str.len())
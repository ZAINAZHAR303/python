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



# var4={
#     "Name": ["Anique", "Ahmad"],
#     "Catogery": ["Software Engineer", "DataScientist", ]
# }

# vari = pd.DataFrame(var4)

# print(vari["Catogery"])




# stu={
#     "name":["anique","ahmad"],
#     "class":["cs","it"],
#     }
# stu1=pd.DataFrame(stu)

# print(stu1["name"][1])

print(var.head())
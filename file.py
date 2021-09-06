import pandas as pd

df = pd.read_csv("stars.csv")
print(df.head())

name = df["Star_name"].tolist()
distance = df["Distance"].tolist()
mass = df["Mass"].tolist()
radius = df["Radius"].tolist()
gravity = df["Gravity"].tolist()

final_star_list = []

temp_dict={}
for i in range(0,len(name)):
  temp_dict["name"] = name[i]
  temp_dict["distance"] = distance[i]
  temp_dict["mass"] = mass[i]
  temp_dict["radius"] = radius[i]
  temp_dict["gravity"] = gravity[i]
  final_star_list.append(temp_dict)
  temp_dict = {}

print(final_star_list)
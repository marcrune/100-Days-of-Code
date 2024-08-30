import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_color = data[["Primary Fur Color", "Unique Squirrel ID"]]
fur_color = fur_color.groupby("Primary Fur Color")["Unique Squirrel ID"].count()
fur_color = pd.DataFrame(fur_color)
fur_color = fur_color.sort_values("Unique Squirrel ID", ascending=False)
fur_color = fur_color.reset_index()
fur_color = fur_color.rename(columns={"Primary Fur Color": "Fur Color", "Unique Squirrel ID": "Count"})
fur_color = fur_color.replace(to_replace=["Black", "Cinnamon", "Gray"], value=["black", "red", "grey"])
print(fur_color)
fur_color.to_csv("fur_color.csv")
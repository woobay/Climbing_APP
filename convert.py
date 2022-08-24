import pandas as pd 


df = pd.read_csv("spots.csv")
df.to_json("newSpots.json")


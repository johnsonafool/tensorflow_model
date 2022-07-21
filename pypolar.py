import polars as pl

# df = pl.DataFrame({'City': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],         'Temperature': [30.5, 32, 25, 38, 40, 29.6, 21.3, 24.9],
#                    'Rain': [103, 125, 90, 75, 130, 200, 155, 127]})

# print(df)


df = pl.read_csv("https://j.mp/iriscsv")
print(df.filter(pl.col("sepal_length") > 5)
      .groupby("species")
      .agg(pl.all().sum())
      )

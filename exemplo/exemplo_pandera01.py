import pandas as pd
import pandera as pa

from pandera import Check, Column, DataFrameSchema

df = pd.DataFrame({
    "column1" : [5, 10, 20],
    "column2" : ['a', 'b', 'c'],
    "column3" : ['2010', '2011', '2012'],
})

schema = pa.infer_schema(df)
print(schema)


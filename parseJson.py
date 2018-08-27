#!/python3
import pandas as pd

url = 'data.json'

# read json data and orient in columns in a DataFrame
df = pd.read_json(url, orient='column')

# change order of columns 
df = df[['Name', 'Position', 'Height', 'Weight','College', 'Year Drafted', 'Year Retired', 'Birthday', 'url']]
df.head(10)
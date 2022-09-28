import pandas as pd

url = 'https://lottery.com/previous-results/il/powerball/2022/'
dfs = pd.read_html(url)
dfs = dfs[0].drop('Unnamed: 4', axis=1)
print(dfs.keys())

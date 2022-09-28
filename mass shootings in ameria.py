import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

df = pd.read_csv('MSDataset.csv', encoding_errors='ignore')
df.Race.fillna('Unknown', inplace=True)
df.Cause.fillna('Unknown', inplace=True)
numBlk = 0
numWyt = 0
numAsi = 0
numLat = 0
numOth = 0
headnum = 322
df = df.head(headnum)
for row in range(len(df)):
    if df.Race[row].find("Black") == 0:
        df.Race[row] = 5
        numBlk += 1
        plt.text(df.Date[df.Race == 5][row],df.Race[df.Race == 5][row],df.Cause[df.Race == 5][row], rotation = -90, ha= 'center', va='bottom', fontsize="7")
    elif df.Race[row].find("White") == 0:
        df.Race[row] = 4
        numWyt += 1
        plt.text(df.Date[df.Race == 4][row],df.Race[df.Race == 4][row],df.Cause[df.Race == 4][row], rotation = -90, ha= 'center', va='bottom', fontsize="7")
    elif df.Race[row].find("Latino") == 0:
        df.Race[row] = 3
        numLat += 1
        plt.text(df.Date[df.Race == 3][row],df.Race[df.Race == 3][row],df.Cause[df.Race == 3][row], rotation = -90, ha= 'center', va='bottom', fontsize="7")
    elif df.Race[row].find("Asian") == 0:
        df.Race[row] = 2
        numAsi += 1
        plt.text(df.Date[df.Race == 2][row],df.Race[df.Race == 2][row],df.Cause[df.Race == 2][row], rotation = -90, ha= 'center', va='bottom', fontsize="7")
    else:
        df.Race[row] = 1
        numOth += 1
        plt.text(df.Date[df.Race == 1][row],df.Race[df.Race == 1][row],df.Cause[df.Race == 1][row], rotation = -90, ha= 'center', va='bottom', fontsize="7")
print(len(df[df.Race == 5][df.Cause == 'racism']))
blu_patch = mpatches.Patch(color="blue", label=f'Black({numBlk})')
red_patch = mpatches.Patch(color='red', label=f'White({numWyt})')
ylw_patch = mpatches.Patch(color='yellow', label=f'Latino({numLat})')
org_patch = mpatches.Patch(color='orange', label=f'Asian({numAsi})')
grn_patch = mpatches.Patch(color='green', label=f'Other({numOth})')
plt.scatter(df.Date[df.Race == 5],df.Race[ df.Race == 5], color = 'blue')
plt.scatter(df.Date[df.Race == 4],df.Race[ df.Race == 4], color = 'red')
plt.scatter(df.Date[df.Race == 3],df.Race[ df.Race == 3], color = 'orange')
plt.scatter(df.Date[df.Race == 2],df.Race[ df.Race == 2], color = 'yellow')
plt.scatter(df.Date[df.Race == 1],df.Race[ df.Race == 1], color = 'green')
plt.xticks(rotation=45)
plt.ylim(0.5, 5.5)
plt.legend(handles=[red_patch, blu_patch,ylw_patch ,org_patch , grn_patch])
plt.title(f"Mass Shootings in US({headnum})")
plt.show()

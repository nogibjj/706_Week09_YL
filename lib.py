import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def describe(df):
    return df.describe()

def getMedian(df):
    return df.median()

def getScatter(csv):
    pd.set_option("display.max_column", None)
    generaldf = pd.read_csv(csv)
    plt.figure(figsize=(7,4))
    a = []
    for i in range(len(generaldf.index)):
        a.append(datetime.strptime(generaldf["Date"][i], "%Y-%m-%d").date())
    generaldf["DateInt"] = a
    df = generaldf.groupby("DateInt").sum()
    df2 = df.reset_index()
    plt.scatter(df2["DateInt"], df2["TotalConfirmed"])
    plt.xlabel("Date")
    plt.ylabel("Total Confirmed")
    plt.show()
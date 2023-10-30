from lib import describe, getMedian, getScatter
import pandas as pd

csv = "https://data.ca.gov/dataset/4a9a896a-e64e-48c2-bb35-5589f80e7c52/resource/5a3f496d-04be-4405-aea0-e83e26076efc/download/covid19dashboard.csv"
data = pd.read_csv(csv)

if __name__ == "__main__":
    res = describe(data)
    print("The descriptive statistics of the data is: ")
    print(res)
    print("The median of total confirmed is: ")
    print(getMedian(data["TotalConfirmed"]))
    print("A scatterplot of total confirmed is below: ")
    getScatter(csv)

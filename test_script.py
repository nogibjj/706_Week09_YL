from lib import describe, getMedian, getScatter
import pandas as pd

def test_main():
    csv = "https://data.ca.gov/dataset/4a9a896a-e64e-48c2-bb35-5589f80e7c52/resource/5a3f496d-04be-4405-aea0-e83e26076efc/download/covid19dashboard.csv"
    data = pd.read_csv(csv)

    describe(data)
    getMedian(data["TotalConfirmed"])
    getScatter(csv)

if __name__ == "__main__":
    test_main()
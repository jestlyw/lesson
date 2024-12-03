import numpy as np
import pandas as pd
cnt_mos = []
cnt_spb = []

data = pd.read_csv("/Users/jstl1/Downloads/organisations.csv")
for index, row in data.iterrows():
    if  row["city"] == "msk" :
        if "30774" in str(row["rubrics_id"]) :
            if row["average_bill"]<= 2500:
                cnt_mos.append(row["average_bill"])
    else:
        if "30774" in str(row["rubrics_id"])\
                :
            if row["average_bill"] <= 2500:
                cnt_spb.append(row["average_bill"])

print(cnt_mos)


print(round(sum(cnt_mos)/len(cnt_mos) - sum(cnt_spb)/len(cnt_spb) ))




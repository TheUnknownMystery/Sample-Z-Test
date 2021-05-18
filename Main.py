import pandas as pd
import statistics as st
import random
import plotly.figure_factory as ff

CSV_File = pd.read_csv("medium_data.csv")
Claps = CSV_File["claps"].tolist()


Population_mean = st.mean(Claps)
Std = st.stdev(Claps)

for a in range(0, 1000):
    All_RandomData = []
    for i in range(0,30):
       RandomNumbers = random.randint(0,len(Claps)-1)
       Data = Claps[RandomNumbers]
       All_RandomData.append(Data)
Sample_Mena = st.mean(All_RandomData)

Z_Socre = (Sample_Mena - Population_mean)/Std

print(Z_Socre)

Fig = ff.create_distplot([Claps], ["Claps Data"],show_hist = False)
Fig.show()
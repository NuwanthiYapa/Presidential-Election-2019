import pandas as pd
import matplotlib.pyplot as plt

pe_dataset = pd.read_csv("pe.csv")

pe_dataset['What is the reason for choosing him?'].fillna('No reason', inplace= True)
pe_dataset['For which party did you vote in last presidential election?'].fillna('No party', inplace= True)

eq = pe_dataset.groupby('What is your highest education qualification?')['Gender'].count()
labels = ['Passed G.C.E. (A/L) Examination','Passed G.C.E. (O/L) Examination','Post Graduated / Professional','Undergraduate']
plt.pie(eq, labels= labels, autopct='%1.1f%%', shadow=True, startangle=140)

eq = pe_dataset.groupby('Who will get the highest vote in next presidential election?')['Gender'].count()
labels = ['General Mahesh Senanayake','Anura Disanayake (NPP)','Gotabhaya Rajapaksha (SLPP)','Sajith Premadasa (UNP)']
plt.pie(eq, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)

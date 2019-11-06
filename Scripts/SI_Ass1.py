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

#Based on education
pprof = [1,5,46,9]
lprof = ['Anura Disanayake (NPP)', 'General Mahesh Senanayake', 'Gotabhaya Rajapaksha (SLPP)', 'Sajith Premadasa (UNP)']
plt.pie(pprof, labels=lprof, autopct='%1.1f%%', shadow=True, startangle=140)

pal = [4,4,18,9]
plt.pie(pal, labels=lprof, autopct='%1.1f%%', shadow=True, startangle=140)

#Based on district
eq = pe_dataset.groupby('District')['Gender'].count()

pdis = [5,11,6,17,14,17,4,4,3,15]
ldis = ['Badulla', 'Colombo','Galle','Gampaha','Hambantota','Kalutara','Kandy','Kegalle','Kurunegala','Matara']
plt.pie(pdis , labels=ldis, autopct='%1.1f%%', shadow=True, startangle=140)

pcol = [9,2]
lcol = ['Gotabhaya Rajapaksha (SLPP)', 'Sajith Premadasa (UNP)']
plt.pie(pcol, labels=lcol, autopct='%1.1f%%', shadow=True, startangle=140)

pgam = [1,11,5]
lgam = ['Anura Disanayake (NPP)', 'Gotabhaya Rajapaksha (SLPP)', 'Sajith Premadasa (UNP)']
plt.pie(pgam, labels=lgam, autopct='%1.1f%%', shadow=True, startangle=140)

pkal = [3,11,3]
lkal = ['General Mahesh Senanayake', 'Gotabhaya Rajapaksha (SLPP)', 'Sajith Premadasa (UNP)']
plt.pie(pkal, labels=lkal, autopct='%1.1f%%', shadow=True, startangle=140)

pham = [1,9,4]
lham = ['General Mahesh Senanayake', 'Gotabhaya Rajapaksha (SLPP)', 'Sajith Premadasa (UNP)']
plt.pie(pham, labels=lham, autopct='%1.1f%%', shadow=True, startangle=140)

pmat = [2,4,9]
lmat = ['Anura Disanayake (NPP)','General Mahesh Senanayake', 'Gotabhaya Rajapaksha (SLPP)']
plt.pie(pmat, labels=lmat, autopct='%1.1f%%', shadow=True, startangle=140)

#Based on gender
eq = pe_dataset.groupby('Gender')['Gender'].count()

plt.pie(eq, labels=['Female','Male'], autopct='%1.1f%%', shadow=True, startangle=140)

pmale = [4,3,43,11]
lmale = ['Anura Disanayake (NPP)','General Mahesh Senanayake', 'Gotabhaya Rajapaksha (SLPP)','Sajith Premadasa (UNP)']
plt.pie(pmale, labels=lmale, autopct='%1.1f%%', shadow=True, startangle=140)

pfem = [2,7,26,8]
lfem = ['Anura Disanayake (NPP)','General Mahesh Senanayake', 'Gotabhaya Rajapaksha (SLPP)','Sajith Premadasa (UNP)']
plt.pie(pfem, labels=lfem, autopct='%1.1f%%', shadow=True, startangle=140)

#Based on occupation
eq = pe_dataset.groupby('What is your occupation?')['Gender'].count()

ppri = [1,5,37,11]
lpri = ['Anura Disanayake (NPP)','General Mahesh Senanayake', 'Gotabhaya Rajapaksha (SLPP)','Sajith Premadasa (UNP)']
plt.pie(ppri, labels=lpri, autopct='%1.1f%%', shadow=True, startangle=140)

pgov = [3,1,14,6]
lgov = ['Anura Disanayake (NPP)','General Mahesh Senanayake', 'Gotabhaya Rajapaksha (SLPP)','Sajith Premadasa (UNP)']
plt.pie(pgov, labels=lgov, autopct='%1.1f%%', shadow=True, startangle=140)

pstu = [1,2,13,2]
lstu = ['Anura Disanayake (NPP)','General Mahesh Senanayake', 'Gotabhaya Rajapaksha (SLPP)','Sajith Premadasa (UNP)']
plt.pie(pstu, labels=lstu, autopct='%1.1f%%', shadow=True, startangle=140)

#Based on Age group
eq = pe_dataset.groupby('Age Group')['Gender'].count()

lagegrp = ['18 -25','26 - 35', '36 - 45', '46 - 55']
plt.pie(eq, labels=lagegrp, autopct='%1.1f%%', shadow=True, startangle=140)

p1 = [3,19,1]
l1 = ['General Mahesh Senanayake', 'Gotabhaya Rajapaksha (SLPP)','Sajith Premadasa (UNP)']
plt.pie(p1, labels=l1, autopct='%1.1f%%', shadow=True, startangle=140)

p2 = [3,6,42,15]
l2 = ['Anura Disanayake (NPP)','General Mahesh Senanayake', 'Gotabhaya Rajapaksha (SLPP)','Sajith Premadasa (UNP)']
plt.pie(p2, labels=l2, autopct='%1.1f%%', shadow=True, startangle=140)

p3 = [3,1,5,3]
l3 = ['Anura Disanayake (NPP)','General Mahesh Senanayake', 'Gotabhaya Rajapaksha (SLPP)','Sajith Premadasa (UNP)']
plt.pie(p3, labels=l3, autopct='%1.1f%%', shadow=True, startangle=140)
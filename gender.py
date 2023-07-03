import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv('data.csv')
male=data['Gender'].str.contains('Male').sum()
female=data['Gender'].str.contains('Female').sum()

labels = 'Male','Female'
sizes = [male,female]
explode = ( 0, 0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

prefer_to_try=data.groupby(['prefer to try new things','Gender'])['Gender','prefer to try new things'].count()
print(prefer_to_try)

prefer_to_try.plot.pie(subplots=True)
prefer_to_try.plot.bar(subplots=True)

plt.show()
why_like=data.groupby(['why do you like your idol','Gender'])['Gender','why do you like your idol'].count()
print(why_like)

why_like.plot.pie(subplots=True)

why_like.plot.bar(subplots=True)
plt.show()
like_to_introduce=data.groupby(['would you like to introduce your idols to others?','Gender'])['Gender','would you like to introduce your idols to others?'].count()
print(like_to_introduce)

like_to_introduce.plot.pie(subplots=True)

like_to_introduce.plot.bar(subplots=True)
plt.show()


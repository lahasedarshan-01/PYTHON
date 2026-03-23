import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Company': ['Microsoft', 'Google', 'Amazon', 'IBM', 'Deloitte', 'Capgemini', 'ATOS', 'Amdocs'],
    'Recruitments': [120, 150, 180, 90, 110, 130, 70, 100]
}

df = pd.DataFrame(data)

plt.figure()
plt.bar(df['Company'], df['Recruitments'])
plt.title("Company Recruitments - Bar Chart")
plt.xlabel("Company")
plt.ylabel("Recruitments")
plt.show()

plt.figure()
plt.pie(df['Recruitments'], labels=df['Company'], autopct='%1.1f%%')
plt.title("Company Recruitments - Pie Chart")
plt.show()

plt.figure()
plt.pie(df['Recruitments'], labels=df['Company'], autopct='%1.1f%%', explode=[0.1,0,0,0,0,0,0,0])
plt.title("Customized Pie Chart")
plt.show()

plt.figure()
plt.pie(df['Recruitments'], labels=df['Company'], wedgeprops=dict(width=0.4), autopct='%1.1f%%')
plt.title("Doughnut Chart")
plt.show()

compare = df[df['Company'].isin(['IBM', 'Amdocs'])]

plt.figure()
plt.bar(compare['Company'], compare['Recruitments'])
plt.title("IBM vs Amdocs Recruitments")
plt.xlabel("Company")
plt.ylabel("Recruitments")
plt.show()
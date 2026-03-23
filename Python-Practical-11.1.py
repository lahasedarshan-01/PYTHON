import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sales_data.csv")

plt.figure()
plt.plot(data['month'], data['total_profit'], color='blue', marker='o')
plt.title("Total Profit per Month")
plt.xlabel("Month")
plt.ylabel("Total Profit")
plt.show()

plt.figure()
plt.plot(data['month'], data['facecream'], label='Face Cream')
plt.plot(data['month'], data['facewash'], label='Face Wash')
plt.plot(data['month'], data['toothpaste'], label='Toothpaste')
plt.plot(data['month'], data['bathingsoap'], label='Bathing Soap')
plt.plot(data['month'], data['shampoo'], label='Shampoo')
plt.plot(data['month'], data['moisturizer'], label='Moisturizer')
plt.title("Product Sales Data")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.show()

plt.figure()
plt.bar(data['month'], data['facecream'], label='Face Cream')
plt.bar(data['month'], data['facewash'], label='Face Wash')
plt.title("Face Cream and Face Wash Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.show()

total_sales = [
    data['facecream'].sum(),
    data['facewash'].sum(),
    data['toothpaste'].sum(),
    data['bathingsoap'].sum(),
    data['shampoo'].sum(),
    data['moisturizer'].sum()
]

labels = ['Face Cream', 'Face Wash', 'Toothpaste', 'Bathing Soap', 'Shampoo', 'Moisturizer']

plt.figure()
plt.pie(total_sales, labels=labels, autopct='%1.1f%%')
plt.title("Yearly Sales Distribution")
plt.show()
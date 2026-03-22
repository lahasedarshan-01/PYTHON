import pandas as pd

df = pd.read_csv("books.csv")

print("Complete Report:")
print(df)

author_name = input("Enter author name: ")
print("Books by author:")
print(df[df['author'] == author_name])

publisher_name = input("Enter publisher name: ")
print("Books by publisher:")
print(df[df['publisher'] == publisher_name])

costliest = df.loc[df['price'].idxmax()]
print("Costliest Book:")
print(costliest['title'])

sorted_books = df.sort_values(by='year')
print("Books sorted by year:")
print(sorted_books[['title', 'year']])
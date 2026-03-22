import pandas as pd

data = {
    'State': ['Maharashtra', 'Gujarat', 'Karnataka', 'Rajasthan', 'Punjab'],
    'Area': [307713, 196244, 191791, 342239, 50362],
    'Population': [112374333, 60439692, 61095297, 68548437, 27743338]
}

df = pd.DataFrame(data)

print("Complete State Information:")
print(df)

largest_area_state = df.loc[df['Area'].idxmax()]
print("State with largest area:")
print(largest_area_state['State'])

largest_population_state = df.loc[df['Population'].idxmax()]
print("State with largest population:")
print(largest_population_state['State'])

df['Density'] = df['Population'] / df['Area']

highest_density_state = df.loc[df['Density'].idxmax()]
print("State with highest population density:")
print(highest_density_state['State'])
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.write('VIOLIN PLOTS')


data = pd.read_csv('gapminder_with_codes.csv.xls')


data_2007=data[data['year']==2007]


lifexp = data_2007['lifeExp']
population = data_2007['pop']
gdp = data_2007['gdpPercap']


#GDP
# Create a violin plot
sns.violinplot(y = data_2007["gdpPercap"])

# Add labels and title
plt.title("Distribution of GDP per capita")
plt.ylabel("GDP per capita")

# Show plot
plt.show()



#   Population
# Create a violin plot
sns.violinplot(y = data_2007["pop"])

# Add labels and title
plt.title("Distribution of Population")
plt.ylabel("Population")

# Show plot
plt.show()


#life expectancy
sns.violinplot(y = data_2007["lifeExp"])

# Add labels and title
plt.title("Life Expectancy Distribution")
plt.ylabel("Life Expectancy")

# Show plot
plt.show()
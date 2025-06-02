import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score,mean_absolute_error


df = pd.read_csv("COVID-19 Dataset.csv")
print(df.head())

print("Dataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe(include='all'))

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

#  Convert date column to datetime
df['Date'] = pd.to_datetime(df['Date'])


#  Ensure all numeric fields are properly typed
numeric_columns = [
    'Confirmed', 'Deaths', 'Recovered', 'Active_Cases', 'CFR', 'Recovery_Rate',
    'Vaccination_Rate', 'People_Vaccinated', 'People_Fully_Vaccinated',
    'Total_vaccinations', 'Tests_Performed', 'Test_Positivity_Rate'
]
print(df[numeric_columns].dtypes)


# 📈 Global COVID-19 Trends Over Time
daily_trends = df.groupby('Date')[['Confirmed', 'Deaths', 'Recovered']].sum()

plt.figure(figsize=(10,6))
plt.scatter(daily_trends.index, daily_trends['Confirmed'], color='blue', label='Confirmed', s=10)
plt.scatter(daily_trends.index, daily_trends['Deaths'], color='red', label='Deaths', s=10)
plt.scatter(daily_trends.index, daily_trends['Recovered'], color='green', label='Recovered', s=10)
plt.title('Global COVID-19 Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.xticks(rotation=45)
plt.show()


# 🌍 Top 10 Countries by People Fully Vaccinated
latest_vax = df.sort_values('Date').groupby('Country/Region')['People_Fully_Vaccinated'].last().dropna()

# Plot with Seaborn graph
plt.figure(figsize=(10,6))
sns.barplot(
    x=latest_vax.sort_values(ascending=False).index,
    y=latest_vax.sort_values(ascending=False).values,
    palette='viridis'
)
plt.title('Top 10 Countries - People Fully Vaccinated')
plt.ylabel('Number of People Fully Vaccinated', fontsize=14)
plt.xlabel('Country', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=12)
plt.tight_layout()
sns.despine()
plt.show()

# 🏆 Top 5 Countries by Confirmed Cases (Pie Chart with Attractive Colors)
top_countries = df.groupby('Country/Region')['Confirmed'].max().sort_values(ascending=False).head(5)

plt.figure(figsize=(8,6))
colors = sns.color_palette('pastel', n_colors=5)
plt.pie(
    top_countries,
    labels=top_countries.index,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    wedgeprops={'edgecolor': 'black', 'linewidth': 1}
)
plt.title('Top 5 Countries by Confirmed Cases (Pie Chart)')
plt.tight_layout()
plt.show()

# 💀 Top 5 Countries by Death Rate
df['Death Rate'] = df['Deaths'] / df['Confirmed']
death_rate = df.groupby('Country/Region')['Death Rate'].max().sort_values(ascending=False).head(5)

plt.figure(figsize=(10,6))
sns.barplot(
    x=death_rate.index,
    y=death_rate.values,
    palette='Reds_r'
)
plt.title('Top 5 Countries by Death Rate (Bar Chart)')
plt.ylabel('Death Rate', fontsize=14)
plt.xlabel('Country', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=12)
plt.tight_layout()
sns.despine()
plt.show()


# --- Linear Regression: Predicting Deaths from Confirmed Cases ---

# Prepare data: drop rows with missing values in relevant columns
reg_df = df[['Confirmed', 'Deaths']].dropna()
X = reg_df[['Confirmed']]
y = reg_df['Deaths']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

plt.figure(figsize=(10,7))
sns.set(style="whitegrid", font_scale=1.2)
plt.scatter(X_test, y_test, alpha=0.6, color="#4a2dd9", label='Actual', s=60, edgecolor='k')
plt.scatter(X_test, y_pred, alpha=0.7, color="#e6b522", label='Predicted', s=60, marker='x')
plt.xlabel('Confirmed Cases', fontsize=14, fontweight='bold')
plt.ylabel('Deaths', fontsize=14, fontweight='bold')
plt.title('Linear Regression: Actual vs Predicted Deaths', fontsize=16, fontweight='bold')
plt.legend(fontsize=12, frameon=True, shadow=True)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
sns.despine()
plt.show()

# Print model coefficients and performance
print("Linear Regression Results:")
print(f"Intercept:", model.intercept_)
print(f"Coefficient for Confirmed:", model.coef_[0])
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))


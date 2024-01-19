import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from getpass import getpass
#from admin_menu import view_all_data
import mysql.connector
from tabulate import tabulate

host = "localhost"
user = "root"
password = "Goutham@3007"
database="rev"

conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

cursor = conn.cursor()
# Sample data
main_data = {
    'data_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Text': ['Enjoying a beautiful day at the park!', 'Traffic was terrible this morning.', 'Just finished an amazing workout!',
             'Excited about the upcoming weekend getaway!', 'Trying out a new recipe for dinner tonight.', 'Feeling grateful for the little things in life.',
             'Rainy days call for cozy blankets and hot cocoa.', 'The new movie release is a must-watch!', 'Political discussions heating up on the timeline.',
             'Missing summer vibes and beach days.'],
    'Platform_id': [1, 1, 2, 3, 2, 1, 3, 2, 1, 3],
    'Sentiment_id': [0, 1, 0, 0, 2, 0, 0, 0, 1, 2],
    'Categories_id': [1, 2, 3, 2, 5, 2, 1, 7, 5, 1],
    'Country_id': [1, 2, 1, 3, 4, 5, 2, 1, 4, 3],
    'Retweets': [15, 10, 40, 15, 25, 50, 20, 30, 60, 35],
    'Likes': [30, 10, 40, 15, 25, 50, 20, 30, 60, 35],
    'Year': [2023] * 10,
    'Month': [1] * 10,
    'Day': [15, 15, 15, 15, 15, 16, 16, 16, 17, 17],
    'Hour': [12, 8, 15, 18, 19, 9, 14, 19, 8, 12]
}

categories_data = {
    'categories_id': [1, 2, 3, 4, 5, 6, 7],
    'categories': ['Nature', 'Travel', 'Fitness', 'Emotion', 'Food', 'Technology', 'Social']
}

country_data = {
    'country_id': [1, 2, 3, 4, 5],
    'country': ['USA', 'Canada', 'UK', 'Australia', 'India']
}

platform_data = {
    'Platform_id': [1, 2, 3],
    'Platform': ['Twitter', 'Instagram', 'Facebook']
}

# Create dataframes
main_df = pd.DataFrame(main_data)
categories_df = pd.DataFrame(categories_data)
country_df = pd.DataFrame(country_data)
platform_df = pd.DataFrame(platform_data)

# Merge dataframes
merged_df = pd.merge(main_df, categories_df, how='left', left_on='Categories_id', right_on='categories_id')
merged_df = pd.merge(merged_df, country_df, how='left', left_on='Country_id', right_on='country_id')
merged_df = pd.merge(merged_df, platform_df, how='left', left_on='Platform_id', right_on='Platform_id')

# Visualization
plt.figure(figsize=(12, 8))


def view_all_data():
    query ="select * from main_table"
    with conn.cursor(dictionary=True) as cursor:
        cursor.execute(query)
        result=cursor.fetchall()
        
        if not result:
            print("No data")
        data_tuples=[(row['data_id'],row['Text'],row['Platform_id'],row['Sentiment_id'],row['Categories_id'],row['Country_id'],row['Retweets'],row['Likes'],row['Year'],row['Month'],row['Day'],row['Hour'])for row in result]
        headers=result[0].keys()
        print(tabulate(data_tuples,headers=headers,tablefmt="pretty"))







def user_menu():
    #username=input("Enter the username :")
    #password=getpass("Enter the password :")
    while True:
        print("\n User menu")
        print("1. View overall main table :")
        print("2. Bar plot for Categories")
        print("3. Distribution of Posts by Country")
        print("4. Retweets and Likes Over Hours")
        print("5. Sentiment vs. Likes")

        choice=input("Enter the choice :")
        if choice=="1":
            view_all_data()
            
        elif choice=="2":
            # Example 1: Bar plot for Categories
            plt.subplot(2, 2, 1)
            sns.countplot(x='categories', data=merged_df)
            plt.title('Number of Posts in Each Category')
            plt.show()
            
        elif choice=="3":
            # Example 2: Pie chart for Country distribution
            plt.subplot(2, 2, 2)
            merged_df['country'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
            plt.title('Distribution of Posts by Country')
            plt.show()
            
        elif choice=="4":
            # Example 3: Line plot for Retweets and Likes
            plt.subplot(2, 2, 3)
            sns.lineplot(x='Hour', y='Retweets', data=merged_df, label='Retweets')
            sns.lineplot(x='Hour', y='Likes', data=merged_df, label='Likes')
            plt.title('Retweets and Likes Over Hours')
            plt.show()
            
        elif choice=="5":
            # Example 4: Scatter plot for Sentiment vs. Likes
            plt.subplot(2, 2, 4)
            sns.scatterplot(x='Sentiment_id', y='Likes', data=merged_df)
            plt.title('Sentiment vs. Likes')
            plt.tight_layout()
            plt.show()
            
        else:
            print("Invalid")
            break
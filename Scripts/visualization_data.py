import matplotlib.pyplot as plt
import seaborn as sns



def visual_distribution_target_value(data):
    plt.figure(figsize=(8, 6))
    sns.histplot(data["Rating"],kde=True,color= "purple",bins=30)
    plt.title("Distribution of movies ratings")
    plt.ylabel("Frequence")
    plt.xlabel("Ratings")
    plt.show()
def visual_numerical_feature(data):
    plt.figure(figsize=(8, 6))
    sns.histplot(data['Duration'], kde=True, color='orange', bins=30)
    plt.title('Distribution of Movie Durations')
    plt.xlabel('Duration (minutes)')
    plt.ylabel('Frequency')
    plt.show()

def votes_rating(data):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=data['Votes'], y=data['Rating'], alpha=0.5, color='green')
    plt.title('Votes vs. Rating')
    plt.xlabel('Votes')
    plt.ylabel('Rating')
    plt.show()

def top_genre_movies(data):
    plt.figure(figsize=(12, 15))
    top_Genre = data['Genre'].value_counts().head(10)
    sns.countplot(y=data['Genre'], order=top_Genre.index, palette='viridis')
    plt.title('Count of Movies by Genre')
    plt.xlabel('Count')
    plt.ylabel('Genre')
    plt.show()

def top_directors(data):
    top_directors = data['Director'].value_counts().head(10)
    top_directors.plot(kind='bar', figsize=(10, 6), color='coral')
    plt.title('Top 10 Directors by Movie Count')
    plt.xlabel('Director')
    plt.ylabel('Number of Movies')
    plt.show()


def correlation(data):
    plt.figure(figsize=(8, 6))
    correlation = data.select_dtypes(include='number').corr()
    sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix')
    plt.show()

def actual_prediction(y_test,y_pred):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=y_test, y=y_pred, alpha=0.6, color='blue')
    plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--', linewidth=2)
    plt.title('Actual vs. Predicted Ratings')
    plt.xlabel('Actual Ratings')
    plt.ylabel('Predicted Ratings')
    plt.show()
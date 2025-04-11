# Task 4 - Recommendation System
# Created by: Nigar Fathima
# CodSoft AI Internship

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = {
    'title': ['Inception', 'The Dark Knight', 'Interstellar', 'The Prestige', 'Memento'],
    'genre': ['Action Sci-Fi', 'Action Crime Drama', 'Adventure Drama Sci-Fi', 'Drama Mystery Sci-Fi', 'Mystery Thriller']
}

df = pd.DataFrame(movies)
cv = CountVectorizer()
count_matrix = cv.fit_transform(df['genre'])
similarity = cosine_similarity(count_matrix)

def recommend(movie_title):
    if movie_title not in df['title'].values:
        print("Movie not found!")
        return
    idx = df[df.title == movie_title].index[0]
    scores = list(enumerate(similarity[idx]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:]
    
    print(f"Movies similar to '{movie_title}':")
    for i in sorted_scores:
        print(df.iloc[i[0]].title)

# Test the recommendation
recommend("Inception")

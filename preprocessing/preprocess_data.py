import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import os
import json

# Path to the raw data
RAW_DATA_DIR = 'data/raw_data/'

# Load data function
def load_data():
    viewed_data = pd.read_json(os.path.join(RAW_DATA_DIR, 'viewed_posts.json'))
    liked_data = pd.read_json(os.path.join(RAW_DATA_DIR, 'liked_posts.json'))
    inspired_data = pd.read_json(os.path.join(RAW_DATA_DIR, 'inspired_posts.json'))
    rated_data = pd.read_json(os.path.join(RAW_DATA_DIR, 'rated_posts.json'))
    summary_data = pd.read_json(os.path.join(RAW_DATA_DIR, 'all_posts_summary.json'))
    return viewed_data, liked_data, inspired_data, rated_data, summary_data

# Handle missing values function
def handle_missing_values(df):
    df = df.dropna(subset=['id', 'username'])  # Use 'id' for post and 'username' for user
    df['average_rating'] = df['average_rating'].fillna(df['average_rating'].median())  # Handle missing ratings
    df['view_count'] = df['view_count'].fillna(0)  # Handle missing views
    df['upvote_count'] = df['upvote_count'].fillna(0)  # Handle missing upvote_count
    df['rating_count'] = df['rating_count'].fillna(0)  # Handle missing rating_count
    return df

# Normalize data function
def normalize_data(df, columns_to_normalize):
    scaler = MinMaxScaler()
    df[columns_to_normalize] = scaler.fit_transform(df[columns_to_normalize])
    return df

# Feature engineering function
def create_features(df):
    # Create an 'interaction_count' as sum of views, ratings, and upvotes
    df['interaction_count'] = df['view_count'] + df['rating_count'] + df['upvote_count']
    # Calculate the user's average rating
    user_avg_rating = df.groupby('username')['average_rating'].mean()
    df['user_avg_rating'] = df['username'].map(user_avg_rating)
    return df

# Merge data function
def merge_data(viewed, liked, inspired, rated):
    merged_df = pd.concat([viewed[['username', 'id', 'interaction_count', 'user_avg_rating']],
                           liked[['username', 'id', 'interaction_count', 'user_avg_rating']],
                           inspired[['username', 'id', 'interaction_count', 'user_avg_rating']],
                           rated[['username', 'id', 'interaction_count', 'user_avg_rating']]], ignore_index=True)
    return merged_df

# Run preprocessing
def preprocess_data():
    # Load data
    viewed, liked, inspired, rated, summary = load_data()
    
    # Handle missing values
    viewed = handle_missing_values(viewed)
    liked = handle_missing_values(liked)
    inspired = handle_missing_values(inspired)
    rated = handle_missing_values(rated)
    
    # Normalize numerical columns
    columns_to_normalize = ['average_rating', 'view_count', 'upvote_count', 'rating_count']
    viewed = normalize_data(viewed, columns_to_normalize)
    liked = normalize_data(liked, columns_to_normalize)
    inspired = normalize_data(inspired, columns_to_normalize)
    rated = normalize_data(rated, columns_to_normalize)
    
    # Feature engineering
    viewed = create_features(viewed)
    liked = create_features(liked)
    inspired = create_features(inspired)
    rated = create_features(rated)
    
    # Merge all data
    merged_data = merge_data(viewed, liked, inspired, rated)
    
    return merged_data

# Preprocess and get final data
final_data = preprocess_data()

# Output the processed data to verify
print(final_data.head())
final_data.to_json('final_preprocessed_data.json', orient='records', lines=True)
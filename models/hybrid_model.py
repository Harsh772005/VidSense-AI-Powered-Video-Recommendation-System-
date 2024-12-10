import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load the data
final_data = pd.read_json(r"data\preprocessd_data\final_preprocessed_data.json")

# Rename 'username' to 'user_id' for consistency with collaborative filtering
final_data.rename(columns={'username': 'user_id'}, inplace=True)

# Content-based filtering function (as implemented earlier)
def get_content_based_recommendations(video_id, top_n=10):
    # Extract features from the final preprocessed data
    content_features = final_data[['interaction_count', 'user_avg_rating']]
    
    # Compute the similarity matrix using cosine similarity
    content_similarity_matrix = cosine_similarity(content_features)
    
    # Get the index of the video in the dataset
    video_index = final_data[final_data['id'] == video_id].index[0]
    
    # Get the similarity scores for the given video
    similarity_scores = content_similarity_matrix[video_index]
    
    # Get the indices of the top N most similar videos
    similar_video_indices = similarity_scores.argsort()[-top_n-1:-1][::-1]
    
    # Get the IDs of the most similar videos
    similar_video_ids = final_data.iloc[similar_video_indices]['id'].values
    
    return similar_video_ids

# Collaborative filtering function (as implemented earlier)
def get_collaborative_recommendations(user_id, top_n=5):
    # Create a user-item interaction matrix
    user_item_matrix = final_data.pivot_table(index='user_id', columns='id', values='interaction_count', fill_value=0)
    
    # Compute cosine similarity between users
    user_similarity_matrix = cosine_similarity(user_item_matrix)
    
    # Get the index of the user
    user_index = user_item_matrix.index.get_loc(user_id)
    
    # Get similarity scores
    similarity_scores = user_similarity_matrix[user_index]
    
    # Get the top N most similar users
    similar_user_indices = similarity_scores.argsort()[-top_n-1:-1][::-1]
    similar_user_ids = user_item_matrix.index[similar_user_indices]
    
    # Get the recommended videos for similar users
    recommendations = user_item_matrix.loc[similar_user_ids].mean(axis=0)
    
    # Get top N recommended videos
    recommended_video_ids = recommendations.sort_values(ascending=False).head(top_n).index.values
    return recommended_video_ids

# Hybrid recommendation system
def get_hybrid_recommendations(user_id, video_id, top_n=5, content_weight=0.5, collaborative_weight=0.5):
    # Get content-based recommendations
    content_based_recommendations = get_content_based_recommendations(video_id, top_n)
    
    # Get collaborative filtering recommendations
    collaborative_recommendations = get_collaborative_recommendations(user_id, top_n)
    
    # Combine both recommendations by weighted average
    combined_recommendations = {}
    
    # Assign weights to content-based recommendations
    for video in content_based_recommendations:
        combined_recommendations[video] = content_weight
    
    # Assign weights to collaborative filtering recommendations, adding to existing ones if already present
    for video in collaborative_recommendations:
        if video not in combined_recommendations:
            combined_recommendations[video] = collaborative_weight
        else:
            combined_recommendations[video] += collaborative_weight
    
    # Sort by combined recommendation score
    sorted_recommendations = sorted(combined_recommendations.items(), key=lambda x: x[1], reverse=True)
    
    # Return the top N recommended videos
    top_recommended_videos = [video[0] for video in sorted_recommendations[:top_n]]
    return top_recommended_videos

# Example: Get hybrid recommendations for user_id 'bloomscroller' and video_id 1386
user_id = 'bloomscroller'  # Example user_id
video_id = 1386  # Example video_id
hybrid_recommendations = get_hybrid_recommendations(user_id, video_id)
print("Hybrid Recommendations:", hybrid_recommendations)

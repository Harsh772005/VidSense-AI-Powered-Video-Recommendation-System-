import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load the preprocessed data from the JSON file
preprocessed_data_path = r'data\preprocessd_data\final_preprocessed_data.json'
final_data = pd.read_json(preprocessed_data_path)

# Step 1: Create a User-Item Interaction Matrix (use 'username' instead of 'user_id')
user_item_matrix = final_data.pivot_table(index='username', columns='id', values='interaction_count', fill_value=0)

# Step 2: Compute User Similarity Matrix using Cosine Similarity
user_similarity_matrix = cosine_similarity(user_item_matrix)

# Convert similarity matrix to DataFrame for easy access
user_similarity_df = pd.DataFrame(user_similarity_matrix, index=user_item_matrix.index, columns=user_item_matrix.index)

# Function to recommend top N videos for a given user_id (username) based on user similarity
def get_collaborative_recommendations(username, top_n=10):
    # Get the most similar users to the given username
    similar_users = user_similarity_df[username].sort_values(ascending=False)[1:top_n+1].index
    
    # Get the videos that similar users have interacted with, weighted by similarity
    recommended_videos = []
    
    for similar_user in similar_users:
        # Get the videos liked by the similar user
        user_data = final_data[final_data['username'] == similar_user]
        
        # Filter out videos the current user has already interacted with
        user_data = user_data[~user_data['id'].isin(final_data[final_data['username'] == username]['id'])]
        
        # Weight the interactions by user similarity
        user_data['weighted_interaction'] = user_data['interaction_count'] * user_similarity_df[username][similar_user]
        
        # Append the weighted interaction values
        recommended_videos.append(user_data[['id', 'weighted_interaction']])
    
    # Combine the recommendations
    all_recommendations = pd.concat(recommended_videos)
    
    # Group by video id and sum the weighted interaction values
    video_scores = all_recommendations.groupby('id')['weighted_interaction'].sum().sort_values(ascending=False)
    
    # Return the top N recommended video IDs
    top_recommended_videos = video_scores.head(top_n).index.values
    return top_recommended_videos

# Example: Get recommendations for a user with username = 'bloomscroller'
collaborative_recommendations = get_collaborative_recommendations('bloomscroller')
print("Collaborative Filtering Recommendations:", collaborative_recommendations)

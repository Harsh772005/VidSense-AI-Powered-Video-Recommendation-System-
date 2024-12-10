from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


preprocessed_data_path = r'data\preprocessd_data\final_preprocessed_data.json'
final_data = pd.read_json(preprocessed_data_path)

content_features = final_data[['interaction_count', 'user_avg_rating']]

# Compute the similarity matrix using cosine similarity
content_similarity_matrix = cosine_similarity(content_features)

# Function to recommend top N similar videos based on a given video index
def get_content_based_recommendations(video_id, top_n=10):
    # Get the index of the video in the dataset
    video_index = final_data[final_data['id'] == video_id].index[0]
    
    # Get the similarity scores for the given video
    similarity_scores = content_similarity_matrix[video_index]
    
    # Get the indices of the top N most similar videos
    similar_video_indices = similarity_scores.argsort()[-top_n-1:-1][::-1]
    
    # Get the IDs of the most similar videos
    similar_video_ids = final_data.iloc[similar_video_indices]['id'].values
    return similar_video_ids

# Example: Get recommendations for a video with id = 1386
content_based_recommendations = get_content_based_recommendations(1214)
print("Content-based Recommendations:", content_based_recommendations)
# Input = 1386 and recommend [1694 1396 1374 1380 1372]
# Input = 1642 and recommend [2099 1447 1506 1532 2200]
# Input = 814 and recommend [1364   11  948  641  774]
# Input = 1214 and recommend [  16 1258  773  702   59]

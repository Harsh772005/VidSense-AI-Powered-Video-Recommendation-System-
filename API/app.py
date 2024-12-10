# import sys
# import os

# # Add the parent directory to sys.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from flask import Flask, request, jsonify
# from models.hybrid_model import get_hybrid_recommendations
# from models.content_based import get_content_based_recommendations
# from models.collaborative_filtering import get_collaborative_recommendations

# app = Flask(__name__)

# # Helper function to generate recommendations
# def generate_recommendations(username=None, category_id=None, mood=None, top_n=10):
#     if username and category_id and mood:
#         # Use hybrid recommendations with all inputs
#         return get_hybrid_recommendations(username, video_id=None, top_n=top_n)
#     elif username and category_id:
#         # Use content-based recommendations with category context
#         return get_content_based_recommendations(video_id=category_id, top_n=top_n)
#     elif username:
#         # Use collaborative filtering for user-specific recommendations
#         return get_collaborative_recommendations(username, top_n=top_n)
#     else:
#         return []

# # API endpoint 1: Recommendations by username, category_id, and mood
# @app.route('/feed', methods=['GET'])
# def get_feed():
#     username = request.args.get('username')
#     category_id = request.args.get('category_id')
#     mood = request.args.get('mood')

#     if not username:
#         return jsonify({"error": "username is required"}), 400

#     recommendations = generate_recommendations(username, category_id, mood)
#     return jsonify({"recommendations": recommendations[:10]})  # Limit to 10 results

# if __name__ == '__main__':
#     app.run(port=5000, debug=True)
















from flask import Flask, request, jsonify
import numpy as np
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.hybrid_model import get_hybrid_recommendations
from models.content_based import get_content_based_recommendations
from models.collaborative_filtering import get_collaborative_recommendations

app = Flask(__name__)

@app.route('/feed', methods=['GET'])
def get_feed():
    username = request.args.get('username')
    category_id = request.args.get('category_id', None)
    mood = request.args.get('mood', None)
    
    # Retrieve recommendations
    if category_id and mood:
        recommendations = get_hybrid_recommendations(username, category_id, mood)
    elif category_id:
        recommendations = get_collaborative_recommendations(username, category_id)
    elif mood:
        recommendations = get_content_based_recommendations(username, mood)
    else:
        recommendations = get_collaborative_recommendations(username)
    
    # Convert recommendations to a list if they're in ndarray format
    recommendations = recommendations.tolist() if isinstance(recommendations, np.ndarray) else recommendations
    
    # Return the recommendations in JSON format
    return jsonify({"recommendations": recommendations[:10]})  # Limit to 10 results

if __name__ == '__main__':
    app.run(debug=True)

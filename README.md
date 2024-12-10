# Video Recommendation System

This project implements a personalized video recommendation system using Flask. It recommends videos based on user preferences and interaction data, integrating content-based, collaborative filtering, and hybrid models to suggest the best possible videos.

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Data Preprocessing](#data-preprocessing)
- [Algorithm Selection](#algorithm-selection)
- [Evaluation Metrics](#evaluation-metrics)
- [Testing](#testing)
- [License](#license)

## Project Overview

The project provides a recommendation system to suggest videos to users based on their past interactions (like, view, rate, and inspire). The goal is to use content-based filtering, collaborative filtering, and hybrid models to provide personalized video recommendations.

### Key Features:
- Personalized video recommendations based on the user’s historical interactions.
- API endpoints that accept parameters such as `username`, `category_id`, and `mood` to provide tailored recommendations.
- Solves the "cold start problem" for new users by leveraging mood data.
- Incorporates both content-based and collaborative filtering approaches.

## Technologies Used

- **Flask**: Python web framework used for developing the API.
- **Python 3.x**: Programming language used for development.
- **pandas, numpy**: Libraries used for data preprocessing and feature engineering.
- **sklearn**: Used for implementing collaborative filtering models.
- **requests**: For making API calls to fetch video metadata.
- **JSON**: Data format for interaction data and video metadata.

## Project Structure

```plaintext
video-recommendation-system/
│
├── api/
│   └── app.py  # Flask API entry point
│
├── data/
│   ├── preprocessd_data/
│   │   └── final_preprocessed_data.json  # Final preprocessed data for recommendation
│   └── raw_data/
│       ├── all_posts_summary.json
│       ├── inspired_posts.json
│       ├── liked_posts.json
│       ├── rated_posts.json
│       └── viewed_posts.json  # Raw video metadata and interaction data
│
├── models/
│   ├── __init__.py  # Makes 'models' a package
│   ├── collaborative_filtering.py  # Collaborative filtering model
│   ├── content_based.py  # Content-based filtering model
│   └── hybrid_model.py  # Hybrid model combining both approaches
│
├── preprocessing/
│   ├── __init__.py  # Makes 'preprocessing' a package
│   ├── clean_data.py  # Data cleaning script
│   ├── feature_engineering.py  # Feature engineering for recommendation
│   ├── fetch_data.py  # Fetch data from APIs
│   └── preprocess_data.py  # Preprocess raw data for recommendation models
│
├── README.md
└── requirements.txt  # Python dependencies
```


## Installation

### Prerequisites

- Ensure you have Python 3.x installed.

### Steps to install

1. Clone the repository:
    ```
    git clone https://github.com/yourusername/video-recommendation-system.git
    cd video-recommendation-system
    ```

2. Create a virtual environment:
    ```
    python3 -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Run the Flask app:
    ```
    python api/app.py
    ```

- This will start the server at http://localhost:5000.


## API Endpoints

# 1. Get Recommendations Based on Username, Category, and Mood

- URL: /feed?username=<username>&category_id=<category_id>&mood=<mood>
- Method: GET

- Parameters:
    1. username: The username of the user requesting recommendations.
    2. category_id :  The category of videos the user wants to see.
    3. mood: The current mood of the user (e.g., "happy", "calm").

- Example Request:
    ```
    GET http://localhost:5000/feed?username=john_doe&category_id=101&mood=happy
    ```
- Response:

    ```
            {
        "recommendations": [
            {"id": 1, "title": "Motivational Video 1", "category_id": 101, "tags": ["motivation", "success"], "mood": "happy"},
            {"id": 2, "title": "Inspirational Video 2", "category_id": 102, "tags": ["inspiration", "hope"], "mood": "calm"}
        ]
        }
    ```

# 2. Get Recommendations Based on Username and Category

- URL: /feed?username=<username>&category_id=<category_id>
- Method: GET

- Parameters:
    1. username: The username of the user requesting recommendations.
    2. category_id :  The category of videos the user wants to see.

- Example Request:
    ```
    GET http://localhost:5000/feed?username=kinha&category_id=814
    ```
- Response:

    ```
            {
                "recommendations": [
                    {"id": 1, "title": "Motivational Video 1", "category_id": 101, "tags": ["motivation", "success"], "mood": "happy"},
                    {"id": 3, "title": "Motivational Video 3", "category_id": 101, "tags": ["growth", "self-improvement"], "mood": "inspirational"}
                ]
            }
    ```


# 3. Get Recommendations Based on Username Only

- URL: /feed?username=<username>
- Method: GET

- Parameters:
    1. username: The username of the user requesting recommendations.

- Example Request:
    ```
    GET http://localhost:5000/feed?username=john_doe
    ```
- Response:

    ```
            {
                "recommendations": [
                    {"id": 2, "title": "Inspirational Video 2", "category_id": 102, "tags": ["inspiration", "hope"], "mood": "calm"},
                    {"id": 4, "title": "Self Growth Video", "category_id": 101, "tags": ["motivation", "success"], "mood": "happy"}
                ]
            }
    ```


## Data Preprocessing

- The data is fetched from external APIs. Here's how the data is processed:

1. Data Fetching:

- Data is fetched from the provided API endpoints.
- Pagination is used to ensure that data isn't fetched repeatedly.

2. Data Cleaning:

- Missing values are handled by filling or removing incomplete records.
- Data normalization ensures consistency in values across different features.

3. Feature Engineering:

- Additional features are created from raw data to enhance the recommendation models, such as categorizing videos, extracting tags, and mapping user preferences.

## Algorithm Selection

1. Content-Based Filtering:

- Content-based filtering recommends videos similar to those the user has interacted with (e.g., viewed, liked). It uses metadata (tags, categories) to find similar videos. This approach works well for users with historical data.

2. Collaborative Filtering:

- Collaborative filtering recommends videos based on the preferences of similar users. This model can improve as more user data is collected. It’s effective when users have diverse preferences but may struggle with new users who don’t have enough interaction history (cold start problem).

3. Hybrid Model:

- A hybrid model combines content-based and collaborative filtering to leverage the strengths of both. It offers personalized recommendations while minimizing the limitations of each individual model.

- The hybrid model was chosen to combine the accuracy of content-based filtering with the broader scope of collaborative filtering, ensuring high-quality recommendations for a wide range of users.


## Evaluation Metrics

1. Mean Absolute Error (MAE):
- MAE measures the average magnitude of errors in the recommendations. The lower the MAE, the better the model’s accuracy.

2. Root Mean Square Error (RMSE):

- RMSE penalizes larger errors more heavily than MAE, providing a more sensitive measure of recommendation quality.

## Testing

* Unit Tests:
    - Unit tests are written for each model to ensure correctness.
    - API testing ensures that the endpoints return the correct recommendations.

## License
* This project is licensed under the MIT License - see the LICENSE file for details.


### Key Points Addressed:
- **Model Selection**: Justified the use of hybrid models that combine content-based and collaborative filtering to handle diverse user needs.
- **Evaluation Metrics**: Summarized how MAE and RMSE are used to assess the model’s recommendation accuracy.
- **Documentation**: Provides detailed setup instructions, API usage, and project structure explanations.

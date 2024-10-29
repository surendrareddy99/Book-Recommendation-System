from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load your dataset
df = pd.read_csv('books.csv')
df.columns = df.columns.str.strip()

@app.route('/')
def home():
    return render_template('index.html')  # Render your frontend template

@app.route('/recommend', methods=['POST'])
def recommend_books():
    filter_type = request.json['filter_type']
    filter_value = request.json['filter_value']

    # Convert 'average_rating' and 'num_pages' columns to numeric, coercing errors to NaN
    df['average_rating'] = pd.to_numeric(df['average_rating'], errors='coerce')
    df['num_pages'] = pd.to_numeric(df['num_pages'], errors='coerce')

    # Drop rows where these columns have NaN values after conversion
    recommendations = df.dropna(subset=['average_rating', 'num_pages']).copy()

    if filter_type == 'Author':
        recommendations = recommendations[recommendations['authors'].str.contains(filter_value, case=False, na=False)]
        recommendations = recommendations.sort_values(by='average_rating', ascending=False)
    elif filter_type == 'Minimum Rating':
        try:
            min_rating = float(filter_value)
            recommendations = recommendations[recommendations['average_rating'] >= min_rating]
        except ValueError:
            return jsonify({'error': 'Please enter a valid rating (e.g., 4.5)'})
    elif filter_type == 'Number of Pages':
        try:
            max_pages = int(filter_value)
            recommendations = recommendations[recommendations['num_pages'] <= max_pages]
        except ValueError:
            return jsonify({'error': 'Please enter a valid number for pages.'})
    elif filter_type == 'Title':
        recommendations = recommendations[recommendations['title'].str.contains(filter_value, case=False, na=False)]

    # Convert recommendations to JSON
    result = recommendations[['title', 'authors', 'average_rating', 'num_pages', 'publisher']].head(10).to_dict(orient='records')

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

# Book Recommendation System

An AI-based Book Recommendation System built using AWS SageMaker, Flask, and Pandas. This system recommends books based on various filters, including author, rating, genre, and more, helping users easily discover books tailored to their preferences.

## Features

- **Author-based Recommendations**: Get the best works of specific authors.
- **Rating-based Recommendations**: Find books with high user ratings.
- **Title Recommendations**: Discover books by  title,nuumber of pages, and more.
- **Interactive UI**: User-friendly interface with dropdown filters for an engaging experience.

## Getting Started

### Prerequisites

- Python 3.7+
- AWS Account with access to S3 and SageMaker
- Basic understanding of Git and GitHub (to clone the repository)

### Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/Book-Recommendation-System.git
   cd Book-Recommendation-System
Install Dependencies: Install the required Python packages with:

pip install -r requirements.txt

2. Install Dependencies: Install the required Python packages with:
       pip install -r requirements.txt

3.AWS S3 Dataset Setup:
Ensure your dataset is uploaded to Amazon S3 in the appropriate bucket. Your dataset file should be accessible at s3://book-recommendation-system-dataset/books.csv.

4.Set Up Environment Variables (if necessary): Configure any AWS access keys and S3 bucket details as environment variables or directly in your code if not managed by IAM roles.

Usage
To start the application, run the following command:

python app.py
The app should start locally on your computer. Open a browser and go to this address to use the Book Recommendation System.

File Structure
app.py: The main Flask application file that runs the recommendation system.
Procfile: Defines the command for deploying the app on platforms like Heroku or AWS Elastic Beanstalk.
requirements.txt: Lists all necessary Python libraries.

Deployment
You can deploy this application on AWS services such as Elastic Beanstalk or Lambda. For local testing, ensure that all dependencies are installed and configurations are set.

Example Usage
Select Filters: Choose filters like author, minimum rating, or num_pages,title.
View Recommendations: The system will display book recommendations based on your selected filters.
License
This project is licensed under the MIT License. Feel free to use and modify it as per the license terms.

Acknowledgments
AWS for providing powerful cloud tools and services.
OpenAI and other resources for inspiration and guidance.

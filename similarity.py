from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def prepare_recommendations(df):
    """Prepare the TF-IDF matrix and cosine similarity with case-insensitive features."""
    df['features'] = (
        df['product_name'].str.lower() + ' ' +
        df['category'].str.lower() + ' ' +
        df['description'].str.lower() + ' ' +
        df['tags'].str.lower()
    )
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['features'])
    return cosine_similarity(tfidf_matrix, tfidf_matrix)

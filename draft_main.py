import pandas as pd

# Load codebook and news data
codebook = pd.read_csv("codebook.csv")
news = pd.read_csv("news.csv")

# Normalize to lowercase for matching
codebook['term'] = codebook['term'].str.lower()
news['text'] = news['text'].str.lower()

# Function to classify an article
def classify_article(text, codebook):
    matches = []
    for _, row in codebook.iterrows():
        if row['term'] in text:
            matches.append(row['category'])
    return list(set(matches)) if matches else ["sin_categoria"]

# Apply classification
news['categories'] = news['text'].apply(lambda t: classify_article(t, codebook))

# Show results
print(news[['id','title','categories']])

# Optionally save results
news.to_csv("classified_news.csv", index=False)

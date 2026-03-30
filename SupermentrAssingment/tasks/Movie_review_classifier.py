#23rd march

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score

# 1. Expanded Dataset (20+ samples)
data = {
    "text": [
        "I love this product", "This is amazing", "Worst experience ever", "I hate this",
        "Very good service", "Not satisfied", "Excellent quality", "Bad product", "It is okay",
        "The plot was gripping", "Cinematography was breathtaking", "Acting was terrible",
        "A complete waste of time", "Highly recommended for fans", "It was a mediocre film",
        "Superb performance by the lead", "I fell asleep halfway through", "Pretty average story",
        "An absolute masterpiece", "The ending was disappointing", "Decent watch for a Sunday",
        "I would watch this again", "Totally unimpressed with the script"
    ],
    "label": [
        "positive", "positive", "negative", "negative", "positive", "negative", "positive", 
        "negative", "neutral", "positive", "positive", "negative", "negative", "positive", 
        "neutral", "positive", "negative", "neutral", "positive", "negative", "neutral", 
        "positive", "negative"
    ]
}

df = pd.DataFrame(data)

# 2. Split data
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

# 3. Text Vectorization using TF-IDF (Term Frequency-Inverse Document Frequency)
# TF-IDF helps by down-weighting common words like 'the' and 'is'
tfidf = TfidfVectorizer(stop_words='english')
X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

# 4. Train Multinomial Naive Bayes Model
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# 5. Evaluation
y_pred = model.predict(X_test_tfidf)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2%}\n")
print(classification_report(y_test, y_pred))

# 6. Test on custom reviews
sample_reviews = ["I really enjoyed the movie!", "It was quite boring and long."]
sample_tfidf = tfidf.transform(sample_reviews)
predictions = model.predict(sample_tfidf)

for review, sentiment in zip(sample_reviews, predictions):
    print(f"Review: '{review}' -> Sentiment: {sentiment}")
from textblob import TextBlob

# 1. Define your 5 movie reviews
reviews = [
    "A cinematic masterpiece! The acting was phenomenal and the plot was gripping.",
    "Utterly disappointing. The pacing was slow and the ending felt rushed.",
    "It was an okay movie. Not great, but not terrible either. Average experience.",
    "I loved every second of it! The visual effects were truly out of this world.",
    "Save your money. This is the worst film I have seen in years. Terrible writing."
]

def analyze_reviews(review_list):
    # Header for the results table
    print(f"{'Review Snippet':<50} | {'Score':<8} | {'Sentiment'}")
    print("-" * 75)

    for text in review_list:
        # Create a TextBlob object for analysis
        analysis = TextBlob(text)
        
        # Determine sentiment based on polarity score
        # Polarity ranges from -1.0 (Negative) to 1.0 (Positive)
        score = round(analysis.sentiment.polarity, 2)
        
        if score > 0.1:
            sentiment = "Positive"
        elif score < -0.1:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        # Format the snippet for clear display
        snippet = (text[:47] + '..') if len(text) > 47 else text
        print(f"{snippet:<50} | {score:<8} | {sentiment}")

if __name__ == "__main__":
    analyze_reviews(reviews)

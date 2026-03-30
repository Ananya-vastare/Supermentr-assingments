#16th march
import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    # 1. Convert to lowercase
    text = text.lower()
    
    # 2. Remove punctuation
    # This creates a translation table that maps every punctuation character to None
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # 3. Tokenize text
    tokens = word_tokenize(text)
    
    # 4. Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    
    # 5. Apply stemming
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]
    
    return stemmed_tokens

# --- Execution ---
input_text = "I am learning NLP and it is very exciting!!!"
output = preprocess_text(input_text)

print(f"Input:  {input_text}")
print(f"Output: {output}")
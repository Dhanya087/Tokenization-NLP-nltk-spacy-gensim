import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# Ensure necessary NLTK data packages are downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def process_text(sentence):
    # Tokenization
    tokens = word_tokenize(sentence)
    print("Tokens:", tokens)
    
    # Stop word removal
    stop_words = set(stopwords.words('english'))
    tokens_without_stopwords = [word for word in tokens if word.lower() not in stop_words]
    print("Tokens without stopwords:", tokens_without_stopwords)
    
    # Stemming
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(word) for word in tokens_without_stopwords]
    print("Stemmed Tokens:", stemmed_tokens)
    
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens_without_stopwords]
    print("Lemmatized Tokens:", lemmatized_tokens)

# Example usage with user input
if __name__ == "__main__":
    sentence = input("Please enter a sentence: ")
    process_text(sentence)

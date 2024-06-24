import spacy

# Load the SpaCy English model
nlp = spacy.load('en_core_web_sm')

# Take input from the user
text = input("Enter the text to be processed: ")

# Tokenization using SpaCy
doc = nlp(text)
tokens = [token.text for token in doc]
print(f"\nTokens: {tokens}")

# Lemmatization using SpaCy
lemmatized_tokens = [token.lemma_ for token in doc]
print(f"\nLemmatized Tokens: {lemmatized_tokens}")

# Stop word removal (using SpaCy's default stop words list)
filtered_tokens = [token.text for token in doc if not token.is_stop]
print(f"\nFiltered Tokens (Stop Words Removed): {filtered_tokens}")

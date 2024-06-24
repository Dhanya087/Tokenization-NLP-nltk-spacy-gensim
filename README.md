NLP Preprocessing with Stemming, Tokenization, Lemmatization, and Stop Word Removal
This repository contains Python scripts that demonstrate how to perform basic NLP preprocessing tasks using three different libraries: SpaCy, NLTK, and Gensim. Each script in this repository showcases the following tasks in a single file per library:

Stemming: Reducing words to their root form.
Tokenization: Splitting text into tokens (words or phrases).
Lemmatization: Determining the lemma or base form of each word.
Stop Word Removal: Filtering out common words (e.g., "and", "the", "is").
Contents
Each directory corresponds to a different NLP library:

Tokenization_spacy/: Contains the Python script for NLP preprocessing using SpaCy.
tokenization_example_nltk/: Contains the Python script for NLP preprocessing using NLTK.
Tokenizationgensim/: Contains the Python script for NLP preprocessing using Gensim.
Usage
To use these scripts:

Clone the repository:

bash
Copy code
git clone https://github.com/Dhanya087/Tokenization-NLP-nltk-spacy-gensim.git
Navigate to the directory of the library you want to use (spacy_example/, nltk_example/, or gensim_example/).

Install the necessary dependencies. For example, if you're using SpaCy:

bash
Copy code
pip install spacy
python -m spacy download en_core_web_sm
Run the Python script:

bash
Copy code
python nlp_preprocessing.py
Dependencies
SpaCy: Ensure you have SpaCy installed (pip install spacy). You might also need to download the English model (python -m spacy download en_core_web_sm).
NLTK: Install NLTK (pip install nltk). Additional data such as stopwords (nltk.download('stopwords')) may be required.
Gensim: Install Gensim (pip install gensim).

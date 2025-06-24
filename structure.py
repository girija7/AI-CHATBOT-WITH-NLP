import nltk
import spacy
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import random
import json
from dotenv import load_dotenv

# Load NLP models
nlp = spacy.load('en_core_web_sm')
lemmatizer = WordNetLemmatizer()

# Download NLTK data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

class ChatBot:
    def __init__(self, intents_file="intents.json"):
        self.intents = self.load_intents(intents_file)
        self.lemmatizer = WordNetLemmatizer()
    
    def load_intents(self, file_path):
        with open(file_path) as file:
            data = json.load(file)
        return data["intents"]
    
    def preprocess_text(self, text):
        # Tokenize and lemmatize
        tokens = word_tokenize(text.lower())
        lemmatized = [self.lemmatizer.lemmatize(token) for token in tokens]
        return lemmatized
    
    def get_intent(self, user_input):
        processed_input = self.preprocess_text(user_input)
        
        # SpaCy for semantic similarity
        input_doc = nlp(user_input.lower())
        
        best_match = None
        highest_similarity = 0
        
        for intent in self.intents:
            for pattern in intent["patterns"]:
                pattern_doc = nlp(pattern.lower())
                similarity = input_doc.similarity(pattern_doc)
                
                if similarity > highest_similarity:
                    highest_similarity = similarity
                    best_match = intent
        
        # Threshold for matching
        if highest_similarity > 0.7:
            return best_match
        return None
    
    def get_response(self, intent):
        return random.choice(intent["responses"])
    
    def chat(self):
        print("ChatBot: Hello! How can I help you today? (Type 'quit' to exit)")
        
        while True:
            user_input = input("You: ")
            
            if user_input.lower() == 'quit':
                print("ChatBot: Goodbye!")
                break
                
            intent = self.get_intent(user_input)
            
            if intent:
                print(f"ChatBot: {self.get_response(intent)}")
            else:
                print("ChatBot: I'm not sure I understand. Could you rephrase that?")

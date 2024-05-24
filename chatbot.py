import spacy
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import random

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Define some responses
responses = {
    "hello": "Hi there!",
    "how are you": "I'm doing well, thank you!",
    "bye": "Goodbye!"
    
}

# Define some predefined intents and responses
intents = {
    "greeting": ["hello", "hi", "hey", 'how are you'],
    "farewell": ["bye", "goodbye"],
    "thanks": ["thank you", "thanks", 'I appreciate it'],
    "positive": ["great", "good", "awesome"],
    "negative": ["bad", "terrible", "awful", "sad"],
    "question": ['?', 'how', "why", "when", "where", "what"]
}

# Define responses for each intent
intent_responses = {
    "greeting": ["Hello! How can I assist you today?", "Hi there! What can I do for you?", 'Nice to talk to you, how can I help?'],
    "farewell": ["Goodbye! Have a great day!", "Farewell! See you later!"],
    "thanks": ["You're welcome!", "No problem, happy to help!"],
    "positive": ["That sounds fantastic!", "Great to hear!"],
    "negative": ["I'm sorry to hear that.", "I understand. Is there anything I can do to help?", "Say mums"],
    'question': ['I can onky recognise questions and not answer them.']
}
# Process user input and generate response
def respond(input_text):
    input_text = input_text.lower()
    doc = nlp(input_text)
    
    # Entity recognition
    entities = [ent.text for ent in doc.ents]
    
    # Sentiment analysis
    sentiment = TextBlob(input_text).sentiment.polarity
    
    # Intent recognition using cosine similarity
    tfidf_vectorizer = TfidfVectorizer()
    intent_texts = list(intents.values())
    intent_texts = [" ".join(intent) for intent in intent_texts]
    intent_texts.append(input_text)
    tfidf_matrix = tfidf_vectorizer.fit_transform(intent_texts)
    similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    intent_index = np.argmax(similarity_scores)
    
    if similarity_scores[0][intent_index] > 0.5:
        detected_intent = list(intents.keys())[intent_index]
        response_options = intent_responses.get(detected_intent, [])
        if response_options:
            return random.choice(response_options)
    
    for token in doc:
        if token.text in responses:
            return responses[token.text]
    
    if "hello" in entities:
        return random.choice(intent_responses["greeting"])
    elif sentiment > 0.5:
        return random.choice(intent_responses["positive"])
    elif sentiment < -0.5:
        return random.choice(intent_responses["negative"])
    else:
        return "I'm sorry, I don't understand that."

# Main loop
while True:
    user_input = input("You: ")
    response = respond(user_input)
    print("Bot:", response)


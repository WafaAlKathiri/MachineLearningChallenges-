from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

# Loading the saved model
model = load_model('/app/french_to_english_model.keras')
print("Model loaded successfully!")

# Loading the tokenizers
with open('/app/english_tokenizer.pkl', 'rb') as f:
    english_tokenizer = pickle.load(f)
with open('/app/french_tokenizer.pkl', 'rb') as f:
    french_tokenizer = pickle.load(f)

# Define the translation function
def translate_sentence(input_sentence):

    input_sequence = english_tokenizer.texts_to_sequences([input_sentence])
    input_padded = pad_sequences(input_sequence, maxlen=15, padding='post')
    predictions = model.predict(input_padded)
    predicted_sequence = predictions[0].argmax(axis=-1)
    reverse_french_word_index = {v: k for k, v in french_tokenizer.word_index.items()}
    translated_sentence = ' '.join([reverse_french_word_index.get(idx, '') for idx in predicted_sequence if idx > 0])

    return translated_sentence

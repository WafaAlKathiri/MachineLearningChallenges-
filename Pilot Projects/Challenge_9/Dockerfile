# Using an official Python runtime as a parent image
FROM python:3.9-slim

# Setting the working directory in the container
WORKDIR /app

# Copying the application code into the container
COPY . /app

# Copying the model file and other necessary files into the container
COPY french_to_english_model.keras /app/french_to_english_model.keras
COPY english_tokenizer.pkl /app/english_tokenizer.pkl
COPY french_tokenizer.pkl /app/french_tokenizer.pkl

# Installing Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exposing the Flask app's port (default: 5000)
EXPOSE 5000

# Running the Flask app
CMD ["python", "app.py"]



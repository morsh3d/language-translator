# Translation and Text-to-Speech

This project uses the Hugging Face Transformers library to translate text to English and then convert the translated text to speech using the Google Text-to-Speech (gTTS) library.

## Files

- `french.py`: This script contains the main functionality of the project. It uses the MarianMT model from the Hugging Face Transformers library to translate French text to English. It then uses the gTTS library to convert the translated text to speech and save it as an MP3 file.

- `app.py`: This script uses Flask to create a web application that provides a user interface for the functionality in `french.py`.

- `tf_model.h5`: This is the Hugging Face model. You can find more details about it on [the Hugging Face website.](https://huggingface.co/google/mt5-base/blob/2e1532e3c3ac67f4e8ed3c4a4d95a2fa0d694fd3/tf_model.h5)

## Languages supported
The project currently supports French only. It is using Helsinki-NLP/opus-mt-fr-en model.

## Installation

To install the necessary dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Usage
To use the project, run the Flask application with the following command:

```bash
python app.py
```

Then, open a web browser and navigate to [http://localhost:5000](http://localhost:5000) (or the URL displayed in your terminal). Enter some text in French and click the "Translate" button to get the English translation and hear the translated text.





# Translation and Text-to-Speech

This project uses the Hugging Face Transformers library to translate text to English and then convert the translated text to speech using the Google Text-to-Speech (gTTS) library.

## Files

- `french.py`: This script contains the main functionality of the project. It uses the MarianMT model from the Hugging Face Transformers library to translate French text to English. It then uses the gTTS library to convert the translated text to speech and save it as an MP3 file.

- `app.py`: This script uses Flask to create a web application that provides a user interface for the functionality in `french.py`.

- `tf_model.h5`: This is the Hugging Face model. You can find more details about it on [the Hugging Face website](https://huggingface.co/google/mt5-base/blob/2e1532e3c3ac67f4e8ed3c4a4d95a2fa0d694fd3/tf_model.h5).

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
flask run
```

Then, open a web browser and navigate to [http://localhost:5000](http://localhost:5000) (or the URL displayed in your terminal). Enter some text in French and click the "Translate" button to get the English translation and hear the translated text.

# How does french.py work?
french.py is the heart of the translation code. This is a simple explanation of what is going on:

1. The translator used a pre-trained data model (tf_model.h5) which contains all the data it needs for the translation.
2. It loads the model and retrieves a Tokenizer. The Tokenizer is the mathematical model used to map text into a possition within the data model.
3. Your text to be translated is ten encoded into a Token.
4. The data model then generates an array of possible matches using the Token as input.
5. The best matching solution is then returned from the array.
6. This is then turned into an audio file for output.

# Installation on Mac's with M1/M2 chipsets
There is a known issue with some Python libraries relating to the M1/M2 chipsets and the GPU. This may cause
issues with some libraries being loaded but causing errors at runtime.

One library that has this issue is the Transformers library used for the Tokenization. A resolution 
for this can be found here (https://towardsdatascience.com/hugging-face-transformers-on-apple-m1-26f0705874d7)

If you experience issues with TensorFlow installation instructions can be found here 
(https://caffeinedev.medium.com/how-to-install-tensorflow-on-m1-mac-8e9b91d93706)

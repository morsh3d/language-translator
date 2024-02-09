from transformers import MarianMTModel, MarianTokenizer
from gtts import gTTS
import io
import os

def load_model(model_name):
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    return model, tokenizer

def translate_text(model, tokenizer, input_text):
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    outputs = model.generate(input_ids, max_length=100, num_beams=16, no_repeat_ngram_size=2, early_stopping=True)
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Convert the translated text to speech
    tts = gTTS(translated_text, lang='en')
    audio_file = "audio.mp3"
    tts.save(audio_file)

    return translated_text, audio_file

if __name__ == "__main__":
    input_text = input("Enter some text in French: ")
    model_name = "Helsinki-NLP/opus-mt-fr-en"
    model, tokenizer = load_model(model_name)
    translated_output, audio_file = translate_text(model, tokenizer, input_text)
    print("Translated text:", translated_output)
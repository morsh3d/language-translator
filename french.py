from transformers import MarianMTModel, MarianTokenizer
from gtts import gTTS
from datetime import datetime
import io
import os

model_name = "Helsinki-NLP/opus-mt-fr-en"
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

def translate_text(input_text):
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    outputs = model.generate(input_ids, max_length=100, num_beams=16, no_repeat_ngram_size=2, early_stopping=True)
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Convert the translated text to speech
    tts = gTTS(translated_text, lang='en')
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")  # Get the current timestamp
    audio_file = f"static/audio_{timestamp}.mp3"  # Append the timestamp to the filename
    
    tts.save(audio_file)

    return translated_text, audio_file

if __name__ == "__main__":
    input_text = input("Enter some text in French: ")
    translated_output, audio_file = translate_text(input_text)
    print("Translated text:", translated_output)
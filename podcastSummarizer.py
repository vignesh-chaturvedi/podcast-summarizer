import speech_recognition as sr
import nltk
import os
import requests
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
from gtts import gTTS

# Speech-to-Text
r = sr.Recognizer()
audio = sr.AudioFile('video.mp3')
with audio as source:
    audio_text = r.record(source)
    text = r.recognize_google(audio_text)

# Saving the whole audio text as "script.txt"
with open("script.txt", "w") as file:
    file.write(text)

# Text Summarization
sentences = sent_tokenize(text)
stop_words = set(stopwords.words("english"))
word_frequencies = {}
for sentence in sentences:
    words = word_tokenize(sentence)
    for word in words:
        word = word.lower()
        if word in stop_words:
            continue
        if word in word_frequencies:
            word_frequencies[word] += 1
        else:
            word_frequencies[word] = 1
n = 10
most_frequent_words = sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True)[:n]

# Saving the summary text in a ".txt" file
with open("summary.txt", "w") as file:
    file.write(summary)

# Text-to-Speech
summary = ''
for word, frequency in most_frequent_words:
    summary += ' ' + word
tts = gTTS(summary)
tts.save("summary.mp3")
os.system("summary.mp3")

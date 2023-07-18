# Import Requirements
import string
from collections import Counter as count
import matplotlib.pyplot as plt
import speech_recognition as sr

type = int(input("Enter 1 for Sound & 0 for Text File as input : "))

if type == 1:
    r = sr.Recognizer()

    mic = sr.Microphone()

    with mic as source:
        print("Speak Now...")
        audio_data = r.listen(source)

    text = r.recognize_google(audio_data)

    print("You Said : ", text)

elif type == 0:
    # Cleaning the Raw Data
    # Fetching the Data
    text = open('data.txt', encoding='latin1').read()

else:
    print("Invalid Input")

# Converting to Lower Case
lower_case = text.lower()

# Removing Special Charaters
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))

# Spliting Text into Words
tokenized_words = cleaned_text.split()

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

# Removing Stop Words from The Tokens
final_words = []
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)
        
# NLP Emotion Algorithm
# 1) Check if the word in the final word list is also present in emotion.txt
#  - open the emotion file
#  - Loop through each line and clear it
#  - Extract the word and emotion using split

# 2) If word is present -> Add the emotion to emotion_list
# 3) Finally count each emotion in the emotion list
emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(":")
        
        if word in final_words:
            emotion_list.append(emotion)
            
w = count(emotion_list)

# Plotting the Emotions on the Graph
fig, ax = plt.subplots()
ax.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show
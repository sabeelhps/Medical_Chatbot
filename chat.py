import random
import json

from jarvis import takeVoiceCommand,speak

import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Aisha"


while True:
    # sentence = "do you use credit cards?"

    ch=input("For Voice Press 1 . For Text click 2:")
    quit=[]
    if ch=="1":
        sentence=takeVoiceCommand()
        quit=sentence.split()
    # sentence = input("You: ")
    elif ch=="2":
        sentence=input()

    elif quit[0].lower() == "goodbye":

        speak("Good Bye,See you Again!!")
        break
    
    elif len(sentence)==0:
        continue

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                reply=f"{random.choice(intent['responses'])}"
                print(f"{bot_name}: {reply}")
                speak(reply)

    else:
        print(f"{bot_name}: I do not understand...")
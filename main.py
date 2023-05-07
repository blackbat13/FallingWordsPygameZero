import pgzrun
from random import random, randint
from faker import Faker


WIDTH = 500
HEIGHT = 900

fake = Faker()

words_list = []


def draw():
    screen.fill("white")

    for word in words_list:
        screen.draw.text(word["word"], center=(word["x"], word["y"]), color="black", fontsize=40)


def update():
    if random() < 0.01:
        words_list.append({
            "word": fake.word().lower(), 
            "x": randint(100, WIDTH - 100), 
            "y": -50, 
            "v": random() + 0.05})
        
    for word in words_list[:]:
        word["y"] += word["v"]
        if word["y"] > HEIGHT + 100:
            words_list.remove(word)


def on_key_down(key):
    character = chr(key)
    for word in words_list[:]:
        if word["word"][0] == character:
            word["word"] = word["word"][1:]
            if len(word["word"]) == 0:
                words_list.remove(word)
            break


pgzrun.go()
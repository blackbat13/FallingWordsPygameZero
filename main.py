import pgzrun
from random import random, randint, choice
from faker import Faker


WIDTH = 500
HEIGHT = 900

fake = Faker()

words_list = []

game = {
        "points": 0,
        "level": 1,
        "word_count": 0
    }

colors_list = ["#E90064", "#FFED00", "#16FF00", "#00F5FF", "#FF8D29", "#F9D371", "#1CC5DC"] 


def draw():
    screen.fill("#191825")

    for word in words_list:
        screen.draw.text(word["word"], center=(word["x"], word["y"]), color=word["color"], fontsize=40)

    screen.draw.text(f"Word count: {game['word_count']}", midleft=(5, HEIGHT - 80), color="#F3CCFF", fontsize=30)
    screen.draw.text(f"Level: {game['level']}", midleft=(5, HEIGHT - 50), color="#865DFF", fontsize=30)
    screen.draw.text(f"Points: {game['points']}", midleft=(5, HEIGHT - 20), color="#A31ACB", fontsize=30)


def update():
    for word in words_list[:]:
        word["y"] += word["v"]
        if word["y"] > HEIGHT + 20:
            game["points"] = 0
            game["level"] = 0
            game["word_count"] = 0
            words_list.clear()
            break


def on_key_down(key):
    character = chr(key)
    max_y = 0
    max_word_index = -1
    for index, word in enumerate(words_list):
        if word["word"][0] == character and word["y"] > max_y:
            max_word_index = index
            max_y = word["y"]

    if max_word_index == -1:
        game["points"] -= 1
        return
    
    words_list[max_word_index]["word"] = words_list[max_word_index]["word"][1:]
    if len(words_list[max_word_index]["word"]) == 0:
        words_list.pop(max_word_index)
        game["points"] += 5 * game["level"]
        game["word_count"] += 1
        if game["word_count"] % 10 == 0:
            game["level"] += 1


def add_word():
    for _ in range(game["level"]):
        words_list.append({
                "word": fake.word().lower(), 
                "x": randint(50, WIDTH - 50), 
                "y": randint(-40, -20), 
                "v": random()/2 + 0.1 * game["level"],
                "color": choice(colors_list)
                })
    
    clock.schedule(add_word, random() * 5 + 1)


add_word()
pgzrun.go()
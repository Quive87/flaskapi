from flask import Flask, jsonify
import random

app = Flask(__name__)

# List of cat picture URLs
cat_pics = [
    "https://cdn2.thecatapi.com/images/MTY3ODIyMQ.jpg",
    "https://cdn2.thecatapi.com/images/MTY1ODUwNA.jpg",
    "https://cdn2.thecatapi.com/images/MTY2NTgwNQ.jpg",
    "https://cdn2.thecatapi.com/images/MTg3MjUzNA.jpg",
    "https://cdn2.thecatapi.com/images/MTk4NTU1MA.jpg"
]

@app.route('/')
def get_cat_pic():
    return jsonify({"url": random.choice(cat_pics)})


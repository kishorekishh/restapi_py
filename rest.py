from flask import Flask, jsonify, request
app = Flask(__name__)
# Sample data
data = [
    {'id': 1, 'name': 'Item 1'},
    {'id': 2, 'name': 'Item 2'},
]

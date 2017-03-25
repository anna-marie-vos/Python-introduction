#!/usr/bin/env python3

from flask import Flask


app = Flask(__name__)

#Basic route
@app.route("/")
def main():
    return "welcome"

if __name__ == "__main__":
    app.run()

from flask import Flask, render_template, request, redirect
import database.db_connector as db
import os

# Configuration

app = Flask(__name__)

# Routes 

@app.route('/')
def root():
    '''Return the homepage'''
    return render_template('index.html')

# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 56124)) 
    app.run(port=port) 
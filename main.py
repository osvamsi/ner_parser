import os
from flask import Flask, request 
import csv 
import pandas as pd 
import spacy 
from config import matcher_patterns
from utils import get_entities,get_matcher_matches

app = Flask(__name__)
nlp = spacy.load('en_core_web_sm')

@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST': 
        byte_data = request.data
        rows = byte_data.decode('utf-8').splitlines()[1:] 
        all_matches = []
        for row  in rows:
            row_data = " ".join(row.split(","))
            doc = nlp(row_data)
            all_matches.extend([("Entities",get_entities(doc)), 
                    ("Matcher_matches",get_matcher_matches(matcher_patterns,doc))])
        
        return str(all_matches)

if __name__ == "__main__":
    
    app.run(debug=True)
  
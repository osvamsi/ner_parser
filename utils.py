from spacy.matcher import Matcher
import re 
import spacy
import pandas as pd 

nlp = spacy.load('en_core_web_sm')

def get_entities(doc : "NLP object"):
    ent_list = []
    for ent in doc.ents:
        ent_list.append((ent.text, ent.label_))
    return ent_list

def get_matcher_matches(pattern_list : list, doc:"NLP object"):
    matches_list = []
    matcher = Matcher(nlp.vocab)
    for p_name, pattern in pattern_list:
        matcher.add(p_name,None,pattern)
    matches = matcher(doc)
    # Iterate over the matches
    for _, start, end in matches:
    # Get the matched span
        matched_span = doc[start:end]
        matches_list.append(matched_span.text)
    return matches_list

# def get_regex_matches(pattern_list: list, doc: "NLP object"):
#     matches_list = []
#     for pattern in pattern_list:
#         for match in re.finditer(pattern, doc.text):
#             start, end = match.span()
#             span = doc.char_span(start, end)
#             # This is a Span object or None if match doesn't map to valid token sequence
#             if span is not None:
#                 #match found
#                 matches_list.append(span.text)
#     return matches_list

# def get_sampled_data(file : "csv file", cols: list):
#     df = pd.read_csv(file)
#     return df.loc[:,cols]



import spacy

nlp = spacy.load('en_core_web_sm')

def advanced_filter(article):
    doc = nlp(article['summary'])
    for ent in doc.ents:
        if ent.label_ == 'ORG' and ent.text in ['SEC', 'Federal Reserve', 'CFTC']:
            return True
    return False
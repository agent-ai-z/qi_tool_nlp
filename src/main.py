import spacy ##serve per addestrare l'intelligenza

##from spacy import displacy
##spacy.cli.download('en_core_web_sm')## installa la lingua
##nlp = spacy.load("en_core_web_sm")##per restituire un'istanza della classe Language
##doc = nlp("Un passo avanti e non sei più nello stesso posto")##Ora possiamo usare questa istanza della classe Language per ottenere l'oggetto Doc
"""print([(w.text, w.pos_) for w in doc])""" ##mette a video la divisione delle parole
##displacy.serve(doc, style='dep')
#nlp = spacy.load("en_core_web_sm")
#doc = nlp("I own a ginger cat.")
#print([token.text for token in doc])## il testo viene suddiviso in token

"""from spacy.symbols import ORTH ##importiamo spaCy e il simbolo ORTH, che rappresenta l'ortografia
nlp = spacy.load("en_core_web_sm")##instanziamo l'oggetto Language come al solito, elaboriamo l'oggetto Doc e stampiamo i token:
doc = nlp("lemme that")
print([w.text for w in doc])
special_case = [{ORTH: "lem"}, {ORTH: "me"}]#possiamo definire il caso speciale in cui la parola "lemme" dovrebbe essere tokenizzata come due token: "lem" e "me":
nlp.tokenizer.add_special_case("lemme", special_case)
print([w.text for w in nlp("lemme that")])"""


nlp = spacy.load("en_core_web_sm")
#text = "Let's go dog!"
#doc = nlp(text)
#tok_exp = nlp.tokenizer.explain(text)## serve per difinire quali sono i token
#print(tok_exp)
#for t in tok_exp:
 #print(t[1], "\t", t[0])# serve per cambiare  l'ordine delle parole
 #for token in doc:
 #print (token.text)



#oc = nlp("This is a sentence. This is the second sentence")
#sentences = list(doc.sents)# è utilizzato per suddividere un testo in frasi separate, permettendo di eseguire operazioni o analisi su ciascuna di esse.
#print(sentences)

from pprint import pprint#quessto ci permette di cambiare un documento doc in Jason
doc = nlp("Hi")
json_doc = doc.to_json()
pprint(json_doc)





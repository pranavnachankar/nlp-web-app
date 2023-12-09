# API Used:- https://komprehend.io/

# Demo for NER :- https://komprehend.io/named-entity-recognition
import paralleldots
paralleldots.set_api_key("Your API Key")
def ner(text):
  ner = paralleldots.ner(text)
  return ner 
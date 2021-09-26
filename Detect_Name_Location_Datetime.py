import spacy
nlp = spacy.load("en_core_web_sm")
import requests
import json

def get_entity_name_location(text):

    '''
    take text as input and get the location person entity in dictionay format
    return dictionary of value GPE and PERSON
    '''
    doc = nlp(text)
    
    
    try:
        dict_ent = {}
        
        temp_gpe = []
        temp_person = []

        for ent in doc.ents:

            if ent.label_ == "GPE":
                temp_gpe.append(ent.text)
            elif ent.label_ == "PERSON":
                temp_person.append(ent.text)
        
        dict_ent["GPE"] = temp_gpe
        dict_ent["PERSON"] = temp_person
    
    except Exception as e:
        print(e)
        dict_ent["GPE"] = []
        dict_ent["PERSON"] = [] 
    
                
    return dict_ent

def get_entity_datetime(input_text,ref_date,lang):

    ''''
    Take Input text, refrence date and langauge as input and output datetime range as 
    phrase detection for datetime like "tomorrow","yesterday", start date and end date 
    in list of json/dict
    '''

    url = "http://hawkingapi-env.eba-epdc5jpi.us-east-1.elasticbeanstalk.com/hawking/api/v1/extract/date"

    payload = json.dumps({
    "input_text":str(input_text),
    "reference_date": str(ref_date),
    "language": str(lang)
    })
    headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
    }
    dict_datetime = {}
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        if response.status_code == 200:
            dict_datetime["Duration_Time"] = json.loads(response.text)
        else:
            dict_datetime["Duration_Time"] = []
    except Exception as e:
        dict_datetime["Duration_Time"] = []
        
    return dict_datetime

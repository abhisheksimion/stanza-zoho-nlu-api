from flask import Flask, render_template,jsonify,request, send_from_directory,abort, url_for
from Detect_Name_Location_Datetime import get_entity_name_location
from Detect_Name_Location_Datetime import get_entity_datetime
import Constants
import json
app = Flask(__name__)

@app.route('/entity',methods = ['POST'])
def get_results():

    ''''
    Take input in json format and sent output in json format
    '''

    data_from_json = json.dumps(request.json)
    data_loads = json.loads(data_from_json)
    user_input_data = data_loads["text"]
    ref_date_input = data_loads["ref_date"]
    lang_ip = data_loads["lang"]

    
    ### Function Call for the entity - Person and Location ##########
    res_person_loc=get_entity_name_location(user_input_data)


    ######### Function call for Date-time #######
    res_datetime = get_entity_datetime(user_input_data,ref_date_input,lang_ip)

    Final_res = {}
    Final_res[Constants.GPE] = res_person_loc["GPE"]
    Final_res[Constants.PERSON] = res_person_loc["PERSON"]
    Final_res[Constants.ORG] = res_person_loc["ORG"]
    Final_res[Constants.DATE_TIME] = res_datetime["Duration_Time"]

    return jsonify(Final_res)

if __name__ == '__main__':
    # app.debug = True
    app.run('0.0.0.0','4321')



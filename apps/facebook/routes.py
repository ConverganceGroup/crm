from re import I
from flask import jsonify
from flask.templating import render_template
from apps import db
from .models import Leadgens,Campaign
from .models import Campaign as comp
from apps.facebook import blueprint
import requests
import json

url = "https://graph.facebook.com/v12.0/110943320581164/leadgen_forms?access_token=EAAEfJmDPHNQBAJpDMxcMjeG4XTsZBPcfsOeDdbRgtmmga0Ef7l21ZCq3eJza1cqbX9DGaruUzegBdsURzAxZC0JG7Snu63vHCfyFVzyTux6DGn6c9zccKuHmg59zhZCZCHZCBr7ZCAyIiPIh4FbCcuQVy8e6qrY99T710v2cBpfsPEJbEQwDMirAgxgqFcDD9AVhdf2zVImmQZDZD&__activeScenarioIDs=[]&__activeScenarios=[]&debug=all&fields=leads_count,name,page,created_time,expired_leads_count,status,locale&format=json&limit=10&method=get&pretty=0&suppress_http_code=1&transport=cors"


#url = "https://graph.facebook.com/v12.0/100590515516281/leadgen_forms?pretty=0&fields=leads_count%2Cname%2Cpage%2Ccreated_time%2Cexpired_leads_count%2Cstatus%2Clocale&limit=10&before=QVFIUnVLU1hVSy0tSDk1WnJiVEFOZAFIyNzM1TkJhWGJ2TWM3MGwzekdRU0xGdkt3R1g1Y19tQmwzZAm1EU2lKS19pczRmTl8wdGR2SC1DZA0wyenRWS1NMNTZAR"
@blueprint.route("/laeds_data",methods=["GET"])
def get_results():
    try:
        laeds_data = Leadgens.get_all_leads_gen()
        return render_template("facebook/lead_gen.html",data=laeds_data) , 200
    except Exception as e:
        return jsonify(str(e))

@blueprint.route("/get_leads_gen",methods=['GET'])
def get_leads_gen():
    respone = requests.get(url=url)
    json_response = json.loads(respone.text)
    next = True
    while next:
        for item in json_response['data']:
            obj = Leadgens(lead_id=item['id'],locale = item['locale'],name=item['name'],status=item['status'],
                leads_count=item['leads_count'],page_name=item['page']['name'],created_time=item['created_time'],expired_leads_count=item['expired_leads_count'])
            Leadgens.save(obj)
        if 'next' in json_response['paging'].keys():
            respone = requests.get(url=json_response['paging']['next'])
            json_response = json.loads(respone.text)
        else:
            next = False
    
    return jsonify(json_response['data'])


from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign


@blueprint.route("/get_campagins",methods=["GET"])
def get_campagins():
    try:
        my_access_token = "EAAEfJmDPHNQBAJpDMxcMjeG4XTsZBPcfsOeDdbRgtmmga0Ef7l21ZCq3eJza1cqbX9DGaruUzegBdsURzAxZC0JG7Snu63vHCfyFVzyTux6DGn6c9zccKuHmg59zhZCZCHZCBr7ZCAyIiPIh4FbCcuQVy8e6qrY99T710v2cBpfsPEJbEQwDMirAgxgqFcDD9AVhdf2zVImmQZDZD"
        my_app_id = '205274791646907'
        my_app_secret = '5f239d35c302458afec9fb113434ab0c'
        FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
        my_account = AdAccount('act_527655717872173')
        campaigns = my_account.get_campaigns(fields=tuple(Campaign. _field_types.keys()))
        # lst = []
        # for index in range(len(campaigns)):
        #     obj = {}
        #     for key,value in campaigns[index].items():
        #         obj[key] = value[0] if type(value) == list  else value
        #     lst.append(obj)
        # for item in lst:
        #     obj_camp =comp(**item)
        #     db.session.add(obj_camp)
        #     db.session.commit()
        return jsonify({
            "code":200,
            "status":"success",
            "message":"add campaigns successfully!"
        })
    except Exception as e:
        return jsonify(str(e))
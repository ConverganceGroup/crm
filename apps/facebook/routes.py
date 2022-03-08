from re import I
from flask import jsonify
from flask.helpers import url_for
from flask.scaffold import F
from flask.templating import render_template
from apps import db
from .models import Leadgens
from apps.facebook import blueprint
import requests
import json

url = "https://graph.facebook.com/v12.0/100590515516281/leadgen_forms?access_token=EAAEfJmDPHNQBAAkKqr9zcHtb9mhhcONVU5rOnQhHZAk7Eyjxbr7k5ZABc0ESZBvUCW6ZAZA2o4JBiJ0MapwIZCf2WjOXNyDHpFCN1v5tUOXCNsi5jza9ytYptYmxmKBibAsYFUzN9BMGbE1H2tI2AhUk2ZBWP6IExlu7JPiw6kfhZCKj03Xiqc2BPLdG1YlfDPiCn65iIqyfZBeVO4QYPC5Ma&__activeScenarioIDs=[]&__activeScenarios=[]&debug=all&fields=leads_count,name,page,created_time,expired_leads_count,status,locale&format=json&limit=10&method=get&pretty=0&suppress_http_code=1&transport=cors"


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
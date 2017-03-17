import requests,json,random
def s4():
    return ''.join([random.choice('0123456789abcdef') for x in range(4)])
def guid():
    return s4()+s4()+'-'+s4()+'-'+s4()+'-'+s4()+s4()+s4()
headers={'content-type': 'application/json','accept':'application/json'}


class api:
    def __init__(self):
        self.baseurl="http://167.114.174.89:8080/"
        self.baseurl_tp="http://167.114.174.89:2080/"
    
    def get_all_routes(self):
        r = requests.get(self.baseurl+"app/routes/getAllRoutes.json")
        return json.loads(r.text)
        
    def get_all_stoppages(self):
        r = requests.get(self.baseurl+"app/stops/getAllStops.json")
        return json.loads(r.text)
        
    
    def get_last_update_time(self):
        r = requests.get(self.baseurl+"app/routes/getLastUpdateTime.json")
        return json.loads(r.text)
        
    def get_kolkata_traffic_update(self):
        r = requests.get(self.baseurl+"app/sm/kolkatatrafficupdate.json")
        return json.loads(r.text)
        
    def get_approaching_veichle(self,stop_id):
        data=json.dumps({'requestId':guid(),'stopId':stop_id})
        r=requests.post(self.baseurl+"app/travel/getApproachingVehicles.json",data=data,headers=headers)
        return json.loads(r.text)
        
    def get_veichles_by_rec_boundary(self,rec):
        data=json.dumps({'pointNW':{'latitude':rec[0],'longitude':rec[1]}},{'pointSE':{'latitude':rec[2],'longitude':rec[3]}})
        r=requests.post(self.baseurl+"app/vehicles/getVehicleList.json",data=data,headers=headers)
        return json.loads(r.text)
    
    
        
        
import requests
import xmltodict
import json
import time

bmkgUrl = 'https://data.bmkg.go.id/autogempa.xml'
apiGateway = 'https://hpxzjjmleg.execute-api.us-east-1.amazonaws.com/dev/updatedata'
tempJam = ''

def dataGempa(url): 
    req = requests.get(url)
    jsonData = json.loads(json.dumps(xmltodict.parse(req.text)))
    return jsonData

def kirimKeGateway(url, tanggal, jam, mag, kedalaman, wil):
    req = requests.post(url, json={"tanggal" : tanggal, "jam" : jam, "magnitude" : magnitude, "kedalaman" : kedalaman, "wilayah" : wil})
    if req.status_code == 200:
        return "Data Updated!"
    else:
        return "Failed to update data"

while True:
    testData = dataGempa(bmkgUrl)
    
    tanggal = testData['Infogempa']['gempa']['Tanggal']
    jam = testData['Infogempa']['gempa']['Jam']
    magnitude = testData['Infogempa']['gempa']['Magnitude']
    kedalaman = testData['Infogempa']['gempa']['Kedalaman']
    wilayah = testData['Infogempa']['gempa']['Wilayah1']

    if(jam == tempJam):
        print("Belum ada pembaharuan data dari BMKG")
    else:
        print(kirimKeGateway(apiGateway, tanggal, jam, magnitude, kedalaman, wilayah))
        tempJam = jam

    time.sleep(60)



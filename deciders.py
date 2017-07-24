import urllib
import json

def yes(arxiv_id):
    return True
    

def no(arxiv_id):
    return False

    
def altmetric_decider(arxiv_id):
    arxiv_id = arxiv_id.split('v', 2)[0]
    url = 'https://api.altmetric.com/v1/arxiv/' + str(arxiv_id)
    try:   
        response = urllib.request.urlopen(url)
        response = json.loads(response.read().decode('utf-8'))
        if response['score'] < .75:
            print("too little activity", url)
            return False
    except urllib.error.HTTPError as e:
        if str(e) == 'HTTP Error 404: Not Found':
            print("no activity", url)
            return False
    return True
import feedparser
from datetime import datetime
from datetime import timedelta
import json

def get_articles(category, channel):
    d = feedparser.parse('http://export.arxiv.org/api/query?search_query=' + category + '&sortBy=lastUpdatedDate&sortOrder=descending&max_results=100')
    f = open('.queue_' + channel, 'a')
    for entry in d['entries']:
        published = datetime.strptime(entry['published'], "%Y-%m-%dT%H:%M:%SZ")
        if published > datetime.now() - timedelta(hours=24):
            print("entry")
            f.write(entry['id'].split('/', 4)[4] + '\n')
    f.close()

config = open("config.json").read()
config = json.loads(config)
for key, value in config['server']['category_channel_pairings'].items():
    get_articles(key, value)




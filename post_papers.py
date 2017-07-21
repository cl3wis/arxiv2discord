import discord
import asyncio
import feedparser
import sympy as sy
import os
import json

sy.init_printing(use_latex='mathjax', pretty_print=True)

config = json.loads(open("config.json").read())

client = discord.Client()


def get_channel_by_file(queuefile):
    channel_name = queuefile.split("_", 1)[1]
    print(channel_name)
    server = discord.utils.get(client.servers, name=config['server']['name'])
    return discord.utils.get(server.channels, name=channel_name)


def read_post_queue(queuefile):
    f = open("./" + queuefile, 'r')
    items = []
    item = f.readline()
    while item:
        items.append(item)
        item = f.readline()
    f.close()
    return items


def get_article(id):
    d = feedparser.parse('http://export.arxiv.org/api/query?id_list=' + id + '&sortBy=lastUpdatedDate&sortOrder=descending&max_results=1')
    entry = d['entries'][0]
    title = entry['title']
    abstract = entry['summary']
    mathjax = '\\textbf{' + title + '}\\\\\\\\' + abstract
    image = sy.preview(mathjax, viewer='file', filename=id+'.png') 
    link = entry['link']
    return({'image': id+'.png', 'link': link})

    
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'test post please ignore')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!post'):
        for item in read_post_queue(".queue_" + message.channel.name):
            await asyncio.sleep(1)
            # [:-1] becaues the current hacked queue system puts a whitepsace \n at the end
            try:
                article = get_article(item[:-1])
                await client.send_file(message.channel, article['image'], content='\n**Find it here: **'+article['link'])
                os.remove(article['image'])
            except Exception as e:
                print(str(e)[1:6])
                if str(e)[1:7] == 'latex':
                    pass
    elif message.content.startswith('!kill'):
        exit()


client.run(config['token'])
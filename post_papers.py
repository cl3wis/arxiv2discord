import discord
import asyncio
import feedparser
import sympy as sy
import os
import json
from deciders import altmetric_decider

sy.init_printing(use_latex='mathjax', pretty_print=True)

config = json.loads(open("config.json").read())

client = discord.Client()


def get_owners_by_server(server):
    return config['servers'][server.name]["owners"]


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


async def post_latex(channel, arxiv_id):
    await asyncio.sleep(1)
    # [:-1] becaues the current hacked queue system puts a whitepsace \n at the end
    try:
        article = get_article(arxiv_id[:-1])
        await client.send_file(channel, article['image'], content='\n**Find it here: **'+article['link'])
        os.remove(article['image'])
    except Exception as e:
        if str(e)[1:7] == 'latex':
            pass

    
async def handle_post(message):
    commands = message.content.split(" ")
    if len(commands) == 1:
        client.send_message(message.channel, "Command not supported. Try '!post all' or '!post altmetrics'")
    elif str(message.author) not in get_owners_by_server(message.server):
       await client.send_message(message.channel, "Not Authorized")
    elif commands[1] == 'altmetrics':
        for item in read_post_queue(".queue_" + message.channel.name):
            if altmetric_decider(item):
                await post_latex(message.channel, item)
    elif commands[1] == 'all':
        for item in read_post_queue(".queue_" + message.channel.name):
            await post_latex(message.channel, item)
    else: 
        await client.send_message(message.channel, "Command not supported. Try '!post all' or '!post altmetrics'")

            
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
        await handle_post(message)


client.run(config['token'])

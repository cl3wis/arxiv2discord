# arxiv2discord
Monitors arXiv papers and posts in a discord server. Maybe someday it will have some kind of filtering to avoid absolutely spamming the chat.

## Usage
### Config
Copypasta `sample_config.json` as `config.json` and fill in appropriate details. Do the magic link thing to add the bot to your server. run the `post_papers.py` script to launch the bot (note: it won't post until you command it to in the server)

### Scraper
Put scrape_arxiv.py on a daily cronjob (any more is pointless. arXiv updates at midnight). Every day, it will add the most recent publications on the arXiv categories specified in config.json to the queue. 

### Commands
* `!post` will post the papers from the queue into the current channel. Also, you'll want to manually delete the `.queue_%channel_name%` files after you do this... I'm working on that.
* `!test` tests that the bot is running.
* `!kill` does that. It literally just has the bot run `exit()`.

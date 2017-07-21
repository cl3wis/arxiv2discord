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

## License
1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. ALSO NO ONE CAN USE THIS BOT ON ANY PLATFORM WITHOUT EXPRESS PERMISSION FROM THE REPOSITORY MAINTAINER.

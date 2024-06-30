# freedium-reddit-bot

A Reddit bot that replies to comments and submissions with a link to [Freedium](https://github.com/Freedium-cfd) to bypass the paywall.

## Usage

1. Clone the repository
2. Install the dependencies with `pip install -r requirements.txt`
3. Create a Reddit app at https://www.reddit.com/prefs/apps
4. Copy `praw.ini.example` to `praw.ini` and fill in all the fields
5. Copy `supervisord.conf.example` to `supervisord.conf` and change the `directory` fields
5. Run the bot with `supervisord -c supervisord.conf`

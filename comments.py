from reddit_bot import initialize_reddit, process_content

# Initialize Reddit instance
reddit = initialize_reddit()

# Stream comments in a specific subreddit
subreddit = reddit.subreddit("all")
for comment in subreddit.stream.comments(skip_existing=True):
    try:
        process_content(comment, reddit)
    except Exception as e:
        print(f"Error processing comment: {e}")

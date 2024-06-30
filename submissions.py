from reddit_bot import initialize_reddit, process_content

# Initialize Reddit instance
reddit = initialize_reddit()

# Stream submissions in a specific subreddit
subreddit = reddit.subreddit("all")
for submission in subreddit.stream.submissions(skip_existing=True):
    try:
        process_content(submission, reddit)
    except Exception as e:
        print(f"Error processing submission: {e}")

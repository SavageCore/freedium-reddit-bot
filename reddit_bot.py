import praw # type: ignore
import re


# Function to initialize Reddit instance
def initialize_reddit():
    try:
        reddit = praw.Reddit()
        print(
            f"Authenticated as {reddit.user.me()}"
        )  # Print bot's username to verify authentication
        return reddit
    except Exception as e:
        print(f"Exception: {e}")
        raise  # Re-raise any other exceptions for further handling


# Function to generate Freedium link
def generate_freedium_link(medium_url):
    return f"https://freedium.cfd/{medium_url}"


# Function to process content (comments, submissions, and text posts)
def process_content(content, reddit):
    try:
        # Check if the content is removed or deleted
        if content.author is None:
            return

        # Skip if the content is posted by the bot itself
        if content.author.name == reddit.user.me().name:
            return

        # List to store all found Freedium links
        freedium_links = []

        if isinstance(content, praw.models.Comment):
            medium_links = re.findall(r"(https?://medium\.com[^\s]+)", content.body)
        elif isinstance(content, praw.models.Submission):
            if content.is_self:  # Check if submission is a text post
                medium_links = re.findall(
                    r"(https?://medium\.com[^\s]+)", content.selftext
                )
            else:  # It's a link post
                medium_links = re.findall(r"(https?://medium\.com[^\s]+)", content.url)
        else:
            print("Unsupported content type")
            # Print all attributes of the content object for debugging
            print(dir(content))
            return

        # Generate Freedium links for each Medium link found
        for link in medium_links:
            freedium_link = generate_freedium_link(link)
            freedium_links.append(freedium_link)

        # If there are Freedium links found, construct reply text
        if freedium_links:
            reply_text = (
                f"Here {'is a' if len(freedium_links) == 1 else 'are'} "
                f"[Freedium](https://github.com/Freedium-cfd) {"link" if len(freedium_links) == 1 else "links"} "
                "to bypass the Medium paywall:\n\n"
            )

            reply_text += "\n\n".join(freedium_links)
            reply_text += "\n\nI am a bot. If you have any feedback or suggestions, please contact my creator u/SavageCore or post an issue on [GitHub](https://github.com/SavageCore/freedium-reddit-bot)"

            # Reply with the constructed message
            content.reply(reply_text)

    except Exception as e:
        print(f"Error processing content: {e}")

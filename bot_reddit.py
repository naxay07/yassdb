import praw
from dotenv import load_dotenv
import os

load_dotenv()

def redditPostScrape():
    reddit = praw.Reddit(
        client_id=os.getenv("reddit_id"),
        client_secret=os.getenv("reddit_secret"),
        user_agent="Reddit scraper bot experiment via PRAW by u/naxaypu",
    )

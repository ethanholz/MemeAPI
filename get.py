import praw
import time
import config

def loginToReddit():
    try:
        print("* Logging into Reddit...")
        reddit = praw.Reddit(client_id=config.client_id,
                             client_secret=config.client_secret,
                             password=config.password,
                             user_agent='meme api by jaychandra'
                             , username=config.username)
        print("* Login successful!")
        return reddit
    except:
        print('* Login failed!')

reddit = loginToReddit()

def main():
    try:
        json_string = {}
        while(True):
            submission = reddit.subreddit(config.subreddits).random()
            if submission.score > 250: #upvotes > 250
                json_string = {
                            "title" : submission.title,
                            "subreddit" : str(submission.subreddit),
                            "author" : str(submission.author),
                            "upvotes" : submission.score,
                            "nsfw" : submission.over_18,
                            "url" : submission.url
                }
                break
            else:
                print("* Fetching new submission...")
                time.sleep(1)

        return json_string
    except Exception as e:
        print("* Something went wrong!")
        print(e)

if __name__ == "__main__":
    main()

### MemeAPI using flask and praw

#### Install praw and flask using the following commands

```
pip install praw
pip install flask
```

#### Run the server using the following command

open the config.py file and add your reddit credentials into it.
```
python app.py
```

#### Usage:

to get one meme: ```localhost:5000``` this fetches memes from default list available in config.py file

to get more than one meme: ```localhost:5000/{number of memes you want}```

to get from different subreddits: ```localhost:5000/{subreddits}/{number of memes you want}```

to get from different subreddits with upvotes limit: ```localhost:5000/{subreddits}/{number of upvotes}/{number of memes you want}```

while passing multiple subreddits via URL, you need to make sure that there are no spaces in between the subreddit names. For example, ```memes + dankmemes + me_irl``` doesn't work, it will throw an error. You should use something like this. ```memes+dankmemes+me_irl"```


you can also find the live version of this API here

fetch only one meme https://memeapi.pythonanywhere.com

fetch more than one meme https://memeapi.pythonanywhere.com/3

fetch from different subreddits https://memeapi.pythonanywhere.com/memes+dankmemes+pewdiepiesubmissions/5

fetch from different subreddits with upvote limit https://memeapi.pythonanywhere.com/memes+dankmemes+pewdiepiesubmissions/500/5

Here's how it looks when ran correctly
![img file](https://github.com/jaychandra6/MemeAPI/blob/main/screenshot.png)

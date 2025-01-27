import praw
#from kafka import kafkaProducer
from dotenv import load_dotenv
import os
import json
import pandas as pd
import psycopg2

load_dotenv()

with open('pw.txt','r') as f:
    pw = f.read()

reddit = praw.Reddit(
    client_id = os.getenv('CLIENT_ID'),
    client_secret = os.getenv('CLIENT_SECRET'),
    password = pw,
    user_agent = 'reddit_etl',
    username = 'py_scripter'
)

print(f"Authenticated as :{reddit.user.me()}")

#subreddit = reddit.subreddit('datascience')

def extract_from_reddit(ds_subreddit):
    
    subreddit = reddit.subreddit(ds_subreddit)

    post_id = []
    post_title = []
    post_url = []
    selftext = []
    author = []
    author_fullname = []
    event_time = []
    permalink = []
    score = []
    votes = []
    no_of_comments = []
    subreddit_type = []
    original_content = []
    video = []

    for post in subreddit.hot(limit=None):
        post_id.append(post.title)
        post_title.append(post.title)
        post_url.append(post.url)
        selftext.append(post.selftext)
        author.append(post.author)
        author_fullname.append(post.author_fullname)
        event_time.append(post.created_utc)
        permalink.append(post.permalink)
        score.append(post.score)
        votes.append(post.upvote_ratio)
        no_of_comments.append(post.num_comments)
        subreddit_type.append(post.subreddit_type)
        original_content.append(post.is_original_content)
        video.append(post.is_video)

#print(f"Title:{post.title}, link:{post.url},id:{post.id},selftext:{post.selftext},author:{post.author},author_name{post.author_fullname},event_time:{post.created_utc},permalink:{post.permalink},score:{post.score},votes:{post.upvote_ratio},no.comments{post.num_comments},type:{post.subreddit_type}")


    post_dict = {
        'id':post_id,
        'title':post_title,
        'url':post_url,
        'content':selftext,
        'author':author,
        'full_name':author_fullname,
        'event_time':event_time,
        'relative_url':permalink,
        'score':score,
        'upvote_ratio':votes,
        'no_comments':no_of_comments,
        'subreddit_type':subreddit_type
    }

    post_df = pd.DataFrame(post_dict,columns=['id','title','url','content','author','full_name',
                                              'event_time','relative_url','score','upvote_ratio','no_comments','subreddit_type']
                                              )

    print(post_df)

    post_df.to_csv('reddit.csv',index=False)

#producer = kafkaProducer(bootsrap_servers='',
#                         value_serializers=lambda v: json.dumps(v).encode('utf-8'))

#def fetch_and_load(subreddit_name):

    #subreddit = reddit.subreddit(subreddit_name)

#    for submission in subreddit.streams.submissions(skip_existing=True):
#        comments = {
#        'id':submission.id,
#        'title':submission.title,
#        'url':submission.url,
#        'content':submission.selftext,
#        'author':submission.author,
#        'full_name':submission.author_fullname,
#        'event_time':submission.created_utc,
#        'relative_url':submission.permalink,
#        'score':submission.score,
#        'upvote_ratio':submission.votes,
#        'no.comments':submission.num_comments,
#        'subreddit_type':submission.subreddit_type
#        }



if __name__=="__main__":
    extract_from_reddit("datascience")



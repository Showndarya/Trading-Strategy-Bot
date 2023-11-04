import praw
import csv

reddit = praw.Reddit(
    client_id='',      
    client_secret='',  
    user_agent='',        
    username='',    
    password=''      
)
#sample query testing
# Fetch the top 10 posts from the Python subreddit
# top_posts = reddit.subreddit('Python').top(limit=10)

# for post in top_posts:
#     print(post.title)

#subreddit query testing
# subreddit = reddit.subreddit('investing')
# posts = []
# for post in subreddit.hot(limit=1000):  # Adjust the limit as needed
#     posts.append([post.title, post.selftext])

# for post in posts:
#     print(post)

keywords = []
with open('keywords.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        keywords.append(row[0]) 

subreddits = []
with open('subreddits.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        subreddits.append(row[0])

with open('reddit_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['keyword', 'subreddit', 'title', 'content', 'score', 'top_comment_1', 'top_comment_2', 'top_comment_3']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    seen_posts = set()

    for subreddit_name in subreddits:
        #print(subreddit_name)
        subreddit = reddit.subreddit(subreddit_name)
        
        for keyword in keywords:
            #print(keyword)
            search_results = subreddit.search(keyword, limit=10) 
            
            for post in search_results:
                if post.id in seen_posts or not post.is_self:
                    continue 
                
                seen_posts.add(post.id)

                post.comments.sort = 'top'
                post.comment_limit = 3
                post.comments.replace_more(limit=0) 
                comments = post.comments[:3]

                writer.writerow({
                    'keyword': keyword,
                    'subreddit': subreddit_name,
                    'title': post.title,
                    'content': post.selftext,
                    'score': post.score,
                    'top_comment_1': comments[0].body if len(comments) > 0 else '',
                    'top_comment_2': comments[1].body if len(comments) > 1 else '',
                    'top_comment_3': comments[2].body if len(comments) > 2 else ''
                })
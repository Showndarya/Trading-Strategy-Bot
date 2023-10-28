import praw

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

subreddits = ["investing", "stocks", "wallstreetbets", "Forex", "options"]
keywords = ["strategy", "logic", "prediction", "probability"]

for subreddit_name in subreddits:
    print(f"Searching in r/{subreddit_name}:")
    
    subreddit = reddit.subreddit(subreddit_name)
    
    for keyword in keywords:
        print(f"\nPosts with the keyword '{keyword}':")
        search_results = subreddit.search(keyword, limit=10)
        
        for post in search_results:
            print(f"{post.title} (Score: {post.score})")
        
        print("-" * 40)
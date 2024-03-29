"""Design Tweet
- 這題不是自己做的，但是總體來說最難的是取出10筆最新的關注內容
- 透過存入的時候增加時間戳訊息可以達到
"""
import heapq

class Twitter:
    def __init__(self):
        #Tracks all users of twitter. Key is the user, value is a set the user follows
        
        self.users = {} 
        #Maps users to all tweets they've made. Tweets are a tuple where we track recency of tweet with the
        #tweet counter below, and the actual tweet ID
        
        self.tweets = {}
        
        #Tracks all tweets being made on twitter. Python doesn't have max heap so we use a negative to record.
        #Every time a tweet is made, tweet_counter is decremented. The most recent tweet will be the most
        #negative number we see. If you use a max heap, this would be the greatest number from a positive,
        #but we use negatives since we can't do max heaps
        self.tweet_counter = -1
        
    def postTweet(self, userId, tweetId):
        #Check if this user exists in our running users and tweets list, since both contains users as keys.
        #If not, just add them with None values for their keys
        if userId not in self.users:
            self.users[userId] = set()
        if userId not in self.tweets:
            self.tweets[userId] = []
        
        #Get list of tweets this user has made. This will be a list of tuples.
        list_of_tweets = self.tweets[userId]
        
        #The tuple consists of tweet counter on twitter itself, and tweetId. We use tweet counter
        #so that we can order tweets from least to most recent to dispaly on our feed.
        new_tweet = (self.tweet_counter, tweetId)
        list_of_tweets.append(new_tweet)
        
        #Assign the updated list to the user in the tweets dictionary, and decrement our running counter
        #by 1 since a new tweet has been made
        self.tweets[userId] = list_of_tweets
        self.tweet_counter -= 1

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        
        #Edge case. User should not follow themselves.
        if followerId == followeeId:
            return
        
        #If the user is already on twitter
        if followerId in self.users:
            #Get the users this person follows. This will be a set
            followed = self.users[followerId]
            #Add the new followee to the set
            followed.add(followeeId)
            #Update the set with the new followee added
            self.users[followerId] = followed
        else:
            #Create the user in the users dictionary with an empty set
            self.users[followerId] = set()
            #Get the set you just created. Will be empty
            followed = self.users[followerId]
            #Add the followee to this set now.
            followed.add(followeeId)
            #Update the set with the new followee added
            self.users[followerId] = followed
            
    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        #First check if the followerId is a user on twitter
        if followerId in self.users:
            #Get the users this person follows. This will be a set
            followed = self.users[followerId]
            #Now check the user actually follows this followee
            if followeeId in followed:
                followed.remove(followeeId)
                #Update the set with the followee deleted
                self.users[followerId] = followed
        else:
            #Create the user in the users dictionary with an empty set. Since nothing to remove, just return after.
            self.users[followerId] = set()
    def getNewsFeed(self, userId: int):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        heap = []
        #First check to see if the user themselves have made tweets in the tweet dictionary. If so, add to
        #our running heap
        if userId in self.tweets:
            my_tweets = self.tweets[userId]
            for tweet_number, tweet_Id in my_tweets:
                heapq.heappush(heap, (tweet_number, tweet_Id))
        
        #Now check what users this person follows. Add their tweets to our heap too
        if userId in self.users:
            my_followed = self.users[userId]
            for followed in my_followed:
                if followed in self.tweets:
                    their_tweets = self.tweets[followed]
                    for tweet_number, tweet_Id in their_tweets:
                        heapq.heappush(heap, (tweet_number, tweet_Id))
        
        #Our max heap now has all tweets we can have. We just now pop the 10 most recent one's. Since
        #it's a heap, we just keep popping it until it's empty, or if we have our max of 10
        return_list = []

        for i in range(len(heap)):
            if len(return_list) >= 10:
                break
            return_list.append(heapq.heappop(heap)[1])
        return return_list

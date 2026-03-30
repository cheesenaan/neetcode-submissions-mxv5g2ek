class Twitter:

    def __init__(self):
        self.following_dp = defaultdict(set) # user_id -> followings 
        self.tweets = defaultdict(list) # user_id : (time, tweet_id)
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count -= 1
        return

    def getNewsFeed(self, userId: int) -> List[int]:
        followers = self.following_dp[userId].copy()
        followers.add(userId)
        maxHeap = []
        res = []
        heapq.heapify(maxHeap)
        # get latest tweet for each follower and push to maxHeap
        for follower in followers:
            # index of latest tweet
            if self.tweets[follower]:
                follower_tweets = self.tweets[follower]
                idx = len(follower_tweets)-1
                time, tweet_id = follower_tweets[-1]
                heapq.heappush(maxHeap, [time, tweet_id, follower, idx-1])
        
        while len(res) < 10 and  maxHeap:
            time, tweet_id, user_id, idx = heapq.heappop(maxHeap)
            res.append(tweet_id)
            if idx >= 0:
                prev_time, prev_tweet_id = self.tweets[user_id][idx]
                heapq.heappush(maxHeap, [prev_time, prev_tweet_id, user_id, idx-1])
                
                
        return res                
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following_dp[followerId].add(followeeId)
        return 
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following_dp[followerId].discard(followeeId)
        return 

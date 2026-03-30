class Twitter:

    def __init__(self):
        self.follow_hp = defaultdict(set) # user_id -> array of user ids
        self.tweets = defaultdict(list) #  user_id -> (time, tweet_id)
        self.time = 0 # track timestamp 
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1
        return 
        

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.follow_hp[userId].copy()
        users.add(userId)

        maxHeap = []
        # Push all candidate tweets first
        for u in users:
            for t, tid in self.tweets[u][-10:]:  # last 10 tweets per user
                heapq.heappush(maxHeap, (-t, tid))

        # Pop top 10 most recent
        res = []
        for _ in range(min(10, len(maxHeap))):
            res.append(heapq.heappop(maxHeap)[1])

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_hp[followerId].add(followeeId)
        return

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            if followeeId in self.follow_hp[followerId]:
                self.follow_hp[followerId].remove(followeeId)
        return 
        

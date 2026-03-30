from collections import defaultdict
import heapq
from typing import List

class Twitter:
    def __init__(self):
        # global counter to timestamp tweets
        # we decrement to make newest tweets have smallest count (min-heap will pop them first)
        self.count = 0  

        # store user tweets: userId -> list of [count, tweetId]
        self.tweetMap = defaultdict(list)  

        # store followees: userId -> set of followeeId
        self.followMap = defaultdict(set)  

    def postTweet(self, userId: int, tweetId: int) -> None:
        # append the tweet with current timestamp
        self.tweetMap[userId].append([self.count, tweetId])

        # decrement counter so newest tweets have smallest count
        self.count -= 1  

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Return the 10 most recent tweetIds in the user's news feed.
        News feed includes tweets by the user and all followees.
        """

        res = []
        minHeap = []

        # make sure the user follows themselves
        self.followMap[userId].add(userId)

        # push the most recent tweet from each followee into the heap
        for followeeId in self.followMap[userId]:
            if self.tweetMap[followeeId]:
                index = len(self.tweetMap[followeeId]) - 1  # start from most recent
                count, tweetId = self.tweetMap[followeeId][index]
                # heap entry: [count, tweetId, followeeId, index of previous tweet]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        # extract top 10 tweets from heap
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            # if followee has older tweets, push the next one into the heap
            if index >= 0:
                prev_count, prev_tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [prev_count, prev_tweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # add followee to follower's set
        if followerId != followeeId:  # cannot follow yourself
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # remove followee from follower's set if present
        if followerId != followeeId:
            self.followMap[followerId].discard(followeeId)

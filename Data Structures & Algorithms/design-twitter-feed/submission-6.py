class Twitter:
    timestamp = 0

    def __init__(self):
        self.tweets = {}
        self.followers = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = deque()
        if userId not in self.followers:
            self.followers[userId] = set([userId])
        self.tweets[userId].appendleft((Twitter.timestamp, tweetId))
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop()
        Twitter.timestamp += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for followee in self.followers[userId]:
            if followee not in self.tweets:
                continue
            for tweet in self.tweets[followee]:
                heapq.heappush(heap, tweet)
                if len(heap) > 10:
                    heapq.heappop(heap)
        res = deque()
        while heap:
            res.appendleft(heapq.heappop(heap)[1])
        return list(res)

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = set([followerId])
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in self.followers:
            self.followers[followerId] = set([followerId])
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        

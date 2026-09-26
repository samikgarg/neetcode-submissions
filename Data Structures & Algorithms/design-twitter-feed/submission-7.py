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
        self.tweets[userId].appendleft((Twitter.timestamp, tweetId, userId))
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop()
        Twitter.timestamp += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        maxHeap = []
        res = []
        pointers = {f : 0 for f in self.followers[userId] if f in self.tweets}
        for f in self.followers[userId]:
            if f not in pointers:
                continue
            heapq.heappush(minHeap, self.tweets[f][0])
            if len(minHeap) > 10:
                popped = heapq.heappop(minHeap)
                del pointers[popped[2]]
            pointers[f] += 1
            if pointers[f] >= len(self.tweets[f]):
                del pointers[f]

        for t in minHeap:
            newTweet = (-t[0], t[1], t[2])
            heapq.heappush(maxHeap, newTweet)
        
        while maxHeap and minHeap and len(res) < 10:
            curr = heapq.heappop(maxHeap)
            res.append(curr[1])
            if curr[2] not in pointers:
                continue
            nextTweet = self.tweets[curr[2]][pointers[curr[2]]]
            newTweet = (-nextTweet[0], nextTweet[1], nextTweet[2])
            heapq.heappush(maxHeap, newTweet)
            pointers[curr[2]] += 1
            if pointers[curr[2]] >= len(self.tweets[curr[2]]):
                del pointers[curr[2]]
    
        return res

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
        

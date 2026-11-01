class Twitter:

    def __init__(self):
        # view the 10 most recent tweets 
        # eeach users and tweets are identfied by the ids
        # soo ig users dictonarry ?? # user tweet dictionary and use freq for a heap of latest tweents 
        # recent so not 
        # users and the  user its following 

        # Follow list
        self.followDict = defaultdict(set)
        self.tweetlist = defaultdict(list)
        self.time = 0 # Tweet id : user Id 
        # problem 10 most recent post for each unique user??

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetlist[userId].append((self.time, tweetId))
        self.time += 1
            

    def getNewsFeed(self, userId: int) -> List[int]:
        # Get 10 most recent tweet at the recent simple 
        heap = []
        users = self.followDict[userId] | {userId}
        for user in users:
            for timestamp, tweetId in self.tweetlist[user]:
                heapq.heappush(heap, (timestamp, tweetId))

                if len(heap) > 10:
                    heapq.heappop(heap)
        return ([tweet for i,tweet in (sorted(heap,key=lambda x: x[0],reverse = True)) ])


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followDict[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followDict[followerId].discard(followeeId)

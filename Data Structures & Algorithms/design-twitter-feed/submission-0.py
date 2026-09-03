from collections import defaultdict
# what twitter feature has?
class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list) #{userId: [(time, tweetId), ...]}
        self.follows = defaultdict(set) #{FollowerId:{self.follows = defaultdict(set)}}
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time,tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # core function. 
        # get user list  :include me
        user_to_check = self.follows[userId] | {userId} 
        #fetch every tweets
        heap = []
        for user in user_to_check:
            for time, tweetId in self.tweets[user]:
                heapq.heappush(heap,(-time,tweetId))

        result = []
        while heap and len(result) <10:
            neg_time, tweet_Id = heapq.heappop(heap)
            result.append(tweet_Id)
        return result




        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
        

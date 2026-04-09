import time
class Twitter:

    def __init__(self):
        # acts as a tweet collection. contains tweets per user id
        # key = user_id
        # value = max heap of tweet ids. (tweedid, timestamp).
        self.tweetdb = {}

        # key = user_id
        # values = list of followees
        # shows all the people the user is following
        self.followingdb = {}



    def postTweet(self, userId: int, tweetId: int) -> None:
        # check if user's data is already present in the db
        usermh = self.tweetdb.get(userId)
        now = time.time()
        if usermh is None:
            usermh = []
            heapq.heapify(usermh)  # optional, empty list is already a heap

        heapq.heappush(usermh, [now, tweetId])

        self.tweetdb[userId] = usermh


    def getNewsFeed(self, userId: int) -> List[int]:
        # get a list of all the users the user is following
        followersList = self.followingdb.get(userId, set())

        # get user's own tweets & the tweets of the people the user is following. get the latest ones
        followersList.add(userId)

        feed = []
        heapq.heapify(feed)

        for follower in followersList:
            # get user's tweets
            tweets = self.tweetdb.get(follower, [])

            for tweet in tweets:
                timestamp, tweetid = tweet
                heapq.heappush(feed, [timestamp, tweetid])
            
                while (len(feed) > 10):
                    heapq.heappop(feed)
            
        res = []
        while feed:
            timestamp, tweetId = heapq.heappop(feed)
            res.append(tweetId)
        return res[::-1]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        # user follows, then we include followee's tweets to user's feed

        followingSet = self.followingdb.get(followerId, set())
        followingSet.add(followeeId)

        self.followingdb[followerId] = followingSet

        # now assign tweet
        # get tweets of the followee

        # ----- parking this for now, as Feed should be generated in real time for the sake of simplicity
        # followeeTweets = self.tweetdb.get(followeeId)
        # for tweet in followeeTweets:
        #     timestamp, tweetId = tweet
        # --------------------------


        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # remove followee from the set
        followingSet = self.followingdb.get(followerId, set())
        if followeeId in followingSet:
            followingSet.remove(followeeId)
        # update db
        self.followingdb[followerId] = followingSet
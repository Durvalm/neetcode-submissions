class Twitter:

    def __init__(self):
        """ each user has:
        posts,
        follows,
        """
        self.hashmap = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if not userId in self.hashmap:
            self.initialize_user(userId)
        self.hashmap[userId]['posts'].append(
            (self.time, tweetId)
        )
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """ Tricky 
        10 most recent posts from anyone the user is following or huimself

        we have all these lists per user:

        self.hashmap[userId][follows] : [3, 4, 7, 10, 5]
        self.hashmap[3]['posts'] : [(0, 233), (5, 277), (10, 300)]
        self.hashmap[userId]['posts] : [(1, 200), (6, 290), (12, 320)]

        we start at the end : heap add (12, 10)
        we store (neg_time, index, tweetId, uid)
        heap will return 12, we decrease current index by -1, so it points to 6, and add to the heap 6 at index 9
        """
        if userId not in self.hashmap:
            return []

        res = []
        heap = []

        # People whose tweets should appear:
        # everyone user follows + themselves
        users = set(self.hashmap[userId]['follows'])
        users.add(userId)

        for uid in users:
            if uid not in self.hashmap:
                continue

            posts = self.hashmap[uid]['posts']

            if posts:
                # Start at this user's most recent tweet
                index = len(posts) - 1
                time, tweetId = posts[index]

                # Python heap is min-heap, so negate time
                heapq.heappush(
                    heap,
                    (-time, tweetId, uid, index)
                )

        while heap and len(res) < 10:
            neg_time, tweetId, uid, index = heapq.heappop(heap)

            res.append(tweetId)

            # Move backward to this user's previous tweet
            index -= 1

            if index >= 0:
                time, tweetId = self.hashmap[uid]['posts'][index]

                heapq.heappush(
                    heap,
                    (-time, tweetId, uid, index)
                )

        return res


        

    def follow(self, followerId: int, followeeId: int) -> None:
        if not followerId in self.hashmap:
            self.initialize_user(followerId)

        if followeeId not in self.hashmap:
            self.initialize_user(followeeId)

        self.hashmap[followerId]['follows'].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.hashmap:
            return

        self.hashmap[followerId]['follows'].discard(followeeId)

    def initialize_user(self, userId):
        self.hashmap[userId] = {'posts': [], 'follows': set()}
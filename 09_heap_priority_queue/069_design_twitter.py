# [069_design_twitter] k-way heap merge news feed | invariant: O(F log F) feed query

from collections import defaultdict
import heapq
import unittest


# --- config ---------------------------------------------------------------

FEED_LIMIT = 10


# --- public api -----------------------------------------------------------

class Twitter:
    """In-memory microblog supporting posting, following, and top-10 feeds."""

    def __init__(self) -> None:
        self._clock = 0
        # invariant: each author's tweet list appends with strictly increasing _clock
        self._tweets: dict[int, list[tuple[int, int]]] = defaultdict(list)
        self._following: dict[int, set[int]] = defaultdict(set)

    def post_tweet(self, user_id: int, tweet_id: int) -> None:
        """Record a new tweet authored by user_id."""
        self._clock += 1
        self._tweets[user_id].append((self._clock, tweet_id))

    def get_news_feed(self, user_id: int) -> list[int]:
        """Return up to 10 most recent tweet IDs from user_id and their followees."""
        authors = self._following[user_id] | {user_id}
        max_heap: list[tuple[int, int, int, int]] = []

        for author_id in authors:
            posts = self._tweets.get(author_id)
            if not posts:
                continue
            last_idx = len(posts) - 1
            seq, tweet_id = posts[last_idx]
            heapq.heappush(max_heap, (-seq, author_id, last_idx, tweet_id))

        feed: list[int] = []
        while max_heap and len(feed) < FEED_LIMIT:
            _, author_id, idx, tweet_id = heapq.heappop(max_heap)
            feed.append(tweet_id)
            if idx > 0:
                prev_seq, prev_tweet = self._tweets[author_id][idx - 1]
                heapq.heappush(max_heap, (-prev_seq, author_id, idx - 1, prev_tweet))

        return feed

    def follow(self, follower_id: int, followee_id: int) -> None:
        """Subscribe follower_id to followee_id's tweets; ignores self-follows."""
        if follower_id != followee_id:
            self._following[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        """Unsubscribe follower_id from followee_id's tweets if present."""
        self._following[follower_id].discard(followee_id)


# --- tests ----------------------------------------------------------------

class TestTwitter(unittest.TestCase):
    def test_examples(self) -> None:
        twitter = Twitter()
        twitter.post_tweet(1, 5)
        self.assertEqual(twitter.get_news_feed(1), [5])
        twitter.follow(1, 2)
        twitter.post_tweet(2, 6)
        self.assertEqual(twitter.get_news_feed(1), [6, 5])
        twitter.unfollow(1, 2)
        self.assertEqual(twitter.get_news_feed(1), [5])

    def test_edges(self) -> None:
        twitter = Twitter()
        twitter.follow(1, 1)
        twitter.unfollow(1, 99)
        self.assertEqual(twitter.get_news_feed(1), [])

        for tweet_id in range(1, 13):
            twitter.post_tweet(2, tweet_id)
        twitter.follow(1, 2)
        twitter.post_tweet(1, 99)
        self.assertEqual(twitter.get_news_feed(1), [99, 12, 11, 10, 9, 8, 7, 6, 5, 4])


if __name__ == "__main__":
    unittest.main()

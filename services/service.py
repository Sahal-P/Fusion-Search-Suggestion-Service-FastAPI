import redis

redis_host = 'redis'  # Replace with your Redis host address
redis_port = 6379               # Replace with your Redis port


from pygtrie import Trie

class SearchSuggestion:
    def __init__(self):
        self.redis = redis.Redis(host=redis_host, port=redis_port)
        self.trie = Trie()

    def insert(self, keyword):
        self.trie[keyword] = True

        # Store the keyword in Redis for quick retrieval
        self.redis.sadd('keywords', keyword)

    def search(self, prefix):
        suggestions = []

        # Retrieve suggestions from Redis using prefix match
        # _keyword_set = self.redis.scan_iter(match=f"{prefix}*")
        keyword_set = self.redis.smembers('keywords')
        for keyword in keyword_set:
            if keyword.decode().startswith(prefix):
                suggestions.append(keyword.decode())

        # Retrieve suggestions from the trie using prefix match
        for suggestion in self.trie.values(prefix):
            suggestions.append(suggestion)

    # def search(self, prefix):
    #     suggestions = []

    #     # Retrieve suggestions from the trie
    #     for suggestion in self.trie.values(prefix):
    #         suggestions.append(suggestion)

    #     # If suggestions are not found in the trie, retrieve them from Redis
    #     if not suggestions:
    #         keyword_set = self.redis.scan_iter(match=f"{prefix}*")
    #         suggestions = [keyword.decode() for keyword in keyword_set]
        return suggestions

    def delete(self, keyword):
        if keyword in self.trie:
            del self.trie[keyword]

        # Remove the keyword from Redis
        self.redis.srem('keywords', keyword)
        
        
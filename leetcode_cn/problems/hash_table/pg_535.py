class Codec:
    hash_table = {}
    count = 0

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        self.count += 1
        self.hash_table[self.count] = longUrl
        return str(self.count)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.hash_table[int(shortUrl)]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

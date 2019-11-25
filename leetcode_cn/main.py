from leetcode_cn.problems.hash_table.pg_535 import Codec

url = 'http://www.leetcode.com/faq/?id=10'
c = Codec()
print(c.decode(c.encode(url)))
url = "https://leetcode.com/problems/design-tinyurl22222222222"
url2 = c.encode(url)
print(url2)
print(c.decode(url2))

# s = Solution()
# ans = s.minCost([[17, 2, 17], [16, 16, 5], [14, 3, 19]])
# print(ans)

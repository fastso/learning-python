from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        self.dfs(image, sr, sc, image[sr][sc], color)
        return image

    def dfs(self, image, sr, sc, old_color, new_color):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != old_color:
            return
        image[sr][sc] = new_color
        self.dfs(image, sr - 1, sc, old_color, new_color)
        self.dfs(image, sr + 1, sc, old_color, new_color)
        self.dfs(image, sr, sc - 1, old_color, new_color)
        self.dfs(image, sr, sc + 1, old_color, new_color)

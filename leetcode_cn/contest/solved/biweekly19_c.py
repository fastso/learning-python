class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minutes_angle = minutes / 60
        if hour == 12:
            hour -= 12
        hour_angle = (hour + minutes / 60) / 12

        ans = abs(minutes_angle - hour_angle) * 360
        if ans > 180:
            ans = 360 - ans

        return ans

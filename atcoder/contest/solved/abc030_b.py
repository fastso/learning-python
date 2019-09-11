n, m = map(int, input().split())

n += m/60
n_d = 360 * (n % 12 / 12)
m_d = 360 * (m / 60)

ans = abs(n_d - m_d)
print(ans if ans <= 180 else (360 - ans))

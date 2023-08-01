import sys

e, s, m = map(int, sys.stdin.readline().split())

#  (1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19)

e_count = 1
s_count = 1
m_count = 1

for i in range(15*28*19+1):
    if e_count == e and s_count == s and m_count == m:
        print(i+1)
        break
    e_count += 1
    s_count += 1
    m_count += 1
    if e_count > 15:
        e_count = 1
    if s_count > 28:
        s_count = 1
    if m_count > 19:
        m_count = 1

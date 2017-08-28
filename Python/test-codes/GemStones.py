N = input()
rocks = []
for _ in range(N):
    rocks.append(set(raw_input()))
gems = set.intersection(*rocks)
print(len(gems))
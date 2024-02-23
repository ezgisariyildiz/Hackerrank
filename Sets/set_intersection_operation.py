n = int(input())
english_subscribers = set(map(int, input().split()))

m = int(input())
french_subscribers = set(map(int, input().split()))

total_subscribers = english_subscribers.intersection(french_subscribers)

total = len(total_subscribers)

print(total)
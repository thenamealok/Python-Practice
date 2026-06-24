def find_oldest_age():
    people = list(map(int, input().split()))
    return max(people)

oldest = find_oldest_age()
print("Oldest Age is: ", oldest)
import collections


# deque를 이용한 LRU 구현
def solution(cacheSize, cities):
    elapsed = 0
    cache = collections.deque(maxlen=cacheSize)

    for city in cities:
        city = city.lower()
        if city in cache: # cache hit
            cache.remove(city)
            cache.append(city)
            elapsed += 1
        else:
            cache.append(city)
            elapsed += 5
    return elapsed


if __name__ == '__main__':
    cacheSizes = [3, 3, 2, 5, 2, 0]
    cities_lst = [
        ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul",
         "NewYork", "LA"],
        ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo",
         "Seoul"],
        ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul",
         "Rome", "Paris", "Jeju", "NewYork", "Rome"],
        ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul",
         "Rome", "Paris", "Jeju", "NewYork", "Rome"],
        ["Jeju", "Pangyo", "NewYork", "newyork"],
        ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
    ]

    for cacheSize, cities in zip(cacheSizes, cities_lst):
        print(cacheSize, cities, solution(cacheSize, cities))

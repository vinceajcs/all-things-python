"""Design a hit counter which counts the number of hits received in the past 5 minutes."""


class HitCounter:
    def __init__(self):
        self.times, self.hits = [0] * 300, [0] * 300  # 60 seconds * 5 (mins) = 300 seconds

    def hit(self, timestamp):
        index = timestamp % 300
        if self.times[index] != timestamp:  # timestamp is over 300 seconds (i.e., 301, 302...)
            self.times[index] = timestamp  # record timestamp
            self.hits[index] = 1  # reset hits
        else:
            self.hits[index] += 1

    def get_hits(self, timestamp):
        total = 0

        for i in range(300):
            if (timestamp - self.times[i] < 300):
                total += self.hits[i]

        return total

"""Design a log storage system."""


class LogSystem:
    def __init__(self):
        self.logs = []

    def put(self, id, timestamp):
        self.logs.append((tid, timestamp))

    def retrieve(self, s, e, gra):
        index = {'Year': 5, 'Month': 8, 'Day': 11,
                 'Hour': 14, 'Minute': 17, 'Second': 20}[gra]  # gra could be 'Year', 'Month', ...etc

        start = s[:index]
        end = e[:index]

        return [tid for tid, timestamp in self.logs if start <= timestamp[:index] <= end]


"""Another idea."""


# map of granularity to index at which the timestamp should be pruned for respective granularity
gmap = {'Year': 1, 'Month': 2, 'Day': 3, 'Hour': 4, 'Minute': 5, 'Second': 6}


class LogSystem:
    def __init__(self):
        self.lookup = {}

    def put(self, id, timestamp):
        t = tuple(timestamp.split(':'))
        self.lookup[t] = id

    def retrieve(self, s, e, gra):
        index = gmap[gra]     # prune from this index onwards
        s = tuple(s.split(':')[:index])
        e = tuple(e.split(':')[:index])

        result = []
        for t in self.lookup.keys():
            if s <= t[:index] <= e:
                result.append(self.lookup[t])
        return result

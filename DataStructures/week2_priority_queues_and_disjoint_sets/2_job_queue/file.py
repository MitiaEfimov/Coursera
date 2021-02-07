from collections import namedtuple

Worker = namedtuple("threads", ["id", "started_at"])

x = Worker(0, 0)
print(x.id)

x.id = 1

print(x.id)

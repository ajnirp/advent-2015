inp = '''Vixen can fly 19 km/s for 7 seconds, but then must rest for 124 seconds.
Rudolph can fly 3 km/s for 15 seconds, but then must rest for 28 seconds.
Donner can fly 19 km/s for 9 seconds, but then must rest for 164 seconds.
Blitzen can fly 19 km/s for 9 seconds, but then must rest for 158 seconds.
Comet can fly 13 km/s for 7 seconds, but then must rest for 82 seconds.
Cupid can fly 25 km/s for 6 seconds, but then must rest for 145 seconds.
Dasher can fly 14 km/s for 3 seconds, but then must rest for 38 seconds.
Dancer can fly 3 km/s for 16 seconds, but then must rest for 37 seconds.
Prancer can fly 25 km/s for 6 seconds, but then must rest for 143 seconds.
'''

class Reindeer:
    def __init__(self, speed, fly_time, rest_time):
        self.speed = speed # speed in km/s
        self.fly_time = fly_time # max possible flying time in s
        self.rest_time = rest_time # time reqd for rest in s
        self.flying = True # is the reindeer currently flying?
        self.flown = 0 # distance covered in km
        self.fly_time_left = fly_time
        self.rest_time_left = 0

    # returns the distance attained by the reindeer
    # after total_t seconds
    def fly(self, total_t):
        t = 0
        while t <= total_t:
            if not self.flying:
                t += self.rest_time
                self.flying = True
                continue
            time_left = total_t - t
            if time_left >= self.fly_time:
                self.flown += self.speed * self.fly_time
                self.flying = False
                t += self.fly_time
            else:
                self.flown += self.speed * time_left
                break

reindeer = []
for line in inp.split('.\n')[:-1]:
    split = line.strip().split()
    reindeer.append(Reindeer(int(split[3]), int(split[6]), int(split[-2])))

for r in reindeer:
    r.fly(2503)

print max(r.flown for r in reindeer) # 2660

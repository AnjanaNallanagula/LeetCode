from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        self.check_ins = defaultdict(list)
        self.check_outs = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id].append([stationName, t])

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        ls = self.check_ins[id]

        for i in range(len(ls)):
            station = ls[i][0]
            time = ls[i][1]
            self.check_outs[stationName].append([station, t - time])
            ls[i][0] = ""

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        sum1 = 0
        count = 0

        for station, time in self.check_outs[endStation]:
            if (station == startStation):
                sum1 += time
                count += 1
        
        avg = sum1 / count

        return avg

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
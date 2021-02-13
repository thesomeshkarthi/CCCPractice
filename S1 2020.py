N = int(input())
observations = []

for i in range(N):
    line = input().split()
    observation = {}
    observation["time"] = int(line[0])
    observation["pos"] = int(line[1])
    observations.append(observation)

def get_time(dict):
    return dict ['time']

observations.sort(key = get_time)

prevTime = None
prevPos = None
maxspeed = None


for observation in observations:
    currentTime = observation["time"]  
    currentPos = observation["pos"]

    if prevTime == None:
        prevTime = currentTime
        prevPos = currentPos
        continue

    timeDifference = currentTime - prevTime
    distance = abs(currentPos - prevPos)
    speed = distance/timeDifference

    if maxspeed == None or speed > maxspeed:
        maxspeed = speed

    prevTime = currentTime
    prevPos = currentPos

print(maxspeed)
    
    
    

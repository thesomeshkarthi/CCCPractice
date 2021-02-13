N = int(input())
swifts = []
semaphores = []

swiftScores = input().split()
semaphoreScores = input().split()


swiftScores_total = None
semaphoreScores_total = None
answer = 0

for i in range(N):

    if swiftScores_total == None:
        swiftScores_total = int(swiftScores[i])
    else:
        swiftScores_total = swiftScores_total + int(swiftScores[i])

    if semaphoreScores_total == None:
        semaphoreScores_total = int(semaphoreScores[i])
    else:
        semaphoreScores_total = semaphoreScores_total + int(semaphoreScores[i]) 

    if swiftScores_total == semaphoreScores_total:
        answer = i+1
        

print(answer)


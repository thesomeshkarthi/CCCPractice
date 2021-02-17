J = int(input())
A = int(input())
jersey = []
asize = []
arequest = []
matches = 0

for i in range(J):
    line = input()
    jersey.append(line)

for i in range(A):
    athleteinfo = input().split()
    athletesize = athleteinfo[0]
    athleterequest = int(athleteinfo[1])
    asize.append(athletesize)
    arequest.append(athleterequest)

for i in range(A):
    if jersey[arequest[i] - 1] <= asize[i]:
        if jersey[arequest[i] - 1] != "Taken":
            matches = matches + 1
            jersey[arequest[i] - 1] = "Taken"

print(matches)







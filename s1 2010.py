N = int(input())
scores = []


for i in range(N):
    line = input().split()
    R = int(line[1])
    S = int(line[2])
    D = int(line[3])
    score = {}
    score["value"] = 2*R+3*S+D
    score["name"] = line[0]
    scores.append(score)

def sort_value(dict):
    return dict['value']

scores.sort(key = sort_value, reverse = True)


print(scores[0]["name"])
if N != 1:
    print(scores[1]["name"])

    
    

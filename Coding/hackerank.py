import math

def mean(X):
    return sum(X) / len(X)

def std(X):
    var = 0
    m = mean(X)
    for i in range(len(X)):
        var += (X[i] - m) ** 2
    return math.sqrt(var / n)
    
def Pearson_corr(X,Y):
    tmp = 0
    mx = mean(X)
    my = mean(Y)
    stdx = std(X)
    stdy = std(Y)
    for i in range(len(X)):
        tmp += (X[i] - mx) * (Y[i] - my)
    return (tmp / (len(X) * stdx * stdy))

def get_rank(X):
    x_rank = dict((x, i+1) for i, x in enumerate(sorted(X)))
    return [x_rank[x] for x in X]
    
n = int(input().strip())

X = [float(x) for x in input().strip().split(" ")]

Y  = [float(y) for y in input().strip().split(" ")]

# print(mean(X), std(X))
# print(mean(Y), std(Y))
# print(round(Pearson_corr(X,Y),3))
rankx = get_rank(X)
ranky = get_rank(Y)

diff = [(rankx[i] - ranky[i]) for i in range(len(rankx))]
#print(diff)

d_square = [d**2 for d in diff]

r = 1 - 6 * sum(d_square) / (n * (n**2 - 1))
print(round(r,3))
    
n = int(input().strip())

X = [float(x) for x in input().strip().split(" ")]

Y  = [float(y) for y in input().strip().split(" ")]

# print(mean(X), std(X))
# print(mean(Y), std(Y))
# print(round(Pearson_corr(X,Y),3))
print(get_rank(X))
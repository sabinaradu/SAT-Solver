import fileinput

K = int(input())
N = int(input())
M = int(input())

edge = [[0 for i in range(N)] for j in range(N)]

for i in range(M):
	e = input()
	nod = e.split(" ")
	nod[0] = int(nod[0])
	nod[1] = int(nod[1])
	edge[nod[0] - 1][nod[1] - 1] = 1

res = ""
nr = 0
string = ""

#partea 1
for i in range(N):
	for j in range(N):
		string = "("
		if(edge[i][j] == 1):
			l = 1
			while l <= K:
				string = string + str((i + 1) * K - l + 1)
				string = string + "V"
				string = string + str((j + 1) * K - l + 1)
				string = string + "V"
				l = l + 1
			string = string[:-1]
			string = string + ")"
			res = res + string + "^"

string = ""

max_var = N * K

#partea 4
for j in range(0, max_var, K):
	string = "(" + "~"
	for i in range(0, K):
		string = string + str(j + 1 + i) + "V" + "~"
	string = string[:-2]
	string = string + ")"
	res = res + string + "^"

string = ""
i = 0
j = 0

#partea 2
while i < K:
	string = "("
	while j < N:
		string = string + str((j + 1) * K - i) + "V"
		j = j + 1
	j = 0
	string = string[:-1]
	string = string + ")"
	res = res + string + "^"
	string = ""
	i = i + 1


#partea 3
i = 0
j = 0
w = 0
while i < K:
	while j < N:
		w = j + 1
		while w < N:
			string = "(" + "~"
			string = string + str((j + 1) * K - i) + "V" + "~"
			string = string + str((w + 1) * K - i)
			string = string + ")" + "^"
			res = res + string
			w = w + 1
		w = 0
		j = j + 1
	j = 0
	i = i + 1
res = res[:-1]
print(res)
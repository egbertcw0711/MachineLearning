def question1(s, t):
	""" determine whether some anagram of t is a substr of s
	input: string s, string t
	output: True or False """

	# construct all possible consecutive substring sets in s
	length_s = len(s)
	substr = [s[i:j+1] for i in range(length_s) for j in range(i,length_s)]

	# check any of the substring in s is anagram of t
	for sstr in substr:
		for c in (range(65, 91) + range(97, 123)):
			if t.count(chr(c)) != sstr.count(chr(c)):
				break
			if c == 122:
				return True
	return False # no such substring

# below is the test case for question1
print('test question1 ...')
s = "udacity"
t = "ad"
print(question1(s,t)) # True

s = "Apple"
t = "elp"
print(question1(s,t)) # True
s = "Apple"
t = "ple"
print(question1(s,t)) # True

s = "MachineLearning"
t = "ML"
print(question1(s,t)) # False



def question2(a):
	""" find the longest palindromic substring contained in a
	input: string
	output: longest palindromic substring 
	NOTE: here if there exists more than one longest palindromic
	substring, the first one will be returned"""
	# speical cases
	if(len(a) == 0): return ""
	if(len(set(a)) == len(a)): return a[0]

	# general cases
	P = ""
	for i in range(len(a)):
		P += ("0"+a[i])
	P += "0"
	# print(P)
	# print('--------')
	center = 1 # center of the longest palindrome
	radius = 1 # the radius of the longest palindrome

	for i in range(2, len(P)-2):
		idx = 1
		# check the index is not out of the range and the chars are symmetric 
		while (i-idx >= 0 and i+idx <= len(P)-1):
			if(P[i-idx] != P[i+idx]):
				break
			else:
				idx += 1
		idx -= 1
		if(idx > radius):
			center = i
			radius = idx

	return P[center-radius+1:center+radius+1:2]

# below the test case for question2
print('\ntest question2 ...')
print(question2("substringnirtsbus")) # substringnirtsbus

print(question2("apple")) # pp

# special cases
print(question2("")) # []
print(question2("a")) # ["a"]
print(question2("pine")) # ["p"]



def question3(G):
	""" find MST within graph G
	input: adjacency list (graph)
	output: adjacency list (MST) """
	dics = {} # {val:[from, to]}
	for node_from in G:
		for node_to, value in G[node_from]:
			dics[value] = [node_from, node_to]
	sorted(dics.keys())
	# print(dics)
	result = {}
	for dist in dics:
		# if not form a circle
		result[dics[dist][0]] = [(dics[dist][1], dist)]
	return result

# test cases (the order does not matter)
print('\ntest question3 ...')
G = {}
print(question3(G)) # {}

G = {'A': [(None, None)]}
print(question3(G)) # {'A': [(None, None)]}

G = {'A':[('B',2)],
	'B': [('A',2)]}
print(question3(G)) # {'A': [('B', 2)]}

G = {'A':[('B',2)],\
	'B':[('A',2), ('C',5)],\
	'C':[('B',5)]}
print(question3(G)) # {'A':[('B',2)], 'B':[('C',5)]}

# test cycle in the graph
G = {'A':[('B',2)], 'B':[('A',2),('C',5)],\
		'C':[('B',5),('A',10)]}
print(question3(G)) # A-B-C


def question4(T, r, n1, n2):
	""" Find the least common ancester between two nodes on a bst.
	Inputs: T: matrix representation of a bst
			r: non-negative integer representing the root
			n1,n2: the value of the two nodes in no particular order
	"""
	if((n1 <= r and n2 >= r) or (n1 >= r and n2 <= r)):
		return r
	# print(r)
	children = [i for i, v in enumerate(T[r]) if v == 1]
	if(len(children) == 2):
		if(n1 < r and n2 < r):
			child = children[0]
		else:
			child = children[1]
	elif(len(children) == 0):
		child = None
	else:
		child = children

	lca = question4(T,child,n1,n2)
	return lca

# test cases
print('\ntest question4 ...')
print(question4([[0,1,0,0,0],
				 [0,0,0,0,0],
				 [0,0,0,0,0],
				 [1,0,0,0,1],
				 [0,0,0,0,0]],
				 3,1,4)) # 3
print("the correct answer should be 3\n ")
print(question4([[0,0,0,0,0],
				 [1,0,1,0,0],
				 [0,0,0,0,0],
				 [0,1,0,0,1],
				 [0,0,0,0,0]],
				 3,0,2)) # 1
print("the correct answer should be 1\n ")
print(question4([[0,0,0,0,0],
				 [1,0,1,0,0],
				 [0,0,0,0,0],
				 [0,1,0,0,1],
				 [0,0,0,0,0]],
				 3,4,2)) # 3
print("the correct answer should be 3\n ")
print(question4([[0,0,0,0,0],
				 [1,0,1,0,0],
				 [0,0,0,0,0],
				 [0,1,0,0,1],
				 [0,0,0,0,0]],
				 3,4,1)) # 3
print("the correct answer should be 3\n ")
print(question4([[0,0,0,0,0],
				 [1,0,1,0,0],
				 [0,0,0,0,0],
				 [0,1,0,0,1],
				 [0,0,0,0,0]],
				 3,1,2)) # 1
print("the correct answer should be 3\n ")


def question5(ll,m):
	""" Find the element in a singly linked list 
	that m element from the end
	Inputs: ll:the first nodeof a linked list
			m: mth number from the end.
	Output: the value of the node at that position
	Note: assuming all the inputs are valid and m is chosen 
		  correctly(i.e not out of the boundary of linked list)."""

	# find the length of the linked list
	length = 1
	tmp = ll
	while tmp.next != None:
		tmp = tmp.next

	# find the value of the node at the position	
	tmp = ll
	for i in range(length-m):
		tmp = tmp.next
	return tmp.data

# HOW TO WRITE THE TEST CASE ? #
# class Node(object):
# 	def __init__(self, data):
# 		self.data = data
# 		self.next = None




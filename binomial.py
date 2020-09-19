import math

def prob(n, p, N):
	return float((math.factorial(N)/(math.factorial(n)*math.factorial(N-n)))*(p**n)*((1-p)**(N-n)))

def infoMeasure(n, p, N):
	temp = prob(n, p, N)
	if temp==0 or temp==1:
		return float(0)
	else:
		return float(-math.log2(temp))

def sumProb(N, p):
	'''
	sumProb with enough large N will yield approximate
	sum of probability of geometric random variable == 1
	'''
	g = 0
	for i in range(1,N+1):
		g += prob(i,p,N)
	return float(g)

def approxEntropy(N, p):
	'''
	H(X) = sum(p(x)*I(x))
	'''
	H = 0
	for i in range(1,N+1):
		H += prob(i,p,N)*infoMeasure(i,p,N)
	return float(H)
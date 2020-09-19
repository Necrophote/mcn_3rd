import math

def prob(n, p, r):
	return float((math.factorial(n-1)/(math.factorial(r-1)*math.factorial(n-r)))*(p**r)*((1-p)**(n-r)))

def infoMeasure(n, p, r):
	temp = prob(n, p, r)
	if temp==0 or temp==1:
		return float(0)
	else:
		return float(-math.log2(temp))

def sumProb(N, p, r):
	'''
	sumProb with enough large N will yield approximate
	sum of probability of geometric random variable == 1
	'''
	g = 0
	for i in range(r,N+1):
		g += prob(i, p, r)
	return float(g)

def approxEntropy(N, p, r):
	'''
	H(X) = sum(p(x)*I(x))
	'''
	H = 0
	for i in range(r,N+1):
		H += prob(i,p,r)*infoMeasure(i,p,r)
	return float(H)
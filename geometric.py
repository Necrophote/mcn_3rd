import math

def prob(n, p):
	return float((1-p)**(n-1)*p)

def infoMeasure(n, p):
	temp = prob(n, p)
	if temp==0 or temp==1:
		return float(0)
	else:
		return float(-math.log2(prob(n, p)))

def sumProb(N, p):
	'''
	sumProb with enough large N will yield approximate
	sum of probability of geometric random variable == 1
	loop over decreasing sequence
	'''
	g = 0
	for i in range(1,N+1):
		g += prob(i, p)
	return float(g)

def approxEntropy(N, p):
	'''
	H(X) = sum(p(x)*I(x))
	approxEntropy(N, 0.5) ~ 2
	'''
	H = 0
	for i in range(1,N+1):
		H += prob(i,p)*infoMeasure(i, p)
	return float(H)
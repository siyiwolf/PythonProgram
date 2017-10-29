import math

PI = 3.1415926;
HIS_LEN = 2**14;
DELETE_NUM = 400;

def calcCircleValue(x):
	cValue = x**2*PI;
	return cValue;

def getHistogram(a):
	His = [0 for i in range(HIS_LEN)];
	for i in range(len(a)):
		index = a[i] % HIS_LEN;
		His[index] = His[index] + 1;

	startSum = 0;
 	i = 0;
	while(startSum < DELETE_NUM):
		startSum = startSum + His[i];
		i = i + 1;
	minValue = i;

	endSum = 0;
	i = 1;
	while(endSum < DELETE_NUM):
		endSum = endSum + His[-i];
		i = i + 1;
	maxValue = HIS_LEN - i;

	return [minValue, maxValue];

def add(x, y, f):
	return f(x) + f(y);

def addabs(a, b):
	return abs(a) + abs(b);
	
def evenfilter(a):
	return a % 2 == 0;

def not_empty(s):
	return s and s.strip();

def revert_com(x, y):
	if x > y:
		return -1;
	elif x < y:
		return 1;
	else:
		return 0;

def mylog(func):
	def wrapper(*args, **kw):
		print 'Call %s():' %func.__name__;
		return func(*args, **kw);
	return wrapper;

@mylog
def nowTime():
	print '2017-10-29';

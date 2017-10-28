#!/usr/bin/env python
#import python_p1 as myFun

#x = float(raw_input('Please input the dir:'));
#y = myFun.calcCircleValue(x);
#print "The circle Value is", y;

#data struct
#1. int float,
#i = 100;
#print i;
#i = 100.0;
#print i;
#print 12 + 3.4
#print 3.4 + 45

#2. string
#str = 'I\'m ok!';
#print str;
#str = 'Python World';
#str = raw_input('Please input your name:');
#welcome = 'Hello, %s' %(str);
#print welcome;

#3. list, tuple, dict and set
#a = [1, 2, 'Two', 'what', 9];
#a.append('what');
#print a;
#print 'The second value of Array a %d is' %(a[1]);
#print 'The last second value of Array a %d is' %(a[-2]);
#a.insert(3, 'one');
#print 'After insert the num one at the index 3 %s' %a;
#c = ['cOne', 'cTwo', 'cThree'];
#a.insert(3, c);
#print 'After insert the self at the index 3 %s' %a;
#print a;
#b = a[3];
#print 'The four value of Array a is %s' %b;
#print b;
#bPop = b.pop();
#aPop = a.pop();
#print 'After pop %s, the list b is %s' %(bPop, b);
#print 'After pop %s, the list a is %s' %(aPop, a);
#bPopA = b.pop(1);
#aPopA = a.pop(1);
#print 'After pop with parameter 1 %s, the list b is %s' %(bPop, b);
#print 'After pop with parameter 1 %s, the list a is %s' %(aPop, a);
#anum = len(a);
#bnum = len(b);
#print 'The length of listA is %d, and the length of listB is %d' %(anum, bnum);

#a[3] = 2;
#print 'After set the index3\'s value of a the a is %s' %(a);

#f = 3.1415926;
#sTuple = (f, 'Fxck', 23);
#a.insert(2, sTuple);
#a.append(f);
#print a;
#dDict = {'Jack':80, 'Mary':98, 'Kevin':100};
#a.append(dDict);
#print a;
#dDict['Jack'] = 89;
#print 'After set value based on Jack:%s' %a;
#kScorce = dDict.get('Kevin');
#print 'The Kevin\'s socrce is %d' %kScorce;
#mMary = dDict.pop('Mary');
#print 'The Mary\'s socrce is %d' %mMary;
#print 'After pop the Mary record, the number is %s' %dDict;

#aSet = set([3, 2, 5]);
#bSet = set([1, 2, 3]);
#addSet = aSet & bSet;
#print 'The and set between two set %s' %addSet;
#orSet = aSet | bSet;
#print 'The or set between two set %s' %orSet;

#a.append(addSet);
#a.append(orSet);

#for aIndex in a:
#	if type(aIndex) == int:
#		print 'The %d is int' %aIndex;
#	elif type(aIndex) == str:
#		print 'The %s is str' %aIndex; 
#	elif type(aIndex) == float:
#		print 'The %d is float' %aIndex;
#	elif type(aIndex) == tuple:
#		print aIndex;
#		print ' is tuple';
#	elif type(aIndex) == list:
#		print 'The %s is list' %aIndex;
#	elif type(aIndex) == dict:
#		print 'The %s is dict' %aIndex;
#	elif type(aIndex) == set: 
#		print 'The %s is set' %aIndex;
#	else:
#		print 'This is a invaild type!';

#4 function
# a. The common function
#a = abs(-0.4);

import python_p1 as myFun;
#a = range(320 * 256);
#print a;
#l = myFun.getHistogram(a);
#print l;
a = myFun.add(-9, 9, abs);
print a;
a = [1, 2, -5, 3, -9];
b = [3, -3, 9, -8, 9];

c = map(myFun.addabs, a, b);
print a;
print b;
print c;

d = reduce(myFun.addabs, a);
print a;
print d;

e = filter(myFun.evenfilter, a);
print a;
print e;

w='kwd wwd ww';
e = filter(myFun.not_empty, w);
print w;
print e;

#for a in 'ABCDEF':
#	print a;

#L = [];
#for i in range(0,11):
#	L.append(i**2);
#print L;



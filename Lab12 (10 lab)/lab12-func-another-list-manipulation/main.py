'''
lab12-func-another-list-manipulation
'''


def list_manipulation(func, l, param=2, **kwargv):
	result = []
    ## Your code goes here
	## Note that: `param` should be a list to use in map

	when = kwargv.get('when')
	how = kwargv.get('how')

	## Filter before ??
	if when == 'pre':
		if how == 'pos':
			l = list(filter(lambda x : x > 0, l))
		elif how == 'neg':
			l = list(filter(lambda x : x < 0, l))

	## Apply map
	result = list(map(lambda x: func(x, param), l))

	## Filter after ??
	if when == 'post':
		if how == 'pos':
			result = list(filter(lambda x : x > 0, result))
		elif how == 'neg':
			result = list(filter(lambda x : x < 0, result))

	return result


### You can observe how input is being treated ###
###      BUT DO NOT EDIT THE CODE BELOW!!      ###

## Two functions available. Both have 2 parameters
funcDict = {1 : lambda x,y: x+y, 2: lambda x,y: x-y}
func = int(input())

## Get list of data. 
data = list(map(lambda x: int(x), input().split(" ")))

param = int(input())

when, how = input().split()

if (when == "pre" or when == "post") and (how == "pos" or how == "neg"):
	print(list_manipulation(funcDict[func], data, param, when=when, how=how))
else:
	print(list_manipulation(funcDict[func], data, param))
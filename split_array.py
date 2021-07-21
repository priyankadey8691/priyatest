import math

# function "groupArrayElements" 
#
# splits array "arr" into "N" different segements of equal length
#
# @params:
#	 arr: array
#	 n: positive integer
#
# @return value:
#	 newarr: array

def groupArrayElements(arr, N):

	try: N=int(N); 
	except: return "Please enter a valid number."; 

	length=len(arr);

	# return the array as it is if N is 1 or N is greater than length
	if N < 2 or N > length+1: return arr;
	
	# declare variables
	i=0; newarr=[]; size=0;
	
	# if array can be equally divided
	if(length % N == 0):
		
		#calculate the size of each array
		size=math.floor(length / N);
		while i<length:
			j=i; i+=size;
			
			# extract the selected elements from arr and append in the newarr
			newarr.append(arr[slice(j, i)]);
	
	# if array can't be divided into equal length
	
	else:
		#calculate the size of each array except for the last one
		N-=1; size = math.floor(length / N);
		if (length%size==0): size-=1;
		while (i < size * N):
			j=i; i+=size;
			
			# extract the selected elements from arr and append in the newarr
			newarr.append(arr[slice(j, i)])
		
		# append the remainder elements combined in another array
		newarr.append(arr[slice(size * N,length+1)])
	
	# return the newarr as output array
	return newarr;


# call the function
print(groupArrayElements([1, 2, 3, 4, 5], 3));
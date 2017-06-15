import collections
def find_missing(arr1,arr2):
	
	#check if arr1 and two are empty
	if len(arr1)&len(arr2)==0:
		return 0
	#check if arr1 and arr2 are same
	if not set(arr1).symmetric_difference(set(arr2)):
		return 0
    #finds and returns missing number
	else:
		#creating sets from parameters 
		first_set = set(arr1)
		second_set = set(arr2)
		
        #returns missing number using Symmetric difference
		return list(first_set.symmetric_difference(second_set) )
	

	
"""
def main():
	#list1 = find_missing([2], [2])
	#list2 = find_missing([4, 6, 8], [4, 6, 8, 10])
	#list3 = find_missing([5, 4, 7, 6, 11, 66], [5, 4, 1, 7, 6, 11, 66])
	#print list2

	#find_missing([list1,list2,list3])

if __name__ == '__main__':
		main()
"""
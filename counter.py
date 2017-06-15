def find_missing(list_one, list_two):
	"""find_missing function
	find the missing number between two lists
	"""
	# check if both lists are empty
	if len(list_one) == len(list_two) == 0:
		return 0

	# check if both lists are similar
	if not set(list_one).symmetric_difference(set(list_two)):
		return 0
	else:
		return list(set(list_one).symmetric_difference(set(list_two)))[0]
# ============================================================================
# EOF
def main():
	#list1 = find_missing([2], [2])
	list2 = find_missing([4, 6, 8], [4, 6, 8, 10])
	#list3 = find_missing([5, 4, 7, 6, 11, 66], [5, 4, 1, 7, 6, 11, 66])
	print list2

	#find_missing([list1,list2,list3])

if __name__ == '__main__':
		main()

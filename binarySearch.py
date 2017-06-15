class BinarySearch(list):
	
	def __init__(self,len,step):
		""" Constructor.
		 Initializing the super class 
		 """
		 super(BinarySearch,self).__init__()
          
         #using len and step to populate class
		 for number in range(1,len+1):
		 	self.append(number*step)

		 #defining len attrib to be same as length of list from super class
		 self.len = len(self)

	#defining search method that performs binary search. 
	#Number to find = searchNumber
	def search (sel , searchNumber):
		"""
		Returns : dict of the form {'count':int,'index':int}
		          index of the search value 
		          and count to show binary iterations
		"""


		# first initialize the first and last indices plus count and index 
		first = 0
		last = len(self) - 1
		val_index = 0
		found = False
		count = 0 

		#checking if the search value is the 1st or last element
		if searchNumber == self[first]:
			val_index = first
			found = True
		elif searchNumber == self[last]:
			val_index = last
			found = True

		#check if search number is not in the list
		if searchNumber not in self:
			found = True
			val_index = -1
		#binary search algorithm using a while loop
		while first <= last and not found:
			mid_value = (first+last)//2
			if self[mid_value] == searchNumber:
				found = True
				val_index = mid_value
			else:
				#increment count when iteration occurs
				count += 1
				if searchNumber < self [mid_value]:
					last = mid_value - 1
				else:
					first = mid_value + 1

		return {'count':count , 'index': val_index}





		
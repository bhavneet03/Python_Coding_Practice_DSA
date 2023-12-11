class Solution:
    def romanToInt(self, s):
	    # use dictionary for value lookup
        dictionary = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        last_value = 0
        sum_of_value = 0
		# look at values from reverse (smallest to biggest)
        for char in reversed(s):
            current_value = dictionary[char]
			# only need to subtract if the current value is less than previous value
			# do not update last_value so we keep the larger last value
            if last_value > current_value:
                sum_of_value -=current_value
            else:
                sum_of_value +=current_value
                last_value = current_value
                
        return sum_of_value

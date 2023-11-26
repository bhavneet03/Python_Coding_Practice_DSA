class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if s == "":
            return 0
        # Starting index of window
        start = 0
        # Ending index of window
        end = 0
        # Maximum length of substring without repeating characters
        maxLength = 0
        # Set to store unique characters
        unique_characters = set()
        # Loop for each character in the string
        while end < len(s):
            if s[end] not in unique_characters:
                unique_characters.add(s[end])
                end += 1
                maxLength = max(maxLength, len(unique_characters))
            else:
                unique_characters.remove(s[start])
                start += 1
        return maxLength
		
		
def find_non_repeating_substring(input_str):
    output_length = 0
    longest_sub_str = ''
    len_str = len(input_str)
    index = 0
    while len_str != 1:
        l_str = ''
        for i in range(index, len(input_str)):
            if input_str[i] not in l_str:
                l_str = l_str + input_str[i]
            else:
                break
        
        sub_str_length = len(l_str)
        if sub_str_length >  output_length:
            output_length = sub_str_length
            longest_sub_str = l_str
        len_str = len_str -1
        index = index + 1
    return output_length,longest_sub_str
if __name__ == '__main__':
    input_str = raw_input("Please enter the string: ")
    sub_str_length, sub_str = find_non_repeating_substring(input_str)
    print ('Longest Substing lenght is "{0}" and the sub string is "{1}"'.format(sub_str_length, sub_str))```
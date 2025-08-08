# Given a string s, find the length of the longest substring without repeating characters.
# Example
# Input: s = "bbbbb"
# Output: 1
#
# Input: s = "pwwkew"
# Output: 3

def longest_substring(s):
    # Create a set to store unique characters
    char_set = set()

    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])

        # Update the max_length if the current window is larger
        max_length = max(max_length, right - left + 1)

    return max_length


# Test cases
print(longest_substring("bbbbb"))
print(longest_substring("pwwkew"))
print(longest_substring("abcabcbb"))
print(longest_substring(""))
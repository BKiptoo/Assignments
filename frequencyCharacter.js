// Given a string, find the first character that does not repeat anywhere in the string. Return None if all characters repeat.

// Input: "Hello"

// Output: "H"
// Input: "Swiss"
// Output: "w"

//time and  space complexity
// Time Complexity: O(n)
// Space Complexity: O(1)

function firstNonRepeatingCharacter(str) {
  const charCount = {};

  // Count occurrences of each character
  for (const char of str) {
    charCount[char] = (charCount[char] || 0) + 1;
  }

  // Find the first character that occurs only once
  for (const char of str) {
    if (charCount[char] === 1) {
      return char;
    }

    //example: "Enock"
    //Enock --> is the character
    // we check for the first character that occurs only once
    // and return it
    // we're checking if the character count is equal to 1
    // if it is, we return the character
    // if not return the next character
    //if the character is found repeatedly, we return null
  }

  return null;
}
console.log(firstNonRepeatingCharacter("Hello")); // Output: "H"
console.log(firstNonRepeatingCharacter("Swiss")); // Output: "w"
console.log(firstNonRepeatingCharacter("aabbccddee")); // Output: null
console.log(firstNonRepeatingCharacter("enoque")); // Output: "E"

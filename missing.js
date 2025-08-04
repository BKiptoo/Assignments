// Given a list containing n distinct numbers from 0 to n, find the missing number.

// Input: [3, 0, 1]

// Output: 2
// NOTE: No number limit

/** 
    * Time Complexity: O(n)
    * basic calculation of the sum of numbers from 0 to n
    * use the formula for the sum of the first n natural numbers
    * Using Arithmetic Progression (AP) formula
    * which is n * (n + 1) / 2
    * and subtract the sum of the numbers in the array from it
    * to find the missing number.
*/

function missingNumbers(nums) {
    let n = nums.length;
    let total = (n * (n + 1)) / 2;

    let actualSum = nums.reduce((acc, num) => acc + num, 0);
    return total - actualSum;
}

// output: 2
console.log(missingNumbers([3, 0, 1]));  //outpute 2


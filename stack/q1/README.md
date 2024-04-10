# 20. Valid Parentheses
Easy

Topics
Companies

Hint
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

## Solution

https://github.com/deleomike/leetcode-prep/blob/510093fcdb353c9fd254b70472fc4181d56bea05/stack/q1/solution.py#L1-L48
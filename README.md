# Top 20 LeetCode Problems for Software Engineering Interviews

A comprehensive collection of the 20 most commonly asked LeetCode problems in software engineering interviews, implemented with **optimal solutions**, **industry-standard coding practices**, and **detailed explanations**.

## Overview

This repository contains clean, efficient, and well-documented Python solutions to the most important LeetCode problems. Each solution includes:
- Complete problem description
- Detailed approach explanation
- Time and space complexity analysis
- Clean, PEP 8 compliant code with type hints
- Comprehensive test cases
- Multiple solution approaches where applicable

## Problem Categories

### Array & Hashing (5 problems)
| # | Problem | Difficulty | Time | Space | Key Technique |
|---|---------|-----------|------|-------|---------------|
| 1 | [Two Sum](01_two_sum.py) | Easy | O(n) | O(n) | Hash Map |
| 2 | [Best Time to Buy and Sell Stock](02_best_time_to_buy_sell_stock.py) | Easy | O(n) | O(1) | Min Tracking |
| 3 | [Contains Duplicate](03_contains_duplicate.py) | Easy | O(n) | O(n) | Hash Set |
| 4 | [Product of Array Except Self](04_product_of_array_except_self.py) | Medium | O(n) | O(1) | Prefix/Suffix Products |
| 5 | [Maximum Subarray](05_maximum_subarray.py) | Medium | O(n) | O(1) | Kadane's Algorithm |

### Two Pointers (3 problems)
| # | Problem | Difficulty | Time | Space | Key Technique |
|---|---------|-----------|------|-------|---------------|
| 6 | [Valid Palindrome](06_valid_palindrome.py) | Easy | O(n) | O(1) | Two Pointers |
| 7 | [3Sum](07_3sum.py) | Medium | O(n²) | O(1) | Sort + Two Pointers |
| 8 | [Container With Most Water](08_container_with_most_water.py) | Medium | O(n) | O(1) | Greedy Two Pointers |

### Sliding Window (2 problems)
| # | Problem | Difficulty | Time | Space | Key Technique |
|---|---------|-----------|------|-------|---------------|
| 9 | [Longest Substring Without Repeating Characters](09_longest_substring_without_repeating.py) | Medium | O(n) | O(k) | Sliding Window + Hash Set |
| 10 | [Minimum Window Substring](10_minimum_window_substring.py) | Hard | O(n+m) | O(m) | Sliding Window + Frequency Map |

### Stack (2 problems)
| # | Problem | Difficulty | Time | Space | Key Technique |
|---|---------|-----------|------|-------|---------------|
| 11 | [Valid Parentheses](11_valid_parentheses.py) | Easy | O(n) | O(n) | Stack Matching |
| 12 | [Min Stack](12_min_stack.py) | Medium | O(1) | O(n) | Auxiliary Stack |

### Linked List (3 problems)
| # | Problem | Difficulty | Time | Space | Key Technique |
|---|---------|-----------|------|-------|---------------|
| 13 | [Reverse Linked List](13_reverse_linked_list.py) | Easy | O(n) | O(1) | Iterative Reversal |
| 14 | [Merge Two Sorted Lists](14_merge_two_sorted_lists.py) | Easy | O(n+m) | O(1) | Dummy Node |
| 15 | [Linked List Cycle](15_linked_list_cycle.py) | Easy | O(n) | O(1) | Floyd's Algorithm |

### Trees (3 problems)
| # | Problem | Difficulty | Time | Space | Key Technique |
|---|---------|-----------|------|-------|---------------|
| 16 | [Invert Binary Tree](16_invert_binary_tree.py) | Easy | O(n) | O(h) | Recursive DFS |
| 17 | [Maximum Depth of Binary Tree](17_maximum_depth_binary_tree.py) | Easy | O(n) | O(h) | DFS/BFS |
| 18 | [Validate Binary Search Tree](18_validate_binary_search_tree.py) | Medium | O(n) | O(h) | In-order Traversal |

### Dynamic Programming (2 problems)
| # | Problem | Difficulty | Time | Space | Key Technique |
|---|---------|-----------|------|-------|---------------|
| 19 | [Climbing Stairs](19_climbing_stairs.py) | Easy | O(n) | O(1) | Fibonacci DP |
| 20 | [Coin Change](20_coin_change.py) | Medium | O(n×m) | O(n) | Bottom-up DP |

## How to Use

### Run Individual Solutions
Each file is self-contained with test cases:

```bash
# Run a specific solution
python 01_two_sum.py

# Expected output: "All test cases passed!"
```

### Run All Tests
```bash
# Run all solutions to verify correctness
for file in *_*.py; do
    echo "Testing $file..."
    python "$file"
done
```

##  Best Practices Demonstrated

### Code Quality
- **Type Hints**: All function signatures include type annotations
- **Docstrings**: Comprehensive Google-style docstrings for all classes and methods
- **PEP 8**: Strict adherence to Python style guidelines
- **Naming**: Descriptive variable and function names

### Problem-Solving Patterns
- **Multiple Approaches**: Many solutions include alternative implementations
- **Optimization**: Each solution uses the most efficient algorithm known
- **Edge Cases**: Extensive test coverage including edge cases
- **Complexity Analysis**: Clear time and space complexity annotations

### Software Engineering
- **Clean Code**: Readable, maintainable implementations
- **Modularity**: Helper functions where appropriate
- **Testing**: Comprehensive test suites for validation
- **Documentation**: Clear explanations of approach and trade-offs

## Study Guide

### Recommended Study Order
1. **Week 1**: Array & Hashing (Problems 1-5)
2. **Week 2**: Two Pointers + Sliding Window (Problems 6-10)
3. **Week 3**: Stack + Linked List (Problems 11-15)
4. **Week 4**: Trees + Dynamic Programming (Problems 16-20)

### Interview Preparation Tips
- Understand the **pattern** behind each solution
- Practice explaining your **thought process** out loud
- Focus on **time/space complexity** analysis
- Learn to recognize when to apply each technique
- Practice coding **without** an IDE first

## Key Algorithms & Data Structures

- **Hash Maps/Sets**: Fast lookups for O(1) access
- **Two Pointers**: Efficient array/string traversal
- **Sliding Window**: Substring/subarray problems
- **Stack**: LIFO operations and bracket matching
- **Linked Lists**: Pointer manipulation
- **Trees**: DFS, BFS, and tree properties
- **Dynamic Programming**: Optimal substructure and memoization

## Complexity Quick Reference

| Notation | Name | Example |
|----------|------|---------|
| O(1) | Constant | Hash map lookup |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Single array pass |
| O(n log n) | Linearithmic | Efficient sorting |
| O(n²) | Quadratic | Nested loops |
| O(2ⁿ) | Exponential | Recursive fibonacci |

## Additional Resources

- [LeetCode Official](https://leetcode.com/)
- [NeetCode Roadmap](https://neetcode.io/roadmap)
- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)
- [Python Time Complexity](https://wiki.python.org/moin/TimeComplexity)

## Notes

- All solutions use **Python 3.8+**
- Time complexities assume average case unless noted
- Space complexities exclude output arrays unless specified
- Some problems include bonus methods with alternative approaches

## ⭐ Why These 20 Problems?

These problems were selected based on:
1. **Frequency**: Most commonly asked in FAANG interviews
2. **Patterns**: Cover essential algorithmic patterns
3. **Foundation**: Build strong problem-solving fundamentals
4. **Scalability**: Techniques applicable to harder problems

## Contributing

Feel free to:
- Suggest optimizations
- Add alternative solutions
- Report bugs or issues
- Improve documentation

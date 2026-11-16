# Audio drill scripts (v1)

Voice: Kokoro `am_michael`, `lang="en-us"`, speed 1.0. Item format: cue, ticking answer gap, answer plus one-line reason. Python names are written exactly; they are spoken as: heapq = "heap Q", deque = "deck", a dot between names = "dot", pop(0) = "pop zero", popleft = "pop left". Tags: [V] verified, [U] unverified. Sources point to deck cards (CX-/SG-/PS-), facts in the source log (F-xx) or earlier items (AU-xxx). AU IDs are immutable.

## Episode 1. Lesson, then constraints to complexity

**Lesson (spoken first):**

- The lesson.
- The size of the input tells you which complexity the interviewer expects. So your first question is always: how big can N get?
- Here is the budget. Python runs roughly ten million simple steps a second. Ten million steps is comfortable. A hundred million is too slow.
- Now the ladder. Five rungs.
- Rung one. N up to about twenty. Exponential time is fine. Two to the twenty is about a million.
- Rung two. N up to about three hundred. Cubic time is fine. Three hundred cubed is twenty seven million.
- Rung three. N up to about five thousand. Quadratic time is fine. Five thousand squared is twenty five million.
- Rung four. N from a hundred thousand to a million. You need O of N, or O of N log N. Quadratic is dead.
- Rung five. N around a billion or more. You cannot even loop over it. You need O of log N, or constant time.
- Next, five rules for counting.
- One. Loops one after another add. Loops inside each other multiply.
- Two. Halving the problem each step gives log N.
- Three. Sorting costs O of N log N.
- Four. A hash set or hash map lookup is O of one on average. Checking membership in a list is O of N.
- Five. Slicing and joining copy the data, so they cost O of N.
- Last thing. Always say both time and space. Space is the extra memory you allocate, plus the depth of any recursion.
- That is the lesson. Now the questions.

| ID | Cue | Gap | Answer + reason | Source | Tag |
|---|---|---|---|---|---|
| AU-001 | N can be as large as one hundred thousand. What time complexity do you need? | 6s | O of N log N, or O of N. Quadratic would be ten billion steps. Far too slow. | SG-004; F-20 | [V] |
| AU-002 | N is at most twenty. What does that tell you? | 6s | Exponential time is acceptable. Two to the twenty is about a million. The problem probably wants you to try every subset. | SG-001; F-20 | [V] |
| AU-003 | N is at most five thousand. What is the slowest complexity that still passes? | 6s | Quadratic. O of N squared. That is twenty five million steps. | SG-003; F-20; F-21 | [V] |
| AU-004 | N is at most three hundred. What is the slowest complexity that still passes? | 6s | Cubic. O of N cubed. That is twenty seven million steps. | SG-002; F-20; F-21 | [V] |
| AU-005 | The input is sorted, and N can reach one billion. What complexity do you need? | 6s | O of log N. Binary search. A billion items takes only about thirty steps. | SG-005; F-13; F-20 | [V] |
| AU-006 | N can be one million. Is O of N log N fast enough? | 6s | Yes. Log of a million is about twenty. So that is twenty million steps. Fine. | SG-004; F-20 | [V] |
| AU-007 | N is ten thousand, and your solution is quadratic. Is that safe in Python? | 7s | No. That is a hundred million steps. Too slow for Python. Look for O of N log N. | F-20; F-21 | [V] |
| AU-008 | Roughly how many steps is N log N, when N is one hundred thousand? | 7s | About one point seven million. Log base two of a hundred thousand is about seventeen. | F-20 | [V] |
| AU-009 | You are asked for three numbers that sum to zero. N is at most three thousand. What does the limit tell you? | 8s | Quadratic is intended. Three thousand squared is nine million. Trying every triple is billions of steps, so cubic is out. | F-23; SG-013 | [V] |
| AU-010 | An array of one hundred thousand numbers. One hundred thousand range sum queries. Each query loops over its range. What is wrong, and what is the fix? | 8s | That is N times Q. Ten billion steps. Build prefix sums once. Then each query is O of one. Total is O of N plus Q. | CX-025; F-32 | [V] |
| AU-011 | N is one hundred thousand, and K is also up to one hundred thousand. Your solution is O of N times K. Good enough? | 7s | No. That is ten billion steps. You need O of N log K, or O of N. | F-20; F-12 | [V] |
| AU-012 | A grid of one thousand by one thousand cells. You visit every cell once. Is that fine? | 6s | Yes. That is one million cells. Linear in the number of cells. | F-20 | [V] |
| AU-013 | The interviewer says: use constant extra space. Which tools does that rule out, and what does it point to? | 8s | It rules out a hash map or a copy of the input. It points to two pointers, or working in place. | F-16; SG-013 | [V] |
| AU-014 | The input array is already sorted. What two ideas should come to mind? | 7s | Binary search, for O of log N. Or two pointers from both ends, for O of N with no extra memory. | SG-005; SG-013; F-13; F-16 | [V] |
| AU-015 | Why do we say a hash lookup is O of one on average, and not always? | 7s | Because of collisions. In the worst case, a lookup can cost O of N. In interviews, say O of one on average. | CX-009; F-05 | [V] |
| AU-016 | Your brute force is quadratic, and N is at most one thousand. Does it pass, and what do you say? | 8s | It passes. That is one million steps. Say so, state the complexity, then offer the faster idea anyway. | F-20 | [U] |

## Episode 2. Cue to pattern: hashing, two pointers, sliding window, stack

**Lesson (spoken first):**

- The lesson. Four patterns, and the signal for each.
- Hashing. The signal is: have I seen this before? Duplicates, counts, grouping, or finding a partner value in unsorted data. A hash set or hash map gives O of N time, and costs O of N space.
- Two pointers. The signal is a sorted array, a pair or triple to find, or comparing both ends of a sequence. One pointer at each end, moving inwards. O of N time, constant space.
- Sliding window. The signal is a contiguous run. A subarray or a substring, with a condition. Longest, shortest, or exactly K long. Both edges only move forward, so it is O of N.
- A window can be fixed size, when the length is given. Or variable size: grow on the right, shrink on the left.
- One warning. Sliding window on sums needs non negative numbers. With negatives, use prefix sums and a hash map.
- Stack. The signal is nesting, or the most recent unfinished thing. Brackets, undo, or the next greater element. Each item is pushed once and popped once, so it is O of N.
- For each cue, say the pattern, the time complexity, and why.

| ID | Cue | Gap | Answer + reason | Source | Tag |
|---|---|---|---|---|---|
| AU-101 | An unsorted list of numbers. Does any value appear more than once? | 6s | Hash set. O of N time, O of N space. You trade memory for instant lookups. | SG-012; CX-009; F-05; F-22 | [V] |
| AU-102 | Two words. Is one a rearrangement of the other? | 6s | Count the letters with a hash map. O of N time. Space is constant, because the alphabet is fixed. | F-05; F-22 | [V] |
| AU-103 | An unsorted list and a target. Find the two numbers that add up to the target. | 6s | Hash map, in one pass. For each number, look up its complement. O of N time, O of N space. | SG-012; F-05; F-30 | [V] |
| AU-104 | Same question, but the list is sorted, and you may only use constant extra space. | 7s | Two pointers from both ends. Sum too small, move the left pointer. Too big, move the right. O of N time, constant space. | SG-013; PS-002; F-16 | [V] |
| AU-105 | A list of words. Put the words that are anagrams of each other into groups. | 7s | Hash map, keyed by a signature of each word. The sorted letters, or the letter counts. O of N times K, where K is the word length. Add a log K factor if you sort. | F-05; F-22 | [U] |
| AU-106 | A list of numbers. Return the K values that occur most often. | 7s | Count with a hash map. Then keep a heap of size K, using heapq. O of N log K. Or bucket by frequency, for O of N. | SG-007; CX-024; F-12; F-34 | [V] |
| AU-107 | An unsorted list. Find the longest run of consecutive integers, in linear time. | 8s | Hash set. Only start counting from a number whose predecessor is missing. O of N time, O of N space. | F-33; F-22 | [U] |
| AU-108 | For every position, give the product of all the other elements. No division allowed. | 8s | Prefix and suffix products. One pass from the left, one from the right. O of N time. | F-32; F-22 | [V] |
| AU-109 | Is this phrase a palindrome, ignoring spaces and punctuation? | 6s | Two pointers, one at each end, moving inwards. O of N time, constant space. | F-16; F-22 | [V] |
| AU-110 | Find all unique triples in a list that sum to zero. | 8s | Sort. Fix one number. Then two pointers on the rest. O of N squared. The sort is cheaper, so it does not matter. | SG-013; CX-023; F-16 | [V] |
| AU-111 | A row of vertical lines of different heights. Pick two that hold the most water between them. | 8s | Two pointers from both ends. Always move the shorter line inwards. O of N time, constant space. | F-31; F-16 | [V] |
| AU-112 | The longest substring with no repeated character. | 6s | Variable sliding window with a set. Grow right. Shrink left while there is a repeat. O of N. | SG-006; PS-001; CX-012; F-14 | [V] |
| AU-113 | Daily share prices. Buy once, sell later. What is the best profit? | 7s | One pass. Track the lowest price so far, and the best profit against it. O of N time, constant space. | F-22 | [U] |
| AU-114 | Does a long string contain any rearrangement of a short pattern? | 8s | Fixed size sliding window, the length of the pattern, with letter counts. O of N. | F-15; F-22 | [V] |
| AU-115 | You may change at most K letters. Find the longest substring that can become all one letter. | 8s | Variable sliding window. The window is valid while its length, minus the count of its most common letter, is at most K. O of N. | F-14; F-22 | [U] |
| AU-116 | Find the shortest piece of a string that contains every character of a pattern. | 8s | Variable sliding window. Grow until it is valid. Then shrink to make it as small as possible. O of N plus M. | F-14; F-22 | [V] |
| AU-117 | Count the subarrays that sum to K. The numbers can be negative. | 8s | Not a sliding window. Negatives break it. Use prefix sums with a hash map. O of N time, O of N space. | SG-006; F-19 | [V] |
| AU-118 | A string of round, square and curly brackets. Is it properly nested? | 6s | Stack. Push each opener. Pop when its closer arrives. O of N time, O of N space. | SG-015; F-17 | [V] |
| AU-119 | Daily temperatures. For each day, how many days until a warmer one? | 8s | Monotonic stack of indices. Pop every day that today is warmer than. O of N, because each day is pushed once and popped once. | SG-015; F-18 | [V] |
| AU-120 | Evaluate an expression where each operator comes after its two numbers. | 7s | Stack. Push the numbers. On an operator, pop two, combine, and push the result. O of N. | F-17; F-22 | [V] |
| AU-121 | Design a stack that can also return its smallest element in constant time. | 8s | Store the minimum so far next to each element. Every operation stays O of one. | F-22 | [U] |

## Episode 3. Complexity of described code

**Lesson (spoken first):**

- list.append() and list.pop() are O of one. list.pop(0) is O of N.
- A collections.deque gives O of one at both ends. That is deque.append(), deque.appendleft(), deque.pop() and deque.popleft().
- Membership with the in operator is O of N on a list. On a set or a dict it is O of one on average.
- A slice copies, so it costs the length of the slice.
- sorted() and list.sort() are O of N log N.
- heapq.heappush() and heapq.heappop() are O of log N. heapq.heapify(), on a whole list, is O of N.
- Now the questions.

| ID | Cue | Gap | Answer + reason | Source | Tag |
|---|---|---|---|---|---|
| AU-201 | One loop over a list of N numbers, adding each to a running total. | 5s | Time O of N. Space O of one. One pass, one variable. | CX-001 | [V] |
| AU-202 | One loop finds the smallest value. Then a second, separate loop finds the largest. | 6s | Time O of N. Space O of one. Loops in sequence add. Two N is still O of N. | CX-002 | [V] |
| AU-203 | Two nested loops over the same list. The inner loop starts just after the outer index. | 6s | Time O of N squared. Space O of one. It is about half of N squared pairs, and the half does not count. | CX-003 | [V] |
| AU-204 | A while loop that halves a number, until it reaches zero. | 6s | Time O of log N. Space O of one. Halving each step gives log N steps. | CX-004 | [V] |
| AU-205 | A for loop over N items. Inside it, a binary search on a sorted list of N items. | 6s | Time O of N log N. N searches, at log N each. Space O of one. | CX-005; CX-011; F-13 | [V] |
| AU-206 | Make a sorted copy of a list with sorted(). Then one pass, comparing neighbors. | 7s | Time O of N log N. The sort dominates the pass. Space O of N, for the sorted copy. | CX-007; F-06; F-07 | [V] |
| AU-207 | A loop over N items. For each one, check if it is already in a list of seen items, then append it. | 7s | Time O of N squared. Membership in a list scans the whole list. Space O of N. | CX-008; F-02 | [V] |
| AU-208 | The same code, but seen items are kept in a set. | 6s | Time O of N on average. Set lookup is O of one on average. Space O of N. | CX-009; F-05 | [V] |
| AU-209 | A loop over a string of length N. On each step, take a slice from the current index to the end. | 7s | Time O of N squared. Each slice copies up to N characters. Pass indices instead. | CX-010; F-03 | [V] |
| AU-210 | Build a string of length N, by adding one character at a time, in a loop. | 7s | Treat it as O of N squared. Each addition builds a new string. Collect the pieces in a list and join once. That is O of N. | F-04 | [V] |
| AU-211 | An outer loop that runs N times. An inner loop that doubles a counter until it reaches N. | 7s | Time O of N log N. The inner loop runs log N times. Space O of one. | CX-011 | [V] |
| AU-212 | A for loop moves a right pointer across a string. Inside, a while loop moves a left pointer forward. The left pointer never moves back. | 8s | Time O of N. It looks nested, but each pointer moves forward at most N times. Two N in total. | CX-012; F-14 | [V] |
| AU-213 | A loop over N numbers. Each index is pushed on a stack. Before pushing, a while loop pops every smaller number. | 8s | Time O of N. Each index is pushed once and popped at most once. Space O of N for the stack. | SG-015; F-18 | [V] |
| AU-214 | A queue built on a plain Python list. A loop removes the front item N times, with list.pop(0). | 7s | Time O of N squared. list.pop(0) shifts every other item. Use a collections.deque. deque.popleft() is O of one. | F-01; F-08 | [V] |
| AU-215 | Call heapq.heapify() on a list of N numbers. | 6s | Time O of N. Not N log N. It works in place, so extra space is O of one. | CX-013; F-09 | [V] |
| AU-216 | Start with an empty list. Call heapq.heappush() N times, once for each number. | 6s | Time O of N log N. Each heapq.heappush() is O of log N. heapq.heapify() would do the same job in O of N. | CX-014; F-10; F-11 | [V] |
| AU-217 | Scan N numbers. Call heapq.heappush() for each one. Whenever the heap grows past K items, call heapq.heappop(). | 8s | Time O of N log K. The heap never holds more than K plus one items, and heapq.heappop() removes the smallest. Space O of K. | CX-024; PS-005; SG-007; F-12 | [V] |
| AU-218 | A loop over N words. Each word has K letters. Inside the loop, sort the letters of the word. | 8s | Time O of N, times K log K. N words, and each sort is K log K. | F-06 | [V] |
| AU-219 | Count the letters of a lowercase string of length N in a dictionary. Then loop over the twenty six letters. | 7s | Time O of N. Space O of one. The dictionary never holds more than twenty six keys. | CX-012; F-05 | [V] |
| AU-220 | Sort a list. Then for each element, sweep two pointers inwards over the rest of the list. | 8s | Time O of N squared. N sweeps of O of N each. The sort, at N log N, is the smaller term. | CX-023; F-16 | [V] |

## Episode 4. Mixed review

| ID | Cue | Gap | Answer + reason | Source | Tag |
|---|---|---|---|---|---|
| AU-301 | N goes up to two hundred thousand. Which complexities are acceptable? | 6s | O of N, or O of N log N. Nothing quadratic. | AU-001 | [V] |
| AU-302 | You need to know whether a list contains a duplicate. Pattern and complexity? | 6s | Hash set. O of N time, O of N space. | AU-101 | [V] |
| AU-303 | A loop of N steps. Each step asks whether a value is in a Python list of up to N items. | 6s | O of N squared. Membership in a list is O of N. Switch to a set. | AU-207 | [V] |
| AU-304 | Find the longest substring that contains at most two different letters. | 8s | Variable sliding window, with a hash map of letter counts. Shrink from the left when a third letter appears. O of N. | AU-112; F-14 | [V] |
| AU-305 | What does heapq.heapify() cost on N items? And what does calling heapq.heappush() N times cost? | 7s | heapq.heapify() is O of N. N calls to heapq.heappush() are O of N log N. | AU-215; AU-216 | [V] |
| AU-306 | N is at most eighteen. What kind of solution is being invited? | 6s | An exponential one. Try every subset. Two to the eighteen is about a quarter of a million. | AU-002 | [V] |
| AU-307 | A sorted array. Find the pair whose sum is closest to a target. Constant extra space. | 8s | Two pointers from both ends. Because the array is sorted, each move rules out a whole set of pairs. O of N time, constant space. | AU-104; F-16 | [V] |
| AU-308 | A function calls itself on the tail of a list, using a slice, N times. | 8s | O of N squared time. Each slice copies what is left. And O of N stack depth. Pass an index instead. | AU-209; F-03 | [V] |
| AU-309 | For each bar in a bar chart, find the next bar to the right that is taller. | 7s | Monotonic stack. O of N. Each bar is pushed once and popped once. | AU-119; F-18 | [V] |
| AU-310 | N is four thousand. You have a quadratic idea, and an N log N idea that is harder to code. Which is acceptable? | 8s | Both. Sixteen million steps is inside the budget. Say that, and start with the simpler one. | AU-003; F-21 | [U] |
| AU-311 | A queue loop takes items from the front of a plain list with list.pop(0). What is the hidden cost? | 7s | Each list.pop(0) is O of N. Use a collections.deque, and deque.popleft(), for O of one. | AU-214; F-08 | [V] |
| AU-312 | Find the highest average over any K consecutive numbers. | 7s | Fixed size sliding window. Add the new number, subtract the one that left. O of N time, constant space. | F-15; AU-114 | [V] |
| AU-313 | A sorted list of one billion numbers. How many steps does binary search need, roughly? | 6s | About thirty. Log base two of a billion. | AU-005 | [V] |
| AU-314 | Find the longest subarray that sums to K. The values can be negative. | 8s | Prefix sums with a hash map. Not a sliding window, because negatives break the shrink rule. O of N. | AU-117; F-19 | [V] |
| AU-315 | Sort N numbers with list.sort(), then loop over them once. Time and space? | 6s | Time O of N log N. Space up to O of N, because list.sort() can need a temporary buffer. | AU-206; F-07 | [V] |
| AU-316 | You see a while loop inside a for loop. When is the total still O of N? | 8s | When the inner loop's pointer only ever moves forward. Then it moves at most N times in total. Sliding windows and monotonic stacks both work this way. | AU-212; AU-213 | [V] |
| AU-317 | A stream of numbers. Keep track of the K largest seen so far. | 7s | A min heap of size K, using heapq. Each number costs O of log K. Space O of K. | AU-217; F-12 | [V] |
| AU-318 | N is five hundred, and your idea is cubic. Is that safe in Python? | 7s | Risky. That is one hundred and twenty five million steps. Cubic is safe up to about three hundred. | AU-004; F-21 | [V] |
| AU-319 | Check whether a line of code has matching brackets and braces. | 6s | Stack. O of N time, O of N space. | AU-118 | [V] |
| AU-320 | Group a list of words by their first letter. Pattern and complexity? | 6s | Hash map from letter to a list of words. O of N. | AU-105 | [V] |
| AU-321 | Second time. Membership test: list against set. | 5s | List is O of N. Set is O of one on average. | AU-303; F-02; F-05 | [V] |
| AU-322 | Second time. heapq.heapify() against N calls to heapq.heappush(). | 5s | heapq.heapify() is O of N. N calls to heapq.heappush() are O of N log N. | AU-305; F-09; F-11 | [V] |

## Episode 5. Binary search, and searching on the answer

**Lesson (spoken first):**

- The lesson.
- Binary search needs one thing: a yes or no question whose answer flips exactly once as you move along the range. Sorted data gives you that. So does any monotonic condition.
- Each step throws away half the range. So it is O of log N time, and O of one space when written as a loop.
- In Python, bisect.bisect_left() returns the first position where a value could be inserted and keep the list sorted. bisect.bisect_right() returns the position after any equal values.
- Three shapes to recognize.
- One. Find a value, or a boundary, in sorted data.
- Two. A sorted array that has been rotated. One half is always still sorted. Work out which half, and whether the target must be inside it.
- Three. Search on the answer. The question asks for the smallest value that works, or the largest value that works. You binary search the range of possible answers, and run a feasibility check each time.
- Search on the answer costs O of N log M. N for each check, and log M checks, where M is the size of the answer range.
- Now the questions.

| ID | Cue | Gap | Answer + reason | Source | Tag |
|---|---|---|---|---|---|
| AU-401 | A sorted list of a million numbers. Is a given number present? | 6s | Binary search. O of log N time, O of one space. About twenty steps. | SG-005; CX-005; F-13 | [V] |
| AU-402 | A sorted list with duplicates. Find the first position of a target value. | 7s | Binary search for the left boundary. In Python, bisect.bisect_left(). O of log N. | F-40 | [V] |
| AU-403 | How many values in a sorted list fall between a low bound and a high bound? | 8s | Two binary searches. bisect.bisect_left() for the low bound, bisect.bisect_right() for the high bound, and subtract. O of log N. | F-40 | [V] |
| AU-404 | A sorted array was rotated at an unknown point. Find its smallest element. | 8s | Binary search. Compare the middle with the right end. If the middle is bigger, the minimum is to the right. Otherwise it is at the middle or to the left. O of log N. | F-42 | [U] |
| AU-405 | The same rotated array. Find a target value. | 8s | Binary search. One half is always sorted. If the target lies inside the sorted half, keep that half. Otherwise keep the other. O of log N. | F-42 | [U] |
| AU-406 | A grid where every row is sorted, and each row starts above the end of the row before. Find a target. | 8s | Treat the grid as one long sorted list, and binary search it. O of log of M times N. | F-42; F-13 | [U] |
| AU-407 | Piles of bananas, and a deadline in hours. Find the slowest eating speed that still finishes in time. | 8s | Binary search on the answer. Search speeds from one up to the largest pile. Each check adds up the hours at that speed. O of N log M, where M is the largest pile. | SG-008; PS-004; F-41 | [V] |
| AU-408 | Packages must ship in order within D days. Find the smallest ship capacity that works. | 8s | Binary search on the answer. Search capacities from the heaviest package up to the total weight. Each check is one greedy pass. O of N, times the log of the total weight. | SG-008; F-41 | [V] |
| AU-409 | Split an array into K contiguous parts, so that the largest part sum is as small as possible. | 8s | Minimize the maximum. That phrase means binary search on the answer. Guess a limit, and greedily count how many parts you need. | SG-008; F-41 | [V] |
| AU-410 | What must be true for binary search on the answer to work? | 7s | The check must be monotonic. If a value works, every larger value works too. Or every smaller one. Then there is a single boundary to find. | SG-008; F-41 | [V] |
| AU-411 | You call bisect.insort() N times to keep a list sorted. What is the total cost? | 7s | O of N squared. The search is O of log N, but each insert shifts items, which is O of N. | F-40 | [V] |
| AU-412 | N is one billion. You can test whether any single value is good or bad, and all the good values come after the bad ones. How do you find the first good one? | 8s | Binary search over the range. About thirty tests. | SG-005; F-13 | [V] |
| AU-413 | A store keeps several timestamped values for each key. Return the value at or just before a given time. | 8s | A hash map from key to a list of timestamps. They arrive in increasing order, so each list is already sorted. Binary search it with bisect.bisect_right(). O of log N per lookup. | F-40; F-22 | [U] |
| AU-414 | Recursive binary search against a loop. What changes? | 7s | Time is the same, O of log N. The recursive version uses O of log N stack space. The loop uses O of one. | CX-005; CX-006 | [V] |
| AU-415 | An unsorted list, and you need one search. Should you sort first and binary search? | 7s | No. Sorting costs O of N log N. One linear scan is O of N. Sorting only pays off when you search many times. | F-06; F-13 | [V] |

## Episode 6. Linked list

**Lesson (spoken first):**

- The lesson.
- A linked list gives you O of one insert and delete once you hold the node, and O of N to reach a position. There is no index.
- Almost every linked list problem uses one of four moves.
- One. A dummy node in front of the head. Use it whenever the head itself might change. It removes the special cases.
- Two. Fast and slow pointers. Slow moves one step, fast moves two. When fast reaches the end, slow is at the middle. And if there is a cycle, they meet.
- Three. Reverse in place, with three names: previous, current and next. O of N time, O of one space.
- Four. Two pointers with a gap. Move one pointer N steps ahead, then move both. When the front one reaches the end, the back one is N from the end.
- Most answers are O of N time and O of one space. If you reach for a hash set, ask whether pointers alone can do it.
- Now the questions.

| ID | Cue | Gap | Answer + reason | Source | Tag |
|---|---|---|---|---|---|
| AU-501 | Reverse a singly linked list. | 6s | Three pointers. Previous, current and next. Point each node backwards as you walk. O of N time, O of one space. | F-43 | [V] |
| AU-502 | Does a linked list contain a cycle? | 6s | Fast and slow pointers. If they ever meet, there is a cycle. If fast reaches the end, there is not. O of N time, O of one space. | F-43 | [V] |
| AU-503 | Find the middle node of a linked list, in one pass. | 6s | Fast and slow pointers. When fast reaches the end, slow is at the middle. O of N time, O of one space. | F-43 | [V] |
| AU-504 | Merge two sorted linked lists into one. | 7s | A dummy node and a tail pointer. Attach the smaller head each time. O of N plus M time, O of one space. | F-43 | [V] |
| AU-505 | Remove the N-th node from the end, in one pass. | 8s | A dummy node, and two pointers with a gap of N. When the front pointer reaches the end, the back pointer sits just before the node to remove. O of N. | F-43 | [V] |
| AU-506 | Reorder a list so it goes: first, last, second, second last, and so on. | 8s | Three known moves. Find the middle with fast and slow. Reverse the second half. Then weave the two halves together. O of N time, O of one space. | F-43; F-22 | [V] |
| AU-507 | Is a linked list a palindrome? Use constant extra space. | 8s | Find the middle, reverse the second half, and compare the two halves. O of N time, O of one space. | F-43 | [V] |
| AU-508 | Copy a linked list where every node also has a random pointer. | 8s | A hash map from each original node to its copy. The first pass makes the copies. The second pass wires up next and random. O of N time, O of N space. | F-43 | [U] |
| AU-509 | Two numbers stored as linked lists, with the digits in reverse order. Add them. | 7s | Walk both lists together with a carry, building the result behind a dummy node. O of the longer length. | F-22 | [U] |
| AU-510 | Design a cache that evicts the least recently used item. Get and put must both be O of one. | 8s | A hash map plus a doubly linked list. The map finds the node. The list keeps the order of use. In Python, collections.OrderedDict does both. | F-54 | [U] |
| AU-511 | Merge K sorted linked lists. | 7s | A min heap holding the head of each list. Pop the smallest, then push its next node. O of N log K, where N is the total number of nodes. | F-46 | [V] |
| AU-512 | An array of N plus one numbers, each between one and N. Find the repeated number without changing the array, in constant space. | 8s | Treat each value as a pointer to the next index. A repeat creates a cycle. Fast and slow pointers find where the cycle starts. O of N time, O of one space. | F-43 | [U] |
| AU-513 | Why use a dummy node? | 6s | Because the head might change. With a dummy in front, inserting or deleting at the head is the same code as anywhere else. | F-43 | [V] |
| AU-514 | You already hold the node before the one you want to delete. What does the delete cost? | 7s | O of one. You re-point a single link. Finding that node in the first place is what costs O of N. | F-43 | [V] |
| AU-515 | Reach the K-th element of a linked list. What does it cost, and how does a Python list compare? | 7s | O of K for the linked list, because you must walk. A Python list is an array, so indexing is O of one. | F-43; F-01 | [V] |

## Episode 7. Trees

**Lesson (spoken first):**

- The lesson.
- A tree problem is almost always a traversal. So the first choice is depth first or breadth first.
- Depth first search, or DFS, uses recursion. Ask each child for an answer, combine, and return. Use it for depth, for paths, and for anything a subtree can report upwards.
- Breadth first search, or BFS, uses a collections.deque as a queue. Use it when the question talks about levels, or the nearest something.
- Both visit every node once, so time is O of N.
- Space is the part people get wrong. DFS uses O of H, the height of the tree. That is O of log N when the tree is balanced, and O of N when it is a single chain. BFS uses O of W, the widest level, which can be about half of all the nodes.
- A binary search tree, or BST, keeps smaller values on the left and larger values on the right. An in order traversal visits a BST in sorted order. Search, insert and delete are O of H.
- Now the questions.

| ID | Cue | Gap | Answer + reason | Source | Tag |
|---|---|---|---|---|---|
| AU-601 | Find the maximum depth of a binary tree. | 6s | DFS. The depth is one plus the larger depth of the two children. O of N time, O of H space. | CX-017; F-44 | [V] |
| AU-602 | Return the values of a tree level by level. | 7s | BFS with a collections.deque. Process one whole level per loop, using the length of the queue at the start of that level. O of N time, O of W space. | F-45 | [V] |
| AU-603 | What can you see when you look at a tree from its right side? | 7s | BFS, keeping the last node of each level. O of N. | F-45; F-22 | [V] |
| AU-604 | Flip a binary tree, left to right. | 6s | DFS. Swap the two children at every node. O of N time, O of H space. | F-44 | [V] |
| AU-605 | Find the longest path between any two nodes in a tree. | 8s | DFS that returns height. At each node, the best path through it is the left height plus the right height. Track the maximum as you go. O of N. | F-45 | [V] |
| AU-606 | Is a binary tree height balanced? | 7s | DFS that returns height, and reports failure as soon as two child heights differ by more than one. One pass. O of N. | F-45 | [V] |
| AU-607 | Is this tree a valid binary search tree? | 8s | DFS carrying a lower and an upper bound down to each node. Or an in order traversal, checking that the values strictly increase. O of N time, O of H space. | F-44 | [V] |
| AU-608 | Find the K-th smallest value in a binary search tree. | 7s | An in order traversal, which visits a BST in sorted order. Stop at the K-th node. O of H plus K. | F-44 | [V] |
| AU-609 | Find the lowest common ancestor of two values in a binary search tree. | 8s | Walk down from the root. If both values are smaller, go left. If both are larger, go right. Otherwise, this node is the answer. O of H time, O of one space. | F-44 | [U] |
| AU-610 | Search in a binary search tree. What does it cost, and what is the catch? | 7s | O of H. That is O of log N when balanced, but O of N when the tree is a chain. | F-44 | [V] |
| AU-611 | A recursive DFS on a tree of N nodes that is one long chain. How much space? | 7s | O of N. The call stack is as deep as the tree. | CX-017; F-44 | [V] |
| AU-612 | Are two trees identical? | 6s | DFS on both at once. The values match here, and the left pair and the right pair both match. O of N. | F-44 | [V] |
| AU-613 | Is one tree a subtree of another? | 7s | For each node of the big tree, run the identical tree check. O of N times M in the worst case. | F-44; F-22 | [U] |
| AU-614 | Rebuild a tree from its pre order and in order traversals. What does each one tell you? | 8s | Pre order gives the root first. In order tells you which values belong to the left subtree and which to the right. With a hash map of in order positions, it is O of N. | F-22 | [U] |
| AU-615 | The distance from the root to the nearest leaf. DFS or BFS? | 7s | BFS. It reaches the nearest leaf first and can stop there. DFS has to explore everything. | F-45 | [U] |
| AU-616 | Maximum path sum in a tree, where a path can start and end anywhere. | 8s | DFS that returns the best downward path from each node, ignoring negative branches. At each node, try joining left and right through it, and track the best overall. O of N. | F-45; F-22 | [U] |

## Episode 8. Heap, priority queue, and tries

**Lesson (spoken first):**

- The lesson.
- A heap answers one question fast: what is the smallest item right now? Reach for it when you need the minimum or the maximum again and again, while the set keeps changing.
- Python's heapq is a min heap. heapq.heappush() and heapq.heappop() are O of log N. Reading the smallest item, at index zero, is O of one. For a max heap, push negated values.
- Four heap shapes.
- One. Top K. Keep a min heap of size K to find the K largest. O of N log K.
- Two. K way merge. Put the head of each sorted list in the heap. O of N log K.
- Three. Two heaps for a running median. A max heap for the lower half, and a min heap for the upper half.
- Four. Scheduling. Always take the most urgent, or the earliest to finish.
- A heap is not sorted. Searching it for an arbitrary value is O of N.
- Last, a trie, spelled T R I E. It is a tree of characters, built for prefix questions. Insert and search cost O of L, the length of the word, however many words are stored.
- Now the questions.

| ID | Cue | Gap | Answer + reason | Source | Tag |
|---|---|---|---|---|---|
| AU-701 | Find the K-th largest number in an unsorted list. | 7s | A min heap of size K. The top of the heap is the answer. O of N log K. Quickselect is O of N on average, but O of N squared in the worst case. | SG-007; F-46 | [V] |
| AU-702 | Find the K points closest to the origin. | 8s | A max heap of size K, keyed on distance. The farthest of the K sits on top and gets evicted. O of N log K. With heapq, push negated distances. | F-46 | [V] |
| AU-703 | Why a min heap to find the K largest? | 7s | Because the smallest of your K candidates is the one to throw out. A min heap keeps exactly that one on top. | PS-005; F-46 | [V] |
| AU-704 | A stream of numbers. Report the median after each one arrives. | 8s | Two heaps. A max heap for the lower half, and a min heap for the upper half, kept within one of each other in size. O of log N to add. O of one to read the median. | F-46 | [V] |
| AU-705 | Merge K sorted lists, with N items in total. | 7s | A min heap holding one item from each list. O of N log K. In Python, heapq.merge() does this for you. | F-46; F-54 | [V] |
| AU-706 | A pile of stones. Repeatedly smash the two heaviest together. | 7s | A max heap. With heapq, push negated weights. Each round is O of log N. | F-46; F-22 | [V] |
| AU-707 | Meetings with start and end times. How many rooms are needed? | 8s | Sort by start time. Keep a min heap of end times. If the earliest end is at or before the next start, reuse that room. O of N log N. | F-46 | [V] |
| AU-708 | Tasks, with a cooldown between two runs of the same task. Find the shortest schedule. | 8s | Greedy, with a max heap of remaining counts. Always run the task with the most left. A queue holds the tasks that are cooling down. | F-46; F-22 | [U] |
| AU-709 | You need the three largest of a million numbers, once. What is the simplest Python call? | 7s | heapq.nlargest(), asking for three. It keeps a small heap, which beats sorting all million. | F-54 | [U] |
| AU-710 | Is a given value somewhere in a heap? What does it cost to find out? | 7s | O of N. A heap only orders a parent against its children. It is not sorted, so you have to scan. | F-46 | [V] |
| AU-711 | You have all N items up front and want a heap. Push them one by one, or call heapq.heapify()? | 7s | heapq.heapify(). It is O of N. Pushing one by one is O of N log N. | CX-013; CX-014; F-09; F-11 | [V] |
| AU-712 | A dictionary of words. Many queries ask: does any word start with this prefix? | 7s | A trie. Each query is O of L, the length of the prefix. | F-47 | [V] |
| AU-713 | Autocomplete. Return all stored words that begin with what the user typed. | 7s | A trie. Walk down the prefix in O of L, then collect everything below that node. | F-47 | [V] |
| AU-714 | A word search where a wildcard matches any single letter. | 7s | A trie with DFS. On a normal letter, follow one child. On a wildcard, try every child. | F-47; F-22 | [U] |
| AU-715 | A grid of letters, and a long list of words. Find every word that can be traced in the grid. | 8s | Put the words in a trie. Then DFS from each cell, walking the trie as you go. A dead prefix prunes the search at once, and one search serves all the words. | F-47 | [V] |

## Episode 9. Backtracking

**Lesson (spoken first):**

- The lesson.
- Backtracking is how you answer: give me all of them. All subsets, all permutations, all valid arrangements.
- The template is three steps. Choose. Explore. Un-choose. Add an option to the current path, recurse, then take it back off.
- It is a depth first search over a tree of decisions. So the cost is the size of that tree.
- Subsets. Each element is either in or out. That is two to the N subsets, and each one can take N to copy. O of N times two to the N.
- Permutations. N choices, then N minus one, and so on. O of N times N factorial.
- Extra space is the recursion depth and the current path. O of N, not counting the output.
- That is why the inputs are small. N around twenty or less for subsets. N around ten or less for permutations.
- If the question asks for the best one, or just a count, and not the full list, think dynamic programming instead.
- Now the questions.

| ID | Cue | Gap | Answer + reason | Source | Tag |
|---|---|---|---|---|---|
| AU-801 | Return every subset of a list of distinct numbers. | 7s | Backtracking. At each index, include the number or skip it. O of N times two to the N. | SG-010; CX-021; F-48 | [V] |
| AU-802 | Return every ordering of a list of distinct numbers. | 7s | Backtracking, with a used marker for each number. O of N times N factorial. | SG-010; CX-022; F-48 | [V] |
| AU-803 | Find all combinations that add up to a target. A number may be used more than once. | 8s | Backtracking with a start index. To reuse a number, recurse without advancing the index. Stop a branch as soon as the sum passes the target. | F-48 | [V] |
| AU-804 | All subsets again, but the input has duplicates and the output must not. | 8s | Sort first. Then, at each level of the recursion, skip a value that equals the one you just tried. | F-48; F-22 | [U] |
| AU-805 | N is at most fifteen, and the question asks for all valid groupings. What does that tell you? | 6s | Exponential time is expected. That is a backtracking problem. | SG-001; SG-010; F-20 | [V] |
| AU-806 | Does a word exist in a grid of letters, moving between neighboring cells without reusing a cell? | 8s | Backtracking DFS from each cell. Mark the cell as used, explore the four neighbors, then unmark it. Exponential in the length of the word. | F-48; F-22 | [V] |
| AU-807 | Place N queens on a board so that none attack each other. | 8s | Backtracking, one row at a time. Keep three sets: the used columns, and the two kinds of diagonal. Checking a square is then O of one. | F-48 | [V] |
| AU-808 | All the letter combinations for a phone number. | 7s | Backtracking, one digit per level. Up to four letters per digit, so O of N times four to the N. | F-48; F-22 | [U] |
| AU-809 | Split a string into pieces so that every piece is a palindrome. Return all the ways. | 8s | Backtracking over cut positions. Only recurse when the piece you just cut is a palindrome. Exponential, with up to two to the N ways to cut. | F-48; F-22 | [U] |
| AU-810 | Generate all valid strings of N pairs of brackets. | 8s | Backtracking. Add an opener while you have some left. Add a closer only when it would not outnumber the openers. | F-48; F-22 | [U] |
| AU-811 | What is pruning, and why does it matter? | 7s | Cutting off a branch as soon as it cannot lead to an answer. It does not change the worst case, but it is often the difference between passing and timing out. | F-48 | [U] |
| AU-812 | Backtracking or dynamic programming? The question asks how many ways there are to climb N stairs. | 7s | Dynamic programming. You need a count, not the list, and the same subproblems keep coming back. | SG-011; F-48 | [V] |
| AU-813 | What extra space does backtracking use, apart from the output? | 6s | O of N. The recursion depth, plus the current path. | CX-021; CX-022 | [V] |

## Episode 10. Graphs

**Lesson (spoken first):**

- The lesson.
- A graph problem often does not say graph. Look for things with connections. A grid of cells. Courses with prerequisites. Accounts that share an email. Cities and roads.
- First, build an adjacency list: a dict from each node to a list of its neighbors. And always keep a visited set, or you will loop forever.
- Then pick the tool by the question.
- Is it connected? How many groups? Use DFS or BFS. Both are O of V plus E. Vertices plus edges.
- Fewest steps, when every step costs the same? BFS. The first time you reach a node is the shortest way there.
- Different costs on the edges, none of them negative? Dijkstra's algorithm, with heapq. O of E log V.
- An order that respects dependencies? Or a cycle in a directed graph? Topological sort. O of V plus E.
- Groups that merge as connections arrive? Union find. Each operation is almost O of one.
- On a grid with R rows and C columns, there are R times C cells, so a traversal is O of R times C.
- Now the questions.

| ID | Cue | Gap | Answer + reason | Source | Tag |
|---|---|---|---|---|---|
| AU-901 | A grid of land and water. Count the islands. | 7s | DFS or BFS from each unvisited land cell, marking the whole island as visited. O of R times C. | CX-018; F-49 | [V] |
| AU-902 | A grid of fresh and rotten oranges. Rot spreads to neighbors every minute. How long until all are rotten? | 8s | BFS, starting from all the rotten oranges at once. Each level of the BFS is one minute. O of R times C. | SG-009; F-49; F-22 | [V] |
| AU-903 | The fewest moves for a knight to reach a given square. | 6s | BFS. Every move costs the same, so the first arrival is the shortest. | SG-009; PS-003; F-49 | [V] |
| AU-904 | Courses with prerequisites. Can you finish them all? | 7s | That is cycle detection in a directed graph. Topological sort. If you cannot place every course, there is a cycle. O of V plus E. | SG-014; F-49 | [V] |
| AU-905 | The same courses. Return a valid order to take them in. | 8s | Topological sort with Kahn's algorithm. Count the incoming edges of each course. Start with the courses that have none. Remove them, and repeat. O of V plus E. | SG-014; F-49 | [V] |
| AU-906 | N nodes and a list of undirected edges. How many connected components? | 7s | Union find. Or DFS from each unvisited node, which is O of V plus E. | F-49; F-50 | [V] |
| AU-907 | Edges are added one at a time to a tree. Which edge creates the first cycle? | 8s | Union find. If the two ends of a new edge are already in the same group, that edge closes a cycle. | F-50 | [V] |
| AU-908 | Is this undirected graph a valid tree? | 8s | A tree has exactly N minus one edges, and is fully connected. Check the edge count, then run one DFS, or use union find. | F-49; F-22 | [U] |
| AU-909 | A road network with travel times. Find the fastest route from A to B. | 7s | Dijkstra's algorithm, with heapq. O of E log V. It needs weights that are not negative. | SG-009; F-49 | [V] |
| AU-910 | A signal spreads through a network, with a different delay on each link. When has every node received it? | 8s | Dijkstra from the source. The answer is the largest of the shortest distances. | F-49; F-22 | [U] |
| AU-911 | Why not plain BFS when the edges have different weights? | 7s | BFS counts edges, not cost. The path with the fewest edges may not be the cheapest. | SG-009; F-49 | [V] |
| AU-912 | Change one word into another, one letter at a time, passing only through valid words. Fewest steps. | 8s | BFS. Each word is a node, and words that differ by one letter are neighbors. | SG-009; F-49; F-22 | [V] |
| AU-913 | Make a deep copy of a graph. | 7s | DFS or BFS, with a hash map from each original node to its copy. The map doubles as your visited set. O of V plus E. | F-49; F-22 | [U] |
| AU-914 | A grid of heights where water flows to equal or lower neighbors. Which cells can reach both oceans? | 8s | Search backwards. Run DFS or BFS inland from each ocean's edge, moving uphill, and take the cells reached from both. | F-22 | [U] |
| AU-915 | Connect all the points at the lowest total cost. | 8s | That is a minimum spanning tree. Prim's algorithm with heapq. Or Kruskal's algorithm: sort the edges and join them with union find. O of E log E. | F-49; F-50 | [V] |
| AU-916 | A recursive DFS on a grid of a thousand by a thousand cells, in Python. What can go wrong? | 8s | The recursion can go a million calls deep, and Python stops it long before that. Use BFS with a collections.deque, or an explicit stack. | F-54 | [U] |
| AU-917 | Which two optimizations make union find almost O of one? | 7s | Path compression in find, and union by rank or size. Together, each operation is very nearly constant. | F-50 | [V] |

## Episode 11. Intervals and greedy

**Lesson (spoken first):**

- The lesson.
- Interval problems start the same way: sort. Usually by start time. After sorting, you only ever compare an interval with the one before it.
- Two intervals overlap when each one starts before the other one ends.
- To merge: if the next interval starts at or before the current end, stretch the current end to the larger of the two ends. Otherwise, start a new interval.
- The sort makes these O of N log N.
- Greedy means taking the best looking choice at each step, and never going back. It is fast. Usually one pass after a sort.
- The danger is that greedy is often wrong. Before you trust it, try to break it with a small counterexample. And be ready to say, in one sentence, why the local choice is safe.
- A classic safe case. To keep the most non overlapping intervals, always keep the one that ends first. It leaves the most room for the rest.
- A classic unsafe case. Making change with arbitrary coin values. Taking the biggest coin first can fail. That one needs dynamic programming.
- Now the questions.

| ID | Cue | Gap | Answer + reason | Source | Tag |
|---|---|---|---|---|---|
| AU-1001 | A list of intervals in any order. Merge all the ones that overlap. | 7s | Sort by start. Sweep once, stretching the current interval or starting a new one. O of N log N. | F-51 | [V] |
| AU-1002 | Intervals that are already sorted and do not overlap. Insert one new interval. | 8s | One pass, no sort. Copy the ones that end before it. Merge the ones that overlap it. Copy the rest. O of N. | F-51 | [V] |
| AU-1003 | Can one person attend every meeting? | 7s | Sort by start. If any meeting starts before the previous one ends, the answer is no. O of N log N. | F-51 | [V] |
| AU-1004 | Remove the fewest intervals so that none overlap. | 8s | Greedy. Sort by end time, and keep each interval that starts at or after the end of the last one you kept. O of N log N. | F-52 | [V] |
| AU-1005 | The minimum number of meeting rooms. | 8s | Sort by start, with a min heap of end times. Or sort the starts and the ends separately, and sweep. O of N log N. | F-46; F-51 | [V] |
| AU-1006 | Why sort by end time when you want the most non overlapping intervals? | 7s | Because the one that ends first leaves the most room for the others. | F-52 | [V] |
| AU-1007 | State the test for whether two intervals overlap. | 6s | Each one starts before the other one ends. | F-51 | [V] |
| AU-1008 | The largest sum of a contiguous subarray. Negative numbers are allowed. | 8s | Kadane's algorithm. Keep a running sum and a best so far. Whenever the running sum drops below zero, throw it away and start again from the next number. O of N time, O of one space. | F-52; F-22 | [U] |
| AU-1009 | Each value in an array is the farthest you can jump from that position. Can you reach the end? | 8s | Greedy. Track the farthest index you can reach so far. If you ever stand beyond it, you are stuck. O of N. | F-52; F-22 | [U] |
| AU-1010 | Gas stations in a circle, each with fuel to gain and fuel needed to leave. Where can you start to complete the loop? | 8s | Greedy. If the total fuel is less than the total cost, it is impossible. Otherwise, whenever the tank goes negative, restart from the next station. O of N. | F-52; F-22 | [U] |
| AU-1011 | Make change with the fewest coins, for any set of coin values. Does greedy work? | 7s | No. Biggest coin first can miss the best answer. Use dynamic programming. | F-52 | [V] |
| AU-1012 | How do you test a greedy idea in an interview? | 7s | Try a small counterexample. If you cannot break it, give a one sentence reason why the local choice never hurts. | F-52 | [V] |
| AU-1013 | Split a string into as many parts as possible, so that each letter appears in only one part. | 8s | Greedy. Record the last position of each letter. Stretch the current part to the farthest last position of any letter inside it. O of N. | F-52; F-22 | [U] |
| AU-1014 | A hand of cards. Can it be split into groups of K consecutive values? | 8s | Greedy, with counts in a hash map. Always start a group from the smallest remaining card, using a min heap or sorted keys. O of N log N. | F-52; F-22 | [U] |

## Episode 12. Dynamic programming, one and two dimensional

**Lesson (spoken first):**

- The lesson.
- Dynamic programming is for two kinds of question. Count the ways. Or find the best: the minimum, the maximum, the longest. And in both, the same smaller questions keep coming back.
- Do not try to see the table. Follow three steps, every time.
- Step one. Write the brute force recursion. What are my choices here, and what smaller problem does each choice leave?
- Step two. Memoize. Cache each answer by its arguments. In Python, functools.cache does it in one line.
- Step three, which is optional. Turn it into a table, filled from the smallest case upwards.
- The arguments that change are called the state. Time is the number of states, times the work per state.
- One changing argument gives one dimensional dynamic programming. Usually O of N.
- Two changing arguments give two dimensional dynamic programming. A position in each of two strings, or a row and a column. Usually O of M times N.
- And if each state only needs the previous one or two, keep just those, and cut the space.
- Now the questions.

| ID | Cue | Gap | Answer + reason | Source | Tag |
|---|---|---|---|---|---|
| AU-1101 | How many ways are there to climb N stairs, taking one or two steps at a time? | 7s | One dimensional dynamic programming. The ways to reach step N are the ways to reach N minus one, plus the ways to reach N minus two. O of N time, and O of one space with two variables. | SG-011; F-53 | [V] |
| AU-1102 | Houses in a row, with money in each. You cannot rob two neighbors. What is the most you can take? | 8s | One dimensional dynamic programming. At each house, take the better of skipping it, or robbing it plus the best from two houses back. O of N time, O of one space. | SG-011; F-53 | [V] |
| AU-1103 | The fewest coins to make an amount, from a given set of coin values. | 8s | Dynamic programming over amounts. The best for an amount is one, plus the best for that amount minus each coin. O of the amount, times the number of coins. | SG-011; F-53 | [V] |
| AU-1104 | The length of the longest strictly increasing subsequence. | 8s | Dynamic programming. For each position, the best ending there is one plus the best earlier position with a smaller value. O of N squared. A faster version uses binary search, for O of N log N. | F-53 | [V] |
| AU-1105 | Can a string be cut into words from a dictionary? | 8s | Dynamic programming over positions. A position is reachable if an earlier reachable position, plus one dictionary word, lands exactly on it. | F-53; F-22 | [U] |
| AU-1106 | A string of digits. How many ways can it be decoded into letters, where one means A, up to twenty six for Z? | 8s | One dimensional dynamic programming. The ways from a position are the ways after taking one digit, plus the ways after taking two, whenever each is valid. O of N. | F-53; F-22 | [U] |
| AU-1107 | Can a list of numbers be split into two parts with equal sums? | 8s | A subset sum problem. Ask whether some subset reaches half of the total. O of N, times the target sum. | F-53 | [V] |
| AU-1108 | Count the paths from the top left of a grid to the bottom right, moving only right or down. | 7s | Two dimensional dynamic programming. The paths into a cell are the paths from above, plus the paths from the left. O of M times N. | F-53 | [V] |
| AU-1109 | The longest common subsequence of two strings. | 8s | Two dimensional dynamic programming, over a position in each string. If the characters match, one plus the diagonal. Otherwise, the better of skipping a character from either string. O of M times N. | F-53 | [V] |
| AU-1110 | The fewest edits to turn one word into another. | 8s | Two dimensional dynamic programming, like longest common subsequence, with three choices: insert, delete, or replace. O of M times N. | F-53 | [V] |
| AU-1111 | Plain recursive Fibonacci of N, with no cache. Time and space? | 7s | Time is exponential, about two to the N. Space is O of N, the depth of the recursion. | CX-019 | [V] |
| AU-1112 | Now add memoization. Time and space? | 7s | O of N time, because there are N states with constant work each. O of N space, for the cache and the call stack. | CX-020; F-53 | [V] |
| AU-1113 | State the rule for the running time of any memoized solution. | 6s | The number of states, times the work per state. | SG-011; F-53 | [V] |
| AU-1114 | The question wants the list of all valid combinations, not the count. Dynamic programming or backtracking? | 7s | Backtracking. Dynamic programming counts or optimizes. Listing everything means visiting everything. | SG-010; SG-011; F-48 | [V] |
| AU-1115 | A two dimensional table where each row depends only on the row above. How do you save space? | 7s | Keep just two rows, or one row updated in place. Space drops from O of M times N to O of N. | F-53 | [V] |
| AU-1116 | Find the longest palindromic substring. | 8s | Expand outwards from each center. There are about two N centers, and each expansion is O of N. O of N squared time, O of one space. | F-22 | [U] |

## Episode 13. Mixed review: episodes 5 to 12

| ID | Cue | Gap | Answer + reason | Source | Tag |
|---|---|---|---|---|---|
| AU-1201 | The smallest value such that something becomes possible. | 6s | Binary search on the answer, with a monotonic feasibility check. | AU-409; AU-410 | [V] |
| AU-1202 | The fewest steps across a grid, where every move costs one. | 6s | BFS. O of rows times columns. | AU-903 | [V] |
| AU-1203 | Give me every valid arrangement. N is at most ten. | 6s | Backtracking. Choose, explore, un-choose. | AU-802 | [V] |
| AU-1204 | How many ways. N goes up to ten thousand. | 6s | Dynamic programming. A count, with overlapping subproblems. | AU-1101 | [V] |
| AU-1205 | Tasks with dependencies. Find a valid order. | 6s | Topological sort. O of V plus E. | AU-905 | [V] |
| AU-1206 | The K smallest values of a very long stream. | 6s | A max heap of size K. O of N log K. | AU-702 | [V] |
| AU-1207 | Does a linked list loop back on itself? | 6s | Fast and slow pointers. O of N time, O of one space. | AU-502 | [V] |
| AU-1208 | Does any stored word begin with this prefix? | 6s | A trie. O of L, the length of the prefix. | AU-712 | [V] |
| AU-1209 | Overlapping time ranges to combine. | 6s | Sort by start, then sweep and merge. O of N log N. | AU-1001 | [V] |
| AU-1210 | The cheapest route, when the roads have different costs. | 6s | Dijkstra's algorithm, with heapq. The costs must not be negative. | AU-909 | [V] |
| AU-1211 | Friend groups that merge as friendships are added. How many groups are left? | 6s | Union find. | AU-906 | [V] |
| AU-1212 | The space used by a recursive DFS on a balanced tree, and on a chain. | 7s | O of log N when balanced. O of N for a chain. It is the height of the tree. | AU-611 | [V] |
| AU-1213 | A sorted array, rotated at an unknown point. Find a value. | 7s | Binary search. One half is always sorted. O of log N. | AU-405 | [U] |
| AU-1214 | The values of a tree, one level at a time. | 6s | BFS, with a collections.deque. | AU-602 | [V] |
| AU-1215 | The time to generate all subsets. And all permutations. | 7s | O of N times two to the N. And O of N times N factorial. | AU-801; AU-802 | [V] |
| AU-1216 | The fewest coins for an amount. Greedy or dynamic programming? | 6s | Dynamic programming. Greedy can fail for arbitrary coin values. | AU-1011; AU-1103 | [V] |
| AU-1217 | The head of a linked list might be removed. What do you add? | 6s | A dummy node in front of the head. | AU-513 | [V] |
| AU-1218 | bisect.insort() inside a loop of N. Total cost? | 6s | O of N squared. Each insert shifts items. | AU-411 | [V] |
| AU-1219 | The running median of a stream. | 6s | Two heaps. A max heap for the lower half, and a min heap for the upper half. | AU-704 | [V] |
| AU-1220 | The rule for the running time of a memoized recursion. | 6s | The number of states, times the work per state. | AU-1113 | [V] |

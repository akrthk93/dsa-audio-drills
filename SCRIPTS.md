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

# Audio drill source log (v1, 16 Nov 2026)

Tags: **[V]** = confirmed in two independent sources, or one source plus a measurement I ran. **[U]** = one source, or standard reasoning I could not confirm twice. Item-level tags are in `audio-drill-scripts.md`; each item's `source` field points here (F-xx) or to deck cards (CX-/SG-/PS-).

Source hierarchy used: (1) Python docs, (2) NeetCode, (3) Hello Interview / Tech Interview Handbook / algorithm references, (4) LeetCode constraints.

**Two access problems to know about:**
- The Python wiki TimeComplexity page returned only a redirect to my fetch tool. I could read it through search excerpts only. Its content now also lives in the official docs page "Time complexity of operations on built-in types" (docs.python.org/3/library/time-complexity.html), which I read in full and used as the primary source.
- neetcode.io and leetcode.com are JavaScript-rendered. I could read NeetCode's category counts, but not its problem lists, and no LeetCode problem page directly. Problem membership and n-limits below come from mirrors, so they are tagged accordingly.

## Python operation costs

| ID | Fact | Sources | Tag |
|---|---|---|---|
| F-01 | list: `append` O(1) amortised, `pop()` O(1), `pop(0)` and `insert(0, x)` O(n) | Python docs time-complexity page (list table, notes 1-2); `collections` docs (list incurs O(n) memory movement for `pop(0)` and `insert(0, v)`) | [V] |
| F-02 | list: `x in l` O(n), `min`/`max` O(n), `len` O(1) | Python docs time-complexity page; Python wiki TimeComplexity (search excerpt) | [V] |
| F-03 | Slice costs the slice length; list concatenation costs the sum of lengths | Python docs time-complexity page; Tech Interview Handbook, array page (slicing and concatenating copy, O(n)) | [V] |
| F-04 | Building a string by repeated concatenation in a loop is quadratic; join once instead | Python docs time-complexity page (note on str concatenation); general reference (cris96spa.github.io complexity notes) | [V] |
| F-05 | dict and set: lookup, insert, delete O(1) average; worst case O(n) when hashes collide | Python docs time-complexity page (dict and set sections); Python wiki TimeComplexity (search excerpt: set "see dict") | [V] |
| F-06 | `list.sort()` / `sorted()` O(n log n) worst case; already-sorted input takes O(n) comparisons | Python docs time-complexity page (note 4); Wikipedia Timsort (best O(n), worst O(n log n)) | [V] |
| F-07 | Sort space: `sorted()` builds a new list, O(n). `list.sort()` is in place but Timsort can need a temporary buffer of up to n/2 pointers, so worst-case extra space is O(n) | CPython `listsort.txt` as quoted on Stack Overflow ("What is the space complexity of the python sort"); Wikipedia/HandWiki Timsort (worst-case space O(n)) | [V] |
| F-08 | `collections.deque`: append and pop at either end O(1); indexing in the middle O(n) | `collections` docs; Python wiki TimeComplexity (search excerpt: appendleft, pop, popleft O(1)) | [V] |
| F-09 | `heapq.heapify` runs in linear time, in place | `heapq` docs ("in-place, in linear time"); Wikipedia binary heap / several algorithm references (build-heap O(n)) | [V] |
| F-10 | Heap push and pop are O(log n); reading the top is O(1). The `heapq` docs do not state this themselves | Wikipedia Binary heap (insert worst case O(log n), delete-min O(log n)); Princeton (Kleinberg-Tardos) priority-queue slides | [V] |
| F-11 | n pushes cost O(n log n); heapify does the same job in O(n) | Gustavus Adolphus lecture notes (n inserts at O(log n) each); F-09 | [V] |
| F-12 | Size-k heap over n items: O(n log k) time, O(k) space | Derived from F-10 (each of n items costs O(log k)); Tech Interview Handbook names a heap for top-K; deck CX-024 / SG-007 | [V] (derived) |

## Patterns and signals

| ID | Fact | Sources | Tag |
|---|---|---|---|
| F-13 | Binary search: needs sorted input, O(log n) time, O(1) space | Hello Interview binary search overview; Tech Interview Handbook techniques page (sorted + faster than linear means binary search) | [V] |
| F-14 | Sliding window: contiguous subarray or substring with a condition; O(n) because neither pointer moves backwards | Hello Interview variable-length sliding window; Tech Interview Handbook array page | [V] |
| F-15 | Fixed window when the length is given; variable window otherwise | Hello Interview (fixed vs variable pages); interviewing.io sliding window guide | [V] |
| F-16 | Two pointers from both ends on sorted data: O(n) instead of the O(n²) pair check, O(1) space; works because sorting makes each elimination safe | Hello Interview two pointers overview; techinterview.org two-pointers guide ("sorted arrays, finding pairs/triplets") | [V] |
| F-17 | Stack for nested structure (brackets, expression parsing); push and pop O(1) | Hello Interview stack overview; Tech Interview Handbook techniques page | [V] |
| F-18 | Monotonic stack for next greater / next warmer; O(n) because each element is pushed once and popped at most once | Hello Interview Daily Temperatures page; algo.monster monotonic stack intro | [V] |
| F-19 | Subarray-sum problems with negative numbers: sliding window fails, use prefix sums + hash map, O(n) | Hello Interview community write-up of Subarray Sum Equals K; coddy.tech and several others say the same | [V] |
| F-30 | Unsorted pair-sum: one pass with a hash map of value to index, looking up the complement | Tech Interview Handbook (hash table for lookups); F-05 | [V] |
| F-31 | Container problem: two pointers, move the shorter side | Hello Interview lists it under two pointers; the move-the-shorter-side argument is from one source | [V] pattern, [U] argument |
| F-32 | Prefix / suffix precomputation for subarray sums and products; prefix sums make each range query O(1) | Tech Interview Handbook array page (precomputation); deck CX-025 (measured) | [V] |
| F-33 | Longest consecutive run with a hash set in O(n) by starting only at numbers with no predecessor | Standard solution; single source | [U] |
| F-34 | Top-k frequent can also be done in O(n) with frequency buckets | Deck SG-007; single external source | [U] |

## Phases 2 to 4 (episodes 5 to 13, added 17 Nov 2026)

Access note: page fetches needed an approval that went unanswered, so these facts were checked from search-result excerpts of the pages named, not from full reads. Python docs excerpts were available for `bisect` only.

| ID | Fact | Sources | Tag |
|---|---|---|---|
| F-40 | `bisect_left` returns the insertion point before any equal entries, `bisect_right` after them; the list must already be sorted. `insort` is O(n): the O(log n) search is dominated by the O(n) insert | Python docs `bisect` (3.10, 3.13 and current pages) | [V] |
| F-41 | Binary search on the answer: works when feasibility is monotonic; search the answer range and run a check each time. The banana-speed problem is O(n log m), m = largest pile | neetcode.io solution page (states the O(n log m) target); Exponent and AlgoMaster write-ups (monotonic argument) | [V] |
| F-42 | Rotated sorted array (find minimum, find target) and the sorted 2-D matrix are binary-search problems | Plan step 10 and NeetCode mirrors list them under Binary Search; the "one half is always sorted" method is standard but not confirmed in two sources here | [U] |
| F-43 | Linked list techniques: sentinel/dummy node when the head may change; fast and slow pointers for the middle and for cycle detection; in-place reversal in O(n) time, O(1) space; merge two lists in O(n + m) | Tech Interview Handbook linked-list page (mirror); Hello Interview linked-list overview; techinterview.org linked-list guide | [V] |
| F-44 | Trees: BST in-order traversal is sorted; BST operations are O(log n) when balanced and O(n) when skewed; traversal space is O(h), which is O(n) for a skewed tree | Tech Interview Handbook tree page; yennj12 complexity cheat sheet; Interview Cake | [V] |
| F-45 | BFS with a queue for level-order questions; bottom-up DFS returning height for diameter and balance checks | techinterview.org tree guide; Exponent tree lesson | [V] |
| F-46 | Heap patterns: size-k heap for top-k in O(n log k), with a min-heap for the k largest; k-way merge O(N log k); two heaps for a running median (O(log n) add, O(1) read); quickselect O(n) average, O(n²) worst; meeting rooms = sort by start + min-heap of end times; searching a heap for an arbitrary value is O(n) | techinterview.org heap guides; designgurus heap article; lyte-code heap notes | [V] |
| F-47 | Trie: search, insert and remove are O(m) in the word length; a trie plus DFS serves many words in one grid search | Tech Interview Handbook trie page (mirror); techinterview.org advanced tree guide | [V] |
| F-48 | Backtracking: choose, explore, un-choose; subsets O(n · 2ⁿ), permutations O(n · n!); use it when all solutions are wanted, and DP when one optimum or a count is wanted | designgurus backtracking article; techinterview.org backtracking guides; resumelens DFS/backtracking article | [V] |
| F-49 | Graphs: DFS, BFS and topological sort are O(V + E); BFS gives shortest paths when all edges cost the same; Dijkstra needs non-negative weights; Kruskal is O(E log E). **Sources write Dijkstra's cost two ways**: O((V + E) log V) and O(E log V). They agree for connected graphs; the audio says O(E log V) | University of Washington CSE 417 reference sheet; techinterview.org graph guide; archman.dev graph notes | [V] |
| F-50 | Union-find with path compression and union by rank: amortised inverse-Ackermann per operation, effectively constant; used for cycle detection and Kruskal | University of Alaska CS 411 notes; techinterview.org graph guide | [V] |
| F-51 | Intervals: sort by start, then extend the current interval when the next one begins before it ends; inserting into an already-sorted list needs one pass and no sort | techinterview.org pattern cheat sheet; dloizides interview-patterns notes | [V] |
| F-52 | Greedy needs the greedy-choice property; earliest finish time is safe for picking non-overlapping intervals; arbitrary coin systems need DP; test with a small counterexample | mcfongtw algorithm-selection notes; gitconnected greedy article; d7m greedy notes | [V] |
| F-53 | DP: signals are min cost, max, number of ways, longest; time = states × work per state; climbing stairs O(n) time, O(1) space; coin change O(amount × coins); LCS and edit distance O(m · n), space reducible to one or two rows; LIS O(n²) or O(n log n); 0/1 knapsack O(n · W) | techinterview.org DP guides; yennj12 complexity cheat sheet; scale.jobs DP summary | [V] |
| F-54 | Python specifics not confirmed in this session (docs fetch was blocked): `heapq.merge` and `heapq.nlargest` behaviour and cost, `collections.OrderedDict` as an LRU base, and the recursion limit | From general knowledge only | [U] |
| F-55 | Pronunciation fixes found while checking phonemes for episodes 5 to 13: "Dijkstra" (was "dayk-struh"), "memoize" (was "mem-oyz"), "N-th" and "K-th" (were spelled out letter by letter), "palindrome" (was "pay-lindrome"; this also affected one line in episode 2, now re-rendered), "trie" (now "try") | kokoro-onnx tokenizer output for `en-us` | [V] (phonemes), [U] by ear |

## Constraints and budgets

| ID | Fact | Sources | Tag |
|---|---|---|---|
| F-20 | Constraint ladder (see the deck diff for the decision). CP Handbook / CSES: n ≤ 20 exponential, ≤ 500 cubic, ≤ 5,000 quadratic, ≤ 10⁶ n log n or n, larger needs log n or O(1). USACO Guide: ≤ 20, ≤ 400, ≤ 7,500, ≤ 5·10⁵ n log n, ≤ 5·10⁶ linear | Codeforces blog 106496 (quoting the Competitive Programmer's Handbook table); usaco.guide/bronze/time-comp. **They disagree** on 400 vs 500 and 5,000 vs 7,500; both assume C++ at about 10⁸ ops/sec | [V] (disagreement resolved in deck diff) |
| F-21 | CPython speed. Measured in this session on CPython 3.13: about 3×10⁷ empty loop iterations a second. n² loop: 5,000 → 0.85 s, 7,500 → 1.7 s. n³ loop: 300 → 0.6 s, 400 → 1.7 s, 500 → 4.1 s. Sorting 10⁶ floats: 0.34 s. Real loop bodies are 2-3x slower, so the brief's 10⁷ simple ops/sec is the right planning number | My measurement (script is in the deck diff); brief's stated figure | [V] (measured) |
| F-22 | NeetCode 150 categories. neetcode.io currently shows Arrays & Hashing 9, Two Pointers 5, Sliding Window 6, **Stack 6**, Binary Search 7. The plan (step 8) says Stack has 7. Problem-to-category membership for the cues comes from GitHub mirrors of the list and from the plan file, not from neetcode.io itself | neetcode.io/practice (counts only); GitHub mirrors (bhanuprasadChesetti/neetcode-dsa-roadmap and others) | [V] counts, [U] membership, **Stack count conflicts with the plan** |
| F-23 | LeetCode limit for the three-numbers-sum-to-zero problem: array length up to 3,000 | Two mirrors of the problem page (leetcode.doocs.org family, coddy.tech); leetcode.com itself not readable | [V] |

## Delivery

| ID | Fact | Sources | Tag |
|---|---|---|---|
| F-24 | Overcast is free and can subscribe to any public feed with "Add URL" on the Add Podcast screen | overcast.fm (free player); overcast.fm/podcasterinfo (any public feed URL via Add URL) | [V] |
| F-25 | Overcast Smart Speed shortens silences and can be switched off for one podcast | overcast.fm; TidBITS Talk thread on Smart Speed | [V] that the setting exists; **[U] whether it trims this show's ticking gaps (not testable from here)** |
| F-26 | Apple Podcasts fallback: Library → menu → "Follow a Show by URL" (free) | Castos help; Blubrry help | [V] |
| F-27 | Apple Books is a poor fallback: an iPhone cannot import your own audiobook file directly; it needs a Mac sync | Six Colors (Aug 2025); ProVideo Coalition | [V] |
| F-28 | Overcast supports CarPlay | App Store description (via iClarified listing); Karthik already uses it this way | [V] |
| F-29 | GitHub Pages serving the feed and m4a files | Files are pushed to `akrthk93/dsa-audio-drills` (17 Nov). Serving is untested until Pages is switched on | [U] |
| F-35 | Pronunciation (v1.1, 17 Nov). The scripts keep exact Python names; a pronunciation table in `generate.py` decides how they are spoken: `heapq` = "heap Q", `deque` = "deck", a dot between names = "dot", `pop(0)` = "pop zero", `popleft` = "pop left". Checked from the phoneme output for every line; "DSA" needed respelling (it was read as "D S uh") | kokoro-onnx tokenizer output for `en-us`; Karthik approved the voice-E sample by ear | [V] (phonemes), full episodes [U] by ear |
| F-36 | Voice quality. Kokoro's author grades `bm_lewis` D+ and the British male voices C at best; `am_michael` is graded higher. v1 also used the compressed int8 model and read one sentence at a time. v1.1 uses `am_michael`, the full-precision model, and whole-passage reading | Kokoro VOICES.md (Hugging Face); A/B samples Karthik listened to | [V] |

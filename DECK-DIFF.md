# Audio drills vs the draft deck: diff and n-threshold decision (16 Nov 2026)

Compared against `claude/prep-complexity-pattern-deck.md` (draft v1, 2 Nov 2026). No card IDs were changed. Where a card's text should change, it is listed as a recommended edit for you to apply in the Prep app.

## 1. The n-threshold decision

**The conflict.** Deck SG-002 / SG-003 say n ≤ ~500 cubic and n ≤ ~5,000 quadratic. `dsa-prep-plan.md` and step 2 of the 100-step plan say ~400 and ~7,500.

**Where the numbers come from [V].** The deck's pair (500 / 5,000) is the table in the Competitive Programmer's Handbook (CSES). The plan's pair (400 / 7,500) is the USACO Guide table. Both assume C++ at roughly 10⁸ simple operations a second. Neither is calibrated for Python.

**Measured on CPython 3.13 in this session [V, measured]:**

| Loop | n | Time (empty loop body) |
|---|---|---|
| n² | 5,000 | 0.85 s |
| n² | 7,500 | 1.7 s |
| n³ | 300 | 0.6 s |
| n³ | 400 | 1.7 s |
| n³ | 500 | 4.1 s |

That is about 3×10⁷ empty iterations a second. A real loop body (an index, a compare, an add) is 2-3x slower, which lands on the brief's figure of about 10⁷ simple ops a second.

**Final thresholds (used in Ep 1 and Ep 4):**

| n up to | Slowest acceptable | Step count at the limit |
|---|---|---|
| ~20 | exponential, O(2ⁿ · n) | 2²⁰ ≈ 10⁶ |
| **~300** | cubic | 2.7 × 10⁷ |
| **~5,000** | quadratic | 2.5 × 10⁷ |
| 10⁵ to 10⁶ | O(n log n) or O(n) | ≤ 2 × 10⁷ |
| ~10⁹ and up | O(log n) or O(1) | ~30 |

**Reasoning.** One budget explains every rung: about 25 million steps, which is 1-3 seconds of CPython. 300³ and 5,000² both sit on it. The plan's 7,500² (5.6 × 10⁷) and the deck's 500³ (1.25 × 10⁸) both blow through it in Python: 500³ took 4.1 s with an empty body. So I took the deck's quadratic number and tightened the cubic one. Also added the missing middle rung as an item (AU-007): n = 10⁴ with a quadratic solution is 10⁸ steps, which is not safe in Python.

**One caveat, which matters more than the exact numbers.** In an interview there is no judge and no time limit. The ladder is for reading the interviewer's intent from the constraint. Problem setters pick limits for the intended complexity in any language, so "n ≤ 500" still signals "cubic intended" even though Python would be slow. Learn the ladder as orders of magnitude (20, hundreds, thousands, 10⁵+, 10⁹), not as exact cut-offs.

**Recommended edits:** SG-002 to "n ≤ ~300 (500 in C++)"; SG-003 stays at ~5,000; change "~400" and "~7,500" in `dsa-prep-plan.md` (Retention drills) to ~300 and ~5,000 so the plan, the deck and the audio agree.

## 2. Places I changed or corrected the deck

| Deck card | Deck says | Finding | Action in audio |
|---|---|---|---|
| SG-002 | n ≤ ~500 cubic | Too generous for Python (4.1 s measured) | ~300 (AU-004, AU-318) |
| SG-003 vs plan | 5,000 vs 7,500 | 5,000 fits the Python budget; 7,500 is the C++ figure | 5,000 (AU-003) |
| CX-007 | "`list.sort()` would be O(1) extra in principle (Timsort uses up to n/2 temp)" | Self-contradictory. A buffer of up to n/2 pointers is O(n) worst-case extra space [V] | AU-206 and AU-315 say O(n). **Recommend fixing the CX-007 reason text.** |
| SG-005 | "Sorted input, or n up to 10⁹ → O(log n): binary search" | Sorted input has two readings: binary search (O(log n)) or two pointers (O(n), O(1) space). The deck gives only one | AU-014 teaches both |
| SG-013 | Two pointers O(n), triplets O(n²) | Correct, but silent on the sort when input is unsorted | AU-110 and AU-220 say the O(n log n) sort is the smaller term |
| SG-012, CX-009 | Hash lookup O(1) | Correct only on average; worst case is O(n) [V, Python docs] | Every hash answer says "on average"; AU-015 drills why |
| Lesson line | "Heap push and pop are O(log n)" | Correct, but the Python `heapq` docs do not state it (they only state heapify is linear). Confirmed from Wikipedia and Princeton slides [V] | Used in Ep 3 lesson |
| Lesson line | "string `+=` ... O(n)" | Docs: building a string in a loop is quadratic in the total length [V]. CPython sometimes optimises this in place [U], so the audio says "treat it as O(n²)" | AU-210 |
| SG-006 | Sliding window if values are non-negative; prefix sums + hashmap with negatives | Confirmed [V] | Kept, and drilled as its own contrast item (AU-117, AU-314) |
| SG-007 | Heap of size k O(n log k); bucket sort O(n) | Heap bound derived and confirmed; the bucket alternative has one source [U] | AU-106 gives both |

## 3. Things the deck has that the audio drops (out of scope for v1)

- **CX-016 to CX-022** (BFS, tree DFS, flood fill, Fibonacci, memoised DP, subsets, permutations): graphs, trees, DP and backtracking are not reached yet.
- **CX-006** (recursive binary search) and **CX-015** (merge sort): recursion-space reasoning, left for the Phase 2 pack.
- **SG-008 to SG-011, SG-014** (binary search on the answer, BFS, backtracking, DP, topological sort): later phases. Binary search appears only as a complexity fact (sorted → log n), not as a pattern cue, because Ep 2 is Phase 1 only.
- **SG-001's** "bitmask DP" mention: the audio keeps "n ≤ 20 means exponential is fine" and drops the DP reference.
- **Deck B (PS cards)**: typed skeletons do not work in audio. Only their complexity facts are used.

## 4. Things the audio adds that the deck does not have

- `pop(0)` on a list is O(n); `deque.popleft()` is O(1) (AU-214, AU-311) [V].
- n = 10⁴ with a quadratic solution is unsafe in Python (AU-007).
- "Constant extra space" as a signal for two pointers or in-place work (AU-013).
- Fixed-size window as its own cue (AU-114, AU-312) [V].
- Prefix and suffix products (AU-108), and prefix sums for many range queries (AU-010).
- "While inside a for can still be O(n)" stated as a rule covering both sliding window and monotonic stack (AU-316).

## 5. Disagreements between sources, and what I picked

- **Ladder numbers:** CSES 500 / 5,000 vs USACO 400 / 7,500. Picked 300 / 5,000 for Python; see section 1.
- **NeetCode Stack count:** neetcode.io now shows **6** Stack problems; step 8 of the 100-step plan says 7, and most mirrors list 7. I could not see which problem moved because the site is JavaScript-rendered. Check neetcode.io before you start step 8. The audio cues do not depend on the count.
- **Best-Time-to-Buy-and-Sell-Stock:** NeetCode files it under Sliding Window; the usual solution is a single pass tracking the minimum. AU-113 teaches the single pass and is tagged [U].

## 6. Pronunciation and voice (revised 17 Nov, v1.1)

- v1 replaced `heapq` with "heap" because the voice misread it. That was the wrong fix and is reverted: **the scripts now use exact Python names** (`heapq.heappush()`, `heapq.heapify()`, `collections.deque`, `deque.popleft()`, `list.pop(0)`, `list.sort()`, `sorted()`).
- A pronunciation table in `generate.py` controls only how names are spoken: `heapq` = "heap Q", `deque` = "deck", a dot between names = "dot", `pop(0)` = "pop zero", `popleft` = "pop left", `heappush` = "heap push".
- Voice changed from `bm_lewis` (graded D+ by Kokoro's author) to `am_michael`, on the full-precision model, reading whole passages instead of single sentences. Karthik picked this from five samples.
- "memoise" is still mispronounced; not used yet. Add it to the table when DP episodes are written.
- I cannot listen to audio. Every line was checked from the phoneme output; the full episodes still need one by-ear pass.

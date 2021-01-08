# Some Categories

## 493 Schedule Problem
   Multiple [s<sub>i</sub>, t<sub>i</sub>] intervals, we need to remove as less as possible
to prevent overlapped intervals

   Solution is quite obvious: sort the arrays in increasing order ordered by t<sub>i</sub>, then
add the first one into the final result. For each interval, judge if it is overlapped with the result.

   Idea is greedy -- based on increasing finish time.
   
   Possible function:<br>
   ```
      heapq.heappush(non_overlapping,-intervals[0][1])

      intervals.sort(key=lambda x:x[1], reverse=True)
   ```

## 1649 Binary IndexTree 
   The situation is quite common -- all the prefix sum

   Binary index tree is a tree structure. For example, with previous tree named a,
   for bit:
   ```
   b[0] = 0 
   b[1] = a[0]
   b[2] = a[1]
   b[3] = a[1] + a[0]
 ``` 
   As you can see, the bit is the sum of particular index number noted by 2-bit presented number
   
   
reverse string: word[::-1] is okay

## 972 regression
```
import re
re.match(pattern, string, flags=0) -> return index of matched string
re.search(pattern, string, flags=0) -> return the first matched string

```
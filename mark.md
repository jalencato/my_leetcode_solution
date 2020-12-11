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


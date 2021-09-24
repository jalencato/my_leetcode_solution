from functools import lru_cache


class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        init_in, init_ex = 120, 40
        lost, gain = 40, 20
        INITIAL = {
            " ": 0,
            "i": init_in,
            "e": init_ex
        }

        def getAdjustHappiness(x, y):
            res = 0
            if x == '' and y == '':
                return 0
            elif (x == '' and y == 'intro') or (x == 'intro' and y == ''):
                return init_in
            elif (x == '' and y == 'extro') or (x == 'extro' and y == ''):
                return init_ex
            elif (x == 'intro' and y == 'extro') or (x == 'extro' and y == 'intro'):
                return init_in + init_ex + gain - lost
            elif (x == 'intro' and y == 'intro'):
                return init_in + init_in - lost - lost
            elif (x == 'extro' and y == 'extro'):
                return init_ex + init_ex + gain + gain
            else:
                return "wtf"

        @lru_cache
        def dp(vis, i, j, introCount, extroCount):
            if introCount == extroCount == 0:
                return 0

            state = []
            state.append('intro') if introCount > 0 else state
            state.append('extro') if extroCount > 0 else state

            for val in state:
                cur_res = INITIAL[val] + getAdjustHappiness(val, vis[j]) + getAdjustHappiness(val, vis[j + 1])
                tmp, vis[j] = vis[j], val
                cur_res += dp(tuple(vis), i + ((j - 1) // n), (j - 1) % n, introvertsCount - int(val == "i"), extrovertsCount - int(val == "e"))
                vis[j] = tmp
                res = max(res, cur_res)
            return 0


        return 0


if __name__ == '__main__':
    m, n = 2, 3
    introvertsCount, extrovertsCount = 1, 2
    s = Solution()
    print(s.getMaxGridHappiness(m, n, introvertsCount, extrovertsCount))
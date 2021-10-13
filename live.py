def sumValues(parents, startPoint, jumpLength):
    res = [0] * len(startPoint)
    jumpMax = max(jumpLength)
    mem = [[-1]* (len(parents)+1)] *(jumpMax+1)
    for i, start in enumerate(startPoint):
        tmp = start
        if(tmp==0):
            res[i]=0
        if(mem[jumpLength[i]][start]==-1):
            while(True):
                if(tmp==-1):
                    break
                # if(mem[jumpLength[i]][tmp] != -1):
                #     res[i] += mem[jumpLength[i]][tmp]
                #     mem[jumpLength[i]][start] = res[i]
                #     break
                jump = 0
                res[i] += tmp
                while jump!=jumpLength[i] and tmp != -1:
                    # if(jumpLength[i]==10):
                    #     print(tmp)
                    tmp = parents[tmp]
                    jump += 1
            print(res[i])
            print(jumpLength[i], start)
            # mem[jumpLength[i]][start] = res[i]
        else:
            print(jumpLength[i],start)
            print(mem[jumpLength[i]][start])
            res[i] = mem[jumpLength[i]][start]
            continue

    return res

if __name__ == '__main__':

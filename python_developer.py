def main():
    T=int(input())
    count=0
    result=[]
    for k in range(T):
        N=int(input())
        villian=[int(x) for x in input().split() ]
        player=[int(x) for x in input().split() ]
        villian.sort(reverse=True)
        player.sort(reverse=True)
        start=0
        for i in range(len(player)):
            for j in range(start,len(villian)):
                if player[i]>villian[j]:
                    start=j+1
                    count+=1
                    break
        if (count==N):
        
            result.append("WIN")
            T-=1
        else:
            result.append("LOSE")
            T-=1
            count=0
    for l in result:
        print(l)
        
main()

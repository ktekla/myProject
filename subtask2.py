def blabla(x,*args):
        m=x
        n=0
        s=0
        a=0
        if x==-1:
            m=-1
            a=-1
            print(n,s,a,m)

        else:
            s=s+x
            n=n+1
            for i in args:
                if i>-1:
                    s=s+i
                    n=n+1
                    a=s/n
                    if n==0:
                        m=i
                    else:
                        if i<m:
                            m=i
                        else:
                            m=m
            print("The count of the numbers: ",n, "Their sum: ",s, "Their minimum: ",m, "Their mean: ",a)



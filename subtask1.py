def squarenumb(n):
    x = n

    q=1
    while q*q<=x:
        if x == 0:
            q = 0
        else:        
            q=q+1

    print((q-1)**2)
    
# it looks like I learned how to use git today

squarenumb(36)

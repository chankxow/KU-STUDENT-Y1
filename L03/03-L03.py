def fac(n,r):
    result = 1
    for i in range(n-r+1,n+1):
        result = i*result
    return result

def combi(n,r):
    return (fac(n,n)//(fac(r,r)*(fac(n-r,n-r))))


ans = (combi(4,3)+combi(7,3)+combi(3,3)+combi(7,3)+combi(10,3))/5
print(ans)
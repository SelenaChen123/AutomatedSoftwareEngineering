import math
import sys 
from functools import cmp_to_key

class SYM():
    def __init__(self):
        self.n = 0
        self.has = {}
        self.most = 0
        self.mode = None
    
    def add(self,x):
        if x != "?":
            self.n += 1
            self.has[x]  = 1 + self.has.get(x,0)
            if self.has[x] > self.most:
                self.most , self.mode = self.has[x], x
    
    def mid(self):
        return self.mode 
    
    def div(self):
        def fun(p):
            return p*math.log(p,2)
        e = 0
        for _,n in self.has.items():
            e = e + fun(n/self.n)
        return -e

# Testing SYM    
sym = SYM()
for x in ["a","a","a","a","b","b","c"]:
    sym.add(x)
print(sym.mid()) # a 
print(sym.div()) # 1.37

class NUM():
    def __init__(self):
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.hi = sys.maxsize
        self.lo = -sys.maxsize

    def add(self, n):
        if n != "?":
            self.n = self.n + 1
            d = n - self.mu
            self.mu = self.mu + d/self.n
            self.m2 = self.m2 + d*(n - self.mu)
            self.lo = min(n, self.lo)
            self.hi = max(n, self.hi)
        
    def mid(self):
            return self.mu
        
    def div(self):
        if (self.m2 < 0 or self.n < 2): 
            return 0
        else:
            return round((self.m2/(self.n-1))**0.5,2)

# Testing NUM
num = NUM()
for x in [1,1,1,1,2,2,3]:
    num.add(x)
print(num.mid())
print(num.div())

def map(t, fun):
    u={}
    for k,v in t.items():
        v,k = fun(v)
        if k != None and k != False:
            u[k] = v
        else:
            u[1+len(u)] = v
    return u

def kap(t, fun):
    u={}
    for k, v in t.items():
        v,k = fun(k)
        if k!= None and k!= False:
            u[k] = v
        else:
            u[1+len(u)]=v
    return u

def sort(t,fun):
    return sorted(t,key=cmp_to_key(fun))

def keys(t):
    return(sort(kap(t.keys())))





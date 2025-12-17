import math

class AnnuityValue:
    @staticmethod
    def FV(A, r, n, payday='end'):
        r=r/100
        FV = A * (((1 + r) ** n - 1) / r)
        if payday == 'end':
            return FV
        elif payday == 'start':
            return FV * (1 + r)
        else: NameError
    @staticmethod
    def CV(A, r, n,payday='end'):
        r=r/100
        CV = A * (1 - (1 + r) ** -n) / r
        if payday == 'end':
            return CV
        elif payday == 'start':
            return CV * (1 + r)
        else: NameError
    
class problem8:
    def GivenFV(fv=27000,n=3*12,r=8.5/12,payday='end'):
        r=r/100
        A=(fv*r)/((1+r)**n-1)
        if payday == 'end':
            return A
        elif payday == 'start':
            return A/(1 + r)
        else: NameError

    def solve(fv=27000,n=3*12,r=8.5/12,payday='end'):
        r=r/100
        A=(fv*r)/((1+r)**n-1)
        if payday == 'end':
            return A
        elif payday == 'start':
            return A/(1 + r)
        else: NameError
    
    def GivenCV(cv=27000,n=3*12,r=8.5/12,payday='end'):
        r=r/100
        A=(cv*r)/(1 - (1+r)**(-n))
        if payday == 'end':
            return A
        elif payday == 'start':
            return A/(1 + r)
        else: NameError

class problem10:
    def GivenFV(fv=300000,A=10000,r=15/12,payday='end'):
        r=r/100
        if payday == 'end':
            up = math.log((fv*r/A) + 1)
        elif payday == 'start':
            up = math.log((fv*r/(A*(1+r))) + 1)
        else: NameError
        
        return up / math.log(1 + r)
    
    def GivenCV(cv=300000,A=10000,r=15/12,payday='end'):
        r=r/100
        if payday == 'end':
            down = 1 - (cv*r/A)
        elif payday == 'start':
            down = 1 - (cv*r/(A*(1+r)))
        else: NameError

        return -math.log(down) / math.log(1 + r)
    
    def solve(fv=300000,A=10000,r=15/12,payday='end'):
        r=r/100
        if payday == 'end':
            up = math.log((fv*r/A) + 1)
        elif payday == 'start':
            up = math.log((fv*r/(A*(1+r))) + 1)
        else: NameError
        return up / math.log(1 + r)
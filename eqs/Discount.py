

class problem1:
    def solve(fv=2300, d=4.9,n=2):

        return fv*(1-d*n/100)
    
class problem3:
    def solve(fv=1250, r=9, n=5/12):
        cv = fv/(1 + r*n/100)
        return fv-cv
    
class problem6:
    def solve(c=1803.75,fv=1850,n=120/360):
        return (1-(c/fv))/n * 100
    

class problem8:
    def solve(c=2900-638,fv=2900,r=11):
        r = r/100
        return (1-(c/fv))/r
    
class problem10:
    def solve(d=7.5,n=60/360):
        d = d/100
        return d/(1-d*n) * 100
    
    def discount_rate(r=8,n=60/360):
        r = r/100
        return r/(1+r*n) * 100
    
    def rate(d=7.5,n=60/360):
        d = d/100
        return d/(1-d*n) * 100
    
class problem15:
    def solve(fv=20000,n=180/360,B=89.56):
        B = B/100
        cv = B * fv
        D = fv-cv
        d = D/(fv*n)
        d_eq = (360 - 3.6 * B *100)/(n*360)
        r = d/(1-d*n)
        return cv , D , d*100 , d_eq *100 , r*100
import math

class DebtLeasing:
    @staticmethod
    def solve(P: float, r: float, t: float,n:float) -> float:
        """
        计算复利终值
        :param P: 贷款
        :param r: 年利率
        :param t: 年数
        :param n: 月数
        :return: 终值
        """
        I = P*r*t
        return I

class problem1:
    def solve(P=1300,r=0.11,t=1.5,n=18):
        I = P*r*t
        PYT=((P + I)/n)
        return PYT
    
    def solveMIP(P=1300,r=0.11,t=1.5,n=18):
        I = P*r*t
        MIP = I/n
        return MIP
    
    def solveMPP(P=1300,r=0.11,t=1.5,n=18):
        I = P*r*t
        PYT=((P + I)/n)
        MIP = I/n
        MPP=PYT-MIP
        return MPP
    
class problem6:
    def solveD(n=42):
        D=(n*(n+1))/2
        return D
    
class problem9:
    def solveLeft(cv=4500,r=0.07,n=3,N=36,P=4500,times=20):
        I=cv*r*n
        PYT=((P+I)/N)
        MIP=I/N
        PPM=PYT-MIP
        Left=cv-PPM*times
        return Left
    
class problem10:
    def parallel(P=2000,r=0.095,t=1):
        I=P*r*t
        return I
    
    def SevenEight(N=18,cv=2000,r=0.095,n=1.5):
        D=(N*(N+1))/2
        I=cv*r*n
        MIP=((7+8+9+10+11+12+13+14+15+16+17+18)/D)*I#一年半的后一年，也就是前6年不算
        return MIP

class problem13:
    def half(P=3400,r=0.065,n=8):#n是按半年结算的t所以是2倍
        I=P*0.5*r*n#由于是半年所以r乘0.5？
        PYT=((P+I)/n)
        return PYT
    
    def total(cv=3400,r=0.065,t=4):#此处cv=P即3400美元的贷款
        I=cv*r*t
        return I
    
class problem14:
    def Pay4Time(P=3750,unpay=0.02,i=0.1975,m=12,year=1):
        PYT=P*unpay
        r=i/m
        MIP=P*r*year
        MPP=PYT-MIP
        n=P/MPP
        return n
    
class problem17:
    def Debt(total=85000,ATP=19550,MM=1850,CC1=320,CC2=190,PL=226,DS=65):
        DP=CC1+CC2+PL+DS
        DI=(total-ATP)/12
        limit=DP/DI
        return limit
    
class problem19:
    def formula(year=20,I=0.08,pay=95000):
        cv=pay*(1-0.2)
        r=I/12
        n=12*year
        A=cv*(r/(1-(1+r)**(-n)))
        return A
    
    
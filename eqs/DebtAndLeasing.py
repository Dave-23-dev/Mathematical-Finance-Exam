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
    def solve(P=1300,r=11,t=1.5,n=18):
        r=r/100
        I = P*r*t
        PYT=((P + I)/n)
        MIP = I/n
        MPP=PYT-MIP
        return PYT, MIP, MPP

class problem6:
    def solveD(n=42):
        D=(n*(n+1))/2
        return D
    
class problem9:
    def solveLeft(P=4500,r=7,t=3,n=36,times=20):
        r=r/100
        PYT, MIP, MPP = problem1.solve(P=P,r=r,t=t,n=n)
        Left=P-MPP*times
        return Left
    
class problem10:
    def Parallel(P=2000,r=9.5,t=18/12,n=18,times=12):
        
        PYT, MIP, MPP = problem1.solve(P=P,r=r,t=t,n=n)
        Left=P-MPP*times
        PaidI= MIP*times
        return Left, PaidI
        
    def SevenEight(P=2000,r=9.5,t=18/12,n=18,times=12,result='result'):
        r=r/100
        D = problem6.solveD(n=n)
        K_i = []
        for i in range(1, n + 1):
            K_i.append((n - i + 1)/D)
        
        I = P * r * t
        MIP_i = []
        for i in range(1,n+1):
            MIP_i.append(I * K_i[i-1])

        PYT=((P + I)/n)
        MPP_i = []
        for i in range(1,n+1):
            MPP_i.append(PYT - MIP_i[i-1])
        
        if result == 'list':
            return MIP_i, MPP_i
        
        elif result == 'result':
            Left=P
            for i in range(times):
                Left=Left-MPP_i[i]

            PaidI=0
            for i in range(times):
                PaidI=PaidI+MIP_i[i]
            
            return Left, PaidI

        else: NameError("result=result,result=list")
        

class problem13:
    def solve(P=3400,r=6.5,t=8,frequency=2):
        """
        计算每期支付额
        :param P: 贷款金额
        :param r: 年利率
        :param t: 贷款时间,单位:年
        :param frequency: 每年还款次数
        """
        r=r/100
        n=frequency*t
        I = P*r*t
        PYT= P*(1+(r/frequency)*n)/n
        return PYT , I
    
    
class problem14:
    def Pay4Time(P=3750,unpay=2,i=19.75,m=12,year=1):
        unpay=unpay/100
        i=i/100
        PYT=P*unpay
        r=i/m
        MIP=P*r*year
        MPP=PYT-MIP
        PPT=P/MPP
        ALLI = MIP*PPT
        return PPT , ALLI
    
class problem17:
    def Debt(total=85000,ATP=19550,MM=1850, DPs = [320,190,226,65]):
        DP=sum(DPs)
        DI=(total-ATP)/12
        limit=DP/DI
        return limit
    
class problem19:
    def formula(p=95000,r=8,year=20,down_payment_ratio=20):
        cv=p*(1-down_payment_ratio/100)
        r=r/100
        r=r/12
        n=12*year
        A=cv*(r/(1-(1+r)**(-n)))
        return A
    
    
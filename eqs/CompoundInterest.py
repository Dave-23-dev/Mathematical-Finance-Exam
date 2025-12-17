import math

class CompoundInterest:
    @staticmethod
    def solve(cv: float, r: float, n: float) -> float:
        """
        计算复利终值
        :param cv: 现值 
        :param r: 年利率
        :param n: 期数
        :return: 终值
        """
        fv = cv * (1 + r / 100) ** n
        return fv
    
class problem3:
    def solve(fv=7950, r=8.5, n=5):
        return fv * (1 + r / 100) ** (-n)
    
class problem11:
    def solve(fv=10866.80,cv=7000,r=14.75):

        return math.log(fv/cv)/math.log(1+r/100)
    
class problem12:
    def solve(r=12,m=12):
        r=r/100
        R = (1+(r/m)) ** m - 1
        return R * 100
    
class problem16:
    def solve(paytime=1,
              r=4.9,
              debt=[
                  [570,8/12],
                  [1380,1.5]
              ]):
        payamount = 0
        r=r/100
        for d in debt:
            payamount += d[0] * (1 + r) ** (paytime-d[1])
        return payamount
    

class problem21:
    def solve(r = 4, count2 = 2, count3 = 2, count5 = 0):
        return (count2 * 72 + count3 *114 + count5 * 167)/r
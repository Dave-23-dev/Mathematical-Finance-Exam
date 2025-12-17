from datetime import date, datetime
from typing import Union

class SimpleInterest:
    @staticmethod
    def solve(cv: float, r: float, n: float) -> float:
        """
        计算单利终值
        :param cv: 现值 
        :param r: 年利率
        :param n: 期数
        :return: 终值
        """
        fv = cv + (cv * r * n) / 100
        return fv

class problem1:
    @staticmethod
    def solve(cv=2350, r=7, n=0.5):
        return (cv * r * n) / 100
    

class problem3:
    @staticmethod
    def solve(I=375, cv=3000, n=2):
        return I/(cv * n) * 100
    
class problem5:
    @staticmethod
    def solve(I=486, cv=900, r=12):
        r=r/100
        return I/(cv * r) 

class problem14:
    @staticmethod
    def solve(cv=3200, fv=4500,n=3):
        return (((fv/cv)-1)/n) * 100

class problem15:
    @staticmethod
    def solve(cv=3200, fv=4500,r=9.5):
        r=r/100
        return (((fv/cv)-1)/r)
    


class ExactTimeCalculator:
    """
    数理金融 - 准确时间计算器
    支持实际天数查询和三种常见准确年分数计算
    """

    @staticmethod
    def days_between(
        start: Union[date, datetime, str],
        end: Union[date, datetime, str]
    ) -> int:
        """
        返回两个日期之间的实际天数（不含结束日，或称“差几天”）
        例如：2025-01-01 到 2025-01-02 → 返回 1
        """
        # 统一转为 date 对象
        if isinstance(start, str):
            start = date.fromisoformat(start)
        if isinstance(end, str):
            end = date.fromisoformat(end)
        if isinstance(start, datetime):
            start = start.date()
        if isinstance(end, datetime):
            end = end.date()

        if end < start:
            raise ValueError("结束日期必须不早于开始日期")

        return (end - start).days

    @staticmethod
    def year_fraction(
        start: Union[date, datetime, str],
        end: Union[date, datetime, str],
        method: str = "actual_365"
    ) -> float:
        """
        计算年分数（支持 actual_365 / actual_360 / actual_actual）
        """
        days = ExactTimeCalculator.days_between(start, end)  # 复用天数计算
        method = method.lower()

        if method == "actual_365":
            return days / 365.0

        if method == "actual_360":
            return days / 360.0

        if method == "actual_actual":
            if start.year == end.year:
                basis = 366 if ExactTimeCalculator._is_leap_year(start.year) else 365
                return days / basis
            else:
                # 跨年处理
                days_start_year = (date(start.year + 1, 1, 1) - start).days
                days_end_year = (end - date(end.year, 1, 1)).days
                basis_start = 366 if ExactTimeCalculator._is_leap_year(start.year) else 365
                basis_end = 366 if ExactTimeCalculator._is_leap_year(end.year) else 365
                return days_start_year / basis_start + days_end_year / basis_end

        raise ValueError('method 必须是 "actual_365", "actual_360" 或 "actual_actual"')

    @staticmethod
    def _is_leap_year(year: int) -> bool:
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


class ApproximateTimeCalculator:
    """
    近似时间计算器（基于教材描述的简单30天/月规则）
    方法：整月数 × 30 + (终止日 - 起始日)
    """

    @staticmethod
    def approximate_days(
        start: Union[date, datetime, str],
        end: Union[date, datetime, str]
    ) -> int:
        """
        计算从 start 到 end 的近似天数（教材描述的方法）

        Args:
            start: 开始日期（date/datetime 或 'YYYY-MM-DD' 字符串）
            end:   结束日期

        Returns:
            int: 近似总天数
        """
        # 统一转为 date 对象
        if isinstance(start, str):
            start = date.fromisoformat(start.replace('/', '-'))
        if isinstance(end, str):
            end = date.fromisoformat(end.replace('/', '-'))
        if isinstance(start, datetime):
            start = start.date()
        if isinstance(end, datetime):
            end = end.date()

        if end < start:
            raise ValueError("结束日期必须不早于开始日期")

        start_year, start_month, start_day = start.year, start.month, start.day
        end_year,   end_month,   end_day   = end.year,   end.month,   end.day

        # Step 1: 计算整月数
        # 从 start 的 (year, month, start_day) 开始，向前推到 end 的同日
        months = (end_year - start_year) * 12 + (end_month - start_month)

        # 如果结束日的“日” < 起始日的“日”，说明没有满最后一个月，需要减1
        if end_day < start_day:
            months -= 1

        # Step 2: 计算剩余天数 = 结束日的日 - 起始日的日
        # 注意：如果跨月了，这里的剩余天数可能是负的？不会，因为上面已经减了1个月
        remaining_days = end_day - start_day
        if remaining_days < 0:
            # 借一个月（30天）来计算剩余
            remaining_days += 30

        # Step 3: 总近似天数
        total_approx_days = months * 30 + remaining_days

        return total_approx_days

class problem21:
    @staticmethod
    def solve(fv=3550,r=7.5,pn=[[30,550],[45,1300],[70,1700]]):
        r=r/100
        cv=0
        for item in pn:
            n=item[0]
            I=item[1]
            cv += I/(1+r*n)
        
        return ((fv/cv)-1)/r

class problem23:
    @staticmethod
    def solve(io = 117.5):
        return io * (72/73)
    
    @staticmethod
    def calculate_ie(io = 117.5):
        return io * (72/73)
    
    @staticmethod
    def calculate_io(ie = 115.84):
        return ie * (73/72)

class problem25:
    @staticmethod
    def solve(start = ['2025-03-15',312.5],
              end = ['2025-10-08',1229],
              items = [
                  ['2025-05-25',617.7],
                  ['2025-06-17',-115.2],
                  ['2025-07-01',250]
              ]):
        cv = end[1]-start[1]
        i = start[1]*ApproximateTimeCalculator.approximate_days(start[0], end[0])/360
        for item in items:
            
            cv -= item[1]
            i += item[1]*ApproximateTimeCalculator.approximate_days(item[0], end[0])/360

        return (cv/i)*100









if __name__ == "__main__":

    print(problem3.solve(I=375, cv=3000, n=2))  # Example usage for problem 3
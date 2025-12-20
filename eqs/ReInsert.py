class ReInsert:
    def formula(known,
                sample1 = [2,44.22702961],
                sample2 = [1.875,43.30793563]):
        """
        线性插值的逆过程，也叫反向线性插值或线性反推

        :param known: 已知的y值
        :param sample1: 第一个样本点 [x1, y1]
        :param sample2: 第二个样本点 [x2, y2]
        """

        if sample1[0] > sample2[0]:
            Sample1 = sample2
            Sample2 = sample1
        else:
            Sample1 = sample1
            Sample2 = sample2
            
        assert known <= Sample2[1] and known >= Sample1[1], "value out of range"

        x = Sample1[0] + (known - Sample1[1]) * (Sample2[0] - Sample1[0]) / (Sample2[1] - Sample1[1])

        return x
    



import scipy.optimize as optimize

class AnnuityRateCalculator:
    """
    一个用于计算年金利率的Python类。
    支持普通年金将来值（Future Value of Annuity）的反向求解利率 r。
    
    公式：FV = P * ((1 + r)^n - 1) / r
    
    使用数值方法（scipy.optimize.root_scalar）求解 r。
    
    使用示例：
    calculator = AnnuityRateCalculator(FV=35507.50, P=1750, n=36)
    quarterly_rate = calculator.solve_rate()
    print(f"季度利率: {quarterly_rate:.6f}")
    """

    def __init__(self, FV, A, n, initial_guess_bracket=[0.001, 0.4]):
        """
        初始化参数。
        :param FV: 年金将来值 (float)
        :param A: 每期支付金额 (float)
        :param n: 期数 (int)
        :param initial_guess_bracket: 求解器的初始搜索区间 [low, high] (list of float)，默认 [0.001, 0.1]
        """
        self.FV = FV
        self.A = A
        self.n = n
        self.bracket = initial_guess_bracket

    def _fv_annuity(self, r):
        """年金将来值计算函数，用于求解。"""
        if abs(r) < 1e-12:  # 避免 r=0 时除零
            return self.A * self.n
        else:
            return self.A * ((1 + r)**self.n - 1) / r
    def _equation(self, r):
        """目标方程：fv_annuity(r) - FV = 0"""
        return self._fv_annuity(r) - self.FV

    def solve_rate(self, method='brentq', tol=1e-10):
        """
        求解每期利率 r。
        :param method: 求解方法，默认为 'brentq' (Brent 方法，适合括号法)
        :param tol: 精度容差 (float)
        :return: 每期利率 r (float)
        
        如果求解失败，会抛出异常。
        """
        sol = optimize.root_scalar(self._equation, bracket=self.bracket, method=method, xtol=tol)
        if sol.converged:
            return sol.root
        else:
            raise ValueError("求解未收敛，请调整搜索区间或方法。")

    def get_annual_nominal_rate(self, periods_per_year=4):
        """
        计算年化名义利率（每期利率 * 每年期数）。
        :param periods_per_year: 每年复合期数 (int)，默认为4（季度）
        :return: 年化名义利率 (float)
        """
        r = self.solve_rate()
        return r * periods_per_year

    def get_annual_effective_rate(self, periods_per_year=4):
        """
        计算年化有效利率 ((1 + r)^periods_per_year - 1)。
        :param periods_per_year: 每年复合期数 (int)，默认为4（季度）
        :return: 年化有效利率 (float)
        """
        r = self.solve_rate()
        return (1 + r)**periods_per_year - 1

    def verify(self):
        """验证：用求得的 r 计算 FV 是否匹配原 FV。"""
        r = self.solve_rate()
        computed_fv = self._fv_annuity(r)
        return abs(computed_fv - self.FV) < 1e-6  # 允许小误差


# 示例使用（基于原问题）
if __name__ == "__main__":
    calculator = AnnuityRateCalculator(FV=35507.50, P=1750, n=36)
    quarterly_rate = calculator.solve_rate()
    print(f"每期（季度）利率: {quarterly_rate:.6f}")
    print(f"年化名义利率: {calculator.get_annual_nominal_rate():.6f}")
    print(f"年化有效利率: {calculator.get_annual_effective_rate():.6f}")
    print(f"验证结果: {calculator.verify()} (True 表示匹配)")
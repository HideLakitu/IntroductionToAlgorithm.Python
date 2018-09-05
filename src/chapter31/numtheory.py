
class _NumberTheory:
    def __init__(self):
        pass

    def gcd(self, a : int, b : int):
        """
        Summary
        ====
        求两个数的最大公约数

        Args
        ===
        `a`: 数字1

        `b`: 数字2

        Return
        ===
        `num` : 最大公约数

        Example
        ===
        ```python
        >>> gcd(24, 30)
        >>> 6
        ```

        """
        assert a >= 0 and b >= 0
        if a == 0 and b == 0:
            return 0
        return 0

    def euclid(self, a, b):
        '''
        欧几里得算法
        '''
        if b == 0:
            return a
        return self.euclid(b, a % b)

    def ismutualprime(self, a : int, b : int):
        """
        判断两个数是不是互质数
        Args
        ===
        `a`: 数字1

        `b`: 数字2
        """
        return self.gcd(a, b) == 1

__number_theory_instance = _NumberTheory()

gcd = __number_theory_instance.gcd
euclid = __number_theory_instance.euclid
ismutualprime = __number_theory_instance.ismutualprime

if __name__ == '__main__':
    print(gcd(24, 30))
else:
    pass

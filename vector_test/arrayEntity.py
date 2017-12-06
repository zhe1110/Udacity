import math


class ArrayEntity():
    """向量计算"""

    def __init__(self, vector):
        self.vector = vector
        self.dimension = len(vector)

    def plus(self, v):
        new_vector = [x + y for x, y in zip(self.vector, v.vector)]
        return new_vector

    def minus(self, v):
        new_vector = [x - y for x, y in zip(self.vector, v.vector)]
        return new_vector

    def multiply_scalar(self, num):
        new_vector = [num * x for x in self.vector]
        return new_vector

    def square(self):
        """坐标平方列表(两个向量的模)"""
        new_vector = [x ** 2 for x in self.vector]
        return math.sqrt(sum(new_vector))

    def vector_standardization(self):
        """向量标准化"""
        try:
            return self.multiply_scalar(1. / self.square())
        except ZeroDivisionError:
            raise Exception("0不能为余数")

    def dot_product(self, v):
        """点积(两个向量的向量积)"""
        try:
            new_vector = [x * y for x, y in zip(self.vector, v.vector)]
            return sum(new_vector)
        except Exception:
            raise Exception("错误")

    def angle_with2(self, v, in_degrees=False):
        """两个向量的夹角(夹角函数)(弧度)
            给出了坐标
            先求出两个向量的模
            再求出两个向量的向量积
            |a|=√[x1^2+y1^2]
            |b|=√[x2^2+y2^2]
            a*b=(x1,y1)(x2,y2)=x1x2+y1y2
            cosθ=a*b/[|a|*|b|]
            =(x1x2+y1y2)/[√[x1^2+y1^2]*√[x2^2+y2^2]]
        """
        try:
            u1 = ArrayEntity(self.vector_standardization())
            u2 = ArrayEntity(v.vector_standardization())

            square1 = self.square()
            square2 = v.square()
            dot_product = self.dot_product(v)
            cosθ = dot_product / abs(square1 * square2)

            if in_degrees:
                return math.acos(cosθ) * (180. / math.pi)
            else:
                return math.acos(cosθ)
        except Exception:
            raise Exception("错误")

    def angle_with(self, v, in_degrees=False):
        try:
            u1 = ArrayEntity(self.vector_standardization())
            u2 = ArrayEntity(v.vector_standardization())
            u3 = u1.dot_product(u2)
            if u3 > 1:
                u3 = 1
            elif u3 < -1:
                u3 = -1
            dot_product = math.acos(u3)

            if in_degrees:
                return dot_product * (180. / math.pi)
            else:
                return dot_product
        except Exception:
            raise Exception("错误")

    def is_parallel(self, v):
        try:
            return self.is_zero() or v.is_zero() or self.angle_with(v) == 0 or self.angle_with(v) == math.pi

        except Exception:
            raise Exception("错误")

    def is_zero(self, tolerance=1e-10):
        try:
            return self.square() < tolerance

        except Exception:
            raise Exception("错误")

    def is_quadrature(self, v, tolerance=1e-10):
        try:
            return abs(self.dot_product(v)) < tolerance

        except Exception:
            raise Exception("错误")

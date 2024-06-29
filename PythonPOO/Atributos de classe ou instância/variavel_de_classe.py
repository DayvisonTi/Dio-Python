class A:
    vc = 123

    def __init__(self):
        self.vc = 321

v = A()
v2 = A()

print(v.vc)
print(v2.vc)

print(A.vc)
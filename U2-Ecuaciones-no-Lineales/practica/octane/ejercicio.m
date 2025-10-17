a = 0.1
b = 0.3
c = -2.e18
d = ( -a + b -a -a) * c

f =@(x) x - 2.0128411
g =@(x) x.^2 - 2.0043

x = -5:0.5:5  % con paso: 0.5
y = f(x)
plot(x,y)
y2 = g(x)
plot(x,y2)


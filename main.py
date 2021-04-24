import turtle as t
from random import random
from math import sqrt

def brown(x0, y0, x1, y1, disp, p, n=8, m=400):
     ''' Рекурсивная функция построения Броуновского моста.
     Параметры:
     x0, y0, x1, y1 - координаты двух точек
     disp -дисперсия
     p - плавность
     n - глубина рекурсии
     m - масштаб

     xm, ym - координаты середины
     delta - смещение
     '''
     t.speed(1000)
     if n == 0:
          t.penup()
          t.goto(x0*m-m/2, y0*m-m/2)
          t.pendown()
          t.goto(x1*m-m/2, y1*m-m/2)
          return
     xm = (x0+x1)/2.0
     ym = (y0+y1)/2.0
     delta = random()*sqrt(disp)
     brown(x0, y0, xm+delta, ym+delta, disp/p, p, n-1)
     brown(xm+delta, ym+delta, x1, y1, disp/p, p, n-1)

def main():
     t.goto(0, 0)
     t.speed(1000)
     h = 0.5
     a = 2.1**(2.1*h)
     brown(0.0, 0.5, 1.0, 0.5, 0.012, a)
     brown(0.0, 0.5, 1.0, 0.5, 0.0021, a)
     t.done()
     t.hideturtle()

if __name__ == '__main__':
    t.speed(1000)
    main()

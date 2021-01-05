import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#https://www.stat.ee/pressiteade-2019-111
#https://www.stat.ee/pressiteade-2019-104

#Формирование данных и построение диаграммы
x1 = np.arange(-9, -1, 0.01) # x - массив np.array
x2 = np.arange(1, 9, 0.01)
x3 = np.arange(-9, -1, 0.01)
x4 = np.arange(1, 9, 0.01)
x5 = np.arange(-9, -6, 0.01)
x6 = np.arange(6, 9, 0.01)
x7 = np.arange(-1, 1, 0.01)

y1 = (-0.0625*((x1+5)**2)+2)
y2 = (-0.0625*((x2-5)**2)+2)
y3 = (0.25*((x3+5)**2)-3)
y4 = (0.25*((x4-5)**2)-3)
y5 = ((-(x5+7)**2)+5)
y6 = ((-(x6-7)**2)+5)
y7 = (-0.5*(x7**2)+1.5)

plt.subplots()
plt.title("Очки")

plt.grid(True)# Отображение сетки на координатной плоскости
plt.plot(x1,y1 ,'--r',linewidth=3)# График красного цвета
plt.plot(x2,y2 ,'--r',linewidth=3)
plt.plot(x3,y3 ,'--r',linewidth=3)
plt.plot(x4,y4 ,'--r',linewidth=3)
plt.plot(x5,y5 ,'--r',linewidth=3)
plt.plot(x6,y6 ,'--r',linewidth=3)
plt.plot(x7,y7 ,'--r',linewidth=3)
plt.legend()
plt.savefig("my_image.png")  # Сохранение изображения или
plt.show()  # Вывод изображения на экран
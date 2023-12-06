import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

# Задаем параметрические уравнения
t = np.linspace(0, 2 * np.pi, 1000)
x = 2**(t-1)
y = 0.25*(t**3 + 1)

# Создаем график
plt.figure(figsize=(8, 8))

# Рисуем параметрический график
plt.plot(x, y, label='Параметрический график: $x = 2^{(t-1)}$, $y = \\frac{1}{4}(t^3+1)$')

# Добавляем сетку
plt.grid(True, linestyle='-', alpha=0.8)

# Добавляем вспомогательную сетку
plt.minorticks_on()
plt.grid(True, which='minor', linestyle='--', alpha=0.4)

# Добавляем подписи для осей и графика
plt.title('Параметрический график')
plt.xlabel('$x$')
plt.ylabel('$y$')

# Сдвигаем подпись графика в верхний левый угол
plt.legend(loc='upper left')

# Устанавливаем пределы значений по осям x и y для увеличения масштаба
plt.xlim(0, 70)
plt.ylim(0, 70)

# Сохраняем график в формате SVG
svg_buf = BytesIO()
plt.savefig(svg_buf, format='svg')
svg_data = svg_buf.getvalue()
svg_buf.close()

# Вставляем SVG данные в HTML шаблон
html_content = f'''
<!DOCTYPE html>
<html>
<head>
    <title>Параметрический график</title>
</head>
<body>
    <h1>Параметрический график</h1>
    <div>{svg_data.decode("utf-8")}</div>
</body>
</html>
'''

# Сохраняем HTML файл
with open('parametric_plot.html', 'w') as html_file:
    html_file.write(html_content)

with open('parametric_plot.svg', 'w') as html_file:
    html_file.write(svg_data.decode("utf-8"))
# Показываем график
plt.show()

from io import BytesIO
import numpy as np
import matplotlib.pyplot as plt

# Задаем уравнение в полярных координатах
phi = np.arange(0, np.pi + np.pi/16, np.pi/16)
p = 4 * np.cos(phi)

# Создаем график в полярных координатах
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})
ax.plot(phi, p, label='$p = 6 \\cos(\\phi)$')

# Добавляем подписи и сетку
ax.set_title('График в полярных координатах')
ax.legend()
ax.grid(True)

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
with open('polar_plot.html', 'w') as html_file:
    html_file.write(html_content)

with open('polar_plot.svg', 'w') as html_file:
    html_file.write(svg_data.decode("utf-8"))
# Показываем график
plt.show()

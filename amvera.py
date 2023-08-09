'''
Начальная настройка в Git:
email и имя пользователя, введенные при регистрации в Amvera:
git config --global user.email "belyakovilya755@gmail.com"
git config --global user.name "master"
'''
from PIL import Image

# Путь к файлу изображения
test_path = 'test_images/1.jpg'
img = Image.open(test_path)

# Вывод изображения на экран
#img.show()
import segment
import matplotlib.pyplot as plt
result = segment.process('test_images/1.jpg')
plt.imshow(result[2])
plt.show()





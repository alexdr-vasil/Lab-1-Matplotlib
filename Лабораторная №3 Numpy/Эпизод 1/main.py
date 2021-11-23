from PIL import Image
import numpy as np


for i in range(1, 4):
    # считаем картинку в numpy array
    img = Image.open("lunar0" + str(i) + "_raw.jpg")
    data = np.array(img)

    # ... логика обработки
    new_data = (data - data.min())*(255/(data.max() - data.min()))
    new_data = new_data.astype(int)

    # запись картинки после обработки
    res_img = Image.fromarray(new_data).convert('RGB')
    res_img.save("lunar0" + str(i) + "_changed.jpg")
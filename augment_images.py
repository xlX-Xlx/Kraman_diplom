import os
import imgaug.augmenters as iaa
from PIL import Image
import numpy as np

def augment_images(input_folder, output_folder):
    # Создаем папку для аугментированных изображений, если её нет
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Создаем экземпляр аугментатора
    seq = iaa.Sequential([
        iaa.Fliplr(0.5),  # Случайное отражение по горизонтали с вероятностью 50%
        iaa.Affine(rotate=(-10, 10))  # Случайное поворот изображения на угол от -10 до 10 градусов
    ])

    # Проходим по всем файлам в папке с изображениями
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Загружаем изображение
            image_path = os.path.join(input_folder, filename)
            image = Image.open(image_path)

            # Применяем аугментацию
            augmented_image = seq(images=np.array([image]))[0]

            # Преобразуем массив numpy обратно в объект изображения PIL
            augmented_image = Image.fromarray(augmented_image)

            # Сохраняем аугментированное изображение
            output_path = os.path.join(output_folder, f"augmented_{filename}")
            augmented_image.save(output_path)

if __name__ == "__main__":
    input_folder = "dataset/map"
    output_folder = "dataset/map"
    augment_images(input_folder, output_folder)

import os
from PIL import Image
import svgwrite

def convert_images_to_svg(input_folder, output_folder):
    # Создаем папку для сохранения SVG, если её нет
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Получаем список файлов в папке с изображениями
    image_files = os.listdir(input_folder)

    # Проходимся по каждому файлу
    for image_file in image_files:
        # Проверяем, что файл имеет расширение изображения
        if image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Определяем путь к текущему изображению
            image_path = os.path.join(input_folder, image_file)
            
            # Определяем имя для SVG файла (без расширения)
            svg_file_name = os.path.splitext(image_file)[0] + ".svg"
            
            # Путь к SVG файлу для сохранения
            svg_file_path = os.path.join(output_folder, svg_file_name)
            
            # Открываем изображение
            with Image.open(image_path) as img:
                # Создаем новый SVG рисунок
                dwg = svgwrite.Drawing(svg_file_path, size=img.size)
                
                # Проходимся по каждому пикселю изображения
                for y in range(img.size[1]):
                    for x in range(img.size[0]):
                        # Получаем цвет пикселя
                        color = img.getpixel((x, y))
                        # Конвертируем цвет в строку в формате "#RRGGBB"
                        color_str = '#{:02x}{:02x}{:02x}'.format(*color)
                        # Создаем прямоугольник с размером 1x1 и устанавливаем его цвет
                        dwg.add(dwg.rect((x, y), (1, 1), fill=color_str))
                
                # Сохраняем SVG файл
                dwg.save()
                
                print(f"Изображение '{image_file}' успешно сконвертировано в SVG и сохранено как '{svg_file_name}'")
    
    # Удаляем оригинальные изображения из папки map_img
    for image_file in image_files:
        image_path = os.path.join(input_folder, image_file)
        os.remove(image_path)
        print(f"Файл '{image_file}' удален.")

# Путь к папке с изображениями
input_folder = "images/map_img"

# Путь к папке для сохранения SVG
output_folder = "images/save_map"

# Вызов функции для конвертации изображений в SVG и удаления оригинальных изображений
convert_images_to_svg(input_folder, output_folder)

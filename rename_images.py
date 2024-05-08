import os

def rename_images(input_folder):
    # Получаем список файлов в папке
    files = os.listdir(input_folder)

    # Счетчик для переименования файлов
    count = 1

    # Проходим по всем файлам в папке
    for filename in files:
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Формируем новое имя файла
            new_filename = str(count) + os.path.splitext(filename)[1]

            # Полный путь к исходному файлу
            old_path = os.path.join(input_folder, filename)

            # Полный путь к новому файлу
            new_path = os.path.join(input_folder, new_filename)

            # Переименовываем файл
            os.rename(old_path, new_path)

            # Увеличиваем счетчик
            count += 1

if __name__ == "__main__":
    input_folder = "dataset/map"
    rename_images(input_folder)

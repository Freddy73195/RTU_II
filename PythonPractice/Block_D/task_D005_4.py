import os
import re

def move_files():
    # Создать папку "Ознакомительная папка"
    if not os.path.exists("GDZ5CLASSVILEKIN\Ознакомительная папка"):
        os.mkdir("GDZ5CLASSVILEKIN\Ознакомительная папка")

    for folder in ['тема A', 'тема B']:
        folder_path = os.path.join("GDZ5CLASSVILEKIN\Ознакомительная папка", folder)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)


    # Получить список файлов в па
    path = "GDZ5CLASSVILEKIN"
    files = os.listdir(path)

    # Определить, в какую папку переместить каждый файл
    for file in files:
        if re.search("task_A", file):
            # Переместить файл в папку "тема A"
            os.replace(os.path.join(path, file), "GDZ5CLASSVILEKIN/Ознакомительная папка/тема A" + file)
        elif re.search("task_B", file):
            # Переместить файл в папку "тема B"
            os.replace(os.path.join(path, file), "GDZ5CLASSVILEKIN/Ознакомительная папка/тема B" + file)


import importlib.util
import time

def execute_files():
    # Получить список подпапок в папке folder_path
    folder_path = "GDZ5CLASSVILEKIN\Ознакомительная папка"
    subfolders = [f.path for f in os.scandir(folder_path) if f.is_dir()]

    # Пройти по каждой подпапке
    for subfolder in subfolders:
        # Получить список файлов в подпапке
        files = os.listdir(subfolder)

        # Отфильтровать файлы, чтобы оставить только те, которые начинаются с "task_" и оканчиваются на ".py"
        py_files = [file for file in files if file.startswith("task_") and file.endswith(".py")]
        start_time = time.time()
        # Пройти по каждому файлу
        for py_file in py_files:
            # Открыть файл для чтения и прочитать его содержимое
            with open(os.path.join(subfolder, py_file), 'r', encoding='utf-8') as f:
                file_contents = f.read()

            # Импортировать модуль из файла
            spec = importlib.util.spec_from_file_location(py_file[:-3], os.path.join(subfolder, py_file))
            module = importlib.util.module_from_spec(spec)

            # Засечь время выполнения
            end_time = time.time()
            # Вывести время выполнения
            print(f"Файл {py_file} выполнен за {end_time - start_time:.7f} секунд")
            spec.loader.exec_module(module)
            print (f"\n")

move_files()
execute_files()
import os
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

def process_data_file(file_path):
    # Создаем папку для сохранения обработанных файлов, если её нет
    output_dir = "processed_data"
    os.makedirs(output_dir, exist_ok=True)
    
    # Читаем данные из файла
    with open(file_path, 'r') as f:
        data = np.loadtxt(f)
    
    # Проверяем, что файл не пустой
    if len(data) == 0:
        print("Файл пуст!")
        return
    
    # Получаем временной шаг (разница между первыми двумя значениями времени)
    time_step = data[1, 0] - data[0, 0] if len(data) > 1 else 0
    
    # Создаем имя нового файла
    now = datetime.now()
    new_filename = f"{now.day}_{now.month}_{now.year}_{time_step:.3f}.txt"
    new_file_path = os.path.join(output_dir, new_filename)
    
    # Сохраняем данные в новый файл
    np.savetxt(new_file_path, data)
    print(f"Данные сохранены в файл: {new_file_path}")
    
    # Создаем графики
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle('Анализ данных', fontsize=16)
    
    # График 1: Напряжение vs время
    ax1.plot(data[:, 0], data[:, 2], 'b-')
    ax1.set_xlabel('Время (годы)')
    ax1.set_ylabel('Напряжение (МПа)')
    ax1.set_title(f'Напряжение vs время\n(шаг: {time_step:.3f} года)')
    ax1.grid(True)
    
    # График 2: Толщина vs время
    ax2.plot(data[:, 0], data[:, 1], 'r-')
    ax2.set_xlabel('Время (годы)')
    ax2.set_ylabel('Толщина (мм)')
    ax2.set_title(f'Толщина vs время\n(шаг: {time_step:.3f} года)')
    ax2.grid(True)
    
    # График 3: Расположение точки максимума напряжений
    ax3.plot(data[:, 0], data[:, 3], 'g-', label='Позиция 1')
    ax3.plot(data[:, 0], data[:, 5], 'm-', label='Позиция 2')
    ax3.set_xlabel('Время (годы)')
    ax3.set_ylabel('Позиция (усл. ед.)')
    ax3.set_title('Расположение точки максимума напряжений')
    ax3.legend()
    ax3.grid(True)
    
    # Делаем графики квадратными
    for ax in [ax1, ax2, ax3]:
        ax.set_aspect('equal', adjustable='box')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    file_path = input("Введите путь к файлу с данными: ")
    try:
        process_data_file(file_path)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
import os
import time

def list_storage():
    try:
        items = os.listdir('storage')
        if items:
            print("[S] > Contents of 'storage':")
            for item in items:
                item_path = os.path.join('storage', item)
                
                # Получаем время создания
                creation_time = os.path.getctime(item_path)
                creation_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(creation_time))
                
                if os.path.isdir(item_path):
                    print(f" - {item}/ (Created: {creation_date})")
                else:
                    print(f" - {item} (Created: {creation_date})")
        else:
            print("[S] > 'storage' is empty.")
    except FileNotFoundError:
        print("[E] > 'storage' directory does not exist.")
import os

def hugo(filename):
    if not filename.endswith('.hgpk'):
        print(f"[E] > File '{filename}' is not a '.hgpk' file.")
        return

    source_folder = 'Hugo'
    destination_folder = 'storage'
    
    source_path = os.path.join(source_folder, filename)
    destination_path = os.path.join(destination_folder, filename[:-5] + '.py')

    if os.path.exists(source_path):
        os.rename(source_path, destination_path)
        print(f"[S] > File '{filename}' has been moved to '{destination_folder}' and renamed to '{filename[:-5]}.py'.")
    else:
        print(f"[E] > File '{filename}' does not exist in '{source_folder}'.")

def hgpk(filename):
    if not filename.endswith('.py'):
        print(f"[E] > File '{filename}' is not a '.py' file.")
        return

    source_folder = 'storage'
    destination_folder = 'Hugo'
    
    source_path = os.path.join(source_folder, filename)
    destination_path = os.path.join(destination_folder, filename[:-3] + '.hgpk')

    if os.path.exists(source_path):
        os.rename(source_path, destination_path)
        print(f"[S] > File '{filename}' has been moved to '{destination_folder}' and renamed to '{filename[:-3]}.hgpk'.")
    else:
        print(f"[E] > File '{filename}' does not exist in '{source_folder}'.")

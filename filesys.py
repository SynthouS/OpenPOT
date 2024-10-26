import os

def create_file(filename):
    if not os.path.exists('storage'):
        os.makedirs('storage')

    file_path = os.path.join('storage', filename)

    with open(file_path, 'w') as f:
        pass

    print(f'[mk] > File in {file_path} created')

def remove_file(filename):
    file_path = os.path.join('storage', filename)

    if os.path.exists(file_path):
        os.remove(file_path)
        print(f'[rm] > File in {file_path} removed')
    else:
        print(f'[rm] > File {file_path} does not exist')
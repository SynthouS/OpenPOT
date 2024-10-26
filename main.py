import os
import filesys
import potfetch
import hugo
import ls

print("Welcome to OpenPOT, if you want more information, type help")

__version__ = 1.0

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def run():
    while True:
        command = input("[/] > ")
        parts = command.split()
        if len(parts) == 1 and parts[0] == "v":
            print(f"[V] > OpenPOT {__version__} Nightly")
        elif len(parts) == 1 and parts[0] == "version":
            print(f"[V] > OpenPOT {__version__} Nightly")
        elif len(parts) == 1 and parts[0] == "exit":
            print("[Q] > Quiting...")
            break
        elif len(parts) == 1 and parts[0] == "q":
            print("[Q] > Quiting...")
            break
        elif len(parts) == 1 and parts[0] == "help":
            print("OpenPOT or OpenPython-OS-in-Terminal it's a free open source OS in terminal.")
            print("q, -exit = Shutdown POT")
            print("v, -version = Shows version of POT")
            print("mk = create file")
            print("rm = delete file")
            print("potfetch = display OpenPOT info")
            print("hugo <filename.hgpk> = Move file from Hugo to storage and change extension to .py")
            print("hgpk <filename.py> = Move file from storage to Hugo and change extension to .hgpk")
            print("clean = Clear the screen")
            print("ls = List files and directories in 'storage'")
        elif command.startswith('mk '):
            filesys.filename = command[3:]
            filesys.create_file(filesys.filename)
        elif command.startswith('rm '):
            filesys.filename = command[3:]
            filesys.remove_file(filesys.filename)
        elif command.startswith('hugo '):
            filesys.filename = command[5:]
            hugo.hugo(filesys.filename)
        elif command.startswith('hgpk '):
            filesys.filename = command[5:]
            hugo.hgpk(filesys.filename)
        elif command == 'potfetch':
            potfetch.potfetch()
        elif command == 'clean':
            clear_screen()
        elif command == 'ls':
            ls.list_storage()
        else:
            print("[/] > Invalid command!")

if __name__ == "__main__":
    run()
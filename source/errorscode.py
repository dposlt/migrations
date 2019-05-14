from source import colors

def terminate():
    print(colors.yellow('Program termination'))


def serverison(server):
    print(colors.green(f'Server {server} is up and ready'))

def availabe(server):
    print(colors.red(f'On server {server} is not access'))

def folder(foldername):
    print(colors.red(f'Folder {foldername} is not exists'))

def copy(foldername):
    print(colors.red(f'Folder {foldername} is not copies'))

def tar(file):
    print(colors.red(f'File {file} is not tar file'))
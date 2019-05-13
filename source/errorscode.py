from source import colors

def terminate():
    print(colors.yellow('Terminate program'))


def serverison(server):
    print(colors.green(f'Server {server} is up and ready'))

def availabe(server):
    print(colors.red(f'On server {server} is not access'))
import configparser, os, tarfile, colorama
from source import colors, errorscode, ping


config = configparser.ConfigParser()

config.read('source/source.ini')

onprem = config['SERVERONPREM']['ServerName']
pathonprem = config['SERVERONPREM']['Path']
awsserver = config['SERVERAWS']['ServerName']
pathaws = config['SERVERAWS']['Path']



if ping.get_Host_name_IP(onprem):
    errorscode.serverison(onprem)

if ping.get_Host_name_IP(awsserver):
    errorscode.serverison(awsserver)


def changedir(server, path):
    try:
        fullserver = "\\\{server}\\D$".format(server = server)
        os.chdir(fullserver)
    except:
        errorscode.availabe(server)
        errorscode.terminate()
        quit()

    if (os.getcwd() == fullserver):
        getpath = os.chdir(path)
        return getpath
    else:
        print(colors.red(f'Path --{path}-- is not available'))
        errorscode.terminate()
        quit()



def getdirs(servername, pathname):
    dirs = os.listdir(changedir(servername, pathname))

    return dirs

def ctar(dir):
    nameofdir = dir+'.tar'
    tar = tarfile.open(nameofdir, "w:gz")
    tar.add(dir)
    tar.close()



if __name__ == '__main__':

    #ctar(getdirs()[0])
    print(getdirs(awsserver,pathaws))

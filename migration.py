#!/usr/lib/env python3

import configparser, os, tarfile, colorama
from source import colors, errorscode, ping, list
import sys
from datetime import datetime



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
        sys.exit()

    if (os.getcwd() == fullserver):
        getpath = os.chdir(path)
        return getpath
    else:
        print(colors.red(f'Path --{path}-- is not available'))
        errorscode.terminate()
        sys.exit()



def getdirs(servername, pathname):
    dirs = os.listdir(changedir(servername, pathname))

    return dirs

def ctar(dir):
    nameofdir = dir+'.tar'
    tar = tarfile.open(nameofdir, "w:gz")
    tar.add(dir)
    tar.close()

def migrations():
    print(colors.green('----Starting migrations----'))
    start = datetime.now()
    print(start)
    migrationlist = list.migrationslist()
    for i in migrationlist:
        if i in getdirs(onprem,pathonprem):
            print(colors.green(f'Starting tar folder {i}'))
            ctar(i)
        else:
            errorscode.folder(i)


    end = datetime.now()
    print(end)
    print(colors.yellow('Duration: {}'.format(end - start)))
    print(colors.green('----Starting migrations----'))
    sys.exit()




if __name__ == '__main__':

    migrations()

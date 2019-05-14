#!/usr/lib/env python3

import configparser, os, tarfile, colorama
from source import colors, errorscode, ping, list, log
import sys
from datetime import datetime
from shutil import copy



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

def utar(file):
    if tarfile.is_tarfile(file):
        tar = tarfile.open(file, 'r:gz')
        tar.extractall()
    else:
        errorscode.tar(file)

def copyTarFiles(source, target):
    try:
        copyfile(source,target)
        log.Loger.writeLog(f'Starting copy file {source} to {target}')
    except:
        errorscode.colors(source)
        log.Loger.writeLog(f"folder {i} is not copies")



def migrations():
    print(colors.green('----Starting migrations----'))
    startmigrations = datetime.now()
    migrationlist = list.migrationslist()
    for i in migrationlist:
        if i in getdirs(onprem,pathonprem):
            start = datetime.now()
            print(colors.green(f'Starting tar folder {i} ----- {start}'))
            log.Loger.writeLog(f'Starting tar folder {i}')
            ctar(i)
            tarcopyfile = i + '.tar'
            log.Loger.writeLog(f'Starting copy file {tarcopyfile} to {awsserver}')
            print(colors.green(f'Starting copy tar file {tarcopyfile} to {awsserver}'))
            targetserver = r'\\{server}\d$\{path}'.format(server = awsserver, path = pathaws)
            copy(tarcopyfile,targetserver)
            os.remove(tarcopyfile) #remove on premis server
            os.chdir(targetserver)
            log.Loger.writeLog(f'Extract tarfile {tarcopyfile}')
            print(colors.green(f'Extract tarfile {tarcopyfile}'))
            extractfile = r'{server}\{file}'.format(server = targetserver, file = tarcopyfile)

            utar(extractfile)
            log.Loger.writeLog(f'Delete tarfile {tarcopyfile}')
            print(colors.yellow(f'Delete tarfile {tarcopyfile} from target server'))
            os.remove(extractfile)
            end = datetime.now()
            print(colors.green(f'Finish migration tar folder {i} ----- {end}'))
            print(colors.yellow('Duration: {}'.format(end - start)))
        else:
            errorscode.folder(i)
            log.Loger.writeLog(f"folder {i} doesn't exists")



    endmigrations = datetime.now()
    print(colors.yellow('All migrations duration: {} minutes'.format(endmigrations - startmigrations)))
    print(colors.green('----Finish migrations----'))
    sys.exit()




if __name__ == '__main__':

    migrations()

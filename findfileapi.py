import os
import psutil
class FindFiles:
    def findFile(path, filename):
        for dirpath, dirnames, filenames in os.walk(path):
            for file1 in filenames:
                if file1.lower() == filename.lower():
                    print(f'file {file1} is found in {dirpath}')

    def findExt(path, ext):
        for dirpath, dirnames, filenames in os.walk(path):
            for file1 in filenames:
                file = os.path.splitext(file1)
                if file[1].lower() == ext.lower():
                    print(file1)

    def findBiggest(path):
        biggestSize = -1
        biggestFile = ''

        for dirpath, dirnames, filenames in os.walk(path):
            for file1 in filenames:
                if os.stat(os.path.join(dirpath, file1)).st_size > biggestSize:
                    biggestSize = os.stat(dirpath + '\\' + file1).st_size
                    biggestFile = dirpath + '\\' + file1
        print (f'The biggest file is {biggestFile} at {biggestSize} bytes')

class ProcUtil:
    def showProc():
        for proc in psutil.process_iter():
            print(f'Name: {proc.name()} ID {proc.pid}')


def main():
    FindFiles.findFile('c:\k', 'K.TXT')
    FindFiles.findExt('c:\k', '.TXT')
    FindFiles.findBiggest('c:\k')
    print(os.environ["PATH"])


if __name__ == "__main__":
    main()

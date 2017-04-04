import os


def iterator_dirfile():

    files = os.popen('ls -ltr * .py')
    fileit = iter(files)
    for files in fileit:
        print(files)

if __name__ == "__main__":
    iterator_dirfile()
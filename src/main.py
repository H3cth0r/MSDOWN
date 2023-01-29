from downloader import Downloader

if __name__ == "__main__":
    """
    1. Download from plist.txt
    2. Download single song
    3. Exit
    """
    option = 0
    while option != 3:
        print("SELECT AN OPTION\n\t1. Download from plist.txt\n\t2. Download single song\n\t3. Exit")
        option = int(input(">>> "))
        if option == 1:
            dld = Downloader()
            num_process = 0
            while num_process != 0 and not isinstance(numprocess, int):
                num_process = int(input("type number of subprocesses: "))
            dld.startDownloading()
        elif option == 2:
            dld = Downloader(input("type url: "))
            dld.startDownloading()
        elif option == 3:
            exit()
        else:
            continue

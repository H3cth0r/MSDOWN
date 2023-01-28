from downloader import Downloader

if __name__ == '__main__':
    songs = ["https://www.youtube.com/watch?v=-yudkRaKRIg",
             "https://www.youtube.com/watch?v=dapgfO59ar8"]
    dld = Downloader(songs)
    dld.number_of_processes = 3
    dld.startDownloading()

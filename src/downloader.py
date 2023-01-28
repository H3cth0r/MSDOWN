import youtube_dl
import concurrent.futures
from concurrent.futures import wait

class Downloader:
    # General conditions for youtube_dl
    conditions_ydl = {'format': 'bestaudio/best','outtmpl': 'UsbStick/%(title)s.%(ext)s','ignoreerrors': True,'postprocessors'    : [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality'  : '192',}],}

    def __init__(self, *args):
        """
        @brief
        Class constructor. Recives any kind of args and will adapt the attributes
        depending on this parameters.
        @params

        args        List of arguments
        """
        # Variable for storing the number of process to open while downloading
        # From a list.
        self.number_of_processes    = 1

        # Setting the youtube_dl constructor
        ydl = youtube_dl.YoutubeDL(self.conditions_ydl)

        if len(args) == 0:
            # Constructor for just reading the plist.txt file
            self.option     =   0
        elif len(args) == 1       and isinstance(args[0], str):
            # Constructor for downloading just one video music
            self.option     =   1
            self.URL    =   args[0]
        elif len(args) == 1      and isinstance(args[0], list):
            # Constructor for downloading a list of links of songs 
            # if args[1] == False, then a list of songs
            self.option     =   2
            self.download_list  = args[0]

    def ddp(self, line_t):
        """
        @brief
        Method that is runned on each downloadPlaylistsPlists subprocessubprocesss.

        @params
        line_t      the url of the playlist

        @returns
        String confirmation
        """
        ydl_t = youtube_dl.YoutubeDL(self.conditions_ydl)
        ydl_t.download([line_t])
        return f"done: {line_t}"

    def downloadPlaylistsPlists(self):
        """
        ®brief
        This method is supposed to start subprocesses, depending on the
        specified number of subprocess to apply, for downloading the
        plist.txt file list of playlists.
        """
        file    =   open("plist.txt")
        lines   =   file.readlines()

        # Setting max num of process == 5
        if self.number_of_processes > 5: self.number_of_processes = 5

        with concurrent.futures.ProcessPoolExecutor(max_workers=self.number_of_processes) as executor:
            results =   executor.map(self.ddp, lines)
            for result in results:
                print(result)

    def downloadFromList(self):
        """
        @brief
        Method for downloading from the list recived as argument on constructor
        """
        lines = self.download_list
        # Setting max num of process == 5
        if self.number_of_processes > 5: self.number_of_processes = 5

        with concurrent.futures.ProcessPoolExecutor(max_workers=self.number_of_processes) as executor:
            results =   executor.map(self.ddp, lines)
            for result in results:
                print(result)


    def startDownloading(self):
        """
        @brief
        Method for start to download the audio, depending on option/configuration
        """
        if self.option   == 0:
            self.downloadPlaylistsPlists()
        elif self.option   == 1:
            self.ddp(self.URL)
        elif self.option   == 2:
            self.downloadFromList()

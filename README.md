# MSDOWN
This is just a simple implementation of the youtube-dl module. In this implementation it's been added
multiprocessing operations, for faster performance and therefore faster downloads for larger sets.

## Installation
For the development of the current implementation, it has beem used python 3.9.6, therefore it is recommended this
or newer versions. Youtube-dl must be install using "pip"(python package installer):
```
pip install youtube_dl
OR
pip3 install youtube_dl
```

Must also install ffmpeg. For MACOS machines it's recommend to install via [Homebrew](https://brew.sh).
[ffmpeg install](https://formulae.brew.sh/formula/ffmpeg)

For Windows machines you can follow this [tutorial](https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/).

For ubuntu/linux servers you can just type the following command:
```
sudo apt update && sudo apt upgrade
sudo apt install ffmpeg
```

Download the current repo in derised directory. It's recommended to work on the "main.py" file for your own
implementations.

## Recommendations
For this personal implementation, it was used as raspberry pi device to run a local ubuntu server, because of the
volume on downloads and time taken to complete the execution; so it's recommended to use an external device.

## TODO
- Apply better exception handlers.
- Reduce and clean code.
- Might be a good idea to get the playlist urls as individual videos and
multiprocess the download.

## Run
A basic program was added for straightforward usage. This basic program gives you the options to download 
a single song or playlist just by typing the url on the command promt; It is also posible to make multiple downloads
given a set of playlists and single videos urls, defined on the "plist.txt" file. The user must
must specify the number of subprocesses to open ( for this implementation it has been limited to 5 subprocesses).
1. Navigate to the src folder.
2. Type the following instruction in the commando prompt:
```
python3 main.py
OR
python main.py
```
3. You'll be able to find the output on the UsbStick folder. You can even mount a usb partition on this folder and
directly saving the output on your external drive.

## Examples
If your making your own implementations, here are some examples you can follow.

### Example for downloading from an array of urls
```
from downloader import Downloader
if __name__ == '__main__':
	songs = ["https://www.youtube.com/watch?v=-yudkRaKRIg",
		 "https://www.youtube.com/watch?v=dapgfO59ar8"]
 	dld = Downloader(songs)
	dld.number_of_processes = 3
	dld.startDownloading()
```

### Example Downloading from single link
```
from downloader import Downloader
if __name__ == '__main__':
 	dld = Downloader("https://www.youtube.com/watch?v=-yudkRaKRIg")
	dld.startDownloading()
```

### Example Downloading from plists.txt
```
from downloader import Downloader
if __name__ == '__main__':
 	dld = Downloader()
	dld.number_of_processes = 3
	dld.startDownloading()

```



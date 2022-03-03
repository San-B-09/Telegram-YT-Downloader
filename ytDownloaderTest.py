from asyncio.windows_events import NULL
import youtube_dl as yt
import json

MAX_VIDEO_SIZE = 1100000

def download_video(link, format='video'):
    print("Fetching Video Details...")
    try:
        with yt.YoutubeDL({}) as ydl:
            dictMeta = ydl.extract_info(link, download=False)
    except yt.utils.DownloadError:
        return "Invalid URL!"

        
    if(format == 'video'):
        availableFormats = [format for format in dictMeta['formats'] if(
            format['filesize'] != None and format['filesize'] <= MAX_VIDEO_SIZE and format['ext']=='mp4')]
        if(len(availableFormats) == 0):
            return "Video is Oversized"

        sorted(availableFormats, key=lambda x: x['format_note'][:-1:])
        print(availableFormats)

        ydl_opts = {
            'format_id': availableFormats[-1]['format_id'],
            'outtmpl': './%(id)s.%(ext)s'
        }
    else:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': './%(id)s.%(ext)s'
        }

    # print(ydl_opts)
    with yt.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    

print(download_video('https://youtu.be/3sZnzyke0gE'))

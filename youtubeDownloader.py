from pytube import YouTube, Playlist
import re


# Function that handles the downloading of a playlist of videos; displays how many videos are to be downloaded and keeps a running tally of downloaded videos.

def playlist_downloader(p_link, dir):
    p = Playlist(p_link)
    total = len(p.videos)
    
    print(f'Total videos: {total}')
    
    count = 0
    space = ''
    padding = space.center(5)
    
    for video in p.videos:
        count += 1
        print(f'Downloading: {video.title} ', padding, count, 'of', total)
        video.streams.first().download(dir)

    print(f'{total} of {total} videos downloaded!')
    
# Function that handles the downloading of single videos; downloads in 720p, but can do other resolutions as well 
def video_downloader(link, dir):
    print('Total videos: 1')

    v = YouTube(link)
    mp4_files = v.streams.filter(file_extension="mp4")
    print(f'Downloading: {v.title}')
    mp4_files_720p = mp4_files.get_by_resolution("720p")
    mp4_files_720p.download(dir)
    
    print('1 of 1 videos downloaded!')
    
# Small splash screen that displays the name and version of the program
def splash():
    header = '\n############ Python YouTube Downloader v1.0 ############\n'
    header_centered = header.center(100, " ")
    print(header_centered)

# Runtime code that displays the name and asks for a link to download from
print('\nThis program will allow you to download the YouTube videos from any playlist or video you choose\n')

link = input('Enter a link to a video or playlist: ')

# Filter code that determines if the link submitted is a single video or a playlist. 
# Calls the proper function to manage the link.
if(re.search('list', link)):
    p_link = link
    dir = 'playlists/'
    splash()
    playlist_downloader(p_link, dir)
    
else:
    dir = 'videos/'
    splash()
    video_downloader(link, dir)

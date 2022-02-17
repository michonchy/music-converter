from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=bnzPJhW9XQg')
stream = yt.streams.first()
finished = stream.download()
from multimedia import MultimediaLibrary
from multimedia import AudioStream
from multimedia import VideoStream

def main():
    
    a = AudioStream('Audio', 'url://localhost/Music/something.mp3', 'Stereo')
    print("Kind should be: Audio")
    print(a.Kind())
    print("Location should be: url://localhost/Music/something.mp3")
    print(a.Location())
    print("Full range channel should be: 2")
    print(a.full_range_channels())
    print(a.__str__())

    print("#############################################" + "\n")
    b = VideoStream("Video", "url://localhost/Movies/The Departed (2006).m4v", "Stereo", "1280x720","Progressive")
    print("Resolution should be: 720p")
    print(b.resolution())
    print(b.__str__())

    print("#############################################" + "\n")

    c = MultimediaLibrary()
    c.oopen('file.txt')
    c.add(c.avStreams)
    print("There should be a object identical to file.txt")
    print(c.avStreams)
    c.network_playlist()
    print(c.network_playlist())


main()

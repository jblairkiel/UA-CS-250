from scanner import Scanner
class AudioStream():

    def __init__(self, kind, location, channels):
        
        self.kind = kind
        self.location = location
        self.channels = channels

    def __str__(self):
        
        #print(self.kind + "!" + self.location + "!" + self.channels)
        return self.kind + "!" + self.location + "!" + self.channels

    def Kind(self):
        
        return self.kind

    def Location(self):
        
        return self.location

    def full_range_channels(self):
        
        if(self.channels == "Mono"):
            return 1
        elif(self.channels == "Stereo"):
            return 2
        elif(self.channels == "5.1"):
            return 5
        elif(self.channels == "3" or "4.1"):
            return 7

class VideoStream(AudioStream):

    def __init__(self, kind, location, channels, dimensions, scanning):

        super().__init__(kind,location,channels)
        self.dimensions = dimensions
        self.scanning = scanning

    def __str__(self):  
    
        s = super().__str__() + "!" + self.dimensions + "!" + self.scanning
        return print(s)
        #return print(super.kind + "!" + super.location + "!" + super.channels + "!" + self.dimensions + "!" + self.scanning)

    def resolution(self):
    
        if(self.dimensions == '640x480' and self.scanning == 'Interlaced'):
            return '480i'
        elif(self.dimensions == '1280x720' and self.scanning == 'Progressive'):
            return '720p'
        elif(self.dimensions == '1920x1080' and self.scanning == 'Progressive'):
            return '1080p'

class MultimediaLibrary():
    
    def __init__(self):
        
        self.avStreams = []
        self.playlistEntries = []

    def oopen(self, filename):
        s = Scanner(filename)
        kind = s.readline()
        location = s.readline()
        channels = s.readline()
        dimensions = s.readline()
        if (dimensions == ""):
            self.audioS = [kind, location, channels] 
            return
        else:
            scanning = s.readline()
            a = [kind, location, channels, dimensions, scanning]
            self.avStreams.append(a)
            s.close() 
        return

    def add(self, stream):
        
        self.avStreams.append(stream) 
        return

    def network_playlist(self): 

        for i in range(len(self.avStreams)):
            if (self.avStreams[i] == 'url://'):
                new = str(self.avStreams) + '\n'
                self.network.append(new)

    def surround_playlist(self):    
        
        for i in range(len(self.avStreams)):    
            if (self.avStream[i][2] == '5.1' or '3' or '4.1'):
                new = str(self.avStream) + '\n'
                self.surround.append(new)

    def save_playlists(self, filename): 

        allPlaylist = '[network]' + '\n' + self.network + '\n' + '[surround]' + self.surround 
        print(allPlaylist)

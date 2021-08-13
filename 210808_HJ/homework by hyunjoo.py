class MP3:
    def __init__(self, song1):
        self.song1 = song1
        self.song2 = ""
 
    def play(self):
        print(self.song1 + "를 재생합니다.")
 
    def add(self, song):
        self.song2 = song
        print(self.song2 + "를 추가합니다.")
 
    def pause(self):
        print(self.song1 +"를 일시정지합니다.")
 
    def delete(self):
        self.song1 = "BIBI - Life is a bi..."
        print(self.song1 +"를 삭제합니다.")
 
 
 
A = MP3("BIBI - Life is a bi...")
A.play()
A.pause()
A.delete()
A.add("BIBI - Bad sad and mad")# your code goes here
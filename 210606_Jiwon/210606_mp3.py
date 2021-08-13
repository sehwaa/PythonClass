class Mp3:
	def __init__(self, song1, song2):
		self.song1 = song1
		self.song2 = song2
		
	def add_song(self, song3):
		print(self.song + song3)
		
	def add_song_play(self):
		print(self.song + "재생")
		
	def add_song_pause(self):
		print(self.song + "일시정지")
		
	def add_song_delete(self):
		print(self.song + "삭제")
		

BTS = Mp3("노래1", "노래2")
BTS.add_song_play()
BTS.add_song_pause()
BTS.add_song_delete()

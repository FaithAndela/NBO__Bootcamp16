class Box():
	"""box is the main object"""
	volume=0
	vol_matchbox=0
	length=0
	width=0
	height=0
	def __init__(self, length=0,width=0,height=0):
		self.length=length
		self.width=width
		self.height=height

	volume=length*width*height
	print(volume)


	class Matchbox(Box):
		"""match box inhrits some fatures form box like length,width  and height"""
		def __init__(self, l,w,h):
			super(Matchbox, self).__init__()
			self.lenth = l
			self.width=w
			self.height=h
	vol_matchbox=(l*w*h)
	print(vol_matchbox)

	
class Movie ( ) :
	def __init__ ( self , title , desc , poster , trailer ) :
		
		self.title = title
		self.desc = desc
		self.poster = poster
		self.trailer = trailer

	def showTrailer ( ) :

		browser.open ( self.trailer )
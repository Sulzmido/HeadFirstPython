import webapp2

class InputPage(webapp2.RequestHandler):

	def get(self):
		html = '<html><body>Hello World!</body></html>'
		self.response.out.write(html)

app = webapp2.WSGIApplication([('/', InputPage)], debug=True)

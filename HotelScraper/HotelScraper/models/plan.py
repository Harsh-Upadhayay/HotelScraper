from .initalizerModel import InitializerModel


class Plan(InitializerModel):

	def __init__(self, props=None):
		self.identifier = None
		self.has_public_page = None
		self.name = None
		self.slug = None
		self.lat = None
		self.lng = None
		self.modified = None
		super(Plan, self).__init__(props)

	def _init_properties_custom(self, value, prop, arr):

		if prop == 'id':
			self.identifier = value

		standart_properties = [
			'has_public_page',
			'name',
			'slug',
			'lat',
			'lng',
			'modified',
		]

		if prop in standart_properties:
			self.__setattr__(prop, value)

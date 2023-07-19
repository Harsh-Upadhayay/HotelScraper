import json
import time


class InitializerModel:

	def __init__(self, props=None):

		"""Array of initialization data"""
		self._data = {}

		self.modified = time.time()
		if len(props) > 0:
			self._init(props)

	def _init(self, props):
		"""
		:param props: props array
		:return: None
		"""
		for key in props.keys():
			try:
				self._init_properties_custom(props[key], key, props)
			except AttributeError:
				# if function does not exist fill help data array
				self._data[key] = props[key]


	def __repr__(self):
		return json.dumps(self, default=lambda o: o.__dict__)
	
	def _filter_text(self, text):
		if text == None:
			text = ''
		else:
			text = text.replace(u'\\n', u' ')
			text = ' '.join(text.split())
		return text

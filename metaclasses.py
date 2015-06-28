class metaclass(type):
	def __new__(cls, future_class_name, future_class_parents, future_class_attr):
		print 'metaclass __new__(%s,%s,%s,%s)' % (str(cls),str(future_class_name),str(future_class_parents),
							str(future_class_attr))
		attrs = {}
		for name, val in future_class_attr.items():
			if not name.startswith('__'):
				attrs[name.upper()] = val
			else:
				attrs[name] = val
		print attrs
		return super(metaclass, cls).__new__(cls, future_class_name,future_class_parents,attrs)


class testmeta(object):
	__metaclass__ = metaclass

	def __init__(self):
		print 'testmeta __init__'


if __name__ == '__main__':
	t = testmeta()

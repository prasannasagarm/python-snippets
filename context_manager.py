from contextlib import contextmanager

@contextmanager
def cm_simple(*args,**kwargs):
	print "Entered context"
	print "args = %s" % str(args)
	print "kwargs = %s" % str(kwargs)
	yield 'return something just for demo'
	print "Leaving context"

class cm_complex(object):
	def __init__(self,*args,**kwargs):
		print 'initialized complex context'

	def __enter__(self):
		# use another context manager to demo chaining
		print 'entered complex context'
		with cm_simple():
			print 'inside simple cm'
		return 'return something from complex cm'

	# def __exit__(self): # this will throw error
	def __exit__(self, exc_type, exc_val, traceback):
		print 'exception details: %s:%s\n%s' % (str(exc_type),str(exc_val),str(traceback))
		# catch exceptions 
		print 'exit complex cm'
		

def test_cm():
	with cm_simple(1,2,named='name') as return_value:
		print 'inside context'
		print 'return value: %s' % return_value

	with cm_complex(3,4,cnamed = 'cname') as return_value:
		print 'inside complex cm'
		raise ValueError('raised exception to test the __exit__ of cm')
		print 'return value: %s' % return_value


if __name__ == '__main__':
	test_cm()

	

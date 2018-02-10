'''
namespace is same as giving name to each element 
__name__ is used to get the name of module 
if we excute the python code it's namespace becomes __main__
'''
print('the namespace __name__',__name__)
if('__main__'== __name__):
	print('the end namespace ',__name__)

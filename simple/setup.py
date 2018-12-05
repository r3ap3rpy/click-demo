from setuptools import setup

setup(
	name = 'simple',
	version = '0.1',
	install_requires = ['Click',],
	py_modules = ['simple'],
	entry_points = '''
	[console_scripts]
	hello=simple:hello
	rock=simple:pythonrocks
	'''
)
from distutils.core import setup
from foreground import __version__, __author__

setup(
    name='foreground',
    packages=['foreground'],
    version=__version__,
    description='Select foreground text color based on background color to get better contrast.',
    long_description='Select foreground text color based on background color to get better contrast.',
    long_description_content_type='text/x-rst',
    author=__author__,
    author_email='azaitsev@gmail.com',
    url='https://github.com/azaitsev/foreground',
    keywords=['colors', 'foreground', 'background', 'text', 'contrast', 'web', 'font'],
    classifiers=[]
)
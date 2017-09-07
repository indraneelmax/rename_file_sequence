from distutils.core import setup

setup(
    name='rename_file_sequence',
    version='1.0.0',
    packages=['rename_file_sequence'],
    url='https://github.com/indraneelmax/rename_file_sequence',
    license='',
    scripts=["bin/rename_file_sequence"],
    author='isrivastava',
    author_email='indraneel.max@gmail.com',
    description='Identifies file sequence in a dir and renames them in sequentially keeping the same order'
)

from distutils.core import setup

setup(
        name='ProcessInteract',
        version="0.0.2",
        author='weirdoo',
        requires=['psutil'],
        author_email='weirdoo145@gmail.com',
        packages=['processinteract'],
        description='Package for easy interacting with processes and command line (bash)',
    )
from setuptools import setup

setup(name='STLLock',
      version='0.0.3',
      description='oauth2.0 stlock',
      packages=['stlock'],
      author_email='office@stl.im',
      zip_safe=False,
      requires=["requests", "PyJWT"])

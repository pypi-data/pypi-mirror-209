from setuptools import setup

setup(name='stlock',
      version='0.0.4',
      description='oauth2.0 stlock',
      packages=['stlock'],
      author_email='office@stl.im',
      zip_safe=False,
      install_requires=["requests", "pyjwt"])

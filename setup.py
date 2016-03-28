import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'waitress',
    'pyramid_jinja2'
    ]

tests_requires = ['pytest', 'pytest-watch', 'tox', 'webtest']
dev_requires = ['ipython', 'pyramid-ipython']

setup(name='Twitter_Tunes',
      version='0.0',
      description='Twitter_Tunes',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      extras_require={
        'test': tests_requires,
        'dev': dev_requires
      },
      test_suite="twitter_tunes",
      entry_points="""\
      [paste.app_factory]
      main = twitter_tunes:main
      """,
      )

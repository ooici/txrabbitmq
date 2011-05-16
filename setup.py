from setuptools import setup

setup(
  name = "txrabbitmq",
  version="0.5",
  description="RabbitMQ's 'rabbitmqctl' as a Twisted Service",
  
  author="OOICI",
  author_email="mmeisinger@ucsd.edu",
  url="http://github.com/ooici/txrabbitmq",
  download_url="http://ooici.net/releases",
  classifiers=[ ],
  packages=['txrabbitmq', 'twisted/plugins'],
  data_files=[('twisted/plugins', ['twisted/plugins/txrabbitmq_plugin.py'])],
  install_requires = ['twotp==0.7', 'Twisted==10.2.0', 'simplejson==2.1.2'],
)

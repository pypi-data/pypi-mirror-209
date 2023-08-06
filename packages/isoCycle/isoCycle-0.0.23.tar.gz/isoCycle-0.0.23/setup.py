from setuptools import setup
setup(
  name = 'isoCycle',         
  packages = ['isoCycle'],   
  version = '0.0.23',      
  license='CC-BY-NC-SA-4.0',        
  description = 'isolating single cycles of oscillatory activity in neuronal spiking',   
  author = 'Ehsan Sabri',                   
  author_email = 'ehsan.sabri@gmail.com',      
  url = 'https://github.com/esiabri/isoCycle',  
  download_url = 'https://github.com/esiabri/isoCycle/archive/refs/tags/0.0.5.tar.gz',   
  keywords = ['Neuroscience', 'Oscillation', 'Cycle'],  
  setup_requires=['setuptools_scm'],
  include_package_data=True,
  install_requires=[            
          'numpy',
        #   'pickle',
        #   'tensorflow',
        #   'scipy',
        #   'ipympl',
        #   'ipywidgets'
      ],
  classifiers=[
    'Development Status :: 2 - Pre-Alpha',     
    'Intended Audience :: Science/Research', 
    'Programming Language :: Python',   
  ],
)
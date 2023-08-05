import setuptools

print(setuptools.find_packages())
setuptools.setup(
     name='CirclesGenderDetectorPython',  
     version='0.0.1',
     author="Circles",
     author_email="info@circles.zone",
     description="PyPI Package for gender detection",
     long_description="This is a package for running gender detection and predicting gender",
     long_description_content_type="text/markdown",
     url="https://github.com/circles-zone/gender-detection-backend",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: Other/Proprietary License",
         "Operating System :: OS Independent",
     ],
 )

from setuptools import setup, find_packages 

with open('requirements.txt') as f: 
	requirements = f.readlines() 

long_description = 'Sample Package made for a demo \
	of its making for the GeeksforGeeks Article.' 

setup( 
		name ='urlsearch', 
		version ='1.0.0', 
		author ='Arnab Datta', 
		author_email ='arnab.datta123@gmail.com', 
		url ='https://github.com/Vibhu-Agarwal/vibhu4gfg', 
		description ='Search for an wikipedia url', 
		long_description = long_description, 
		long_description_content_type ="text/markdown", 
		license ='MIT', 
		packages = ["code_section"], 
		entry_points ={ 
			'console_scripts': [ 
				'urlsearch = code_section.main:main'
			] 
		}, 
		classifiers =( 
			"Programming Language :: Python :: 3", 
			"License :: OSI Approved :: MIT License", 
			"Operating System :: OS Independent", 
		),  
		install_requires = requirements, 
		zip_safe = False
) 


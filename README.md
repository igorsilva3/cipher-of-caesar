<!-- Header -->
<p align="center">
  <img src="https://i.imgur.com/kpkGHxw.png" alt="Logo">
 </p>
<p align="center">
  	<img alt="Repository size" src="https://img.shields.io/github/repo-size/igorsilva3/cipher-of-caesar">
  	<a href="https://github.com/igorsilva3/cipher-of-caesar/commits/master">
    	<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/igorsilva3/cipher-of-caesar">
  	</a> 
  	<img alt="License" src="https://img.shields.io/github/license/igorsilva3/cipher-of-caesar">
  	<a href="https://github.com/igorsilva3/cipher-of-caesar/stargazers">
    	<img alt="Stargazers" src="https://img.shields.io/github/stars/igorsilva3/cipher-of-caesar">
  	</a>
</p>

<!-- Description  -->
> *This is project is a desktop cryptography application written with Python. The encryption method is the Caesar cipher. :stars:*

<!-- Table of contents -->
## :pushpin: Table of Contents
- [Application screenshot](#application-screenshot)
- [Technologies](#technologies)
- [Prerequisites](#prerequisites)
- [How to run](#how-to-run)
- [GUI modification](#gui-modification)
- [License](#license)

<!-- Application screenshot -->
## Application screenshot

| ![Application Image 1](https://i.imgur.com/rOIH0JP.jpg) | ![Application Image 2](https://i.imgur.com/DlzLnwI.jpg) |
| ------------------------------------------------------- | ------------------------------------------------------- |

<!-- Technologies -->
## Technologies
* [Python](https://www.python.org/) 
* [PySide2](https://wiki.qt.io/Qt_for_Python)

<!-- Prerequisites -->
## Prerequisites
* Python 3.7.1+ installed in your machine

- #### Creation of virtual environment
	```bash
	# Installing virtualenv for Python
	$ python3 -m pip install virtualenv

	# Creating your virtual environment
	$ python3 -m virtualenv name-of-your-virtual-environment

	# Activating virtual environment
	$ source name-of-your-virtual-environment/bin/activate
	```

- #### Installing dependencies
	```bash
	# Enter in folder of project
	$ cd cipher-of-caesar/
	``` 
  	Make sure what the virtual environment this activated.
	```bash
	# Installing requirements
	(name-of-your-virtual-environment) $ pip install -r requirements.txt
	``` 
	
## How to run

With your virtual environment enabled
```bash
# Running the application
(name-of-your-virtual-environment) $ python main.py
```

## GUI modification 

**If you choose modify GUI will need generate a Python class and file**

- #### Generating a Python class from the .ui file
	```bash
	# Enter in folder app of project
	$ cd app/
	``` 
	Make sure what the virtual environment this activated.
	```bash
	# Generating a Python class
	(name-of-your-virtual-environment) $ pyside2-uic ./UI/gui.ui > gui.py
	```
	
	**For more informations acess:** [Using .ui Files (QUiLoader and pyside2-uic)](https://doc.qt.io/qtforpython/tutorials/basictutorial/uifiles.html)
  	
- #### Generating a Python file from the .qrc file
	```bash
	# Enter in folder app of project
	$ cd app/
	``` 
	Make sure what the virtual environment this activated.
	```bash
	# Generating a Python file
	(name-of-your-virtual-environment) $ pyside2-rcc ./UI/resources/resources.qrc -o resources_rc.py
	```
	
	**For more informations acess:** [Using .qrc Files (pyside2-rcc)](https://doc.qt.io/qtforpython/tutorials/basictutorial/qrcfiles.html)


<!-- License -->
## License

Released in 2020 :closed_book: License.

Made with :heart: by [Igor Silva](https://github.com/igorsilva3).
This project is under the [MIT license](./LICENSE).

Give a :star: if this project helped you!

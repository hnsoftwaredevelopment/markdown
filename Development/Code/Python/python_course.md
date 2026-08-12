python_course

Managing Python 3thrd party packages with pip

Virtualenv and virtualenvwrapper

pylint (code resharper)

Spphinx code documentation

setiptools create own distribution package



-------------------

Make sure everybody gets the same packages installs as you have:

- [ ]  pip freeze > requirements.txt

Saves you're installed packages, including version to requirements.txt

pip install -r requirements.txt

- [ ]  Installs all packages listed in requirements.txt



# Virtual environments

To create an environment with only those packages installed for that project use Virtualenvironments



pip install virtualenv

create a folder in your python data folder to store the different environments

md .virtualenv

Create a virtual environment for all projects you want to run in a specific environment

virtualenv project1

this will create an environment called project1

To work in this environment please activate it vfirst

project1\scripts\activate.bat

your prompt will change and it shows that you are working in the project1 environment now

Type pip lists

and see this only contains the default packages. Install all packages you need in this environment using pip. You can make use of an requirements file to do this

# Sphinx Documentation tool

Create documentation

Install sphinx with pip

pip install spinx



for documentation create a 'docs'  directory in the project folder

goto that folder and type

sphinx-quickstart

use default answers to most questions. Be sure to use rst format and suse the autodoc functionality (give answer: y)

Change the created index.rst file for the documentation

Works more or less like markup code.



Blank line underneath each chapter.

Codeblocks have a blank line before and after, and the text just before the code block ends with ::

Hyperlinks are written like: ``Link tekst<www.test.com>```

(Only 1 ` at the start and the end of the hyperlink is enough)

Internal reference :ref:'api'

This references to a api.rst file that starts wit the line:

.. _api:



![1549544244007](images/1549544244007.png)

![1549544302612](images/1549544302612.png)



![1549544803886](images/1549544803886.png)





![1549545014813](images/1549545014813.png)



## Code documentation

![1549545076450](images/1549545076450.png)



## Get documentation from the code

Change class in autoclass

![1549545198678](images/1549545198678.png)

![1549549245895](images/1549549245895.png)

![1549549334633](images/1549549334633.png)



![1549549526908](images/1549549526908.png)

Run Make HTML



Sphinx gets documentation from the source code

doumentation code is surroundend wit tripple """

![1549549429757](images/1549549429757.png)



## Create setups and distribution files

![1549549707782](images/1549549707782.png)

![1549549804309](images/1549549804309.png)


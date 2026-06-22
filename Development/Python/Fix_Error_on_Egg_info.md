Fix_Error_on_Egg_info



# Error about Egg_info during installation of packages to Python

Error message:

<span style="color:red">
Command "python setup.py egg_info" failed with error code 1 in C:\Users\HERBER~1.NIJ\AppData\Local\Temp\pip-install-6kv1rj4_\mscxyz</span>

![1550216341128](images/1550216341128.png)

It mentions an encoding error in file **"C:\Program Files (x86)\Python37-32\lib\encodings\cp1252.py"**

Encoding files in Python are saved as **UTF-8-BOM**

Open the specified file in Notepad++ and save it with encoding **UTF-8**

Now its likely that the installation of the package will work

![1550218202864](images/1550218202864.png)

Don't forget to change the encoding of the changed file back to UTF-8-BOM after installation because it is the default encoding for Python
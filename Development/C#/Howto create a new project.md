Howto create a new project

# Howto create a new project

Start in the root folder where you hold your projects for example `C:\data\DevOps`

And create the following folder structure
```CMD
MD <mainprojectname>
CD <mainprojectname>
MD src
MD test
CD src
MD <ProjectName>
CD <ProjectName>
```

Now you can create the basefiles for the new Project
For example when you want to create a console application use:

`dotnet new console`

for other available templates to use on start use:
'dotnet new --help'
Kali Linux On Windows

# Kali Linux On Windows

!! NEEDS Windows 10 version 2004 or higher !!

[Youtube instruction video](https://www.youtube.com/watch?v=AfVH54edAHU&list=WL)

⚙  means Copy past the  nexttekst 

## INSTALL WSL 2

- RUN POWERSHELL as administrator

	⚙️ Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux


- RESTART

	⚙️ dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

	⚙️ dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

- RESTART
- [Download Linux Kernel](https://aka.ms/wsl2kernel)
	- Run the downloaded MSI and install the kernel
 

- RUN POWERSHELL as administrator
	- SET DEFAULT TO WSL 2

		⚙️ wsl --set-default-version 2

	- CHECK VERSION 
 
		⚙️ wsl --list --verbose

## INSTALL GUI
	⚙️ sudo apt update && sudo apt upgrade -y
	⚙️ sudo apt install kali-desktop-xfce -y

- XRDP

	⚙️ sudo apt install xrdp -y

	⚙️ sudo service xrdp start

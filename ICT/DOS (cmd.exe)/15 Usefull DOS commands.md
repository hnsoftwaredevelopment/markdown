```insta-toc
---
title:
  name:
  level:
  center:
exclude:
style:
  listType:
omit:
levels:
  min:
  max:
---

# Inhoudsopgave

- ASSOC
- CIPHER
- Driverquery
- File Compare
- Ipconfig
- Netstat
- PING
- PathPing
- Tracert
- Powercfg
- Shutdown
- Systeminfo
- System File Checker
- Tasklist
- Taskkill
- CMD Commands Recommended by Readers
```

Microsoft has slowly pushed aside CMD commands in the Windows interface. This is not without reason; it is an antiquated and mostly unnecessary tool from an era of text-based input. But many commands remain useful, and Windows 8 and 10 even added new features.

Here we present the essential commands every Windows user needs to know.

## ASSOC
![f7cc6a9706d5dacd6dc2c0bada8567b7.png](attachments/8edd04564be4432abdbf1edadf884480.png)

Most files in Windows are associated with a specific program that is assigned to open the file by default. At times, remembering these associations can become confusing. You can remind yourself by entering the command “assoc” to display a full list of file name extensions and program associations.

You can also extend the command to change file associations. For example, “assoc .txt=” will change the file association for text files to whatever program you enter after the equal sign. The “Assoc” command itself will reveal both the extension names and program names, which will help you properly use this command. You can probably do this more easily in the GUI, but the command line interface is a perfectly functional alternative.

## CIPHER
![dd08027113a2fa1a9d7f812fd7a6b5b9.png](attachments/554df3b48b07432f970411523ab0b741.png)
Deleting files on a mechanical hard drive doesn’t really delete them at all. Instead, it marks the files as no longer accessible and the space they took up as free. The files remain recoverable until the system overwrites them with new data, which can take some time.

The cipher command, however, wipes a directory by writing random data to it. To wipe your C drive, for example, you’d use the command “cipher /w:c”, which will wipe free space on the drive. The command does not overwrite undeleted data, so you will not wipe out files you need by running this command.

You can use a host of other cipher commands, however, they are generally redundant with BitLocker enabled versions of Windows.

## Driverquery
![70575e5ad864ec0488d499af7e941980.png](attachments/f74e52817af5400bbfa462a31cab5f05.png)
Drivers remain among the most important software installed on a PC. Improperly configured or missing drivers can cause all sorts of trouble, so its good to have access to a list of what’s on your PC. That’s exactly what the “driverquery” command does. You can extend it to “driverquery -v” to obtain more information, including the directory in which the driver is installed.

## File Compare
![b2c96fd6473dc826a26f3252ad14ba91.png](attachments/5220f5de85b54f6d8dbe726f704913ec.png)
You can use this command to identify differences in text between two files. It’s particularly useful for writers and programmers trying to find small changes between two versions of a file. Simply type “fc” and then the directory path and file name of the two files you want to compare.

You can also extend the command in several ways. Typing “/b” compares only binary output, “/c” disregards the case of text in the comparison, and “/l” only compares ASCII text.

So, for example, you could use the following:

```fc /l "C:\Program Files (x86)\example1.doc" "C:\Program Files (x86)\example2.doc"```

The above command compares ASCII text in two word documents.

## Ipconfig
![3f3dfe46848f83300d86c8187e1f0a34.png](attachments/23d2945ae1334ce9b2b5b2c69bf37480.png)
This command relays the IP address that your computer is currently using. However, if you’re behind a router (like most computers today), you’ll instead receive the local network address of the router.

Still, ipconfig is useful because of its extensions. “ipconfig /release” followed by “ipconfig /renew” can force your Windows PC into asking for a new IP address, which is useful if your computer claims one isn’t available. You can also use “ipconfig /flushdns” to refresh your DNS address. These commands are great if the Windows network troubleshooter chokes, which does happen on occasion.

## Netstat
![808060e2a0fa94ef38fed91bd3841b72.png](attachments/12027b6ad6ca47a4946351e865f51899.png)
Entering the command “netstat -an” will provide you with a list of currently open ports and related IP addresses. This command will also tell you what state the port is in – listening, established or closed.

This is a great command for when you’re trying to troubleshoot devices connected to your PC or when you fear a Trojan infected your system and you’re trying to locate a malicious connection.

## PING
![009b3ac3d8119c5e368e5ac364f195f6.png](attachments/58a1fc694762471d8e9f87fc14f94ac7.png)
Sometimes, you need to know whether or not packets are making it to a specific networked device. That’s where ping comes in handy.

Typing “ping” followed by an IP address or web domain will send a series of test packets to the specified address. If they arrive and are returned, you know the device is capable of communicating with your PC; if it fails, you know that there’s something blocking communication between the device and your computer. This can help you decide if the root of the issue is an improper configuration or a failure of network hardware.

## PathPing
![7f2e0eed3b0bd061d32bc6246ec06a0c.png](attachments/40719ab1d0d441918fd953dbd2b24884.png)
This is a more advanced version of ping that’s useful if there are multiple routers between your PC and the device you’re testing. Like ping, you use this command by typing “pathping” followed by the IP address, but unlike ping, pathping also relays some information about the route the test packets take.

## Tracert
![b4121a9f3702317019fb25cceafec55f.png](attachments/3fbcfcca405d4f2ba93fd54fffda73a0.png)
The “tracert” command is similar to pathping. Once again, type “tracert” followed by the IP address or domain you’d like to trace. You’ll receive information about each step in the route between your PC and the target. Unlike pathping, however, tracert also tracks how much time (in milliseconds) each hop between servers or devices takes.

## Powercfg
![6a613df423b98e73ae17cf0d79b438c1.png](attachments/909b64d215e347f8988e0203c1326798.png)
Powercfg is a very powerful command for managing and tracking how your computer uses energy. You can use the command “powercfg hibernate on” and “powercfg hibernate off” to manage hibernation, and you can also use the command “powercfg /a” to view the power-saving states currently available on your PC.

Another useful command is “powercfg /devicequery s1_supported”, which displays a list of devices on your computer that support connected standby. When enabled, you can use these devices to bring your computer out of standby — even remotely. You can enable this by selecting the device in Device Manager, opening its properties, going to the Power Management tab and then checking the Allow this device to wake the computer box.

“Powercfg /lastwake” will show you what device last woke your PC from a sleep state. You can use this command to troubleshoot your PC if it seems to wake from sleep at random.
![30fec3d729b6289387f0ffabe5c313a1.png](attachments/8c750a154e3449c29485f2336b8a9c46.png)
You can use the “powercfg /energy” command to build a detailed power consumption report for your PC. The report saves to the directory indicated after the command finishes. This report will let you know of any system faults that might increase power consumption, like devices blocking certain sleep modes, or poorly configured to respond to your power management settings.

Windows 8 added “powercfg /batteryreport”, which provides a detailed analysis of battery use, if applicable. Normally output to your Windows user directory, the report provides details about the time and length of charge and discharge cycles, lifetime average battery life, and estimated battery capacity.

## Shutdown
![49f45413ab5008fdde6c15291f2ded6a.png](attachments/c0d960ab646e40df956119d936b8e70b.png)
Windows 8 introduced the shutdown command that—you guessed it!—shuts down your computer.

This is, of course, redundant with the already easily accessed shutdown button, but what’s not redundant is the “shutdown /r /o” command, which restarts your PC and launches the Advanced Start Options menu, which is where you can access Safe Mode and Windows recovery utilities. This is useful if you want to restart your computer for troubleshooting purposes.

## Systeminfo
![db7b7e1505a686e90b3f7d29a21eb1cf.png](attachments/5c610189f60b4ee184b616e54d895e71.png)
This command will give you a detailed configuration overview of your computer. The list covers your operating system and hardware. For example, you can look up the original Windows installation date, the last boot time, your BIOS version, total and available memory, installed hotfixes, network card configurations, and more.

Use “systeminfo /s” followed by the host name of a computer on your local network, to remotely grab the information for that system. This may require additional syntax elements for the domain, user name, and password, like this: “systeminfo /s [host_name] /u [domain]\[user_name] /p [user_password]”

## System File Checker
![660809cf69e694c4c6defe7c96836551.png](attachments/ba7a78fffda1464284e6be0cc159d465.png)
System File Checker is an automatic scan and repair tool that focuses on Windows system files.

You will need to run the command prompt with administrator privileges and enter the command “sfc /scannow”. If SFC finds any corrupt or missing files, it will automatically replace them using cached copies kept by Windows for this purpose alone. The command can require a half-hour to run on older notebooks.

## Tasklist
![b29c1ae318ea3c5604e36c0b0b67c832.png](attachments/75d4533f9fca4cb58bf451bb32ca2706.png)
You can use the “tasklist” command to provide a current list of all tasks running on your PC. Though somewhat redundant with Task Manager, the command may sometimes find tasks hidden from view in that utility.

There’s also a wide range of modifiers. “Tasklist -svc” shows services related to each task, use “tasklist -v” to obtain more detail on each task, and “tasklist -m” will locate .dll files associated with active tasks. These commands are useful for advanced troubleshooting.

## Taskkill
![db50517cfbf00aa4e76878e3e7e88dd6.png](attachments/3cbcdc2603454e4b8296d49c101afeaf.png)
Tasks that appear in the “tasklist” command will have an executable and process ID (a four- or five-digit number) associated with them. You can force stop a program using “taskkill -im” followed by the executable’s name, or “taskkill -pid” followed by the process ID. Again, this is a bit redundant with Task Manager, but you can use it to kill otherwise unresponsive or hidden programs.

# CMD Commands Recommended by Readers
These are the commands our readers use regularly:
- nbstat: “For looking up names of computers on your network.”
- netstat -ano | find “est”: “To get a list of processes with established CP connections.”
- tasklist | find “[process id]”: “To get the name of the executable associated with the particular process id that I’m interested in.”
- cacls: This command is “most handy to manually access hidden files and folder. (A41202813)
- net use: “To map drives of networked CNC machines.”
- chkdsk /f C: “Checks your C: partition hard disk for errors and fixes bad sectors.”
- Schtasks: To schedule tasks.

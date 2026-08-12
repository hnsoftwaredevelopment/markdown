# VACAM upgrade procedure



# Introduction

This page and its child pages describes all manual steps necessary to upgrade VACAM to a higher version.

Upgrading within a VACAM branches is not in scope of this page and typically does not require manual steps.

Details of individual upgrade procedures are describe on child/linked pages of this page.

If manual steps are required due to new development in VACAM for the next branch, then the manual steps be documented on this page.

Please be aware that some changes needs to be executed by the Commissioning engineer onsite. Please add description to this page : Commissioning engineer manual \[Document\]. This document will be exported and given as an attachment to the Commissioning engineer.

When a new version of VACAM is released these upgrade procedures must be exported to PDF and stored as a copy along side the VACAM Setups: \\\\vasoftware\\setups\\VACAM\\UpgradeProcedures

Up**dates** are within a branch, for example 4.8.**100** to 4.8.**150**  
Up**grades** go from one branch to another one for example 4.**8**.321 to 4.**11**.26

Our goal is to keep updating as smooth as possible, user should be warned if a manual action is required (for instance with a configuration error) and everything should be scripted and automated as much as possible.

Upgrades are known to contain (major) refactoring causing breaking changes. Our goal is to document them in this page so the upgrade can still be performed with some manual changes.


## In our pursuit of a fully automatic update process, we no longer want manual steps. All necessary changes will have to be automated.  
In case of any questions please contact SWMS team.

# Upgrading to VACAM 4.31 or higher

- For a right to left machines with web support validate that cylinder 1 is operating the left cylinder (outfeed side). For details see: [#18929](https://github.com/voortman-steel-machinery/vacam-twincat/pull/18929).

# Upgrading to VACAM 4.21 or higher

- .NET 8 x86 runtime is needed by the installer. It can be downloaded here: <https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-desktop-8.0.11-windows-x86-installer>  

# Upgrading to VACAM 4.20 or higher

- On a Fabricator install [https://aka.ms/vs/17/release/vc\_redist.x64.exe](https://aka.ms/vs/17/release/vc_redist.x64.exe) (should be included in image of PC). Symptom if this is not done is that VACAM will not be able to generate a cycle list because it cannot generate a rotator setup.

# Upgrading to VACAM 4.19 or higher

- **\[VSB/VP\] **The following properties are moved (and merged) from the Shotblaster and Painting machine object to the GlobalSettings:   
Because these settings move from the machine config database to the VACAM database it is unfortunately not possible to script this. So these values need to be moved by hand if they were used.  

| **VSB / VP (MC-config)** | **GlobalSettings (VACAM)** | **Note** |
| --- | --- | --- |
| UseBlastFieldOfProduct | SurfaceTreatmentSource | These booleans are now merged as an option in the SurfaceTreatmentSource “Use Product Field” |
| UsePaintFieldOfProduct |  |  |
| UseINBlockForBlastField | SurfaceTreatmentSource | These booleans are now merged as an option in the SurfaceTreatmentSource “Use IN block of product” |
| UseINBlockForPaintField |  |  |
| INBlockBlastKey | INBlockBlastKey |  |
| INBlockBlastValue | INBlockBlastValue |  |
| INBlockPaintKey | INBlockPaintKey |  |
| INBlockPaintValue | INBlockPaintValue |  |

Surface treatment options (VACAM 4.19 and up) (aka Shot blasting and painting option)  describes were to find the settings.

- **\[General\]** VACAM 4.19 is based on the .NET8 framework of Microsoft. In order to run it, the .NET runtimes need to be installed on the machine. The installers for the runtimes can be found here: \\\\vasoftware\\Setups\\DotNet Installers . When installing VACAM, there will be a check whether the runtimes are installed. If not, you will be prompted to do it. Besides the .NET runtimes there is also a new installer for CameraRtspPlayer. In case the machine has such a camera, the old software needs to be uninstalled. The new installer is also available in \\\\vasoftware\\Setups\\DotNet Installers. This installer need to be executed AFTER the installation of VACAM.

# Upgrading to VACAM 4.18.0 or higher

- **\[Fabricator\]** Reduce rising edge time of pressure switch on hydraulic generators to 100ms.

# Upgrading to VACAM 4.16.0 or higher

- **\[General\]** From VACAMOfficeStarter use at least version 1.1.3.
    - See [\[SWMS-4218\] Investigate whether machine edition can be used instead of machineversion=true/false - JIRA (atlassian.net)](https://voortmanjira.atlassian.net/browse/SWMS-4218)
- ***\[Fabricator\]*** Max voltage may have to be increased. See: 
- ***\[Fabricator/V808\]*** Panasonic DTPS is x64 only. Requires DTPS version 4.06.04 (64 bit) or higher, installer here: \\\\vasoftware\\setups\\valkwelding\\2023-11-29 DTPS 4.06.04 64 Bits official (VACAM 4.16+). Not tested with V808, if a V808 is upgraded beyond 4.11 we might need additional testing to guarantee it’s functioning. V807’s are not affected.

# Upgrading to VACAM 4.15.0 or higher

- Make sure this dtps version is installed: \\\\vasoftware\\setups\\valkwelding\\2023-07-24 DTPS 4.06.03 64 Bits official (VACAM 4.15+) and the dll is replaced (see readme.txt). First uninstall the existing PC tool. Do not change any option during install, just hit next… next…

# Upgrading to VACAM 4.13.5 or higher

- ***\[V325\] ***Change the configuration for the handling of the manual flame ignition buttons
    - See Configuration change: Flame ignition
- ***\[Fabricator\]*** Max voltage may have to be increased. See: 

# Upgrading to VACAM 4.13.3.0 or higher

- ***\[Rotating chuck\]*** 24V signals from chuck have to be linkend/configurad.
    - see 24 Signals <https://voortman.atlassian.net/wiki/spaces/TC/pages/3626762343/How+to+add+Rotating+Chuck+Configuration+manual#24V-signals> 
- ***\[V303/V304/V310(MK2)/V320/V325\]  *****OPTIONALLY*****; ***Change reference of fuel-gas on oxy-unit.
    - see [https://voortmansteelgroup.sharepoint.com/:w:/r/sites/KnowledgeBase/\_layouts/15/Doc.aspx?sourcedoc=%7B6F91996F-9890-46AE-BAA7-DAAB0209316C%7D&file=WI-SW-56102.docx&action=default&mobileredirect=true](https://voortmansteelgroup.sharepoint.com/:w:/r/sites/KnowledgeBase/_layouts/15/Doc.aspx?sourcedoc=%7B6F91996F-9890-46AE-BAA7-DAAB0209316C%7D&file=WI-SW-56102.docx&action=default&mobileredirect=true) 

# Upgrading to VACAM 4.13.2.0 or higher

- **\[General\]** Reload tmc file
- ***\[Plate Machines\]*** Panel upgrade required: <https://voortman.atlassian.net/wiki/spaces/TC/pages/3657269249/MachineControlPanel+ConfigurationManual>  
    - ***\[V325\] **Refer the service request buttons to the machinezone*
- ***\[V310Mk2\] ***Set machine object type to “V310MK2“ within properties.

- Within Vacam version below 4.12 there is no difference between machine type. (V310MK2 is recognized by spindle type.)

- ***\[V310Mk2\] ***Refer the 'Walk-in overwrite safetygroup' on the cuttingunit: <https://voortman.atlassian.net/wiki/spaces/TC/pages/3069542441/Shut+down+oxy-valve+on+interruption+light+curtain.#Link-%27Walk-in-overwrite-safetygroup%27-on-the-cuttingunit.> 
- ***\[V303/V310Mk2\] ***When a BeamTubeRotator is sold How to add : Rotating Chuck Configuration manual
- ***\[Hybrid Milling\] When installing the module, make sure *****that there are no DLL’s in the x86 folder installed. If so, copy them manully to the vacam-folder to have the milling-module work.**

# Upgrading to VACAM 4.12 or higher

- **\[General\]** Reload tmc file 
- **\[General for anything with IM\]** Increase load buffer size to 512 kByte of interpolationmanager: 
- IM\_Extra

# Upgrading to Vacam 4.11.27 or higher

- **\[V633T\] **when seeing the following error the following step should be done

  The X-axis of the feedertruck need a reference to the Hydraulic brake of the Clamp roll unit (see image)  

# Upgrading to VACAM 4.11.15 or higher

- **\[V807 module\]** If a customer already had Vacam 4.11, then their right to the Cambered castellation wizard will remain. Therefore, please check if they are allowed to have the wizard and the harmonic movements. If yes, then you can check the “Cambered castellation” box in modules. See: . Currently only applies to customer Mouw.

# Upgrading to VACAM 4.11.14 or higher 

- **\[ABB Remote Control\]**  From this version systems with a ABB Remote control need to switch on/off the remote control on the remote itself. Button D3\_1 is used for that, and therefore it is not allowed to have commands to be programmed under that button.  Switch on/off remote control ABB type \>4.11

# Upgrading to VACAM 4.11.13 or higher 

- **\[BufferLinkPreferences\] **Validate buffer link preferences. The buffer link preferences AccordingToBufferItemRouting(5), AccordingToProductRouting(26) and ContainsProductRouting(27) are removed. New preference named 'ContainsPreferableOutfeedSection (42)' is created to be able to configure preferences for preferred outfeed sections. F106 Directing parts to a specific outfeed section

# Upgrading to VACAM 4.11.8 or higher

- ***\[DrillV2\]*** Fill in the *Spindle position during tool change* parameter on the toolchanger. The correct value can be found on the S-axis, copy the *Reference position*.

# Upgrading to VACAM 4.11 or higher

- **\[General\]** When there are custom pictures made for the system, copy them from C:\\Program Files (x86)\\Voortman\\Vacam\\Pictures to C:\\Program Files\\Voortman\\Vacam\\Pictures
    - Same for the system.security.dll. 
- **\[General\]** Validate the allowed profiles for the drill unit. (Settings-\>Options-\>Permit profiles) (the DrillUnitV2 is now also checking the allowed profiles table whether the profile is allowed for the drill unit).  
- ***\[V807\]*** All batches should to be reset when a V807 is in a split line. (When the batch was made with a (very) old version of 4.8 the ordering of the copes will be incorrect)
- ***\[VSB, VP, VSB-VP\]***  (E1-1008-VSB1500) Digital input ‘Material detection’ of outfeed must be defined as type photocell with X-offset according to the position of the sensor.
- ***\[VB\] from 4.11.8 ***Added script to set Z-offset material detection to 10mm if it is still on 0mm.
- ***\[Safety\] ***Check distance to roller conveyor
- **\[V630,V613\] **Check that the correct reference is assigned to *Sensor System Pressure Present* (Air Pressure DI) for all Toolchangers.

  

# Upgrading to VACAM 4.10 or higher

- ***\[General\]\[Commissioning\]*** Update TwinCAT to version 4024.11
    - Run `Updated BSOD TC fix.bat`  (bcdedit /set UseLegacyApicMode false)


- **\[General\]** Reload tmc file 
    - Relink interpolation manager for all machines, <https://voortman.atlassian.net/wiki/spaces/TC/pages/2198339619/IM+Change+PLC+link+to+interpolation+channel> (only applies when the machine uses an interpolation manager, does not apply to stand alone saw, shotblaster or V807 for instance).
    - ***\[V631M\] ***Ignore not restored link 'MachineObjectsArray.MotorDrive\[x\].Safety.SMM\_Profile'. Variable is not used from 4.8. 
- ***\[General\] \[Rename\]***PLC project. Name should be “MachineControl\_PLC”
- ***\[V302, V304, V310\]*** Add MainTaskFast to configuration. Configuration change for using scope with error 'Attempted to devide by zero'.   
Perform : Step 3a - Reload TMC File.
- ***\[V807\] ***When updating delete all applications from the controller (empty out ftp://\<robotip\>/usr/usrapp) and deploy again from VACAM using manual=\>robot=\>controller deployment=\>deploy.
- ***~~\[V807\] ~~***~~When updating we require a new (Robot) CPU to be installed, first \~30 machines did have an old CPU, we can check that from a backup. ~~All machines have been retrofitted.
- ***\[V630/V631\]***All drill machines will have to use rolling taps from this version or higher. Default parameters will be updated according to this document: F80 Roll-tapping
- ***\[V302/V304/V310\]*** For machines with the old panel the ButtonTop1 must be assigned manually to the ControlLaserPointer button of the transport manager as explained <https://voortman.atlassian.net/wiki/spaces/TC/pages/2997092420/Carriage+pLaserpointer#Vacam-4.10>.
- ***\[V303/V310MK2\]*** In case of an Plate machine with oxyfuel torch, a new output ‘Reset Capacitive Sensor’ has to be added with an falling edge of 500ms. Teach In VHC : Reset capacitive sensor

Reset Capacitive sensor is only applicable on the GCE torch. <https://voortman.atlassian.net/wiki/spaces/PTD/pages/2295660592/V303+-+Cutzone+Oxy-fuel#GCE-Torch> 

- ***\[V325\]*** When updating add a transportgroup to the transportmanager. This is needed for the motion control on the X-axis. DualSideGripper steering: MoveAbsoluteX
- ***\[V325\]\[Commissioning\]*** Please update kinematic transformation software. See : Driver files
- ***\[V310\] ***Set torque difference for V310\_V1 (2x 6%)  
<https://voortman.atlassian.net/wiki/spaces/TC/pages/3306881025/DR2+CalculateTorqueMatDetection> 
- ***\[V302/V303/V304/V310\]*** The breakaway functionality has changed within 4.10. The plasma collision sensors should NOT be inverted. For more information see : <https://voortman.atlassian.net/wiki/spaces/TC/pages/3697213541/ClearanceControl+I+BreakawayHandling> . The feedback in vacam will be matching the actual sensor.
- ***\[V320\]***split up BreakAwaySensor to multi input. <https://voortman.atlassian.net/wiki/spaces/TC/pages/3696501849/FB+MovementEnabled+-+One+breakaway+sensor+and+one+movement+enabled+sensor#Configuration-manual> 
- ***\[V325\] ***add a delay filter of 20ms on the readings of the side grippers sensors <https://voortman.atlassian.net/wiki/spaces/TC/pages/3792699409/Dual+side+gripper+configuration#Side-gripper-sensors>.
- ***\[V310\] ***when a Auxiliray tool is sold Auxiliary20pos: How to add - Configuration manual

## Upgrading to VACAM 4.9 or higher

- In case of an Kjellberg powersource, the eprom should be at least V1.29 because of error 0x003c (see [https://voortman.atlassian.net/wiki/spaces/\~81636524/pages/3477700641/Error+situations#0x003C---PowerSourceErrorDescriptions](https://voortman.atlassian.net/wiki/spaces/~81636524/pages/3477700641/Error+situations#0x003C---PowerSourceErrorDescriptions)  )
- ***\[V302/V303/V304/V310\] ***Add buffers to the production screen. (see <https://voortman.atlassian.net/wiki/spaces/PTD/pages/1627324438/PLTS-10+Plate+machine+buffer+feature#User-settings> )

## Rollback from VACAM 4.8.406 to an older version

Doing a rollback from VACAM 4.8.406 (or up) to an older version (older/lower than 4.8.406), you need to cleanup all Lock and UnLock tables in the VACAM database. You can use the script below:

delete from BatchLock

delete from BatchUnLock

delete from BeamAssemblyLock

delete from BeamAssemblyUnLock

delete from BufferItemLock

delete from BufferItemUnLock

delete from BufferLock

delete from BufferUnLock

delete from PieceOperationLock

delete from PieceOperationUnLock

delete from ProductLock

delete from ProductUnLock

delete from ProfileLock

delete from ProfileUnLock

delete from ToolLock

delete from ToolUnLock

delete from UnloadZoneLock

delete from UnloadZoneUnLock

## Updating to VACAM 4.8.405 or higher

- When using Tekla EPM integration:
    - Use connection port 9154 (instead of 3306)
    - Password may not be blank anymore 
    - other permissions: see attachment: 


## Updating to VACAM 4.8.403 or higher

- ***\[General\]*** \[E10-34-HydraulicGeneratorSaw\] Analog output type ‘non linear’ need correct values of the properties x% value (10-90). 10% \> ‘Minimum value’, 90% \< 'Maximum value'. Between 10% and 90% the values should increase. 
- ***\[VB1x50b\] ***Change type input of material detection to type ‘Reset’

## Updating to VACAM 4.8.223 or higher

- ***\[V807\] ***The prototype laser shielding for front measurement installed, it’s behavior will be inverted. This only concerns very few machines (2-3).


## Updating to VACAM 4.8.215 or higher

- ***\[V807\] ***Check if the popup conveyor is referenced:


## Updating to VACAM 4.8.125 or higher

- ***\[V630/V631\] ***Reevaluate infeed/outfeed roller offsets. First and last roll definitions  & Conveyor: fOffsetFirstRoller / fOffsetLastRoller definition offsets

## Updating to VACAM 4.8.66 or higher

- ***\[General\]*** Add MainTaskFast to configuration. Configuration change for using scope with error 'Attempted to devide by zero'.   
Perform : Step 3a - Reload TMC File.
- ***\[VB750/VB600\]*** This saw types never delivered with 4.8 and since they are skipped from product portfolio not supported in this version.

# Upgrading to VACAM 4.6 or higher

- ***\[General\]*** Typically replace IPC
- ***\[General\]*** Install 64-bit version windows of windows and install TwinCAT 3
- ***\[General\]*** Update TwinCAT system configuration to TwinCAT 3.   
See HowTo: Migrate TwinCAT 2 I/O Config to TwinCAT 3 \[Document\]
- ***\[General\]*** Create and link TwinCAT 3 safety project
- ***\[Feedertruck V1\] ***(E12-58-FeederTruck Digital input configuration error) . Digital inputs referred as ‘Infeed crash protection x’ should set with type ‘Photocell’ and have a valid X-offset.
- **\[V808\]** update cut charts and re-create tools: Steps required for upgrade

# Upgrading to VACAM 4.2 or higher

- ***\[G0 machines\]*** In case you machine use G-code, the G0 code is from now on used. 
    - See Step 3h - G0 adjustment  to adjust the parameters. 
    - See Step 3g - Update ITP M-Functions  to add M60

# Updating to VACAM 2.32.756 or higher

- Replication is not longer supported anymore. Before(!!) update you need to setup CDS as alternative for Replication, using <https://voortmansteelgroup.sharepoint.com/:w:/s/KnowledgeBase/ERGPyTNEdAVHovtvenBhp6sBmxIedPpuoCkxrguZGcXT-A?e=c95c1R> .

# Updating to VACAM 2.32.633 or higher

- **\[VSB\]** Motor drive running check is changed for M300 drive. It now compares the actual velocity with the target velocity. In case the target velocity property is not set right (to high) the drive will never reach this target speed and drive never return the running state. Shotblaster will not start up. Set ‘Max. speed’ property of ‘Drive Elevator’ to 1500. 

# Upgrading to VACAM 2.32 or higher

- Install two saw band pressure sensors on the sawing machines (Mechanical en electrical), connected to one analog PLC input. Step 5b - Saw configuration
- In case of a V808 (type 1) follow this procedure in consult with Robotics team: [https://voortmansteelgroup.sharepoint.com/:w:/r/sites/KnowledgeBase/\_layouts/15/Doc.aspx?sourcedoc=%7BDDAC7AC3-E0B8-48AF-B6C6-91EAD0A97035%7D&file=upgrade%20a%20V808%20type%201%20from%202.24%20to%202.32.docx&action=default&mobileredirect=true&cid=38c45da4-5e88-4bb3-94e1-cad1dcfebaac](https://voortmansteelgroup.sharepoint.com/:w:/r/sites/KnowledgeBase/_layouts/15/Doc.aspx?sourcedoc=%7BDDAC7AC3-E0B8-48AF-B6C6-91EAD0A97035%7D&file=upgrade%20a%20V808%20type%201%20from%202.24%20to%202.32.docx&action=default&mobileredirect=true&cid=38c45da4-5e88-4bb3-94e1-cad1dcfebaac) 
- The experience of projects is that the upgrade from 2.22 to a version up (like 4.8) is not going well. suggestion is to upgrade first to f.e. 2.32 and then from that version going up to f.e. 4.8. The issues mentioned where in TwinCAT to change the unrestored links.
- **\[VB1050\]** In case of a saw with Bosch servo drive for saw band control the max. acceleration, deceleration and jerk (95.75, 95.75 and 873.3) 
- ***\[General\]*** Validate configuration transverse transport hydraulic lifters. Compact unit machine object is needed under LifterCylinder

# Upgrading to VACAM 2.2 or higher

- Upgrade to SQL Server 2008

# Upgrading to VACAM 2.0 or higher

- Upgrade to SQL server 2005 (not needed when upgrading to 2.2 or higher)
- Create a buffer configuration
- Configure allowed profiles
- Fill/check the machine table in the VACAM database

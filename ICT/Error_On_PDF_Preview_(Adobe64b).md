Error_On_PDF_Preview_(Adobe64b)

## Fixes for 64-bit Adobe Reader preview handler and thumbnails

**December 2014:** A new, improved version is coming soon!

[Update 02/May/2011: New version of the thumbnail fix which hopefully fixes PDF thumbnails appearing for the wrong files. Note the instructions about clearing your thumbnail cache.]
[Update 10/Feb/2011: Just a note to say that, yes, the fix works with Adobe Reader X.]
[Update 02/May/2010: Added a note that the preview handler fix may still need to be run once, even after installing Adobe Reader 9.3.2, on machines which were upgraded from Vista to Windows 7. Thanks to Jonathan Van Dusen for the heads up.]
[Update 28/Apr/2010: Page and tools updated for Adobe Reader 9.3.2 and Office 2010 RTM. Summary here. Thanks to Alex Bantzhaff!]
[Update 06/Feb/2010: Thumbnails fix updated: Workaround for black thumbnails caused by bug in Windows shell.]
[Update 04/Feb/2010: Thumbnails fix added.]
[Update 25/Jan/2010: Fix for preview handler in 64-bit Office 2010. Thanks to Winfried Pohl!]
[Update 15/Dec/2009: Added automated fix tool.]
[Update 15/Sep/2009: Added extra info that helps in some scenarios.]
[Update 11/Sep/2009: Added another rendering bug in the preview handler to the Hey, Adobe... list.]

## Contents:

- Introduction
  - [Preview Handler](https://www.pretentiousname.com/adobe_pdf_x64_fix/#prevu)
  - [Thumbnails](https://www.pretentiousname.com/adobe_pdf_x64_fix/#thumb)
- [**Download the fixes**](https://www.pretentiousname.com/adobe_pdf_x64_fix/#downl)
- [Donate](https://www.pretentiousname.com/adobe_pdf_x64_fix/#donat)
- [Detail on the preview handler fix tool](https://www.pretentiousname.com/adobe_pdf_x64_fix/#fixer)
- [Fixing the preview handler by hand or group policy](https://www.pretentiousname.com/adobe_pdf_x64_fix/#handy)
- [Detail on the thumbnail fix](https://www.pretentiousname.com/adobe_pdf_x64_fix/#thfix)
- [Hey, Adobe...](https://www.pretentiousname.com/adobe_pdf_x64_fix/#adobe)
- [Rant](https://www.pretentiousname.com/adobe_pdf_x64_fix/#ffuuu)
- [Thank you](https://www.pretentiousname.com/adobe_pdf_x64_fix/#thank)

## Introduction:

This page contains simple fixes for Adobe's PDF preview handler and thumbnails on 64-bit versions of Windows.

Before I looked into this, people had been [complaining about it for over two years](http://forums.adobe.com/thread/303008) with no official response.

**Only the thumbnails fix is still needed, except if you upgraded from Vista to Windows 7, where both fixes may still be needed.** Half a year after I published the information, Adobe finally incorporated the preview handler fix (but no thumbnails fix, and they leave the preview handler broken if you upgraded from Vista to Windows 7) into the installer for Adobe Reader 9.3.2 (April 2010).

Maybe in 2011 Adobe will manage to fix the thumbnails as well; until then you can get my fix for them below. :-)

### Preview Handler

Preview handlers are lightweight components which let you view various file types within programs like Windows Explorer (in Windows Vista and Windows 7), Outlook 2007/2010 and [Directory Opus](https://www.pretentiousname.com/opus/index.html) (via [my bundled plugin](https://www.pretentiousname.com/activex/index.html)).

Adobe Reader comes with Adobe's PDF preview handler but the installer had a mistake which meant the preview handler did not work on 64-bit systems.

It turned out the problem could be fixed via a simple registry change. The change is described below and a small program which performs the fix is also provided for your convenience.

Unlike the thumbnail fix, described below, the preview handler fix should no longer be needed by *most* people, since Adobe have finally fixed their installer, but it's still provided in case it helps repair things. **If you had Adobe Reader installed under Vista and later upgraded to Windows 7 then you will probably still need to run the preview handler fix once** to clean up a registry value which Adobe set inconsistently between the two OS versions. **If in doubt, run the fix** and it will tell you if anything needs to be done. If everything is good already then the preview handler fix won't change anything.

[![Adobe PDF preview handler working on a 64-bit system](images/adobe_pdf_x64_fix_example_small.png)](https://www.pretentiousname.com/adobe_pdf_x64_fix/adobe_pdf_x64_fix_example_large.png)

### Thumbnails

Adobe Reader's ability to generate thumbnails for Windows Explorer, File->Open/Save dialogs, etc. is still broken, out of the box, on 64-bit systems. This is because Adobe still haven't produced a 64-bit version of their thumbnail generator (or much else, to be honest).

Fixing the thumbnail problem was more complicated than the preview handler one, but fixes for both can now be found below.

While fixing the thumbnails I took the opportunity to improve the way they look. The white border around each thumbnail is now removed.

[![Adobe PDF thumbnails and preview handler working on a 64-bit system](images/adobe_pdf_thumbnails_fix_small.png)](https://www.pretentiousname.com/adobe_pdf_x64_fix/adobe_pdf_thumbnails_fix_large.png)

## Download the fixes:

**December 2014:** A new, improved version is coming soon!

- **With installer: Adobe_Reader_x64_fixes_v3_001_installer.zip** (1MB)
- **Without installer: Adobe_Reader_x64_fixes_v3_001_noinstaller.zip** (1MB)

The installer and executables are digitally signed. Thanks to GPSoftware for signing them for me.

An uninstaller is provided.

**Note about jumbled-up PDF thumbnails:** Some people PDF thumbnails appearing above the wrong files. As far as I can tell, it was yet another error on Adobe's part. Hopefully the latest version fixes this, although I only got one confirmation so far. *Note that you will need to clear your thumbnail cache: Run **Disk Cleanup** from the start menu, select C:, put a tick in the Thumbnails checkbox and then click OK.*

## Donate:

A few people have asked to be able to donate money to say thanks for the fixes. You don't have to but if you send money to **jpotter@lss.com.au** via [PayPal](https://www.paypal.com/) and **make a note that it's for the PDF fix**, it'll get to me. That isn't actually my account (this is the first time I've needed one since I closed mine a while ago) but it belongs to a friend who will pass on the money provided the note makes it clear who it's for. :-)

| US $5 |      | US $10 |      | US $20 |      | This one's for Adobe :-) US $10,000                         |
| ----- | ---- | ------ | ---- | ------ | ---- | ----------------------------------------------------------- |
|       |      |        |      |        |      | ![It's not really clickable. :-)](images/btn_donate_LG.gif) |

## Detail on the preview handler fix tool:

For the preview handler problem, I wrote a program to automate the required registry changes. You just run the tool and click Apply Fix. The tool takes of all the details (e.g. differences between Windows 7 clean vs upgrade installs).

This program was written in my spare time and is given away for free. I wrote it due to the popularity of the fix, to help non-technical people, and to celebrate Adobe ignoring the problem for another three months even though the solution was given to them on a plate. I hope this helps more people.

Details of the registry fix are still provided below, for those who wish to make the changes by hand, but using the program is recommended for most people, especially less technical people.

![Adobe Reader preview handler x64 fixer screenshot](images/Reader_x64_fixer3.png)

The preview handler fix tool:

- Tells you if anything needs fixing and offers to fix things if so.
- Understands differences between XP, Vista, Windows 7 and upgrade installs.
- Requests elevation via UAC.
- Checks that you're using 64-bit Windows.
- Checks that Adobe Reader is installed.
- Checks that Adobe Reader's preview handler is associated with PDF files. (If not you'll be asked if you want to associate it. This does *not* affect what happens when you double-click PDF files; use the Open-With menu for that.)
- Checks that Adobe Reader's preview handler is registered under both the 32-bit and 64-bit registry (the latter is required for it to work under 64-bit Office 2010 beta but not the retail version of Office 2010).
- Allows you to undo the fix. (Only the fix itself. If you changed the association and want to go back then you'll usually have to reinstall or repair-install your alternative viewer.)
- Does not need to be installed or uninstalled and, other than the fix itself, leaves nothing behind.
- Is digitally signed so you can detect if it has been tampered with. (Thanks to GPSoftware for signing the exe for me.)

Additional notes on the preview handler fix tool:

- **The preview handler fix should no longer be required for Adobe Reader 9.3.2 and above except if you had previously installed Adobe Reader on Windows Vista and then upgraded to Windows 7.** If you fall into the latter group then you will still need to run the preview handler fix once to clean-up some mess that Adobe's installer leaves behind.

  Note that, at the time of writing, Adobe's website only lets you download Adobe Reader 9.3.0 and you must run its update checker after installing it in order to get the latest version with the x64 fix. Adobe are usually too lazy/incompetent/negligent to copy the latest installer to their website even though older versions of Adobe Reader tend to have serious security flaws which are often being exploited in the wild and even though making people update right after installing often causes an unnecessary reboot. Sigh.

- With earlier versions of Adobe Reader, you may need to re-apply the fix if you update or re-install Adobe Reader.

- **The fix is only needed on 64-bit versions of Windows** that have Adobe Reader installed. There's no need for the fix on 32-bit versions of Windows. If you're not sure what you have use **Start -> Control Panel -> System and Security -> System** and look at the reported **system type**.

- **If you are using a pre-release version of Office 2010 64-bit:** Newer versions of the fix should work for you as well. Note that **the retail (RTM) version of Office 2010 fixed the need for additional registry changes**. The fix tool now has a checkbox to specify whether or not you need the Office 2010 beta fixes.

- The fix requires Administrator access (UAC elevation) because it modifies values below HKEY_LOCAL_MACHINE in the registry.

- What the fix does is explicitly documented ([screenshot](https://www.pretentiousname.com/adobe_pdf_x64_fix/adobe_pdf_x64_fix_msdn.png)) in Microsoft's guidelines on [registering preview handlers](http://msdn.microsoft.com/en-us/library/cc144144%28VS.85%29.aspx) so it shouldn't cause any problems.

- The fix affects Windows Explorer and Outlook but not Internet Explorer. IE uses the full Adobe Reader, not the preview handler, and Adobe Reader has a problem with IE8 and/or Windows 7 where it opens a standalone window for PDF files even if it's configured to display PDFs in the browser. The fix won't affect that.

- You do not need to apply the fix to make PDF viewing work in newer versions of Directory Opus. My bundled viewer plugin has a workaround built-in.

- Users on earlier versions of Opus may run into the same problem that affects IE8 and/or Windows 7. Update to Opus 9.1.3.4 or above.

Source code for the preview handler fix tool:

- Interested programmers may download the C++ source code: [Reader_x64_fixer_1200_source.zip](https://www.pretentiousname.com/adobe_pdf_x64_fix/Reader_x64_fixer_1200_source.zip) (103 KB) ([PGP Sig](https://www.pretentiousname.com/adobe_pdf_x64_fix/Reader_x64_fixer_1200_source.zip.sig)))

History of the preview handler fix tool:

- **v1.2.0.0 (28/Apr/2010):** Now has a checkbox to specify extra fixes for Office 2010 beta which are no longer required for Office 2010 RTM. Also updated the text to reflect that the preview handler fix should no longer be required with Adobe Reader 9.3.2 and above. (Thanks to Alex Bantzhaff for noticing and letting me know!)
- **v1.1.0.1 (04/Feb/2010):** Updated the message it displays to reflect the new/separate thumbnails fix.
- **v1.1.0.0 (25/Jan/2010):** Added fix for problem with **64-bit Office 2010**. Thanks to Winfried Pohl for providing the extra step!
- **v1.0.0.1 (15/Dec/2009):** Initial release.

## Fixing the preview handler by hand or group policy:

If you want to apply the preview handler registry fix using group policy, see [Alan Burchill's guide](http://www.grouppolicy.biz/2010/02/how-to-use-group-policy-to-make-adobe-reader-work-in-64bit-windows/).

If you want to apply the preview handler registry fix by hand, or are just curious about the detail:

- First, read all of the section above about the tool. Most of the information also applies to doing the fix by hand.

- Open RegEdit and go to:

  **HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Classes\CLSID\{DC6EFB56-9CFA-464D-8880-44885D7DC193}**

  If it doesn't exist then you may not have Adobe Reader installed in the first place. Or Adobe may have changed the way they install it. Or you may be on 32-bit Windows. Or you may be on 64-bit Windows but have run the 32-bit version of RegEdit.exe by mistake.

- There should be an existing **AppID** value, incorrectly set to {6d2b5079-2f0b-48dd-ab7f-97cec514d30b}

- Change the AppID value to **{534A1E02-D58F-44f0-B58B-36CBED287C7C}**

  ![Adobe PDF preview handler registry fix](images/adobe_pdf_x64_fix_reg.png)

- Now see if the same registry path exists but *without* the **Wow6432Node** part. If it does exist, make the same change as before. If it doesn't exist then that's fine and you can skip this part.

  (This second area will exist if Adobe Reader was installed on Windows Vista. That includes Vista machines which were later upgraded to Windows 7. I think it's due to changes in the way 32-bit registry redirection works in Windows 7. If you have both values you need to change both; if you only have one you only need to change that one.)

- If you are using 64-bit Office 2010 beta then the second area (without the Wow6432Node) must exist for the preview handler to work. Copy the registry keys/values there if it doesn't exist. Or just use the automated tool above as it will do this for you. This extra step is not required for the retail (RTM) version of Office 2010; only for the beta.

- If you have/had another PDF preview handler installed, such as FoxIt or PDF-XChange, then whichever handler was installed last will usually be the one which is used. Uninstalling preview handlers does not always put back the previous ones; instead, do a repair install or a re-install of the preview handler you wish to use so that it takes over the PDF preview handler registration. You can also do this by editing the PDF file-type in the registry. The tool above takes care of this and all the other issues so use that if you get stuck.

## Detail on the thumbnail fix:

To fix the thumbnails, I wrote a "32/64-bit thumbnail bridge" which allows 64-bit programs like Windows Explorer to talk to 32-bit thumbnail generators like Adobe Reader's.

- As soon as you install the bridge you should see PDF thumbnails appear in Windows Explorer, File->Open/Save dialogs, etc.
- The thumbnail bridge also trims the white border which Adobe Reader places around the thumbs it generates, making them look a lot better. (As a result, even 32-bit users may wish to install it.)
- If you find that your thumbnails still do not work after installing the thumbnail bridge, do a Repair install of Adobe Reader to ensure its thumbnail generator is correctly installed. The thumbnail bridge acts as a translator between the 32- and 64-bit worlds and does not actually generate the thumbnails itself; it still relies on Adobe Reader to do that.
- Windows XP-x64 users: Sorry, but the thumbnail fix requires Windows Vista or above.
- See the [Thanks](https://www.pretentiousname.com/adobe_pdf_x64_fix/#thank) section...

History of the thumbnail fix:

- **v1.0.0.4 (09/Apr/2011):** (Public release 02/May/2011.) This hopefully fixes yet another problem in Adobe's thumbnailer which caused PDF thumbnails for files in a folder to get jumbled up. You should clear your thumbnail cache, too.
- **v1.0.0.3 (06/Feb/2011):** Fixed problem of black thumbnails appearing. This was due to a bug in the Windows shell that I had to work around. [See comment I added to IThumbnailProvider::GetThumbnail](http://msdn.microsoft.com/en-us/library/bb774612%28VS.85%29.aspx) for technical info.
- **v1.0.0.2 (05/Feb/2010):** Fixed an error which meant the small Thumbridge.exe process may have stayed around longer than it needed to.
- **v1.0.0.1 (04/Feb/2010):** Initial release.

## Hey, Adobe...

There are a few other things wrong with your PDF preview handler that should be fixed:

- It doesn't correctly respond to [IPreviewHandler::TranslateAccelerator](http://msdn.microsoft.com/en-us/library/bb775320%28VS.85%29.aspx) or call [IPreviewHandlerFrame::TranslateAccelerator](http://msdn.microsoft.com/en-us/library/bb775311%28VS.85%29.aspx) in response. In particular, it swallows tab key presses when it has focus, breaking tab cycling in the host application.
- Calls to [IPreviewHandler::SetFocus](http://msdn.microsoft.com/en-us/library/bb775317%28VS.85%29.aspx) and [IPreviewHandler::QueryFocus](http://msdn.microsoft.com/en-us/library/bb775316%28VS.85%29.aspx) always fail.
- If the PDF preview handler receives its first WM_MOUSEWHEEL messages when it doesn't have the focus then it will start to draw blank pages instead of the document contents while its scrollbar will often change size to indicate a long document only has a few pages.
- UPDATE 11/Sep/2009: If the PDF preview handler is scrolled by rapidly pushing the cursor or page up/down keys, it can draw blanks as well. ([Screenshot](https://www.pretentiousname.com/adobe_pdf_x64_fix/adobe_pdf_rendering_bug.png).)
- When the PDF preview handler has the focus it draws an ugly dotted-line border around its toolbar at the bottom. It looks like it thinks it's in ActiveX design mode or something. ([Zoomed-in screenshot](https://www.pretentiousname.com/adobe_pdf_x64_fix/adobe_pdf_dotted_line_with_focus.png).)
- Not a bug but it'd be nice if it had a simple text-search feature, please.
- Well done for releasing Adobe Reader X in a state where the preview handler's mousewheel and scrollbar do not work properly. Outstanding work, as always! -.-

## Rant:

- It's constant excitement, maintaining working Adobe PDF support and cleaning up Adobe's mess all the time, let me tell you!

  Directory Opus uses my bundled plugin as a bridge for various third-party viewers, including Adobe Reader if it's installed. I made earlier versions use the full Adobe Reader by default. I had to write a 64-to-32-bit ActiveX proxy process to make the Adobe Reader and Flash viewers work within 64-bit Opus. A lot of effort due to Adobe being so lax at producing 64-bit components. Adobe Reader was originally used instead of the preview handler because of [various issues with the preview handler](https://www.pretentiousname.com/adobe_pdf_x64_fix/#adobe).

  Then Windows 7 came out and Adobe Reader embedding was completely broken. (That could be Microsoft's fault but my bet is it's Adobe's.) So I worked around the preview handler issues, including the main one this page is about, and that is now the default in Opus.

  I wish I could bill Adobe for my time fixing their mess. The ridiculous thing is that whenever we've tried to officially inform Adobe of bugs in their code (like blindly calling through a null pointer after a failed QueryInterface), bugs which we've found and worked around for ourselves but which may cause problems for other people, they've asked *us*to pay *them* for a support contract. WTF? Who is supporting whom here, exactly?

  I don't think "CS" stands for "Creative Suite" anymore; I'm fairly sure it is actually the favourite word of Deadwood's Mr. Wu...

  (And yet, I keep [giving them so much money](https://www.pretentiousname.com/adobe_pdf_x64_fix/adobe_boxes.jpg).)

  (This is not to mention the constant stream of security issues in Adobe Reader and Adobe Flash, Adobe management thinking that releasing patches every three months is a fast response (faster than when they were even more useless, maybe, but not fast enough when their software is the #1 malware vector for the last year or two), the way the Flash and Reader update checkers do a terrible job of informing people of updates even when they are critical, the way you have to update Flash in each browser separately, the way Adobe try to make you install a download manager that's probably as big as the thing it actually downloads (which isn't big enough to warrant a download manager, either way), the way you download the Reader installer on a new machine then run the updater to find there's a MONTHS OLD update that they couldn't be bothered to package into the main installer despite the fact the update is blatantly the same size and overall content as the main installer, the still-unfixed bugs in Reader and Photoshop under Windows 7 (e.g. when maximizing with Aero), the foolish decision to add JavaScript to PDF for even more security issues (as if a file format only suited to storing legacy paper-based documents really needed interactivity given the obvious risks that come with JavaScript *even with good programmers/management*). Heck, even the latest version of Photoshop (CS4), the one Adobe app I actually like, has taken a nose-dive in terms of its UI. Sigh. What is wrong with that company? Okay, they didn't write iTunes or Lotus Notes, but they're getting close...)

  ...Anyway, [FoxIt](http://www.foxitsoftware.com/pdf/reader/) and the [FoxIt preview handler](http://timheuer.com/foxit/) also work in Office/IE/Explorer/Opus, if you prefer them. (Personally, [I find Adobe's font rendering easier to read](https://www.pretentiousname.com/adobe_pdf_x64_fix/pdf_comparison), despite my other complaints.) [PDF-XChange](http://www.docu-track.com/) works, too, though I only discovered it recently and haven't used it much.

## Thank you:

- Writing of the thumbnail fix was funded by someone who wishes to remain anonymous but still deserves thanks, not least of which for allowing the fix to be given away for free to everyone else.
- The [post and discussion](http://www.edbott.com/weblog/?p=2620) about the original version of this fix at [Ed Bott's Windows Expertise](http://www.edbott.com/weblog/) unearthed further useful information and caveats on different Windows installs. That information has been incorporated into the fix tool and this page. Credit to Ed and the commenters on his blog for their help.
- Winfried Pohl gets the credit for discovering the extra step needed to fix the preview handler under 64-bit Office 2010 beta. Thanks, Winfried! (Update: MS also fixed the retail (RTM) version of Office 2010 so it no longer requires this extra step.)
- Thanks to Alex Bantzhaff for getting in touch after he noticed that the installer for Adobe Reader 9.3.2 incorporated the preview handler registry fix. (Adobe didn't mention it in the change log, let alone credit me for finding it, but at least they finally fixed it. Maybe they'll fix the thumbnails next year? :) )
- Thanks to Jonathan Van Dusen for pointing out that the preview handler fix is still needed, even after Adobe Reader 9.3.2, for people who upgraded from Vista to Windows 7. This is because Adobe's installer is inconsistent about which registry values it sets on the different OS and on Windows 7 it fails to remove/update some incorrect values left behind by previous installs on Vista. My fix tool will deal with this and clean things up.
- Thanks to all the people who took the time to e-mail me to say thanks themselves, and for confirming that the fixes worked for them. It's great to know that so many people have found the fixes useful.
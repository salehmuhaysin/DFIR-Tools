# Tools
All the useful tools interesting to be used 



### DFIR tools:

Tool              | Description
----------------- | ----------------
[ArtifactExtractor](https://github.com/Silv3rHorn/ArtifactExtractor) | This tool extract Windows artifacts (registry, windows events, some logs) from raw disk image
[Autopsy](https://www.sleuthkit.org/autopsy/)           | Disk image browser and parser (you could parse for .exe files, email messages, IP addresses, URL links, disk indexing,...) and you could browse the file system
[log2timeline](https://github.com/log2timeline/plaso) | Generate super timeline (how to use it: [Here](https://medium.com/dfclub/how-to-use-log2timeline-54377e24872a))
[Yara](http://yara.readthedocs.io/en/v3.7.1/index.html) | Tool primarily used in malware research and detection using some rules (for a  great Yara rules [Here](https://github.com/Yara-Rules/rules) )
[YaraGenerator](https://github.com/Xen0ph0n/YaraGenerator) | Generate a yara rule for a given samples on automated way 
[ZipDump](https://github.com/DidierStevens/DidierStevensSuite/edit/master/zipdump.py) | Tool could be used to search using Yara rules inside given archive file
[FTK Imager](https://accessdata.com/product-download)  | Tool used to take disk/memory image of the machine
[RegistryChangesView](https://www.nirsoft.net/utils/registry_changes_view.html) | Registry change viewer, give the changes happen to the registry
[VirusTotalHashScanner](https://github.com/salehmuhaysin/VirusTotalHashScanner) | Check a list of hashes in VirusTotal for any malicious file
[Prefetch Parser](https://github.com/bromiley/tools/tree/master/win10_prefetch) | Prefetch file parser, get execution time and execution count.
[Eric Zimmerman](https://ericzimmerman.github.io/#!index.md) | List of useful tools for DFIR 
[OfficeParser](https://github.com/unixfreak0037/officeparser) | parse office documents, good to extract the VBA files inside them
[CDIR](https://github.com/CyberDefenseInstitute/CDIR) | Artifacts ccollector
[Glogg](http://glogg.bonnefon.org/download.html) | GUI version for grep command across multiple platform 
[Rekall](https://github.com/google/rekall) | Memory analysis framework, (similar to volatility)
[bulk_volatility_scanner](https://github.com/rcobb76101/bulk_volatility_scanner) | This is a great easy to use script that runs all volatility plugins on all memory images provided. it takes the path of the images and the path of the output dir. Run it and sip tea or do something else until it is done (wink)
[BMC viewer](https://github.com/0xTowel/BMC-Viewer-Backup) | viewer for pictures of .bmc files
[PC Hunter](https://www.majorgeeks.com/files/details/pc_hunter.html) | GUI tool gives detailed information of processes, dlls, hooks both ring 0 and 3, (similar to process hacker)
[MemProcFS](https://github.com/ufrisk/MemProcFS) | Accesses memory as a mounted filesystem. It can be used as an API as well. Can be used on live memory or a memory dump file.
[TC4shell](http://www.tc4shell.com/en/download/) | Decompress most of compressed files, such as AD1, etc.
[Recyclebin](https://df-stream.com/recycle-bin-i-parser/) | Recyclebin parser for ($I) files

---



### Malware Analysis and Reverse Engineer:

Tool              | Description
----------------- | ----------------
[PEStudio](https://www.winitor.com/binaries.html) | Malware Initial Assessment, give file information, strings, resources, imports,...
[dnSpy](https://github.com/0xd4d/dnSpy) | dnSpy is a debugger and .NET assembly editor
[Sysinternals](https://docs.microsoft.com/en-us/sysinternals/downloads/) | windows sysinternals utilities to monitor the system 
[DLLExportViewer](http://www.nirsoft.net/utils/dll_export_viewer.html) | Show all the export functions for any DLL file
[PDF-Parser & pdfid](https://blog.didierstevens.com/programs/pdf-tools/) | Python script to parse PDF files
[Snowman](https://derevenets.com/) | Is an executable decompiler to C/C++
[exiftool](https://www.sno.phy.queensu.ca/~phil/exiftool/) | Tool extract the metadata for a given file
[PE-Sieve](https://github.com/hasherezade/pe-sieve) | Tool take PID and check if the original file same as the file loaded in memory
[Jmp2it](https://github.com/adamkramer/jmp2it/releases) | Tool used to load a shellcode into executable, and attach IDA to debug the shellcode
[File Signature](https://www.filesignatures.net/index.php?page=all) | Website contain a list of file extensions and signature

---


### Unpackers/Obfuscators
Tool              | Description
----------------- | ----------------
[UPXEasyGUI](http://www.novirusthanks.org/products/upx-easy-gui/) | UPX Packer and Unpacker
[RDGPackerDetector](http://www.rdgsoft.net/) | Detect the type of the packer for a given program
[ConfuserEx-DeObfuscate](https://github.com/salehmuhaysin/DFIR-Tools/blob/master/Tools/ConfuserEx%20Collection.zip) | These tools could be used to deobfuscate executables packed by ConfuserEx
[Scylla](http://www.woodmann.com/collaborative/tools/index.php/Scylla) | A great tool used to rebuild the import address table of executable (useful for manual unpacking of executables)
[Protection_ID.eXe](https://tuts4you.com/e107_plugins/download/download.php?view.400) | tool used to detect the obfuscation type

---
### Helpful links
link              | Description
----------------- | ----------------
[XSS cheat sheet](https://www.owasp.org/index.php/XSS_Filter_Evasion_Cheat_Sheet#No_closing_script_tags) | include a list of XSS technquies could be used.
[Stego tools](http://stegano.net/tools) | List of stego tools

---

### Helpful Commands
> for f in \*/Logs/\*.evtx ; do echo "$f" ; mkdir -p $(echo "./Events/$f" | awk -F '/' '{print $1 "/" $2 "/" $3 "/" $4 "/"}') ; evtx_dump.py "$f" > "./Events/${f%.xml}.xml" ; echo " Done ..." ; done

this command will read all evtx files on \*/Logs/ folders and convert them into xml files under the folder ./Events with same directories from the original one.

> for f in \*/Logs/\*.evtx ; do echo "$f" ; mkdir -p $(echo "./Events/$f" | awk -F '/' '{print $1 "/" $2 "/" $3 "/" $4 "/"}') ; test ! $(wc -c "$f" | awk '{print $1 }' ) -le 550000000;  $(\[\[ $? -eq 1 \]\] && evtx_dump.py "$f" > "./Events/${f%.xml}.xml") ; echo " Done ..." ; done

Same command but, this will check the file size not more than 550000000 bytes

fast command: 
> for f in ./*.evtx ; do echo "$f" ; evtx_dump.py "$f" > "./Events/${f%.xml}.xml" ; echo " Done ..." ; done

---
copy files and show the progress 
> rsync -r --info=progress2 source destination
---
Extract VBA macro from a list of document files
> for f in * ; do echo "$f" ; mkdir -p $(echo "./output/$f") ; officeparser --extract-macros $f -o "./output/$f" ; echo " Done ..." ; done

---
How to use xargs to do multiprocessing commands:
> find ./ -name '*.log' | xargs -rtP 20 -L1 grep "pattern" > output.txt

-P 20: number of processes at the same time

-t: print the command

-r: run only if there is argument

-L1: one argument at the same time, means one file per command

Note: if you use -L1 and write output on text file, the result might be missed up, so it is better not using it if there are many input files

---
How to set Linux Forwarder machine from one interface to another

> modprobe iptable_nat

> echo 1 > /proc/sys/net/ipv4/ip_forward

> iptables -t nat -A POSTROUTING -d 0/0 -s 10.0.1.0/24 -j MASQUERADE

> iptables -A FORWARD -s 10.0.1.0/24 -d 0/0 -j ACCEPT

> iptables -A FORWARD -s 0/0 -d 10.0.1.0/24 -j ACCEPT


--- 

If one use zgrep just like you use grep.
If many:

> find -iname "*.gz" | xargs zgrep <options like -P or -i ...> "<str or regex if using -P>"

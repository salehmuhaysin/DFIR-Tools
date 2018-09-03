# Tools
All the useful tools interesting to be used 



### DFIR tools:

Tool              | Description
----------------- | ----------------
[ArtifactExtractor](https://github.com/Silv3rHorn/ArtifactExtractor) | This tool extract Windows artifacts (registry, windows events, some logs) from raw disk image
[Autopsy](https://www.sleuthkit.org/autopsy/)           | Disk image browser and parser (you could parse for .exe files, email messages, IP addresses, URL links, disk indexing,...) and you could browse the file system
[log2timeline](https://github.com/log2timeline/plaso) | Generate super timeline (how to use it: [Here](https://medium.com/dfclub/how-to-use-log2timeline-54377e24872a))
[Yara](http://yara.readthedocs.io/en/v3.7.1/index.html) | Tool primarily used in malware research and detection using some rules (for a  great Yara rules [Here](https://github.com/Yara-Rules/rules) )
[ZipDump](https://github.com/DidierStevens/DidierStevensSuite/edit/master/zipdump.py) | Tool could be used to search using Yara rules inside given archive file
[FTK Imager](https://accessdata.com/product-download)  | Tool used to take disk/memory image of the machine
[RegistryChangesView](https://www.nirsoft.net/utils/registry_changes_view.html) | Registry change viewer, give the changes happen to the registry
[VirusTotalHashScanner](https://github.com/salehmuhaysin/VirusTotalHashScanner) | Check a list of hashes in VirusTotal for any malicious file
[Prefetch Parser](https://github.com/bromiley/tools/tree/master/win10_prefetch) | Prefetch file parser, get execution time and execution count.
[Eric Zimmerman](https://ericzimmerman.github.io/#!index.md) | List of useful tools for DFIR 

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


---


### Unpackers/Obfuscators
Tool              | Description
----------------- | ----------------
[UPXEasyGUI](http://www.novirusthanks.org/products/upx-easy-gui/) | UPX Packer and Unpacker
[RDGPackerDetector](http://www.rdgsoft.net/) | Detect the type of the packer for a given program
[ConfuserEx-DeObfuscate](https://github.com/salehmuhaysin/DFIR-Tools/blob/master/Tools/ConfuserEx%20Collection.zip) | These tools could be used to deobfuscate executables packed by ConfuserEx
[Scylla](http://www.woodmann.com/collaborative/tools/index.php/Scylla) | A great tool used to rebuild the import address table of executable (useful for manual unpacking of executables)

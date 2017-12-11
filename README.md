# Introduction
 Welcome to the readr [`github`](https://techcrunch.com/2012/07/14/what-exactly-is-github-anyway/) page!  This will be a live repository for all of the  materials used in the workshops. We will update you when pertinent information goes up on this site. The current action items include:
  * Read through the preparatory materials.
  * Provide us your travel itinerary and requirements.
  * Set up your your computer.

Over the next couple of weeks I will be compiling a reference of computing resources and tools. If you are interested keep an eye on this site.
--- Prithvi

Contact: If you have any issues with the setup instructions please contact me at prithvi.reddy@anu.edu.au.

# Software and System Setup
Some of the workshops that will require to you to write code. Don't panic if you are unfamiliar with programming. The workshops will not require much computer science background. However, if you are interested in preparing beforehand, there is a jupyter notebook with examples and exercies included in this repository, follow the instructions are included `Jupyter Notebook` section. It should help you to hit the ground running  (if you want more help, an alternate resource is the following [primer on programming](https://python.swaroopch.com/) in python).
To participate in the workshops you will also need a couple of software tools. The key resources you will need to have set up on your system are:
  * [`python`](https://www.python.org/) (3.5 or later),
  * [`jupyter` Notebook](http://jupyter.org/)
  * [`tensorflow`](https://www.tensorflow.org/),
  * and [`CERN root`](https://root.cern.ch/).

In the interest of saving time during the event, please attempt to get these working on your own device before readr. I have provided detailed installation instructions . There are two different approaches:

  1. Quick-Start: Where I walk you through setting up a virtual computer on device that can emulate a pre-packaged operating system with everything set-up already.
  2. System Install: Links, suggestions and guides to installing the software directly onto your system. This option will be much more involved and I can not guarantee that everything will work on your particular system.

I strongly suggest following the Quick-Start instructions.

## Quick-start
1. Install `Oracle VirtualBox`. This program will allow you to emulate a virtual computer so that you can run multiple operating systems without needing to dual-boot.
   * [Linux instructions](https://www.virtualbox.org/wiki/Linux_Downloads)
   * [OSX installer](http://download.virtualbox.org/virtualbox/5.2.0/VirtualBox-5.2.0-118431-OSX.dmg)
   * [Windows installer](http://download.virtualbox.org/virtualbox/5.2.0/VirtualBox-5.2.0-118431-Win.exe)
2. Download the pre-built `ubuntu` environment (`readr.ova`) from [clourstor](https://cloudstor.aarnet.edu.au/sender/?s=download&token=ec6fc5cd-e722-976a-e908-f0d263b3d722). Note: this download will go quicker if you are on `aarnet` (your home university network).
3. Import this operating system into `VirtualBox`:
   * Open `VirtualBox`,
   * in the file menu select import appliance. <p align="center"><img width="460" height="300" src="https://raw.githubusercontent.com/pmRed/readr-repo/master/imgs/instr/VBoxInstr02.png"></p>
   * Navigate to the directory containing `readr.ova` and select this file. <p align="center"><img width="460" height="300" src="https://raw.githubusercontent.com/pmRed/readr-repo/master/imgs/instr/VBoxInstr03.png"></p>
   * This will bring up a window detailing all of the properties of the virtual machine. It should look like <p align="center"><img width="460" height="300" src="https://raw.githubusercontent.com/pmRed/readr-repo/master/imgs/instr/VBoxInstr04.png"></p>
   * Here you can change the amount of ram or the number of processes devoted to the virtual machine to suit your own system. The resources you devote to the setup will make it faster/slower. You can also change this in the settings later if you need to.
   * Click the import button and agree to the licence.
4. You should now have access to the `readrenv` machine which is powered off. Click start and `ubuntu` should start up in another window.

      <img align="left" width="405" src="https://raw.githubusercontent.com/pmRed/readr-repo/master/imgs/instr/VBoxInstr01.png"><img align="left" width="405" src="https://raw.githubusercontent.com/pmRed/readr-repo/master/imgs/instr/VBoxInstr05.png">
 
5. Now you are ready to go!
## System Install

Disclaimer: 

- There are multiple ways of getting these things to run. In particular, evironment managment can be tricky in `python`. The following only applies to a clean build of `python3`. If you have multiple conflicting versions of python running it can turn into a mess. If you want to be able to do this learn how to set up an `anaconda` and/or `virtualenv` environment.
- I have only tested this on my own device.

### Linux
Assuming that you have a Debian (Ubuntu) environment:
1. [Install `python3` and `pip`](http://docs.python-guide.org/en/latest/starting/install3/linux/)
2. `pip3 install tensorflow jupyter`
3. [Installing/Building Cern Root](https://root.cern.ch/root/html534/guides/users-guide/InstallandBuild.html)

If you are using another system, the process should be analogous.
### OSX
  1.  Install [Homebrew](https://brew.sh/). It is a software management package for OSX which hosts a large set of brews "formulae" for installing open source software onto your OSX box. It is well written and will handle most of the dependencies and installation hassles.
  3. If you don't already have `python` installed open the terminal application and run `brew install python3`. The homebrew install will also provide the `pip3` application which will let you install and manage python packages.
  4. Now you have `pip3` you can install `jupyter` and `tensorflow` easily by running `pip3 install jupyter tensorflow`.  
  5. Finally,  [here](https://alexpearce.me/2016/02/root-on-os-x-el-capitan/) is a guide to installing `root`. This link will also work for the Sierra version of OSX. Please be aware that this will not work for earlier versions. The author provides alternate instructions for older OSX versions. If none of this works refer to these [installation instructions](https://root.cern.ch/root/html534/guides/users-guide/InstallandBuild.html).
### Windows
Sorry people, still working on a windows guide for this part. Come back later or use the VM.  =)

# Jupyter notebook
The file `1. Scientific Programming with Python.ipynb` included in this repository is an introduction to python and jupyter written by Josh Issacs.
You can:
1. (Recommended) Open it directly on your environment (once you have set up python and jupyter as detailed above). 
    - Download the repository using the green `clone or download` button on the main page.
    - Once you have Jupyter installed open it by either using the terminal (typing `jupyter` into it) or finding the desktop/menu icon. This will open a browser window with a notebook interface. 
    - Click upload file, and choose the `1. Scientific Programming with Python.ipynb` file that you downloaded.
    - Upload the file. You can now open it, and run the Python examples within.
2. View it online [here](https://github.com/josh146/readr/blob/cff48e4c5e99f1512ac3bc86a99ad99291d20945/1.%20Scientific%20Programming%20with%20Python.ipynb). Notably, this option will not give you access to the interactive components of the notebook.

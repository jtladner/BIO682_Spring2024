# Class 3 - Feb. 2nd 2024
- In this class we will:
    - Learn to download, install and run open source software
    - Learn to use for loops in the shell to batch run multiple similar commands
    - Learn to combine shell commands within a file to create shell scripts

### Required Reading (**Must be completed ahead of time**)
Practical Computing for Biologists, Chapter 6, 21

### Preparation for next class

Python scripts are generally simple text files that are executed on the command line, just like the shell scripts we'll be generating in today's class. However, there are also GUIs available that allow for python scripts (and those written in other programming languages), to be written and executed without needing the command line. We will use this type of interactive interface for our initial introduction to Python programming and also later in the class, when we learn how to use Python to generate figures. The interactive GUI we will use is called Jupyter Notebook (NOT Jupyter Lab!). 

1. Install Jupyter Notebook

There are multiple ways that you can [install the Jupyter Notebook](http://jupyter.org/install), but I highly recommend installing using the [Anaconda Distribution](https://www.anaconda.com/download/). Anaconda is available for Windows, Linux and MacOS and the Jupyter Notebook is automatically installed as a part of the Anaconda distribution. Please install the Python 3 version of Anaconda. Although your book uses Python 2, Python 3 is the current version and it is pretty easy to translate commands between the two versions. 

After Anaconda has been installed, open a terminal window (Mac/Linux) or the "Anaconda Prompt" (Windows) and run the following command: ```jupyter notebook```

This should automatically open the jupyter notebook within your default web browser. 

### Assignment

1. Follow the instructions on PCfB p.85-88 to set up your own ```scripts``` and ```programs``` directories and add these directories to your system's PATH. After you've finished, run the following command in the shell and copy and paste the output in the **Assignment Answer Sheet**.

```echo $PATH```

2. Downloading and using a precompiled binary

    1. Download precompiled binaries for [NCBI's BLAST+ tool](https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/) that is appropriate for your operating system. For Mac users, I recommend ```ncbi-blast-2.15.0+-x64-macosx.tar.gz```, for Windows/Linux users I recommend ```ncbi-blast-2.15.0+-x64-linux.tar.gz```. For those working in WSL-Ubuntu, it may be easiest to download via your command line using ```curl``` or ```wget```.
    
    2. After downloading, decompress the archive using ```tar -xf```. This should generate a directory called ```ncbi-blast-2.15.0+```. Inside this directory, locate the ```bin``` directory, which contains all of the binaries. Move the ```makeblastdb``` and ```blastn``` binaries into your ```programs``` directory. 
    
    3. Use ```chmod``` to ensure that these newly downloaded binaries are executable. Veryify the permissions are set properly using ```ls -l```. Enter the commands you used and the current permissions for the binaries in the **Assignment Answer Sheet**.
    
    4. Within the shell, move into  the ```mysteryVirus``` directory, which is located within the ```Assignment``` directory for this week's class (```Week03_Shell-pt2/Assignment```).
    
    5. If you have properly added the ```programs``` directory to your PATH, and the blast binaries are executable, you should be able to use these programs from anywhere on your computer just using the name of the binary (i.e., without specifying the location of the binary). Check that this works by simply typing ```makeblastdb``` in your shell and hitting ```return```. If things are working as expected, you should see some usage information printed to your terminal window. 
    
    6. Use the newly downloaded makeblastdb binary to create a custom blast database from the sequences contained in ```Week03_Shell-pt2/Assignment/virus_references.fasta``` using the following command:
    
    ```makeblastdb -in virus_references.fasta -dbtype nucl```
    
    7.  Use the newly downloaded blastn binary to compare the mystery virus to the references using the following command:
    
    ```blastn -query mystery_sequence.fasta -db virus_references.fasta -out out.tsv -outfmt 6```
    
    8.  Step #7 will generate a tab-delimted file with information about the best reference match. The name of the best reference match will be in the 2nd column of the output. Please enter this name in your **Assignment Answer Sheet** and **Upload your result file** (```out.tsv```) to Canvas along with the Assignment Answer Sheet. 


3. Download and compile source code
    
    1. Download the source code for [FLASH from Sourceforge]("https://sourceforge.net/projects/flashpage/files/") just as shown in today's demo. If desired, move source code to ```source``` directory then decompress with ```tar -xf```. 
    
    2. Within the shell, move into the decompressed source code directory, which should be called ```FLASH-1.2.11```. 
    
    3. Compile the FLASH program using ```make```. While the compilation is running, you will see a bunch of text printed to the screen, which probably won't make a lot of sense. As long as you don't see "fatal error" in red, every thing is probably OK. 
        
    4. To test the compiled binary, run the following command: ```./flash```. This should print some basic usage information to the screen. Copy this information into the **Assignment Answer Sheet**.
    

4. Move into ```Week03_Shell-pt2/Assignment/zika_genomes```. This directory contains 89 fasta files. 88 of these each contain a single Zika virus genome, and each sequence containing line within these fasta files has a maximum length of 70 nucleotides. The other is a test file containing a dummy sequence wrapped 5 nucleotides per line.

    This directory also contains a simple python script - "wrap_fasta.py" - that changes the length of the sequence lines in a fasta file. Here is an example command that will take an input fasta and generate a new version with sequence containing lines up to 20,000 nucleotides long:

    ```wrap_fasta.py  input.fasta  output.fasta 20000```

    1. Copy this python script into your 'scripts' directory and make it executable.  

    2. Test that the program is working by running the following command:

    ```wrap_fasta.py  dummy.fasta  dummy_singleline.fasta 20```

    3. This command should create a new file within your working directory called "dummy_singleline.fasta" and in this file, the dummy sequence should now be contained on a single line (instead of being split across four lines, as in dummy.fasta)

    4. Use a for loop (entered directly within the terminal window) to batch process all of these Zika virus genomes, using wrap_fasta.py to create new versions in which each viral genome sequence will be contained on a single line.
    
    **Hint 1**: the Zika virus genome is a little less than 11,000 nucleotides long. 
    
    **Hint 2**: Make sure that you do not overwrite the original versions of the fasta sequences (i.e., the output.fasta name must be different from the input.fasta name).
    
    5. Enter your successful for loop in the **Assignment Answer Sheet** and **upload 1 of the output fasta files** to Canvas along with the Assignment Answer Sheet.

5. Move into the ```Week03_Shell-pt2/Assignment``` directory. Within this directory, you will find a file called ```dummy.txt```. Write and execute a simple shell script called ```dummy.sh``` that will:
    1. Create a new directory within ```Week03_Shell-pt2/Assignment``` called "dummy_dir"
    2. Move "dummy.txt" into this new directory
    3. Rename "dummy.txt" to "done.txt"
    4. **Upload your shell script** to Canvas along with the Assignment Answer Sheet. 


6. Move into ```Week03_Shell-pt2/images```. This directory contains several pdf files. 
    1. Using ```ls``` in combination with regular expressions within your text editor, as described in PCfB p.91-96, generate a shell script called called ```renamer.sh``` that will create renamed copies of all of these pdf files within a new sub-directory called "images\_renamed". For the image files that start with "test\_", the new names should omit "test\_3.6.7\_" from the beginning of the file names and ".txt" from within the file names. For the remaining files, omit the portion of the name that comes prior to the '-' character (and the '-' character itself).
    2. **Upload your shell script** to Canvas along with the Assignment Answer Sheet. 



## Extra fun

[Terminus game](http://web.mit.edu/mprat/Public/web/Terminus/Web/main.html)

[Command-line Murder Mystery](https://github.com/veltman/clmystery/)

Copyright (C) 2024  Jason Ladner

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.




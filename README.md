# rename_file_sequence

**How to Install**

git clone https://github.com/indraneelmax/rename_file_sequence

cd rename_file_sequence

pip install .

rename_file_sequence --help


usage: rename_file_sequence [-h] [--pad [PAD]] [--mock] [--verbose]

   [input_dir]

Given a directory identifies a sequence of files based on file name and
extension, and renames them sequentially keeping the same order! Sample usage:
rename_file_sequence.py /path/to/directory


positional arguments:


  input_dir    Path to input directory containing files


optional arguments:

  -h, --help   show this help message and exit
  
  
  --pad [PAD]  minimum padding for digits in renamed sequence, default is 2
  
  
  --mock       mock mode, do not rename
  
  
  --verbose    verbose mode


Sample Output:


rename_file_sequence /path/to/directory --verbose --pad 3

Looking at Input directory: /path/to/directory

123asda234.png file is not valid format, will not rename

123asda23.png file is not valid format, will not rename

Renamed ashish11.jpg  -->  ashish001.jpg

Renamed ashish15.jpg  -->  ashish002.jpg

Renamed ashish03.png  -->  ashish001.png

Renamed ashish06.png  -->  ashish002.png

Renamed ashish13.png  -->  ashish003.png

Renamed garvit1.jpg  -->  garvit001.jpg

Renamed garvit2.jpg  -->  garvit002.jpg

Renamed garvit7.jpg  -->  garvit003.jpg

Renamed garvit14.jpg  -->  garvit004.jpg

Renamed jaski1.jpg  -->  jaski001.jpg

Renamed jaski5.jpg  -->  jaski002.jpg

Renamed jaski9.jpg  -->  jaski003.jpg

Renamed jaski3.png  -->  jaski001.png

jaski5..png file is not valid format, will not rename

Renamed neel06.jpeg  -->  neel001.jpeg

Renamed neel01.jpg  -->  neel001.jpg

Renamed neel02.jpg  -->  neel002.jpg

Renamed neel09.jpg  -->  neel003.jpg

sonu12inu.jpg file is not valid format, will not rename

sonu1inu.jpg file is not valid format, will not rename

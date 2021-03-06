# LED Matrix Fonts

## Description

This repository contains scripts to decode .ttf files to bitmaps (using otf2bdf), and code to display those fonts on an led matrix.

## Installation

1.  Install dependencies: `apt-get install otf2dbf python3 git`.

2.  Build and install [jgarff's rpi_ws281x library.](https://github.com/jgarff/rpi_ws281x)

3.  Clone the repository using `git clone https://github.com/iconoptic/LedMatrixFonts.git`.

## Usage

To decode a ttf file, run the script `font2bitmaps.sh`. This script accepts 0-1 arguments, enter the path to a ttf file. Default output is to STDOUT, redirect the output to a python source file.

Import the source file to ledSquare.py and replace instances of 'arial.font' with '_your font name_.font'.

Import ledSquare into test.py, or your preferred main program. Print a string to the led matrix by typing ledSquare.shStr("_your string_").



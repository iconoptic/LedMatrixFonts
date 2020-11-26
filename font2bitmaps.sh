#!/bin/bash

if [ "$#" -ne 1 ]; then
		echo -n "Enter path to ttf file: "
		read -e file
else
		file=$1
fi


outfile=`echo $file | sed 's/...$/txt/g'`
otf2bdf -p 8 $file | sed -n '/ENCODING [0-9]/,/ENDCHAR/p' \
		| sed '/.WID.*/d;/BIT.*/d;s/ENCODING //g;s/BBX [0-9]\+ [0-9]\+.[-]\{0,1\}[0-9] //g;s/ENDCHAR/;/g' \
		 > $outfile

./decode.py $outfile

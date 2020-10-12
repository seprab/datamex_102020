#! /bin/bash
for i in $(ls lorem)
do
	echo $i;
	echo $i | wc -m;
done

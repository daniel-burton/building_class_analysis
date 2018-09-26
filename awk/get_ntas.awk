#! /bin/awk

BEGIN {OFS=","; FS=",";} 
{print $3, $1, $4, $5, $6, $7} 

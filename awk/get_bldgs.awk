#! /bin/awk

BEGIN { FS=","; OFS=","} #set field separator
NR==1 {print $72, $1, $2, $3, $4, $5, $6, $17, $29, $74} #print column labels
$74~/..../ {$74 = $74 "00"} #if tract is 4 digits, append "00"
($72~/........../) {print $72, $1, $2, $3, $4, $5, $6, $17, $29, $74}
#get the appropriate fields only if BBL known, BBL will be primary key 

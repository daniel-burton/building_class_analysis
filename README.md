#building class analysis

1. Download PLUTO file from NYC open data website, currently using 18v1.
2. Use the awk scripts to process the data and get only the important columns. One for NTA equivalency, one for the PLUTO files. Also fixes zero-padding on census tract.
3. Use python loaders to load NTA equivalency and PLUTO files into SQL database.

To do:
* Create script to download the PLUTO files
* Create script to go through all borough PLUTO files with awk, rather than running script on each separately
* Make awk script for NTAs fix the borough + tract column merge, rather than fixing in excel
* Look over building typology and condense categories that are functionally equivalent like types of parking garage
* Create SQL queries to do the work! Creating profiles of NTAs by prevalence of building types

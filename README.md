#Building Class Analysis for NYC Neighborhoods

1. Download PLUTO file from NYC open data website, currently using 18v1.
2. Use the awk scripts to process the data and get only the important columns. One for NTA equivalency, one for the PLUTO files. Also fixes zero-padding on census tract.
3. Use python loaders to load NTA equivalency and PLUTO files into SQL database.

To do:
* Expand bash script, adding in python steps
* Replace awk scripts ; _ ; with Python/Pandas scripts for consistency
* Create script to go through all borough PLUTO files with awk, rather than running script on each separately
* Make awk script for NTAs fix the borough + tract column merge, rather than fixing in excel
* Look over building typology and condense categories that are functionally equivalent like types of parking garage
* use pandas.pivot() to create the neighborhood summaries. 

#Building Class Analysis for NYC Neighborhoods

1. Downloads PLUTO file from NYC open data website, currently using 18v1.
2. Current branch uses awk to select appropriate columns, python to load them into postgres
3. Creating branch that uses python and pandas for everything instead.

To do:
* Expand bash script, adding in python steps
* Create script to go through all borough PLUTO files with awk, rather than running script on each separately
* Make awk script for NTAs fix the borough + tract column merge, rather than fixing in excel
* Look over building typology and condense categories that are functionally equivalent like types of parking garage
* create the neighborhood summaries. 

#!/usr/bin/python
# textgrid2csv.py
# D. Gibbon
# 2016-03-15
# 2016-03-15 (V02, includes filename in CSV records)

#-------------------------------------------------
# Import modules

import sys, re

#-------------------------------------------------
# Text file input / output

def inputtextlines(filename):
    handle = open(filename,'r')
    linelist = handle.readlines()
    handle.close()
    return linelist

def outputtext(filename, text):
    handle = open(filename,'w')
    handle.write(text)
    handle.close()

#-------------------------------------------------
# Conversion routines

def converttextgrid2csv(textgridlines,textgridname):

    csvtext = '# TextGrid to CSV (D. Gibbon, 2008-11-23)\n# Open the file with OpenOffice.org Calc or MS-Excel.\nFileName\tTierType\tTierName\tLabel\tStart\tEnd\tDuration\n'

    newtier = False
    for line in textgridlines[9:]:
        line = re.sub('\n','',line)
        line = re.sub('^ *','',line)
        linepair = line.split(' = ')
        if len(linepair) == 2:
            if linepair[0] == 'class':
                classname = linepair[1]
            if linepair[0] == 'name':
                tiername = linepair[1]
            if linepair[0] == 'xmin':
                xmin = linepair[1]
            if linepair[0] == 'xmax':
                xmax = linepair[1]
            if linepair[0] == 'text':
                text = linepair[1]
                diff = str(float(xmax)-float(xmin))
                csvtext += textgridname + '\t' + classname + '\t' + tiername + '\t' + text + '\t' + xmin + '\t' + xmax + '\t' + diff + '\n'
    return csvtext

#-------------------------------------------------
# Main caller

def main():    

    if len(sys.argv) < 2:
        print("Usage: textgrid2csv.py <textgridfilename>")
        exit()
    textgridname = sys.argv[1]
    csvname = textgridname + '.csv'

    textgrid = inputtextlines(textgridname)

    textcsv = converttextgrid2csv(textgrid,textgridname)

    outputtext(csvname,textcsv)

    print("Output file: " + csvname)

    return

#-------------------------------------------------

main()

#--- EOF -----------------------------------------

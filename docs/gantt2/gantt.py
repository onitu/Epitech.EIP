#!/usr/bin/env python

import csv
import sys
from datetime import date

TITLE = "Gantt Onitu"
HEADER = """
\\begin{ganttchart}
    [vgrid,hgrid]{24}
\\gantttitle {%s}{24} \\\\
""" % (TITLE)
FOOTER = """
\end{ganttchart}
"""

def write_gantt(ganttbar_list):
    print HEADER
    for bar in ganttbar_list:
        print bar
    print FOOTER

def convert_to_latex(csv_content):
    ganttbar_list = []
    txt = csv_content[0][2].split('-')
    origin_start = date(int(txt[0]), int(txt[1]), int(txt[2]))
    origin_year = int(txt[0])
    for row in csv_content[1:]:
        txt = row[2].split('-')
        start = date(int(txt[0]), int(txt[1]), int(txt[2]))
        start_year = int(txt[0])
        txt = row[3].split('-')
        end = date(int(txt[0]), int(txt[1]), int(txt[2]))
        end_year = int(txt[0])
        # start = (start - origin_start) + 1
        # end = (end - origin_start).days + 1
        if row[-1] != "blue2":
            ganttbar_list.append("\\ganttgroup {%s}{%s}{%s} \\\\" % (row[1],
                                                                     (start_year - origin_year) * 12 + start.month -5,
                                                                     (start_year - origin_year) * 12 + end.month -5))
        else:
            ganttbar_list.append("\\ganttbar {%s}{%s}{%s} \\\\" % (row[1],
                                                                   (start_year - origin_year) * 12 + start.month - 5,
                                                                   (start_year - origin_year) * 12 + end.month - 5))
    return ganttbar_list

def read_gantt(filename):
    lines = []
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        try:
            for row in reader:
                lines.append(row)
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
    return lines

def main():
    if len(sys.argv) < 2:
        print "Oukilerlefichier?"
        return

    gantt = read_gantt(sys.argv[1])
    latex_gantt = convert_to_latex(gantt[1:])
    write_gantt(latex_gantt)


main()

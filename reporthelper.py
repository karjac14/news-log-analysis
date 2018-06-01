#!/usr/bin/env python
# "Helper code" for the log reports


def beautify(report_num, list):

    text = ''
    if report_num == 0 or report_num == 1:
        for x in list:
            text += x[0] + " - " + str(x[1]) + " views \n"
        text += "\n"
        return text
    elif report_num == 2:
        for x in list:
            text += x[0] + " - " + str(x[1]) + "% errors \n"
        text += "\n"
        return text

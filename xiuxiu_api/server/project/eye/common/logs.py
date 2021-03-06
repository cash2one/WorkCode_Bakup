# coding: utf-8

import sys


class Logs(object):
    @staticmethod
    def print_current_function_name_and_line_number(ex):
        try:
            raise Exception()
        except:
            f = sys.exc_info()[2].tb_frame.f_back
        print "function name: " + f.f_code.co_filename + "; line no: " + str(f.f_lineno) + "; exception: " + ex.message

    @staticmethod
    def print_log(name, value):
        print name + ":" + str(value)

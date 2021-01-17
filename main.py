# -*- coding: utf-8 -*-
from logger import *
import chardet
import codecs

extensions = ['.cpp', '.h', '.md', '.txt']
out_code = 'utf-8'

def convert_code(file_path):

    if not os.path.isfile(file_path):
        return False

    with open(file_path, "rb") as f_in:
        f_data = f_in.read()
        this_detect = chardet.detect(f_data)['encoding']

        if this_detect == None:
            put_log_msg('Not detect encodeing, pass:' + file_path, 2)
            return

        if this_detect != out_code:
            try:
                with codecs.open(file_path, 'r', this_detect) as f_in:
                    new_content = f_in.read()
                    f_out = codecs.open(file_path, 'w', out_code)
                    f_out.write(new_content)
                    f_out.close

                put_log_msg('Convert succeeded:' + file_path, 1)
            except:
                put_log_msg('Convert failed:' + file_path, 2)
        else:
            put_log_msg('Already right coded:' + file_path, 1)


def convert_codes(path):
    search_file(path, lambda f: convert_code(f))

def search_file(path, call):
    files = os.listdir(path)
    for f in files:
        full_f = os.path.join(path, f)
        if os.path.isdir(full_f):
            search_file(full_f, call)
        else:
            if os.path.splitext(f)[-1] in extensions:
                call(full_f)

if __name__ == '__main__':
    convert_codes('/Users/mac/**/*')

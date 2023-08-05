#!/usr/bin/env python3

#----- imports -----

from .__init__ import *
from .__init__ import __version__ as VERSION, __doc__ as DESCRIPTION
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from fnmatch import fnmatchcase
from glob import glob
from os import makedirs as md, remove as rm, rename as mv, chdir as cd
from pdfrw import PdfReader, PdfWriter
from shutil import copy2 as cp
from sys import argv, stderr
from time import localtime, sleep
from warnings import simplefilter
import PySimpleGUI as sg

#----- constants -----

EMPT, CODE, TEXT, PICT, CONT, FIGU, CAPT, INDX, CHP1, CHP2, HEA1, HEA2 = range(12) # line kinds

KINDS = 'EMPT, CODE, TEXT, PICT, CONT, FIGU, CAPT, INDX, CHP1, CHP2, HEA1, HEA2'.split(', ')
    # values in buf.buffer[KIND]
    # EMPT empty line
    # CODE Python code line
    # TEXT text line
    # PICT picture line
    # CONT contents chapter line
    # FIGU figure chapter line
    # CAPT figure caption line
    # INDX index chapter line
    # CHP1 numbered chapter line, level == 1
    # CHP2 numbered chapter line, level > 1
    # HEA1 page header, first line
    # HEA2 page header, second line

JINP, KIND, JPAG, LPIC, LINE = range(5) # positions in buf.buffer
    # JINP line index in input file
    # KIND line kind, see before
    # JPAG page number
    # LPIC number of lines in picture
    # LINE content of line

LABL, TITL, JOUT = range(3) # positions in buf.contents and buf.captions
    # LABL chapter label, as '1.' in buf.contents or '1.a.' in buf.captions
    # TITL chapter title
    # JOUT line index in buf.buffer

HORIZTAB = '\t' # horizontal tab, replaced by INDENT in input lines
LINEFEED = '\n' # line separator
CARRIAGE = '\r' # carriage return
FORMFEED = '\f' # first character of first line of page headers
MACRON = '¯' # characters of second line of page headers
ZEROWIDTHSPACE = '\u200b' # character to be removed from input
ZEROWIDTHNONJOINER = '\u200c' # character to be removed from input
ZEROWIDTHJOINER = '\u200d' # character to be removed from input
QUOTES = "'" + '"' # single and double quotation marks
INDENT = 4 * ' ' # standard indentation
MIN_MARGIN = '2cm' # margin < MIN_MARGIN is deprecated
MAX_QUALITY = 5 # max lp/lpr print quality
ROUND = 6 # rounding factor in display of floats
MAX_HIST = 20 # max number of items in history of recent files

YAWP_ROOT = long_path('~/.yawp') # yawp's hidden directory
md(YAWP_ROOT, exist_ok=True) # create if not exists
YAWP_CORR = long_path('~/.yawp/.yawp.corr') # correction file
YAWP_HIST = long_path('~/.yawp/.yawp.hist') # file of history of recent files (GUI mode only)
YAWP_SESS = long_path('~/.yawp/.yawp.sess') # session file containing last text file of previous session (GUI mode only)
YAWP_LOG = new_file('~/.yawp/.yawp.%Y.%m.%d-%H.%M.%S.log') # timestamped log file
YAWP_PDF = local_file('docs/.yawp.pdf') # manual file

SGTS = 16 # PySimpleGUI text size
SGAS = 32 # PySimpleGUI argument size
SGFS = 84 # PySimpleGUI file size
SGBS = 12 # PySimpleGUI button size

BUTTON_TOOLTIP = { # tooltips for buttons in GUI main window
    'New':      'create a new empty text file',
    'Open':     'browse the file system\nto select the text file',
    'Recent':   'browse the list of recent files\nto select the text file',
    'Saveas':   'clone current text file into a target text file',
    'Help':     'browse the yawp-generated YAWP Manual\nthrough the PDF browser defined by -Y',
    'Exit':     "save arguments and finish",
    'Edit':     'edit the text file\nthrough the text editor defined by -y',
    'Format':   'process the text file in Format mode',
    'Noformat': 'process the text file in Noformat mode',
    'Undo':     'restore the text file to its previous content',
    'Log':      'browse the log file\nthrough the text editor defined by -y',
    'Correct':  'manage the correction file\n(edit reset or restore)'}

PAPERSIZE = { # format names for -S --paper-size
    'HALF-LETTER':  '5.5x8.5in',
    'LETTER':       '8.5x11.0in',
    'LEGAL':        '8.5x14.0in',
    'JUNIOR-LEGAL': '5.0x8.0in',
    'LEDGER':       '11.0x17.0in',
    'TABLOID':      '11.0x17.0in',
    'A0':  '841x1189mm',
    'A1':  '594x841mm',
    'A2':  '420x594mm',
    'A3':  '297x420mm',
    'A4':  '210x297mm',
    'A5':  '148x210mm',
    'A6':  '105x148mm',
    'A7':  '74x105mm',
    'A8':  '52x74mm',
    'A9':  '37x52mm',
    'A10': '26x37mm',
    'B0':  '1000x1414mm',
    'B1':  '707x1000mm',
    'B1+': '720x1020mm',
    'B2':  '500x707mm',
    'B2+': '520x720mm',
    'B3':  '353x500mm',
    'B4':  '250x353mm',
    'B5':  '176x250mm',
    'B6':  '125x176mm',
    'B7':  '88x125mm',
    'B8':  '62x88mm',
    'B9':  '44x62mm',
    'B10': '31x44mm'}

CORRECTORS = '''
# ┌────────────────────┐
# │ ~/.yawp/.yawp.corr │
# └────────────────────┘

plm 0mm 6mm # portrait left margin
plm 10mm 16mm
plm 20mm 24mm
plm 30mm 35mm
plm 40mm 43mm
plm 50mm 52mm
plm 60mm 62mm
plm 70mm 72.5mm
plm 80mm 83mm
plm 90mm 92mm
plm 100mm 101mm

llm 0mm 12mm # landscape left margin
llm 5mm 16mm
llm 10mm 20.5mm
llm 20mm 29.5mm
llm 30mm 39mm
llm 40mm 48mm
llm 50mm 57mm
llm 60mm 66.5mm
llm 70mm 75.5mm
llm 80mm 84.5mm
llm 90mm 94mm
llm 100mm 104mm

prm 0mm 8.5mm # portrait right margin
prm 10mm 15mm
prm 20mm 25.5mm
prm 30mm 34.5mm
prm 40mm 44.5mm
prm 50mm 54.5mm
prm 60mm 64.5mm
prm 70mm 72mm
prm 80mm 81mm
prm 90mm 91.5mm
prm 100mm 100mm

lrm 0mm 12mm # landscape left margin
lrm 5mm 17mm
lrm 10mm 22mm
lrm 20mm 30mm
lrm 30mm 40mm
lrm 40mm 49.5mm
lrm 50mm 58mm
lrm 60mm 68mm
lrm 70mm 77.5mm
lrm 80mm 86mm
lrm 90mm 96mm
lrm 100mm 104mm

ptm 0mm 2mm # portrait top margin
ptm 10mm 11.5mm
ptm 20mm 21mm
ptm 30mm 30.5mm
ptm 40mm 39.5mm
ptm 50mm 49mm
ptm 60mm 59mm
ptm 70mm 68mm
ptm 80mm 77.5mm
ptm 90mm 87mm
ptm 100mm 96mm

ltm 0mm 2mm # landscape top margin
ltm 5mm 7mm 
ltm 10mm 11mm
ltm 20mm 20.5mm
ltm 30mm 30mm
ltm 40mm 39mm
ltm 50mm 48.5mm
ltm 60mm 57.5mm
ltm 70mm 67mm
ltm 80mm 76mm
ltm 90mm 85mm
ltm 100mm 95mm

pbm 0mm 16mm # portrait bottom margin
pbm 10mm 24mm
pbm 20mm 34mm
pbm 30mm 43mm
pbm 40mm 52.5mm
pbm 50mm 62mm
pbm 60mm 71mm
pbm 70mm 81mm
pbm 80mm 90mm
pbm 90mm 100mm
pbm 100mm 109.5mm

lbm 0mm 14.5mm # landscape bottom margin
lbm 5mm 19mm
lbm 10mm 24mm
lbm 20mm 32mm
lbm 30mm 42mm
lbm 40mm 52mm
lbm 50mm 60mm
lbm 60mm 70mm
lbm 70mm 80mm
lbm 80mm 88mm
lbm 90mm 99mm
lbm 100mm 107mm

pcw 100mm 94.674mm # portrait character width

lcw 100mm 92.200mm # landscape character width

pch 100mm 94.358mm # portrait character height

lch 100mm 92.647mm # landscape character height
'''

#----- yawp-specific functions -----

def inform(message):
    'information message'
    log.print(message)
    if arg.verbose:
        print(message, file=stderr)

def strfile_inform(strfile, title):
    'information message about a file read as a string'
    inform(title)
    inform(f'    {strfile.count(LINEFEED)+1} lines')
    inform(f'    {len(strfile)} chars')    

def warning(message):
    'warning message'
    inform('WARNING: ' + message)

def error(message, jline=None, line=None):
    'error message'
    message = message[0].upper() + message[1:]
    message = f'ERROR: {message}' if jline is None else f'ERROR: {message}:\nLINE {jline+1}: {line}'
    log.print(message)
    if var.gui:
        print(message, file=stderr)
        raise YawpError(message)
    else:
        log.close()
        exit(message)

def yield_lines(file):
    'yield lines read from a file'
    file = file.strip()
    if not file:
        error(f'text file is undefined')
    file = long_path(file)
    path = dirname(file)
    if not isdir(path):
        error(f'directory {path!r} not found')
    if not exists(file):
        error(f'file {file!r} not found')
    if not isfile(file):
        error(f'file {file!r} exists but is not a file')
    try:
        for line in open(file):
            yield ''.join(INDENT if char == HORIZTAB else '' if ZEROWIDTHSPACE <= char <= ZEROWIDTHJOINER else char for char in line).rstrip()
    except UnicodeDecodeError:
        error(f'file {file!r} is not correctly UTF8-encoded')
    except Exception as exception:
        error(f'{exception} reading file {file!r}')

def get_lock_file(text_file):
    'create a (not timestamped) filename for lock file of text_file'
    if not text_file:
        return ''
    path, name = splitpath(long_path(text_file))
    return normpath(f'{path}/.yawp.{name}.lock')

def get_args_file(text_file):
    'create a (not timestamped) filename for args file of text_file'
    if not text_file:
        return ''
    path, name = splitpath(long_path(text_file))
    return normpath(f'{path}/.yawp.{name}.args')

def get_temp_file(text_file):
    'create a (not timestamped) filename for temp file of text_file'
    if not text_file:
        return ''
    path, name = splitpath(long_path(text_file))
    return normpath(f'{path}/.yawp.{name}.temp')

def new_back_file(text_file):
    'create a timestamped filename for backup file of file'
    if not text_file:
        return ''
    path, name = splitpath(long_path(text_file))
    return new_file(f'{path}/.yawp.{name}.%Y.%m.%d-%H.%M.%S.back')

def old_back_file(text_file):
    "return filename of the newest timestamped backup of file, or raise FileNotFoundError if not found"
    if not text_file:
        return ''
    path, name_ext = splitpath(long_path(text_file))
    return max_file(f'{path}/.yawp.{name_ext}.[2-9][0-9][0-9][0-9].[01][0-9].[0-3][0-9]-[0-2][0-9].[0-5][0-9].[0-5][0-9].back')

def chapter_level(prefix):
    "level of a chapter prefix: '0.' -> 1, '0.0.' -> 2, ..., else -> 0"
    status = 0; level = 0
    for char in prefix:
        if status == 0:
            if char.isdecimal():
                status = 1
            else:
                return 0
        else: # status == 1
            if char.isdecimal():
                pass
            elif char == '.':
                level += 1
                status = 0
            else:
                return 0
    return level if status == 0 else 0

def figure_level(prefix):
    "level of a figure caption: 'x.' -> 1, '0.x.' -> 2, '0.0.x.' -> 3, ..., else -> 0"
    if fnmatchcase(prefix, '[a-z].'):
        return 1
    elif not fnmatchcase(prefix, '*[a-z].'):
        return 0
    else:
        chaplevel = chapter_level(prefix[:-2])
        return 0 if chaplevel == 0 else chaplevel + 1

def page_number(number, page_offset):
    'display page number, possibly by a Roman number'
    return int2roman(number) if number <= -page_offset else str(number + page_offset)

def max_len_page_number(max_number, page_offset):
    'max length of display page numbers from 1 until max_number'
    arab = len(str(max_number + page_offset))
    roma = 0 if page_offset >= 0 else max((len(int2roman(n)) for n in range(min(max_number, -page_offset) + 1)))
    return max(arab, roma)

def ask_yes(title, question, tooltip_yes, tooltip_no=''):
    "show a question (Yes/No) window and return True if 'Yes', False if 'No' or alt-F4 or 'x' button"
    lines = question.split('\n')
    text_width = max(len(line) for line in lines)
    text_height = len(lines)
    layout = [[sg.Text(question, size=(text_width, text_height))],
              [sg.Button('Yes', tooltip=tooltip_yes, size=SGBS),
               sg.Button('No', tooltip=tooltip_no or f"do not {tooltip_yes}", size=SGBS)]]
    return sg.Window(title, layout).read(close=True)[0] == 'Yes'

def ask_ok(button, message):
    "show an error message window, exit by 'OK' or alt-F4 or 'x' button"
    title = f'YAWP - {button} - ERROR'
    lines = message.split('ERROR: ')[-1].split('\n')
    message = '\n'.join(lines)
    text_width = max(SGAS, max(len(line) for line in lines))
    text_height = len(lines)
    layout = [[sg.Text(message, size=(text_width, text_height))],
              [sg.Button('OK', tooltip='go back', size=SGBS)]]
    sg.Window(title, layout).read(close=True)

#----- class YawpError -----

class YawpError(Exception): pass # error control in GUI mode

#----- class Variables -----

class Variables: pass # global not-arguments scalar variables

var = Variables()

#----- class Arguments -----

class Arguments:

    def __init__(arg):
        arg.name_default = {} # {name: default} filled by get__arguments()
        arg.letter_tooltip = {} # {letter: tooltip} button tooltips (argument tooltips added later by get_arguments())
        arg.LETTERS = 'vygwlcifFeEoOnaXYPWASZLRTBKt' # letters in main window, all but radio -p and -C
        arg.BLACKLIST = {'help','view_manual','version','usage_mode','text_file'} # do not read/write from/into args file
        arg.shorts_longs = [] # [(short, long), ...]

    def dump(arg):
        show('arg.__dict__, arg.name_default, arg.letter_tooltip, arg.LETTERS, arg.BLACKLIST')
 
    def read_from_argv(arg, argv):
        parser = ArgumentParser(prog='yawp', formatter_class=RawDescriptionHelpFormatter, description=DESCRIPTION)
        UNITS = ", unit: 'pt' 'in' 'mm' or 'cm'"
        #
        def varg(short, long, version):
            'version argument'
            # no need for arg.name_default arg.letter_tooltip arg.letters arg shorts_longs
            parser.add_argument(short, long, action='version', version=VERSION)
        #
        def barg(short, long, help):
            'boolean argument'
            name = long[2:].replace('-','_')
            arg.name_default[name] = False
            letter = short[1]
            tooltip = help.replace(' (','\n(').replace(', ',',\n')
            arg.letter_tooltip[letter] = tooltip
            help=help.replace('%','%%')
            parser.add_argument(short, long, action='store_true', help=help)
            arg.shorts_longs.append((short, long))
        #
        def sarg(short, long, default, help, note=''):
            'string argument'
            name = long[2:].replace('-','_')
            arg.name_default[name] = default
            letter = short[1]
            help = f"{help} (default: {default!r}{note})"
            tooltip = help.replace(' (','\n(').replace(', ',',\n')
            arg.letter_tooltip[letter] = tooltip
            help=help.replace('%','%%')
            parser.add_argument(short, long, default=default, help=help)
            arg.shorts_longs.append((short, long))
        #
        def parg(name, nargs, help):
            'positional argument'
            arg.name_default[name] = ''
            letter = name[0]
            tooltip = help.replace(' (','\n(').replace(', ',',\n')
            arg.letter_tooltip[letter] = tooltip
            help=help.replace('%','%%')
            parser.add_argument(name, nargs=nargs, help=help)
            arg.shorts_longs.append(('', name))
        #
        # usage arguments
        barg('-H', '--view-manual',     'browse the yawp-generated PDF Yawp Manual and exit')
        varg('-V', '--version',         'yawp' + VERSION)
        barg('-v', '--verbose',         'write all messages on stderr (default: write errors only)')
        sarg('-M', '--usage-mode',      'g', "run yawp in this usage mode", " = GUI, 'e' = Edit, 'f' = Format, 'n' = Noformat, 'U' = undo")
        # format arguments
        sarg('-y', '--text-editor',     'idle', "editor for text files")
        barg('-g', '--graphics',        "redraw '`'-segments and '^'-arrowheads")
        sarg('-w', '--chars-per-line',  '0', 'line width in characters per line', ' = automatic')
        barg('-l', '--just-left-only',  'justify text lines at left only (default: at left and right)')
        sarg('-c', '--contents-title',  'contents', "title of contents chapter")
        sarg('-i', '--index-title',     'index', "title of index chapter")
        sarg('-f', '--figures-title',   'figures', "title of figures chapter")
        sarg('-F', '--caption-prefix',  'figure', "first word of figure captions")
        # paging arguments:
        sarg('-p', '--page-headers',    'n', "insert page headers", " = no, 'f' = on full page, 'p' = and on broken pictures, 'c' = and on level-1 chapters")
        sarg('-e', '--even-left',       '%n/%N', "headers of even pages, left")
        sarg('-E', '--even-right',      '%F %Y-%m-%d', "headers of even pages, right")
        sarg('-o', '--odd-left', '%c',  "headers of odd pages, left")
        sarg('-O', '--odd-right',       '%n/%N', "headers of odd pages, right")
        sarg('-n', '--page-offset',     '0', 'offset of page numbers', ", min: '-3999', if negative it is count of initial Roman numbers")
        barg('-a', '--all-pages-E-e',   "put in all page headers -E at left and -e at right")
        # export arguments
        barg('-X', '--export-view-pdf', "after processing export and browse PDF file")
        sarg('-Y', '--pdf-browser',     'xdg-open', "browser for PDF files")
        sarg('-P', '--pdf-file',        '%f.pdf', "exported PDF file")
        sarg('-W', '--char-width',      '0', "character width", " = automatic" + UNITS)
        sarg('-A', '--char-aspect',     '3/5', "character aspect ratio = char width / char height", ", '1' = square grid")
        sarg('-S', '--paper-size',      'A4', "portrait paper size width x height", " = '210x297mm'" + UNITS)
        barg('-Z', '--landscape',       "turn page by 90 degrees (default: portrait)")
        sarg('-L', '--left-margin',     '2cm', "left margin", UNITS)
        sarg('-R', '--right-margin',    '2cm', "right margin", UNITS)
        sarg('-T', '--top-margin',      '2cm', "top margin", UNITS)
        sarg('-B', '--bottom-margin',   '2cm', "bottom margin", UNITS)
        sarg('-C', '--correct-sizes',   'd', "correct character size and page margins", " = by default values, 'n' = no, 'f' = by correction file")
        barg('-K', '--fake-margins',    'get left margin by blanks and top margin by empty lines')
        # file argument
        parg('text_file', '?', 'text file to be processed, ASCII or UTF8-encoded')
        # arguments ──▷ arg.*
        parser.parse_args(argv[1:], arg)
        # text_file
        arg.text_file = long_path(arg.text_file or '') # None ──▷ ''
        # -h is managed by ArgumentParser
        # -V is managed by ArgumentParser
        # -H
        if arg.view_manual:
            arg.check_pdf_browser()
            shell(f'{arg.pdf_browser} {YAWP_PDF}')
            exit(0)
        # -M
        if arg.usage_mode not in set('gefnu'):
            error(f"wrong -M {arg.usage_mode!r}, it must be 'g' 'e' 'f' 'n' or 'u'")    
        # text_file
        arg.text_file = (arg.text_file or '').strip()
        if arg.usage_mode == 'g': # text_file optional, other arguments forbidden
            if len(argv) != 1 + bool(arg.text_file):
                error(f"in GUI mode no argument is allowed, except possibly text_file")
            if not arg.text_file:
                arg.read_text_file_from_sess_file(YAWP_SESS)
        else:
            if not arg.text_file: # text_file mandatory, other arguments optional
                error(f'in CLI mode (-M {arg.usage_mode!r}) the text_file argument is mandatory')
        if arg.text_file:        
            dir_of_text_file = dirname(arg.text_file)
            if not isdir(dir_of_text_file):
                error(f'path {dir_of_text_file!r} of text_file {arg.text_file!r} not found')
            if exists(arg.text_file) and not isfile(arg.text_file):
                error(f'text_file {arg.text_file!r} exists but is not a file')
            if not isfile(arg.text_file):
                if arg.usage_mode == 'e':
                    open(arg.text_file, 'w').write('')
                elif arg.usage_mode == 'u': 
                    pass
                else:
                    error(f'text_file {arg.text_file!r} not found')
        arg.open_text_file(arg.text_file)

    def inform(arg):
        inform('Arguments:')
        inform('    -h --help = False')
        inform('    -V --version = False')
        for short, long in arg.shorts_longs:
            name = long.replace('--','').replace('-','_')
            value = eval(name, arg.__dict__, arg.__dict__)
            inform(f'    {short} {long} = {value!r}')
            
    def read_from_args_file_of(arg, text_file):
        arg.set_default()
        if text_file:
            args_file = get_args_file(text_file)
            if isfile(args_file):
                lines = list(yield_lines(args_file))
                try:
                    for jline, line in enumerate(lines):
                        line = line.split('#')[0].strip()
                        if line:
                            name, value = line.split('=')
                            name = name.strip()
                            if name in arg.name_default and name not in arg.BLACKLIST:
                                setattr(arg, name, eval(value.strip(), {}, {}))
                except:
                    error(f'in argument file, syntax error', jline, line)

    def write_into_args_file_of(arg, text_file):
        if text_file:
            args_file = get_args_file(text_file)
            with open(args_file, 'w') as output:
                for name in sorted(arg.name_default.keys()):
                    if name not in arg.BLACKLIST:
                        print(f'{name} = {getattr(arg, name)!r}', file=output)

    def read_text_file_from_sess_file(arg, sess_file):
        arg.text_file = ''
        if isfile(sess_file):
            text_file = long_path(open(sess_file).read())
            if isfile(text_file):
                arg.text_file = text_file

    def write_text_file_into_sess_file(arg, sess_file):
        open(sess_file, 'w').write(arg.text_file)

    def read_from_window(arg, window):
        (arg.verbose, arg.text_editor, arg.graphics, arg.chars_per_line, arg.just_left_only,
         arg.contents_title, arg.index_title, arg.figures_title, arg.caption_prefix,
         arg.even_left, arg.even_right, arg.odd_left, arg.odd_right, arg.page_offset, arg.all_pages_E_e,
         arg.export_view_pdf, arg.pdf_browser, arg.pdf_file, arg.char_width, arg.char_aspect, arg.paper_size, arg.landscape,
         arg.left_margin, arg.right_margin, arg.top_margin, arg.bottom_margin, arg.fake_margins, arg.text_file) = [
             window[char].get() for char in arg.LETTERS]
        arg.page_headers = get_radio(window, 0, 'nfpc')
        arg.correct_sizes = get_radio(window, 4, 'ndf')

    def write_into_window(arg, window):
        for letter, value in zip(arg.LETTERS,
            (arg.verbose, arg.text_editor, arg.graphics, arg.chars_per_line, arg.just_left_only,
             arg.contents_title, arg.index_title, arg.figures_title, arg.caption_prefix,
             arg.even_left, arg.even_right, arg.odd_left, arg.odd_right, arg.page_offset, arg.all_pages_E_e,
             arg.export_view_pdf, arg.pdf_browser, arg.pdf_file, arg.char_width, arg.char_aspect, arg.paper_size, arg.landscape,
             arg.left_margin, arg.right_margin, arg.top_margin, arg.bottom_margin, arg.fake_margins, arg.text_file)
            ): window[letter].update(value)
        put_radio(window, 0, 'nfpc', arg.page_headers)
        put_radio(window, 4, 'ndf', arg.correct_sizes)
        window.refresh()

    def set_default(arg):
        for name, default in arg.name_default.items():
            if name not in arg.BLACKLIST:
                setattr(arg, name, default)

    def set_default_if_empty(arg):
        for name, default in arg.name_default.items():
            if name not in arg.BLACKLIST:
                value = getattr(arg, name)
                if isinstance(value, str) and not value.strip():
                    setattr(arg, name, default)

    def print(arg):
        for name, default in sorted(arg.name_default.items()):
            print(f'{name} = {getattr(arg, name)!r} # default = {default!r}')

    def check(arg):
        arg.inform()
        # -y
        arg.check_text_editor()
        # -w
        try:
            var.chars_per_line = int(arg.chars_per_line)
            assert var.chars_per_line >= 0
        except (ValueError, AssertionError):
            error(f'Wrong -w --chars-per-line {arg.chars_per_line!r}, it must be an integer ≥ 0')
        # -c
        var.contents_title = unqupper(shrink(arg. contents_title))
        if not var.contents_title:
            error(f"wrong -c --contents-title '', it cannot be empty")
        # -i
        var.index_title = unqupper(shrink(arg. index_title))
        if not var.index_title:
            error(f"wrong -i --index-title '', it cannot be empty")
        # -f
        var.figures_title = unqupper(shrink(arg. figures_title))
        if not var.figures_title:
            error(f"wrong -f --figures-title '', it cannot be empty")
        # -c -i -f
        if len(set([var.contents_title, var.index_title, var.figures_title])) < 3:
            error(f'Wrong -c -i -f, they must be all different')
        # -F
        var.caption_prefix = unqupper(shrink(arg. caption_prefix))
        if not var.caption_prefix:
            error(f"wrong -F --caption-prefix '', it cannot be empty")
        if ' ' in var.caption_prefix:
            error(f"wrong -F --caption-prefix {arg.caption_prefix!r}, it cannot contain blanks")
        # -p
        if arg.page_headers not in list('nfpc'):
            error(f"wrong -p --page-headers {arg.page_headers!r}, it must be 'n' 'f' 'p' or 'c'")
        # -e
        try:
            evalchar(arg.even_left, 'PpfFeYmdHMSnNc', 'PpfFeYmdHMSnNc', '%')
        except ValueError as illegal:
            error(f'Wrong -e --even-left {arg.even_left!r}, illegal {str(illegal)!r}')
        # -E
        try:
            evalchar(arg.even_right, 'PpfFeYmdHMSnNc', 'PpfFeYmdHMSnNc', '%')
        except ValueError as illegal:
            error(f'Wrong -E --even-right {arg.even_right!r}, illegal {str(illegal)!r}')
        # -o
        try:
            evalchar(arg.odd_left, 'PpfFeYmdHMSnNc', 'PpfFeYmdHMSnNc', '%')
        except ValueError as illegal:
            error(f'Wrong -o --odd-left {arg.odd_left!r}, illegal {str(illegal)!r}')
        # -O
        try:
            evalchar(arg.odd_right, 'PpfFeYmdHMSnNc', 'PpfFeYmdHMSnNc', '%')
        except ValueError as illegal:
            error(f'Wrong -O --odd-right {arg.odd_right!r}, illegal {str(illegal)!r}')
        # -n
        try:
            var.page_offset = int(arg.page_offset)
            assert var.page_offset >= -3999
        except (ValueError, AssertionError):
            error(f'Wrong -n --page-offset {arg.page_offset!r}, it must be an integer ≥ -3999')
        # -Y
        arg.check_pdf_browser()
        # -P
        try:
            evalchar(arg.pdf_file, 'PpfFeYmdHMS', 'PpfFeYmdHMS', '%')
        except ValueError as illegal:
            error(f'Wrong -P --file-pdf {arg.pdf_file!r}, illegal {str(illegal)!r}')
        if not arg.pdf_file.endswith('.pdf'):
            error(f"wrong -P --file-pdf {arg.pdf_file!r}, not ending with '.pdf'")
        # -W
        try:
            var.char_width = str2inch(arg.char_width)
            assert var.char_width >= 0.0
        except (ValueError, AssertionError):
            error(f"wrong -W --char-width {arg.char_width!r}, it must be zero (as '0' or 0.0')\nor value + 'in'/'pt'/'cm'/'mm' (as '0.5pt'), value ≥ 0")
        # -A
        try:
            var.char_aspect = ratio(arg.char_aspect)
        except ValueError:
            error(f"wrong -A --char-aspect {arg.char_aspect!r}, it must be a value (as '0.6')\nor value1 + '/' + value2 (as '3/5'), values > 0")
        # -S
        try:
            var.paper_width, var.paper_height = str2inxin(PAPERSIZE.get(arg.paper_size.upper(), arg.paper_size))
            assert 0.0 < var.paper_width <= var.paper_height
        except (ValueError, AssertionError):
            error(f"wrong -S --paper-size {arg.paper_size!r}, it must be a paper format name (as 'A4')\nor width + 'x' + height + 'in'/'pt'/'cm'/'mm' (as '210x297mm'), 0 < width ≤ height")
        # -Z
        if arg.landscape:
            var.paper_width, var.paper_height = var.paper_height, var.paper_width
        # -L
        min_margin = str2inch(MIN_MARGIN)
        try:
            var.left_margin = str2inch(arg.left_margin)
        except ValueError:
            error(f"wrong -L --left-margin {arg.left_margin!r}, it must be float + 'in'/'pt'/'cm'/'mm', value ≥ '0'")
        if var.left_margin < min_margin:
            warning(f"-L --left-margin {arg.left_margin!r} < {MIN_MARGIN}, it may give unexpected results")
        # -R
        try:
            var.right_margin = str2inch(arg.right_margin)
        except ValueError:
            error(f"wrong -R --right-margin {arg.right_margin!r}, it must be float + 'in'/'pt'/'cm'/'mm', value ≥ '0'")
        if var.left_margin < min_margin:
            warning(f"-L --left-margin {arg.left_margin!r} < {MIN_MARGIN}, it may give unexpected results")
        # -T
        try:
            var.top_margin = str2inch(arg.top_margin)
        except ValueError:
            error(f"wrong -T --top-margin {arg.top_margin!r}, it must be float + 'in'/'pt'/'cm'/'mm', value ≥ '0'")
        if var.top_margin < min_margin:
            warning(f"-L --top-margin {arg.top_margin!r} < {MIN_MARGIN}, it may give unexpected results")
        # -B
        try:
            var.bottom_margin = str2inch(arg.bottom_margin)
        except ValueError:
            error(f"wrong -B --bottom-margin {arg.bottom_margin!r}, it must be float + 'in'/'pt'/'cm'/'mm', value ≥ '0'")
        if var.left_margin < min_margin:
            warning(f"-L --left-margin {arg.left_margin!r} < {MIN_MARGIN}, it may give unexpected results")
        # -C
        if arg.correct_sizes not in list('ndf'):
            error(f"wrong -C --correct-sizes {arg.correct_sizes!r}, it must be 'n' 'd' or 'f'")

    def check_text_file(arg, must_exist=True):
        arg.text_file = (arg.text_file or '').strip()
        if not arg.text_file:
            error('text file is undefined')
        arg.text_file = long_path(arg.text_file)
        path = dirname(arg.text_file)
        if not isdir(path):
            error('directory {path!r} of text file {arg.text_file!r} not found')
        if exists(arg.text_file) and not isfile(arg.text_file):
            error('text file {arg.text_file!r} exists but is not a file')
        if must_exist and not exists(arg.text_file):
            error('text file {arg.text_file!r} not found')

    def check_text_editor(arg):
        if not command_exists(arg.text_editor):
            error(f'Wrong -y --text-editor {arg.text_editor!r}, command not found')

    def check_pdf_browser(arg):
        if not command_exists(arg.pdf_browser):
            error(f'Wrong -Y --pdf-browser {arg.pdf_browser!r}, command not found')
            
    def open_text_file(arg, new_text_file):
        new_text_file = long_path(new_text_file or '')
        if isfile(new_text_file):
            arg.text_file = new_text_file
            lock.seize(arg.text_file)
            hist.add(arg.text_file)
            if arg.usage_mode == 'g':
                arg.read_from_args_file_of(arg.text_file)
            var.PpfFeYmdHMS = get_PpfFeYmdHMS(arg.text_file)
            cd(dirname(arg.text_file))

    def close_text_file(arg):
        if isfile(arg.text_file):
            arg.write_into_args_file_of(arg.text_file)
            lock.release(arg.text_file)
            
    def swap_text_file(arg, new_text_file):
        arg.close_text_file()
        arg.open_text_file(new_text_file)

arg = Arguments()

#----- class History -----

class History:

    def __init__(hist, max_files, file):
        hist.max_files = max_files
        hist.file = long_path(file)
        hist.files = []
 
    def read(hist):
        if isfile(hist.file):
            hist.files = [file.strip() for file in yield_lines(hist.file) if isfile(file.strip())]
        else:
            hist.files = []

    def write(hist):
        open(hist.file, 'w').write('\n'.join(unique([file.strip() for file in hist.files if file.strip() and isfile(file.strip())])[:hist.max_files]))

    def clear(hist):
        open(hist.file, 'w').write('')

    def add(hist, file):
        if arg.usage_mode == 'g' and isfile(file):
            hist.read()
            if not (hist.files and hist.files[0] == file):
                hist.files = [file] + hist.files
                hist.write()

    def select(hist):
        hist.read()
        if not hist.files:
            error(f'list of recent files is empty')
        layout = [[sg.Text(f'{jfile+1:2}.'), sg.Button(file, size=0, tooltip='select this file as the text file to be processed')] for jfile, file in enumerate(hist.files)] + [
            [sg.Button('Clear', size=SGBS, tooltip='clear the list of recent files'),
             sg.Button('Cancel', size=SGBS, tooltip='exit with no selection')]]
        window = sg.Window(f'YAWP - Recent', layout)
        while True:
            event, values = window.read()
            if event in [None, 'Cancel']:
                window.close()
                return None
            elif event == 'Clear':
                if ask_yes('YAWP - Recent', 'History of recent text files will be lost\nDo you want to clear history?', 'clear'):
                    hist.clear()
                    var.ok_message = ', list of recent files is empty'
                    window.close()
                    return ''
                else:
                    continue
            else:
                file = event
                if not (hist.files and hist.files[0] == file):
                    hist.files = [file] + hist.files
                    hist.write()
                window.close()
                return file

hist = History(MAX_HIST, YAWP_HIST)

#----- class Log -----

class Log:

    def __init__(log):
        log.output = None

    def open(log):
        log.output = open(YAWP_LOG, 'w')

    def print(log, line):
        print(line, file=log.output)

    def close(log):
        log.output.close()
        log.output = None

    def reopen(log):
        log.output = open(YAWP_LOG, 'a')

    def browse(log):
        log.close()
        shell(f'{arg.text_editor} {YAWP_LOG}')
        log.reopen()

log = Log()

#----- class Lock -----

class Lock:

    def __init__(lock):
        lock.files = set()

    def seize(lock, file):
        if isfile(file):
            lock_file = get_lock_file(file)
            if isfile(lock_file):
                if open(lock_file).read() == YAWP_LOG: # file is already locked by me
                    return
                else: # file is already locked by another YAWP instance
                    error(f'file {file!r} is locked by another YAWP instance')
            else: # file is not locked, lock it
                open(lock_file, 'w').write(YAWP_LOG)
                lock.files.add(file)

    def release(lock, file):
        if file in lock.files:
            lock_file = get_lock_file(file)
            if isfile(lock_file) and open(lock_file).read() == YAWP_LOG:
                rm(lock_file)
                lock.files.remove(file)

lock = Lock()

#----- class Paragraph -----

class Paragraph:

    def __init__(par):
        par.string = ''
        par.jinp = 0
        par.indent = 0

    def assign(par, string, jinp, indent):
        assert not par.string
        par.string = shrink(string)
        par.jinp = jinp
        par.indent = indent
        if indent > var.chars_per_line // 2:
            error(f"indent of indented paragraph = {indent} > -w / 2 = {var.chars_per_line // 2}", jinp, '• ' + string)

    def append(par, string):
        assert par.string
        par.string += ' ' + shrink(string)

    def flush(par, buffer2):
        if not par.string:
            return
        prefix = (par.indent - 2) * ' ' + '• ' if par.indent else ''
        while len(par.string) > var.chars_per_line - par.indent:
            jchar = rfind(par.string[:var.chars_per_line-par.indent+1], ' ')
            if jchar <= 0:
                error(f'impossible to left-justify', par.jinp, par.string)
            string, par.string = par.string[:jchar], par.string[jchar+1:]
            if not arg.just_left_only:
                try:
                    string = expand(string, var.chars_per_line - par.indent)
                except ValueError:
                    error(f'impossible to right-justify', par.jinp, string)
            buffer2.append([par.jinp, TEXT, 0, 0, prefix + string])
            prefix = par.indent * ' '
        if  par.string:
            buffer2.append([par.jinp, TEXT, 0, 0, prefix + par.string])
            par.string = ''

par = Paragraph()

#----- class Correction -----

class Correction:

    def __init__(corr):
        corr.points = {k: [] for k in 'plm llm prm lrm ptm ltm pbm lbm pcw lcw pch lch'.split()}
        # read correction points from YAWP_CORR
        if arg.correct_sizes != 'n':
            for jline, line in enumerate(yield_lines(YAWP_CORR) if arg.correct_sizes == 'f' else CORRECTORS.split('\n')):
                stmt = line.split('#')[0].strip()
                if stmt:
                    kyx = stmt.split()
                    if len(kyx) != 3:
                        error(f'in correction file, found {len(kyx)} values instead of 3', jline, line)
                    k, sy, sx = kyx
                    if k not in corr.points:
                        error(f'in correction file, wrong key {k!r}', jline, line)
                    try:
                        x = str2inch(sx)
                        assert x >= 0.0 and (not corr.points[k] or x > corr.points[k][-1][0])
                    except (ValueError, AssertionError):
                        error(f'in correction file, wrong x-value {sx!r}, must be ', jline, line)
                    try:
                        y = str2inch(sy)
                        assert y >= 0.0 and (not corr.points[k] or x > corr.points[k][-1][1]) 
                    except (ValueError, AssertionError):
                        error(f'in correction file, wrong y-value {sy!r}', jline, line)
                    corr.points[k].append((x, y))
            for k in 'plm llm prm lrm ptm ltm pbm lbm pcw lcw pch lch'.split():
                corr.points[k].sort()
        # nonprintable borders in paper sheet
        var.left_border =   [corr.points['plm'][0][0] if corr.points['plm'] and corr.points['plm'][0][1] == 0.0 else 0.0,
                             corr.points['llm'][0][0] if corr.points['llm'] and corr.points['llm'][0][1] == 0.0 else 0.0]
        var.right_border =  [corr.points['prm'][0][0] if corr.points['prm'] and corr.points['prm'][0][1] == 0.0 else 0.0,
                             corr.points['lrm'][0][0] if corr.points['lrm'] and corr.points['lrm'][0][1] == 0.0 else 0.0]
        var.top_border =    [corr.points['ptm'][0][0] if corr.points['ptm'] and corr.points['ptm'][0][1] == 0.0 else 0.0,
                             corr.points['ltm'][0][0] if corr.points['ltm'] and corr.points['ltm'][0][1] == 0.0 else 0.0]
        var.bottom_border = [corr.points['pbm'][0][0] if corr.points['pbm'] and corr.points['pbm'][0][1] == 0.0 else 0.0,
                             corr.points['lbm'][0][0] if corr.points['lbm'] and corr.points['lbm'][0][1] == 0.0 else 0.0]
        
#----- class Pdf -----

class Pdf:

    def text2temp(pdf, text_file, temp_file, left_blanks, top_lines):
        'copy text_file into temp_file, adding left_blanks blanks and top_lines LINEFEED'
        assert text_file != temp_file
        left_string = left_blanks * ' '
        top_string = top_lines * LINEFEED
        with open(temp_file, 'w') as temp:
            print(top_string, file=temp)
            for jline, line in enumerate(open(text_file)):
                line = line.rstrip()
                if (arg.page_headers == 'n'):
                    if jline and (jline % var.lines_per_page == 0):
                        print(FORMFEED + top_string, end='', file=temp)
                else:
                    if line.startswith(FORMFEED):
                        print(FORMFEED + top_string, end='', file=temp)
                        line = line[1:]
                print(left_string + line, file=temp)

    def text2pdf(pdf, text_file, pdf_file=None, left=0, right=0, top=0, bottom=0):
        '''export text_file into pdf_file and return pdf_file name,
        if pdf_file is None return original ~/PDF/*.pdf written by lpr'''
        shell(f'lpr -P PDF ' # export
              f'-o print-quality={MAX_QUALITY} '
              f'-o media=Custom.{in2pt(var.paper_width)}x{in2pt(var.paper_height)} '
              f'-o cpi={var.chars_per_inch2} '
              f'-o lpi={var.lines_per_inch2} '
              f'-o page-top={in2pt(top)} '
              f'-o page-left={in2pt(left)} '
              f'-o page-right={in2pt(right)} '
              f'-o page-bottom={in2pt(bottom)} '
              f'{text_file!r}')
        while any(line.startswith('active') for line in shell(f'lpq -P PDF')): # wait lp completion
            sleep(0.1)
        sleep(1)
        pattern = '~/PDF/.*.pdf' if basename(text_file).startswith('.') else '~/PDF/*.pdf' # hidden or not
        try:
            last_pdf = last_file(pattern) # seek the most recent one
        except FileNotFoundError:
            error(f'exported PDF file not found')
        if pdf_file is None:
            return last_pdf
        else:
            mv(last_pdf, pdf_file)
            return pdf_file

    def pdfpdf2pdf(pdf, even_pdf_file, odd_pdf_file, pdf_file):
        'merge even pages from even_pdf_file with odd pages from odd_pdf_file into pdf_file'
        even_pages = PdfReader(even_pdf_file).pages
        odd_pages = PdfReader(odd_pdf_file).pages
        pdf_writer = PdfWriter()
        for jpage, (even_page, odd_page) in enumerate(zip(even_pages, odd_pages)):
            pdf_writer.addpage(even_page if jpage % 2 else odd_page)
        pdf_writer.write(var.pdf_file)

    def export_and_browse(pdf, text_file):
        var.pdf_file = long_path(evalchar(arg.pdf_file, 'PpfFeYmdHMS', var.PpfFeYmdHMS, '%'))
        if not isdir(dirname(var.pdf_file)):
            error(f'Wrong -P --file-pdf {arg.pdf_file!r}, directory {dirname(var.pdf_file)!r} not found')
        if isfile(var.pdf_file):
            rm(var.pdf_file)
        if var.left_margin == var.right_margin or arg.all_pages_E_e: # export directly into var.pdf_file
            if arg.fake_margins: # text -> temp -> pdf
                temp_file = get_temp_file(arg.text_file)
                pdf.text2temp(arg.text_file, temp_file, var.left_blanks, var.top_lines)
                pdf.text2pdf(temp_file, var.pdf_file)
                rm(temp_file)
            else:                # text -> pdf
                pdf.text2pdf(arg.text_file, var.pdf_file, left=var.left_margin2, right=var.right_margin2, top=var.top_margin2, bottom=var.bottom_margin2)
        else: # export into var.pdf_file through even_pdf_file and odd_pdf_file
            if arg.fake_margins: # text -> temp -> even; text -> temp -> odd; even, odd -> pdf
                temp_file = get_temp_file(arg.text_file)
                pdf.text2temp(arg.text_file, temp_file, var.left_blanks, var.top_lines)
                even_pdf_file = pdf.text2pdf(temp_file)
                pdf.text2temp(arg.text_file, temp_file, var.right_blanks, var.top_lines)
                odd_pdf_file = pdf.text2pdf(temp_file)
                rm(temp_file)
                pdf.pdfpdf2pdf(even_pdf_file, odd_pdf_file, var.pdf_file)
            else:                # text -> even; text -> odd; even, odd -> pdf
                even_pdf_file = pdf.text2pdf(arg.text_file, left=var.left_margin2, right=var.right_margin2, top=var.top_margin2, bottom=var.bottom_margin2)
                odd_pdf_file = pdf.text2pdf(arg.text_file, left=var.left_margin3, right=var.right_margin3, top=var.top_margin2, bottom=var.bottom_margin2)
                pdf.pdfpdf2pdf(even_pdf_file, odd_pdf_file, var.pdf_file)
        inform(f'Export:  {arg.text_file!r} ──▷')
        inform(f'         {var.pdf_file!r}')
        shell(f'{arg.pdf_browser} {var.pdf_file!r}') # browse

pdf = Pdf()

#----- class Buffer -----

class Buffer:

    def __init__(buf, file=None):
        buf.buffer = [] # [[jinp, kind, jpag, lpic, line]] # output buffer
        # jinp: line index in buf.input
        # kind: kind of line: CODE, TEXT, PICT, CONT, INDX, FIGU, CHP1, CHP2, HEA1, HEA2
        # jpag: page number
        # lpic: lines in picture (in first line of pictures only, else 0)
        # line
        buf.contents = [] # [[pref, titl, jout]], if words == line.split():
        # pref: words[0], chapter numbering as '1.', '1.1.'...
        # titl: ' '.join(words[1:])
        # jout: position of chapter line in buf.buffer
        buf.contents_found = False # file contains a contents chapter line?
        buf.contents_jout = -1 # position of contents chapter line in output
        buf.qsub_jouts = SetDict() # {subject: {jout}}
        # subject: subject between double quotes
        # jout: position of subject in buf.buffer
        buf.uqsub_jouts = SetDict() # {subject: {jout}}
        # subject: subject not between double quotes
        # jout: position of subject in buf.buffer
        buf.index_found = False # file contains an index chapter line?
        buf.index_jout = -1 # position of index chapter line in output
        buf.subjects = set()
        buf.figures_found = False # file contains a figures chapter line?
        buf.figures_jout = -1 # position  of figures chapter line in buf.buffer
        buf.figures = [] # [[pref, titl, jout]] , if words == line.split() ...
        # words[0] == var.figures_title
        # pref: words[1], figure numbering as 'a.', '1.b.', '1.1.c.'...
        # titl: ' '.join(words[2:])
        # jout: position of caption line in buf.buffer
        buf.head_num_lines, buf.head_chars, buf.head_words, buf.head_max_chars_per_line, buf.num_pages = 0, 0, 0, 0, 1
        buf.body_num_lines, buf.body_chars, buf.body_words, buf.body_max_chars_per_line = 0, 0, 0, 0
        if file:
            buf.read_from_file(file)

    def read_from_file(buf, file):
        buf.buffer = []
        buf.head_num_lines, buf.head_chars, buf.head_words, buf.head_max_chars_per_line, buf.num_pages = 0, 0, 0, 0, 1
        buf.body_num_lines, buf.body_chars, buf.body_words, buf.body_max_chars_per_line = 0, 0, 0, 0
        for jinp, line in enumerate(yield_lines(file)):
            buf.buffer.append([jinp, PICT, 1, 0, line])
            if line.startswith(FORMFEED):
                buf.head_chars += len(line) - 1
                buf.head_words += len(line[1:].split())
                buf.head_max_chars_per_line = max(buf.head_max_chars_per_line, len(line) - 1)
                buf.head_num_lines += 1
                buf.num_pages += 1
            elif line.startswith(MACRON):
                buf.head_chars += len(line)
                buf.head_words += len(line.split())
                buf.head_max_chars_per_line = max(buf.head_max_chars_per_line, len(line))
                buf.head_num_lines += 1
            else:
                buf.body_chars += len(line)
                buf.body_words += len(line.split())
                buf.body_max_chars_per_line = max(buf.body_max_chars_per_line, len(line))
                buf.body_num_lines += 1
           
    def write_into_file(buf, file):
        buf.head_num_lines, buf.head_chars, buf.head_words, buf.head_max_chars_per_line, buf.num_pages = 0, 0, 0, 0, 1
        buf.body_num_lines, buf.body_chars, buf.body_words, buf.body_max_chars_per_line = 0, 0, 0, 0
        with open(file, 'w') as file_w:
            for reco in buf.buffer:
                line = reco[LINE]
                print(line, file=file_w)
                if line.startswith(FORMFEED):
                    buf.head_chars += len(line) - 1
                    buf.head_words += len(line[1:].split())
                    buf.head_max_chars_per_line = max(buf.head_max_chars_per_line, len(line) - 1)
                    buf.head_num_lines += 1
                    buf.num_pages += 1
                elif line.startswith(MACRON):
                    buf.head_chars += len(line)
                    buf.head_words += len(line.split())
                    buf.head_max_chars_per_line = max(buf.head_max_chars_per_line, len(line))
                    buf.head_num_lines += 1
                else:
                    buf.body_chars += len(line)
                    buf.body_words += len(line.split())
                    buf.body_max_chars_per_line = max(buf.body_max_chars_per_line, len(line))
                    buf.body_num_lines += 1

    def copy(buf):
        buf2 = Buffer()
        buf.head_num_lines, buf.head_chars, buf.head_words, buf.head_max_chars_per_line, buf.num_pages = 0, 0, 0, 0, 1
        buf.body_num_lines, buf.body_chars, buf.body_words, buf.body_max_chars_per_line = 0, 0, 0, 0
        for reco in buf.buffer:
            rec2 = reco[:] # deep copy
            buf2.buffer.append(rec2)
            line = rec2[LINE]
            if line.startswith(FORMFEED):
                buf.head_chars += len(line) - 1
                buf.head_words += len(line[1:].split())
                buf.head_max_chars_per_line = max(buf.head_max_chars_per_line, len(line) - 1)
                buf.head_num_lines += 1
                buf.num_pages += 1
            elif line.startswith(MACRON):
                buf.head_chars += len(line)
                buf.head_words += len(line.split())
                buf.head_max_chars_per_line = max(buf.head_max_chars_per_line, len(line))
                buf.head_num_lines += 1
            else:
                buf.body_chars += len(line)
                buf.body_words += len(line.split())
                buf.body_max_chars_per_line = max(buf.body_max_chars_per_line, len(line))
                buf.body_num_lines += 1
        return buf2

    def inform(buf, title):
        'write informations about buf after last buf.read_from_file() or last buf.write_into_file() or buf.copy()'
        inform(title)
        inform(f"    header: {plural(buf.head_num_lines, 'line')}, "
               f"{plural(buf.head_words, 'word')}, {plural(buf.head_chars, 'char')}, "
               f"max {plural(buf.head_max_chars_per_line, 'char')} per line, {plural(buf.num_pages, 'page')}")
        inform(f"    body:   {plural(buf.body_num_lines, 'line')}, "
               f"{plural(buf.body_words, 'word')}, {plural(buf.body_chars, 'char')}, "
               f"max {plural(buf.body_max_chars_per_line, 'char')} per line")
        inform(f"    total:  {plural(buf.head_num_lines + buf.body_num_lines, 'line')}, "
               f"{plural(buf.head_words+buf.body_words, 'word')}, {plural(buf.head_chars+buf.body_chars, 'char')}, "
               f"max {plural(max(buf.head_max_chars_per_line, buf.body_max_chars_per_line), 'char')} per line")

    def __eq__(buf, buf2):
        return len(buf.buffer) == len(buf2.buffer) and all(record[LINE] == record2[LINE] for record, record2 in zip(buf.buffer, buf2.buffer))

    def char(buf, jout, jchar):
        "return buf.buffer[jout][LINE][jchar], if not PICT or on IndexError return '*', used by redraw_segments() and redraw_arroheads()"
        if jout < 0 or jchar < 0:
            return '*'
        else:
            try:
                line = buf.buffer[jout][LINE]
                return line[jchar] if buf.buffer[jout][KIND] == PICT else '*'
            except IndexError:
                return '*'

    def compute_and_correct_sizes(buf):
        if buf.body_max_chars_per_line == 0:
            error(f'text file is empty')
        # set correction parameters depending on arg.correct_sizes
        corr = Correction()
        # free space
        inform(f'Compute: page width {inch2str(var.paper_width, ROUND)}')
        inform(f'Compute: page height {inch2str(var.paper_height, ROUND)}')
        var.free_width = var.paper_width - var.left_margin - var.right_margin
        inform(f'Compute: free width {inch2str(var.free_width, ROUND)}')
        if var.free_width <= 0:
            error(f'-L and/or -R too large, no horizontal space on paper')
        var.free_height = var.paper_height - var.top_margin - var.bottom_margin
        inform(f'Compute: free height {inch2str(var.free_height, ROUND)}')
        if var.free_height <= 0:
            error(f'-T and/or -B too large, no vertical space on paper')
        # corrected -L -R -T -B
        var.left_margin2 = max(0.0, broken_line(corr.points['pl'[arg.landscape] + 'lm'], var.left_margin))
        var.right_margin2 = max(0.0, broken_line(corr.points['pl'[arg.landscape] + 'rm'], var.right_margin))
        var.top_margin2 = max(0.0, broken_line(corr.points['pl'[arg.landscape] + 'tm'], var.top_margin))
        var.bottom_margin2 = max(0.0, broken_line(corr.points['pl'[arg.landscape] + 'bm'], var.bottom_margin))
        # compute automatic -w -W
        if var.chars_per_line and not var.char_width: # if -w and not -W == 0: -W = f(-w)
            var.char_width = var.free_width / var.chars_per_line
            inform(f'Compute: -W --char-width {inch2str(var.char_width, ROUND)}')
            if var.char_width <= 0:
                error(f'Wrong -W --char-width {inch2str(var.char_width, ROUND)} ≤ 0')
        elif not var.chars_per_line and var.char_width: # if not -w and -W: -w = f(-W)
            var.chars_per_line = int(var.free_width / var.char_width)
            inform(f'Compute: -w --chars-per-line {var.chars_per_line}')
            if var.chars_per_line <= 0:
                error(f'Wrong -w --chars-per-line {inch2str(var.chars_per_line, ROUND)} ≤ 0')
        elif not var.chars_per_line and not var.char_width: # if not -w and not -W: -w = f(file); -W = f(-w)
            var.chars_per_line = buf.body_max_chars_per_line # set by read_file()
            inform(f'Compute: -w --chars-per-line {var.chars_per_line}')
            if var.chars_per_line <= 0:
                error(f'Wrong -w --chars-per-line {inch2str(var.chars_per_line, ROUND)} ≤ 0')
            var.char_width = var.free_width / var.chars_per_line
            inform(f'Compute: -W --char-width {inch2str(var.char_width, ROUND)}')
            if var.char_width <= 0:
                error(f'Wrong -W --char-width {inch2str(var.char_width, ROUND)} ≤ 0')
        # correct -L -R -T -B -W
        if arg.correct_sizes == 'n':
            var.left_margin2 = var.left_margin
            var.right_margin2 = var.right_margin
            var.left_margin3 = var.right_margin # swapped for even pages
            var.right_margin3 = var.left_margin # swapped for even pages
            var.top_margin2 = var.top_margin
            var.bottom_margin2 = var.bottom_margin
            var.char_width2 = var.char_width
        else:
            var.char_width2 = max(0.0, broken_line(corr.points['pl'[arg.landscape] + 'cw'], var.char_width))
            inform(f'Correct: -W --char-width {inch2str(var.char_width2, ROUND)}')
            var.right_margin2 = max(0.0, broken_line(corr.points['pl'[arg.landscape] + 'rm'], var.right_margin))
            var.left_margin2 = max(0.0, broken_line(corr.points['pl'[arg.landscape] + 'lm'], var.left_margin))
            if var.left_margin == var.right_margin or arg.all_pages_E_e:
                inform(f'Correct: -L --left-margin {inch2str(var.right_margin2, ROUND)} (all pages)')
                inform(f'Correct: -R --right-margin {inch2str(var.left_margin2, ROUND)} (all pages)')
            else:
                inform(f'Correct: -L --left-margin {inch2str(var.right_margin2, ROUND)} (odd pages)')
                inform(f'Correct: -R --right-margin {inch2str(var.left_margin2, ROUND)} (odd pages)')
                var.right_margin3 = max(0.0, broken_line(corr.points['pl'[arg.landscape] + 'rm'], var.left_margin))
                inform(f'Correct: -L --left-margin {inch2str(var.right_margin3, ROUND)} (even pages)')
                var.left_margin3 = max(0.0, broken_line(corr.points['pl'[arg.landscape] + 'lm'], var.right_margin))
                inform(f'Correct: -R --right-margin {inch2str(var.left_margin3, ROUND)} (even pages)')
            var.top_margin2 = max(0.0, broken_line(corr.points['pl'[arg.landscape] + 'tm'], var.top_margin))
            inform(f'Correct: -T --top-margin {inch2str(var.top_margin2, ROUND)} (all pages)')
            var.bottom_margin2 = max(0.0, broken_line(corr.points['pl'[arg.landscape] + 'bm'], var.bottom_margin))
            inform(f'Correct: -B --bottom-margin {inch2str(var.bottom_margin2, ROUND)} (all pages)')
        # compute char_height, chars_per_inch, lines_per_inch, lines_per_page
        var.char_height = var.char_width / var.char_aspect
        inform(f'Compute: char height {inch2str(var.char_height, ROUND)}')
        var.chars_per_inch = 1.0 / var.char_width
        inform(f'Compute: chars per inch {round(var.chars_per_inch, ROUND)}')
        var.lines_per_inch = 1.0 / var.char_height
        inform(f'Compute: lines per inch {round(var.lines_per_inch, ROUND)}')
        # correct char_height, chars_per_inch, lines_per_inch
        if arg.correct_sizes == 'n':
            var.char_height2 = var.char_height
            var.chars_per_inch2 = var.chars_per_inch
            var.lines_per_inch2 = var.lines_per_inch
        else:
            var.char_height2 = max(0.0, broken_line(corr.points['pl'[arg.landscape] + 'ch'], var.char_height))
            inform(f'Correct: char height {inch2str(var.char_height2, ROUND)}')
            var.chars_per_inch2 = 1.0 / var.char_width2
            inform(f'Correct: chars per inch {round(var.chars_per_inch2, ROUND)}')
            var.lines_per_inch2 = 1.0 / var.char_height2
            inform(f'Correct: lines per inch {round(var.lines_per_inch2, ROUND)}')
        # compute lines_per_page
        var.lines_per_page = int(var.lines_per_inch * var.free_height) - 2 * (arg.page_headers != 'n') - 1
        inform(f'Compute: lines per page {var.lines_per_page}')
        # compute fake margins
        if arg.fake_margins:
            var.left_blanks = int((var.left_margin - var.left_border[arg.landscape]) / var.char_width)
            var.right_blanks = int((var.right_margin - var.left_border[arg.landscape]) / var.char_width) # sic
            var.top_lines = int((var.top_margin - var.top_border[arg.landscape]) / var.char_height)
            inform(f'Fake: left blanks {var.left_blanks}')
            inform(f'Fake: right blanks {var.right_blanks}')
            inform(f'Fake: top empty lines {var.top_lines}') 

    def remove_page_headers(buf):
        buf.buffer = [record for record in buf.buffer if not (record[LINE].startswith(FORMFEED) or record[LINE].startswith(MACRON))]

    def justify_lines(buf):
        buffer2 = []
        for jinp, x, x, x, line in buf.buffer:
            if not line: # empty line
                par.flush(buffer2)
                buffer2.append([jinp, EMPT, 0, 0, ''])
            else:
                jdot = findchar(line, '[! ]')
                if jdot >= 0 and line[jdot:jdot+2] in ['• ','. ']: # dot line
                    if jdot + 2 > var.chars_per_line:
                        error('Dot line indentation {jdot+2} > chars per line {var.chars_per_line}')
                    par.flush(buffer2)
                    par.assign(line[jdot+2:].strip(), jinp, jdot + 2)
                elif line[0] == ' ': # indented line
                    if par.string:
                        par.append(line)
                    else:
                        buffer2.append([jinp, PICT, 0, 0, line])
                elif par.string: # unindented line
                    par.append(line)
                else:
                    par.assign(line, jinp, 0)
        par.flush(buffer2)
        buf.buffer = buffer2

    def redraw_segments(buf):
        charstr = '`─│┐│┘│┤──┌┬└┴├┼'
        #          0123456789ABCDEF
        charset = frozenset(charstr)
        for jout, (jinp, kind, jpag, lpic, line) in enumerate(buf.buffer):
            if kind == PICT:
                chars = list(line)
                for jchar, char in enumerate(chars):
                    if char in charset:
                        kchar = (1 * (buf.char(jout, jchar - 1) in charset) +
                                 2 * (buf.char(jout + 1, jchar) in charset) +
                                 4 * (buf.char(jout - 1, jchar) in charset) +
                                 8 * (buf.char(jout, jchar + 1) in charset))
                        if kchar:
                            chars[jchar] = charstr[kchar]    
                buf.buffer[jout][LINE] = ''.join(chars)

    def redraw_arrowheads(buf):
        charstr = '^▷△^▽^^^◁^^^^^^^'
        #          0123456789ABCDEF
        charset = frozenset(charstr)
        for jout, (jinp, kind, jpag, lpic, line) in enumerate(buf.buffer):
            if kind == PICT:
                chars = list(line)
                for jchar, char in enumerate(chars):
                    if char in charset:
                        kchar = (1 * (buf.char(jout, jchar - 1) == '─') +
                                 2 * (buf.char(jout + 1, jchar) == '│') +
                                 4 * (buf.char(jout - 1, jchar) == '│') +
                                 8 * (buf.char(jout, jchar + 1) == '─'))
                        if kchar:
                            chars[jchar] = charstr[kchar]    
                buf.buffer[jout][LINE] = ''.join(chars)

    def renumber_chapters(buf):
        levels = []; max_level = 1; nout = len(buf.buffer)
        for jout, (jinp, kind, jpag, lpic, line) in enumerate(buf.buffer):
            prev_line = buf.buffer[jout-1][LINE] if jout > 0 else ''
            next_line = buf.buffer[jout+1][LINE] if jout + 1 < nout else ''
            if kind == TEXT and line and not prev_line and not next_line:
                words = line.split()
                level = chapter_level(words[0])
                title = unqupper(line)
                if level > 0: # numbered chapter line
                    if level > max_level:
                        error(f'numbered chapter level is {level} > {max_level}', jinp)
                    elif level == len(levels) + 1:
                        levels.append(1)
                    else:
                        levels = levels[:level]
                        levels[-1] += 1
                    title = unqupper(' '.join(words[1:]))
                    buf.buffer[jout][KIND] = CHP1 if level == 1 else CHP2
                    buf.buffer[jout][LINE] = '.'.join(str(level) for level in levels) + '. ' + title
                    max_level = len(levels) + 1
                elif title == var.contents_title: # contents chapter line
                    buf.buffer[jout][KIND] = CONT
                    buf.buffer[jout][LINE] = title
                    max_level = 1
                elif title == var.figures_title: # figures chapter line
                    buf.buffer[jout][KIND] = FIGU
                    buf.buffer[jout][LINE] = title
                    max_level = 1
                elif title == var.index_title: # index chapter line
                    buf.buffer[jout][KIND] = INDX
                    buf.buffer[jout][LINE] = title
                    max_level = 1
                else: # no chapter line
                    title = ''

    def add_chapters_to_contents(buf):
        for jout, (jinp, kind, jpag, lpic, line) in enumerate(buf.buffer):
            if kind == CONT:
                if buf.contents_found:
                    error(f'more than one contents line in text file', jinp)
                buf.contents_found = True
                # contents chapter doesn't list itself
            elif kind == FIGU:
                if buf.figures_found:
                    error(f'more than one figures line in text file', jinp)
                buf.figures_found = True
                buf.contents.append(['', unqtitle(var.figures_title), jout])
            elif kind == INDX:
                if buf.index_found:
                    error(f'more than one index line in text file', jinp)
                buf.index_found = True
                buf.contents.append(['', unqtitle(var.index_title), jout])
            elif kind in [CHP1, CHP2]:
                prefix, title = (line.split(None, 1) + [''])[:2]
                buf.contents.append([prefix, unqtitle(title), jout])

    def add_captions_to_figures(buf):
        if buf.figures_found:
            seek = False
            max_len_caption = 0
            chapter = ''
            letter = prevchar('a')
            for jout, record in enumerate(buf.buffer):
                jinp, kind, jpag, lpic, line = record
                if kind in [CONT, INDX, FIGU]:
                    seek = True
                elif kind in [CHP1, CHP2]:
                    seek = False
                    chapter = line.split()[0]
                    letter = prevchar('a')
                elif not seek and kind == PICT and (
                    jout == 0 or buf.buffer[jout-1][KIND] == EMPT) and (
                    jout == len(buf.buffer) - 1 or buf.buffer[jout+1][KIND] == EMPT):
                    words = unqtitle(line).split()
                    if len(words) >= 2:
                        prefix, label, *title = unqtitle(line).split()
                        title = ' '.join(title)
                        if prefix.upper() == var.caption_prefix and figure_level(label.lower()) > 0:
                            if letter == 'z':
                                error(f'in text file, more than 26 figure captions in a single chapter', jinp, line)
                            letter = nextchar(letter)
                            label = f'{chapter}{letter}.'
                            caption = f'{prefix} {label} {title}'
                            max_len_caption = max(max_len_caption, len(caption))
                            blanks = (var.chars_per_line - len(caption)) // 2 * ' '
                            buf.figures.append((label, title, jout))
                            record[LINE] = blanks + caption
                            record[KIND] = CAPT
                            if jout >= 2 and buf.buffer[jout - 2][KIND] == PICT:
                                buf.buffer[jout - 1][KIND] = PICT # paste caption with previous picture

    def add_quoted_subjects_to_index(buf):
        if buf.index_found:
            buf.qsub_jouts = SetDict() # {subject: jout}
            quote = False; subject = ''; seek = True
            for jout, (jinp, kind, jpag, lpic, line) in enumerate(buf.buffer):
                if kind in [CONT, FIGU, INDX]:
                    seek = False
                elif kind in [CHP1, CHP2]:
                    seek = True
                elif seek and kind == TEXT:
                    for jchar, char in enumerate(line + ' '):
                        if quote:
                            if (char == '"' and get(line, jchar-1, ' ') not in QUOTES and get(line, jchar+1, ' ') not in QUOTES):
                                subject = shrink(subject)
                                buf.qsub_jouts.add(subject, jout)
                                buf.subjects.add(subject)
                                quote = False
                            else:
                                subject += char
                                if len(subject) > var.chars_per_line // 2:
                                    error(f'length of subject "{subject}..." > -w / 2 = {var.chars_per_line // 2}')
                        elif (char == '"' and get(line, jchar-1, ' ') not in QUOTES and get(line, jchar+1, ' ') not in QUOTES):
                            subject = ''
                            quote = True
                else:
                    if quote:
                        error(f'unpaired \'"\' found while filling the index')
            if quote:
                error(f'unpaired \'"\' found while filling the index')

    def add_unquoted_subjects_to_index(buf):
        if buf.index_found:
            buf.uqsub_jouts = SetDict() # {subject: jout}
            charset = set(chars('[a-zA-Z0-9]') + ''.join(buf.qsub_jouts.keys()))
            word_jouts = [] # [(word, jout)]
            seek = True
            for jout, (jinp, kind, jpag, lpic, line) in enumerate(buf.buffer):
                if kind in [CONT, FIGU, INDX]:
                    seek = False
                elif kind in [CHP1, CHP2]:
                    seek = True
                elif seek and kind == TEXT:
                    for word in take(line, charset, ' ').split():
                        word_jouts.append((word, jout))
            sub0_subws = ListDict() # {subject.word[0]: subject.word[1:]}
            for subject in buf.qsub_jouts.keys():
                subjectwords = subject.split()
                sub0_subws.append(subjectwords[0], subjectwords[1:])
            for jword_jouts, (sub0, jout) in enumerate(word_jouts):
                if sub0 in sub0_subws:
                    for subw in sub0_subws[sub0]:
                        subject = sub0 + ' ' + ' '.join(subw) if subw else sub0
                        if subject == ' '.join(w for w, j in word_jouts[jword_jouts: jword_jouts + len(subw) + 1]):
                            buf.uqsub_jouts.add(subject, jout)
                            buf.subjects.add(subject)

    def insert_contents_figures_and_index_chapters(buf):

        def append_contents_to(buffer2):
            jinp = buffer2[-1][JINP]
            buffer2.append([jinp, TEXT, 0, 0, ''])
            fmt_labl = max((len(labl) for labl, titl, jpag in buf.contents), default=0)
            fmt_titl = max((len(titl) for labl, titl, jpag in buf.contents), default=0)
            for labl, titl, jpag in buf.contents:
                line = f'{INDENT}• {edit(labl, fmt_labl)} {edit(titl, fmt_titl)}'
                if len(line.rstrip()) > var.chars_per_line:
                    error(f'length of contents chapter line {line!r} is {len(line.rstrip())} > -w = {var.chars_per_line}')
                buffer2.append([jinp, TEXT, 0, 0, line])
            buffer2.append([jinp, TEXT, 0, 0, ''])

        def append_figures_to(buffer2):
            jinp = buffer2[-1][JINP]
            buffer2.append([jinp, TEXT, 0, 0, ''])
            fmt_labl = max((len(labl) for labl, titl, jpag in buf.figures), default=0)
            fmt_titl = max((len(titl) for labl, titl, jpag in buf.figures), default=0)
            for labl, titl, jpag in buf.figures:
                line = f'{INDENT}• {edit(labl, fmt_labl)} {edit(titl, fmt_titl)}'
                if len(line.rstrip()) > var.chars_per_line:
                    error(f'length of figures chapter line {line!r} is {len(line.rstrip())} > -w = {var.chars_per_line}')
                buffer2.append([jinp, TEXT, 0, 0, line])
            buffer2.append([jinp, TEXT, 0, 0, ''])

        def append_index_to(buffer2):
            jinp = buffer2[-1][JINP]
            buffer2.append([jinp, TEXT, 0, 0, ''])
            room = max((len(subject) for subject in buf.subjects), default=0) + 1
            for subject in sorted(buf.subjects):
                line = f'{INDENT}• {edit(subject, room)}'
                if len(line.rstrip()) > var.chars_per_line:
                    error(f'length of index chapter line {line!r} is {len(line.rstrip())} > -w = {var.chars_per_line}')
                buffer2.append([jinp, TEXT, 0, 0, line])
            buffer2.append([jinp, TEXT, 0, 0, ''])

        buffer2 = [] 
        copy = True
        for record in buf.buffer:
            kind = record[KIND]
            if kind == CONT:
                buf.contents_jout = len(buffer2)
                buffer2.append(record)
                append_contents_to(buffer2)
                copy = False
            elif kind == FIGU:
                buf.figures_jout = len(buffer2)
                buffer2.append(record)
                append_figures_to(buffer2)
                copy = False
            elif kind == INDX:
                buf.index_jout = len(buffer2)
                buffer2.append(record)
                append_index_to(buffer2)
                copy = False
            elif kind in [CHP1, CHP2]:
                buffer2.append(record)
                copy = True
            elif copy:
                buffer2.append(record)
        buf.buffer = buffer2

    def check_line_lengths(buf):
        for jinp, kind, zero, lpic, line in buf.buffer:
            if kind != CODE and len(line) > var.chars_per_line:
                error(f'in text file, line length {len(line)} > -w --chars-per-line {var.chars_per_line} in text file', jinp, line)

    def count_picture_lines(buf):
        jpic = 0
        for jout, record in retroenum(buf.buffer):
            if record[KIND] in [PICT, CAPT]:
                jpic += 1
                if jout == 0 or buf.buffer[jout-1][KIND] not in [PICT, CAPT]:
                    buf.buffer[jout][LPIC] = jpic
            else:
                jpic = 0

    def count_pages(buf):
        jpag, jpagline = 1, 0
        for jout, (jinp, kind, zero, lpic, line) in enumerate(buf.buffer):
            if (arg.page_headers in 'fpc' and jpagline >= var.lines_per_page or
                arg.page_headers in 'pc' and lpic < var.lines_per_page and jpagline + lpic >= var.lines_per_page or
                arg.page_headers == 'c' and kind in [CONT, INDX, FIGU, CHP1] and not (jout >= 2 and not buf.buffer[jout-1][LINE] and buf.buffer[jout-1][JPAG] > buf.buffer[jout-2][JPAG])):
                jpag += 1
                jpagline = 0
            else:
                jpagline += 1
            buf.buffer[jout][JPAG] = jpag

    def add_page_numbers_to_contents(buf):
        if buf.contents_jout > -1:
            width = max_len_page_number(buf.buffer[-1][JPAG], var.page_offset) + 1
            for jcontents, (prefix, titl, jout) in enumerate(buf.contents):
                line = buf.buffer[buf.contents_jout + 2 + jcontents][LINE] + edit(page_number(buf.buffer[jout][JPAG], var.page_offset), width, right=True)
                if len(line) > var.chars_per_line:
                    error(f'length of contents chapter line {line!r} is {len(line)} > -w = {var.chars_per_line}')
                buf.buffer[buf.contents_jout + 2 + jcontents][LINE] = line

    def add_page_numbers_to_index(buf):
        if buf.index_jout > -1:
            qsub_jpags = SetDict() # {quoted_subject: {jpag}}
            for subject, jouts in buf.qsub_jouts.items():
                for jout in jouts:
                    qsub_jpags.add(subject, buf.buffer[jout][JPAG])
            uqsub_jpags = SetDict() # {unquoted_subject: {jpag}}
            for subject, jouts in buf.uqsub_jouts.items():
                for jout in jouts:
                    jpag = buf.buffer[jout][JPAG]
                    if jpag not in qsub_jpags[subject]:
                        uqsub_jpags.add(subject, jpag)
            for jindex, subject in enumerate(sorted(buf.subjects)):
                jpag_strjs = sorted((jpag, f'"{page_number(jpag, var.page_offset)}"'
                                     if jpag in qsub_jpags[subject] else page_number(jpag, var.page_offset))
                    for jpag in (qsub_jpags[subject] | uqsub_jpags[subject])) # [(jpag, str(jpag))]
                line = buf.buffer[buf.index_jout + 2 + jindex][LINE] + ', '.join(strj for jpag, strj in jpag_strjs)
                if len(line) > var.chars_per_line:
                    warning(f"Index line for {subject!r} longer than -w --chars-per-line {var.chars_per_line}, truncated")
                    while True:
                        line = line[:line.rfind(',')]
                        if len(line) + 5 <= var.chars_per_line:
                            break
                    line += ', ...'
                buf.buffer[buf.index_jout + 2 + jindex][LINE] = line

    def add_page_numbers_to_figures(buf):
        if buf.figures_jout > -1:
            width = max_len_page_number(buf.buffer[-1][JPAG], var.page_offset) + 1
            for jfigures, (prefix, title, jout) in enumerate(buf.figures):
                line = buf.buffer[buf.figures_jout + 2 + jfigures][LINE] + edit(page_number(buf.buffer[jout][JPAG], var.page_offset), width, right=True)
                if len(line) > var.chars_per_line:
                    error(f'length of figures chapter line {line!r} is {len(line)} > -w {var.chars_per_line}')
                buf.buffer[buf.figures_jout + 2 + jfigures][LINE] = line

    def insert_page_headers(buf):
        if buf.buffer:
            jout = 0; jpag0 = 1; chapter = ''; npag = buf.buffer[-1][JPAG]
            header2 = var.chars_per_line * MACRON
            while jout < len(buf.buffer):
                jinp, kind, jpag, lpic, line = buf.buffer[jout]
                if kind in [CONT, INDX, FIGU, CHP1]:
                    chapter = unqtitle(line)
                if jpag > jpag0:
                    left, right = ((arg.even_right, arg.even_left) if arg.all_pages_E_e else
                                   (arg.odd_left, arg.odd_right) if jpag % 2 else
                                   (arg.even_left, arg.even_right))
                    PpfFeYmdHMSnNc = var.PpfFeYmdHMS + (page_number(jpag, var.page_offset), str(npag), chapter)
                    left = evalchar(left, 'PpfFeYmdHMSnNc', PpfFeYmdHMSnNc, '%')
                    right = evalchar(right, 'PpfFeYmdHMSnNc', PpfFeYmdHMSnNc, '%')
                    blanks = ' ' * (var.chars_per_line - len(left) - len(right))
                    if not blanks:
                        header1 = f'{left} {right}'
                        error(f"length of header {header1!r} is {len(header1)} > -w {var.chars_per_line}")
                    header1 = f'{FORMFEED}{left}{blanks}{right}'
                    buf.buffer.insert(jout, [0, HEA2, jpag, 0, header2])
                    buf.buffer.insert(jout, [0, HEA1, jpag, 0, header1])
                    jout += 2
                    jpag0 = jpag
                elif jout >= 3 and not buf.buffer[jout-1][LINE] and buf.buffer[jout-3][LINE].startswith(FORMFEED):
                    left, right = ((arg.even_right, arg.even_left) if arg.all_pages_E_e else
                                   (arg.odd_left, arg.odd_right) if jpag % 2 else
                                   (arg.even_left, arg.even_right))
                    PpfGeYmdHMSnNc = var.PpfFeYmdHMS + (str(jpag), str(npag), chapter)
                    left = evalchar(left, 'PpfFeYmdHMSnNc', PpfFeYmdHMSnNc, '%')
                    right = evalchar(right, 'PpfFeYmdHMSnNc', PpfFeYmdHMSnNc, '%')
                    blanks = ' ' * (var.chars_per_line - len(left) - len(right))
                    if not blanks:
                        header1 = f'{left} {right}'
                        error(f"length of header {header1!r} is {len(header1)} > -w --chars-per-line {var.chars_per_line}")
                    buf.buffer[jout-3][LINE] = f'{FORMFEED}{left}{blanks}{right}'
                jout += 1

#----- main window -----

def main_window():
    'main window of GUI mode'
    sg.theme('Python')
    button = 'Main'
    while True: # loop after 'x' button or Alt-F4 error
        layout = [
            # format arguments
            [sg.Text('-v --verbose',         size=SGTS), sg.Checkbox('', default=arg.verbose,         key='v', tooltip=arg.letter_tooltip['v'])],
            [sg.Text('-y --text-editor',     size=SGTS), sg.Input(arg.text_editor, size=SGAS,         key='y', tooltip=arg.letter_tooltip['y']),
             sg.Text('-g --graphics',        size=SGTS), sg.Checkbox('', default=arg.graphics,        key='g', tooltip=arg.letter_tooltip['g'])],
            [sg.Text('-w --chars-per-line',  size=SGTS), sg.Input(arg.chars_per_line, size=SGAS,      key='w', tooltip=arg.letter_tooltip['w']),
             sg.Text('-l --just-left-only',  size=SGTS), sg.Checkbox('', default=arg.just_left_only,  key='l', tooltip=arg.letter_tooltip['l'])],
            [sg.Text('-c --contents-title',  size=SGTS), sg.Input(arg.contents_title, size=SGAS,      key='c', tooltip=arg.letter_tooltip['c']),
             sg.Text('-i --index-title',     size=SGTS), sg.Input(arg.index_title, size=SGAS,         key='i', tooltip=arg.letter_tooltip['i'])],
            [sg.Text('-f --figures-title',   size=SGTS), sg.Input(arg.figures_title, size=SGAS,       key='f', tooltip=arg.letter_tooltip['f']),
             sg.Text('-F --caption-prefix',  size=SGTS), sg.Input(arg.caption_prefix, size=SGAS,      key='F', tooltip=arg.letter_tooltip['F'])],
            # paging arguments
            [sg.Text('-p --page-headers',    size=SGTS),
                sg.Radio('n=no',       'p',  default=arg.page_headers=='n', tooltip="do not insert page headers"),
                sg.Radio('f=fullpage', 'p',  default=arg.page_headers=='f', tooltip="insert page headers on full page"),
                sg.Radio('p=picture',  'p',  default=arg.page_headers=='p', tooltip="...and on broken picture"),
                sg.Radio('c=chapter',  'p',  default=arg.page_headers=='c', tooltip="...and before level-1 chapters")],
            [sg.Text('-e --even-left',       size=SGTS), sg.Input(arg.even_left, size=SGAS,           key='e', tooltip=arg.letter_tooltip['e']),
             sg.Text('-E --even-right',      size=SGTS), sg.Input(arg.even_right, size=SGAS,          key='E', tooltip=arg.letter_tooltip['E'])],
            [sg.Text('-o --odd-left',        size=SGTS), sg.Input(arg.odd_left, size=SGAS,            key='o', tooltip=arg.letter_tooltip['o']),
             sg.Text('-O --odd-right',       size=SGTS), sg.Input(arg.odd_right, size=SGAS,           key='O', tooltip=arg.letter_tooltip['O'])],
            [sg.Text('-n --page-offset',     size=SGTS), sg.Input(arg.page_offset, size=SGAS,         key='n', tooltip=arg.letter_tooltip['n']),
             sg.Text('-a --all-pages-E-e',   size=SGTS), sg.Checkbox('', default=arg.all_pages_E_e,   key='a', tooltip=arg.letter_tooltip['a'])],
            # export arguments
            [sg.Text('-X --export-view-pdf', size=SGTS), sg.Checkbox('', default=arg.export_view_pdf, key='X', tooltip=arg.letter_tooltip['X'])],
            [sg.Text('-Y --pdf-browser',     size=SGTS), sg.Input(arg.pdf_browser, size=SGAS,         key='Y', tooltip=arg.letter_tooltip['Y']),
             sg.Text('-P --file-pdf',        size=SGTS), sg.Input(arg.pdf_file, size=SGAS,            key='P', tooltip=arg.letter_tooltip['P'])],
            [sg.Text('-W --char-width',      size=SGTS), sg.Input(arg.char_width, size=SGAS,          key='W', tooltip=arg.letter_tooltip['W']),
             sg.Text('-A --char-aspect',     size=SGTS), sg.Input(arg.char_aspect, size=SGAS,         key='A', tooltip=arg.letter_tooltip['A'])],
            [sg.Text('-S --paper-size',      size=SGTS), sg.Input(arg.paper_size, size=SGAS,          key='S', tooltip=arg.letter_tooltip['S']),
             sg.Text('-Z --landscape',       size=SGTS), sg.Checkbox('', default=arg.landscape,       key='Z', tooltip=arg.letter_tooltip['Z'])],
            [sg.Text('-L --left-margin',     size=SGTS), sg.Input(arg.left_margin, size=SGAS,         key='L', tooltip=arg.letter_tooltip['L']),
             sg.Text('-R --right-margin',    size=SGTS), sg.Input(arg.right_margin, size=SGAS,        key='R', tooltip=arg.letter_tooltip['R'])],
            [sg.Text('-T --top-margin',      size=SGTS), sg.Input(arg.top_margin, size=SGAS,          key='T', tooltip=arg.letter_tooltip['T']),
             sg.Text('-B --bottom-margin',   size=SGTS), sg.Input(arg.bottom_margin, size=SGAS,       key='B', tooltip=arg.letter_tooltip['B'])],
            [sg.Text('-C --correct-sizes',   size=SGTS),
                sg.Radio('n=no',      'C',   default=arg.correct_sizes=='n', tooltip="do not correct char size and page margins"),
                sg.Radio('d=default', 'C',   default=arg.correct_sizes=='d', tooltip="correct char size and page margins\nby default values"),
                sg.Radio('f=file',    'C',   default=arg.correct_sizes=='f', tooltip="correct char size and page margins\nby correction file"),
             sg.Text('', size=0),
             sg.Text('-K --fake-margins',    size=SGTS), sg.Checkbox('', default=arg.fake_margins,     key='K', tooltip=arg.letter_tooltip['K'])],
            # text_file argument, read-only
            [sg.Text('text_file',            size=SGTS), sg.Text(arg.text_file, size=SGFS, key='t', tooltip=arg.letter_tooltip['t'])],
            # action buttons
            [sg.Button(button, tooltip=BUTTON_TOOLTIP[button], size=SGBS) for button in ['New','Open','Recent','Saveas','Help','Exit']],
            [sg.Button(button, tooltip=BUTTON_TOOLTIP[button], size=SGBS) for button in ['Edit','Format','Noformat','Undo','Log','Correct']]]
        window = sg.Window(f'YAWP - Main', layout, finalize=True)
        while True: # window.read() loop
            try:
                if not arg.text_file:
                    arg.read_text_file_from_sess_file(YAWP_SESS)
                    arg.read_from_args_file_of(arg.text_file)
                    arg.write_into_window(window)
                button, values = window.read()
                if not button: # 'x' button or Alt-F4 error
                    message = "ERROR: You cannot close YAWP by typing alt-F4 or clicking the 'x' button\nClick the 'Exit' button instead"
                    log.print(message)
                    print(message, file=stderr)
                    ask_ok('Main', message)
                    break
                inform(frame(f'{button:<10} {now()}'))
                arg.read_from_window(window)
                arg.set_default_if_empty()
                arg.write_into_window(window)
                old_text_file = arg.text_file
                var.ok_message = ''
                {'New':      New_button,
                 'Open':     Open_button,
                 'Recent':   Recent_button,
                 'Saveas':   Saveas_button,
                 'Correct':  Correct_button,
                 'Help':     Help_button,
                 'Exit':     Exit_button,
                 'Edit':     Edit_button,
                 'Format':   Format_button,
                 'Noformat': Noformat_button,
                 'Undo':     Undo_button,
                 'Log':      Log_button}[button]()
                arg.text_file = long_path(arg.text_file)
                var.PpfFeYmdHMS = get_PpfFeYmdHMS(arg.text_file)
                path = dirname(arg.text_file)
                if isdir(path):
                    cd(path)
                if old_text_file != arg.text_file: # altered by New/Open/Recent/Saveas?
                    if isfile(old_text_file):
                        arg.write_into_args_file_of(old_text_file)
                    arg.read_from_args_file_of(arg.text_file)
                    cd(dirname(arg.text_file))
                arg.write_into_window(window)
            except YawpError as yawp_error:
                ask_ok(button, f'{button}: {yawp_error}')
            else:
                inform(f'{button}: OK')

#----- buttons, first line: New Open Recent Saveas Help Exit -----

def New_button():
    'create a new empty text file, which becomes the new text file'
    new_file = long_path(sg.popup_get_file('', no_window=True, save_as=True))
    # if new file aready exists, confirmation window is issued by sg.PopupGetFile() itself
    if new_file:
        dir_of_new_file = dirname(new_file)
        if not isdir(dir_of_new_file):
            error(f'directory {dir_of_new_file!r} of new file {new_file!r} not found')
        if exists(new_file) and not isfile(new_file):
            error(f'new text file {new_file!r} exists but is not a file')
        open(new_file, 'w').write('') # create empty new file
        new_file_args = get_args_file(new_file)
        if exists(new_file_args):
            rm(new_file_args) # virtually set args of new file to default values
        arg.swap_text_file(new_file)
        inform(f'New: new text file {new_file!r} created')
    else:
        inform('New: new text file NOT created')

def Open_button():
    'browse file system and select the text file to be processed'
    new_file = long_path(sg.PopupGetFile('', no_window=True, save_as=False))
    # if new_file doesn't exist, error window is issued by sg.PopupGetFile() itself
    if new_file:
        if exists(new_file) and not isfile(new_file):
            error('target file exists but is not a file')
        arg.swap_text_file(new_file)
        inform('Open: text file {new_file!r} selected')
    else:
        inform('Open: text file NOT selected')

def Recent_button():
    'browse list of recent files and select the text file to be processed'
    new_file = long_path(hist.select())
    if new_file:
        arg.swap_text_file(new_file)
        inform('Recent: text file {new_file!r} selected')
    else:
        inform('Recent: text file NOT selected')

def Saveas_button():
    'clone current text file into a copy, which becomes the new text file'
    new_file = long_path(sg.popup_get_file('', no_window=True, save_as=True))
    # if target file aready exists, confirmation window is issued by sg.PopupGetFile() itself
    if new_file:
        if arg.text_file == new_file:
            error('you cannot save a text file into itself')
        if exists(new_file) and not isfile(new_file):
            error('target file exists but is not a file')
        cp(arg.text_file, new_file) # copy text file
        text_file_args = get_args_file(arg.text_file)
        if isfile(text_file_args):
            new_file_args = get_args_file(new_file)
            cp(text_file_args, new_file_args) # copy args file, if any
        arg.swap_text_file(new_file)
        inform(f'Saveas: {arg.text_file!r} ──▷')
        inform(f'        {new_file!r}')
    else:
        inform('Saveas: target text file NOT selected')

def Help_button():
    'show colophon and possibly browse the YAWP User Manual'
    if ask_yes('YAWP - Help', f'''
                        YAWP {VERSION}
             Yet Another Word Processor
                          2023-05-18
             https://pypi.org/project/yawp
                 Carlo Alessandro Verre
         carlo.alessandro.verre@gmail.com

Do you want to browse the YAWP User Manual?''', 'browse'):
        arg.check_pdf_browser()
        shell(f'{arg.pdf_browser} {YAWP_PDF}')

def Exit_button():
    'terminate execution'
    if isfile(arg.text_file):
        arg.close_text_file()
        if arg.usage_mode == 'g':
            arg.write_text_file_into_sess_file(YAWP_SESS)
    log.close()
    exit()

#----- buttons, second line: Edit Format Noformat Undo Log Correct -----

def Edit_button():
    'edit current text file'
    arg.check_text_file()
    arg.check_text_editor()
    old = Buffer(arg.text_file)
    old.inform('Before:')
    shell(f'{arg.text_editor} {arg.text_file}')
    new = Buffer(arg.text_file)
    if old == new:
        inform('Edit: text file NOT altered, backup NOT performed')
    else:
        back_file = new_back_file(arg.text_file)
        old.write_into_file(back_file)
        inform(f'Backup:  {arg.text_file!r} ──▷')
        inform(f'         {back_file!r}')
        new.inform('After:')
        inform('Edit: text file altered, backup performed')

def Format_button(format=True):
    'format current text file, and export in PDF format'
    arg.check_text_file()
    button = ['Noformat','Format'][format]
    arg.check()
    old = Buffer(arg.text_file)
    inform(f'Read:    YAWP ◁── {arg.text_file}')
    old.compute_and_correct_sizes()
    old.inform('Before:')
    new = old.copy()
    if format:
        new.remove_page_headers()
        new.justify_lines()
    if arg.graphics: # -g ?
        new.redraw_segments()
        new.redraw_arrowheads()
    if format:
        new.renumber_chapters()
        new.add_chapters_to_contents()
        new.add_captions_to_figures()
        new.add_quoted_subjects_to_index()
        new.add_unquoted_subjects_to_index()
        new.insert_contents_figures_and_index_chapters()
        new.check_line_lengths()
        if arg.page_headers != 'n': # -p ?
            new.count_picture_lines()
            new.count_pages()
            new.add_page_numbers_to_contents()
            new.add_page_numbers_to_figures()
            new.add_page_numbers_to_index()
            new.insert_page_headers()
    if (not format and not arg.graphics) or old == new:
        inform(f'{button}: text file NOT altered, backup NOT performed')
    else:
        back_file = new_back_file(arg.text_file)
        old.write_into_file(back_file)
        inform(f'Backup:  {arg.text_file!r} ──▷')
        inform(f'         {back_file!r}')
        new.write_into_file(arg.text_file)
        inform(f'Rewrite: YAWP ──▷ {arg.text_file!r}')
        new.inform('After:')
        inform(f'{button}: text file altered, backup performed')
    if arg.export_view_pdf: # -X ?
        pdf.export_and_browse(arg.text_file)

def Noformat_button():
    'do not format current text file, but run graphics, and export in PDF format'
    Format_button(format=False)
    
def Undo_button():
    'restore current text file to its previous version'
    arg.check_text_file(must_exist=False)
    try:
        back_file = old_back_file(arg.text_file)
    except FileNotFoundError:
        error(f'backup file for text file {arg.text_file!r} not found')
    if not isfile(back_file):
        error(f'backup file {back_file!r} for text file {arg.text_file!r} exists but is not a file')
    if arg.usage_mode == 'u' or not isfile(arg.text_file) or ask_yes('YAWP - Undo',
            'Current content will be lost\nDo you want restore previous content?','restore'):
        old = Buffer(arg.text_file)
        old.inform('Before:')
        rm(arg.text_file)
        mv(back_file, arg.text_file)
        inform(f'Restore: {arg.text_file!r} ◁──')
        inform(f'         {back_file!r}')
        new = Buffer(arg.text_file)
        if old != new:
            new.inform('After:')
            inform('Undo: text file altered')
        else:
            new.compute_and_correct_sizes()
            inform('Undo: text file NOT altered')
        if arg.export_view_pdf: # -X ?
            pdf.export_and_browse(arg.text_file)

def Log_button():
    'browse current log file'
    arg.check_text_editor()
    log.browse()

def Correct_button():
    'manage correction file'

    def Correct_Edit_button():
        'edit correction file'
        arg.check_text_editor()
        lock.seize(YAWP_CORR)
        old = open(YAWP_CORR).read()
        strfile_inform(old, 'Before:')
        shell(f'{arg.text_editor} {YAWP_CORR}')
        new = open(YAWP_CORR).read()
        if old == new:
            inform('Correct - Edit:correction file NOT altered, backup NOT performed')
        else:
            back_file = new_back_file(YAWP_CORR)
            open(back_file, 'w').write(old)
            inform(f'Backup:  {YAWP_CORR!r} ──▷')
            inform(f'         {back_file!r}')
            strfile_inform(new, 'After:')
            inform('Correct - Edit: correction file altered, backup performed')

    def Correct_Reset_button():
        'reset correction file to default values'
        lock.seize(YAWP_CORR)
        old = open(YAWP_CORR).read()
        strfile_inform(old, 'Before:')
        open(YAWP_CORR, 'w').write(CORRECTORS)
        new = CORRECTORS
        if old == new:
            inform('Correct - Reset: correction file NOT altered, backup NOT performed')
        else:
            back_file = new_back_file(YAWP_CORR)
            open(back_file, 'w').write(old)
            inform(f'Backup:  {YAWP_CORR!r} ──▷')
            inform(f'         {back_file!r}')
            strfile_inform(new, 'After:')
            inform('Correct - Reset: correction file altered, backup performed')
    
    def Correct_Undo_button():
        'restore correction file to the previous version'
        try:
            back_file = old_back_file(YAWP_CORR)
        except FileNotFoundError:
            error(f'backup file for correction file not found')
        if not isfile(back_file):
            error(f'backup file {back_file!r} for correction file exists but is not a file')
        if ask_yes('YAWP - Correct - Undo','Current content will be lost\nDo you want to restore previous content?','restore'):
            lock.seize(YAWP_CORR)
            old = open(YAWP_CORR).read()
            strfile_inform(old, 'Before:')
            rm(YAWP_CORR)
            mv(back_file, YAWP_CORR)
            inform(f'Restore: {YAWP_CORR!r} ◁──')
            inform(f'         {back_file!r}')
            new = open(YAWP_CORR).read()
            if old == new:
                inform('Correct - Undo: correction file NOT altered')
            else:
                strfile_inform(new, 'After:')
                inform('Correct - Undo: correction file altered')
    
    layout = [[sg.Text('edit reset or restore the correction file?')],
        [sg.Button('Edit',   size=SGBS, tooltip='edit correction file\nthrough the text editor defined by -y'),
         sg.Button('Reset',  size=SGBS, tooltip='reset correction file\nto default values'),
         sg.Button('Undo',   size=SGBS, tooltip='restore correction file\nto its previous content'),
         sg.Button('Cancel', size=SGBS, tooltip='do nothing and go back')]]
    window = sg.Window(f'YAWP - Correct', layout)
    event, values = window.read(close=True)
    if event and event != 'Cancel':
        {'Edit': Correct_Edit_button,
         'Reset': Correct_Reset_button,
         'Undo': Correct_Undo_button}[event]()

#----- main -----

def main():
    try:
        var.gui = False
        simplefilter('ignore')
        if not exists(YAWP_CORR):
            open(YAWP_CORR, 'w').write(CORRECTORS)
        log.open()
        arg.read_from_argv(argv)
        inform(frame(YAWP_LOG))
        if arg.usage_mode == 'g':
            var.gui = True
            main_window()
        elif arg.usage_mode == 'e':
            inform(frame(f'{"Edit":<10} {now()}'))
            Edit_button()
        elif arg.usage_mode == 'f':
            inform(frame(f'{"Format":<10} {now()}'))
            Format_button()
        elif arg.usage_mode == 'n':
            inform(frame(f'{"Noformat":<10} {now()}'))
            Noformat_button()
        else: # arg.usage_mode == 'u'
            inform(frame(f'{"Undo":<10} {now()}'))
            Undo_button()
        Exit_button()
    except KeyboardInterrupt:
        Exit_button()

if __name__ == '__main__':
    main()

#----- end -----

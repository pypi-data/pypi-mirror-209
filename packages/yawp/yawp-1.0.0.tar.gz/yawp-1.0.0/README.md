```
usage: yawp [-h] [-H] [-V] [-v] [-M USAGE_MODE] [-y TEXT_EDITOR] [-g]
            [-w CHARS_PER_LINE] [-l] [-c CONTENTS_TITLE] [-i INDEX_TITLE]
            [-f FIGURES_TITLE] [-F CAPTION_PREFIX] [-p PAGE_HEADERS]
            [-e EVEN_LEFT] [-E EVEN_RIGHT] [-o ODD_LEFT] [-O ODD_RIGHT]
            [-n PAGE_OFFSET] [-a] [-X] [-Y PDF_BROWSER] [-P PDF_FILE]
            [-W CHAR_WIDTH] [-A CHAR_ASPECT] [-S PAPER_SIZE] [-Z]
            [-L LEFT_MARGIN] [-R RIGHT_MARGIN] [-T TOP_MARGIN]
            [-B BOTTOM_MARGIN] [-C CORRECT_SIZES] [-K]
            [text_file]

Yet Another Word Processor, a word processor for text files, with PDF export

"YAWP" here means Yet Another Word Processor, and YAWP is a pure-Python Linux-only
word  processor  for plain text files, with PDF export. If you really need all the
features  of  a  full-fledged  WYSIWYG  word processor (with italic bold fonts etc
etc)  as LibreOffice Writer, YAWP is not for you. But if you just want to create a
draft or a simple quick-and-dirty no-frills document, give YAWP a try.

Main features are:

    • YAWP has a GUI interface, but can be used as a CLI command too
    • YAWP  processes  in  place a single plain text file, hereinafter referred to
      simply as the "text file"
    • YAWP  before  rewriting the text file creates a timestamped backup, allowing
      Undo operation
    • YAWP justifies text at left and right in:
        • unindented paragraphs
        • dot-marked indented paragraphs (as this one)
    • YAWP  justification  is driven by the text in the text file and by arguments
      only, not by commands or tags embedded in text
    • YAWP  accepts  unjustified  pictures  (as schemas, tables and code examples)
      freely intermixed with text
    • YAWP  performs  automatic multi-level renumbering of chapters and inserts an
      automatic Contents chapter in the text file
    • YAWP  recognizes  relevant subjects (quoted by '"') and inserts an automatic
      Index chapter in the text file
    • YAWP  performs  automatic  multi-level  renumbering  of  figure captions and
      inserts an automatic Figures chapter in the text file
    • YAWP  cuts  the  text  file  in  pages, by inserting two-lines page headers,
      allowing  page  numbering  control  and  insertion of initial Roman-numbered
      pages
    • YAWP also has some graphic features, you can sketch pictures with horizontal
      and vertical segments (by '`') and arrowheads (by '^'), YAWP redraws them by
      suitable Unicode graphic characters
    • YAWP  exports  the text file in PDF format, with control over character size
      and  page  layout,  and  lets  you  browse  the generated PDF file, allowing
      preview and printing
    • YAWP keeps a distinct argument set for each text file
    • YAWP  in GUI mode saves the last processed text file and restores it at next
      invocation
    • YAWP in GUI mode saves a list of the 20 most recent processed text files and
      allows to select one at next invocation
    • YAWP  tries  to  correct  errors  made  by CUPS-PDF about font size and page
      margins,  you  can  use default corrections or redefine them by a correction
      file
    • YAWP  writes  messages  about  processing on terminal and into a timestamped
      session log file
    • YAWP  locks the text file to  be processed in order to avoid interference by
      other concurrent YAWP executions
    • YAWP  is  stable,  if  after a YAWP execution you run YAWP again on the same
      file with the same arguments, the text file content does not change
    • believe  or  not,  YAWP   has   been  kept as simple as possible, about 3000
      lines of Python code  (plus 3000 lines of this YAWP User Manual)

In  order to install YAWP, we assume that your Linux belongs to the Debian family.
Type at terminal:

    │ $ sudo apt-get update
    │ $ sudo apt-get purge printer-driver-cups-pdf
    │ $ sudo apt-get install printer-driver-cups-pdf idle python3-pip
    │ $ pip3 install yawp

Imagine your user name is 'xxxx'. If you see a message like this:

    WARNING: The script yawp is installed in '/home/xxxx/.local/bin'
    which is not on PATH

you can fix the problem by typing:

    │ $ echo 'PATH=$PATH:/home/xxxx/.local/bin' >> /home/xxxx/.bashrc

Now you can close the terminal, open another one, and call YAWP. Syntax is:

    │ $ yawp -h # show a help message and exit
    │ $ yawp -V # show program's version number and exit
    │ $ yawp -H [-Y pdf_browser] # browse the PDF YAWP User Manual and exit
    │ $ yawp -M e [-y text_editor] text_file # run YAWP in CLI Edit mode
    │ $ yawp -M f [...arguments...] text_file # run YAWP in CLI Format mode
    │ $ yawp -M n [...arguments...] text_file # run YAWP in CLI Noformat mode
    │ $ yawp -M u [...arguments...] text_file # run YAWP in CLI Undo mode
    │ $ yawp text_file # run YAWP in GUI mode, explicit text file, no arguments
    │ $ yawp # run YAWP in GUI mode, text file from previous session, no arguments

This is the GUI Main window:

 ┌───┬───────────────────────────────────────────────────────────────────┬───┬───┐
 │   │                              YAWP - Main                          │ _ │ x │
 ├───┴───────────────────────────────────────────────────────────────────┴───┴───┤
 │ -v --verbose         □                                                        │
 │ -y --text-editor    [idle............] -g --graphics        □                 │
 │ -w --chars-per-line [0...............] -l --just-left-only  □                 │
 │ -c --contents-title [contents........] -i --index-title    [index...........] │
 │ -f --figures-title  [figures.........] -F --caption-prefix [figure..........] │
 │ -p --page-headers    ◎ n=no  ○ f=fullpage  ○ p=picture  ○ c=chapter           │
 │ -e --even-left      [%n/%N...........] -E --even-right     [%F %Y-%m-%d.....] │
 │ -o --odd-left       [%c..............] -O --odd-right      [%n/%N...........] │
 │ -n --page-offset    [0...............] -a --all-pages-E-e   □                 │
 │ -X --export-pdf      □                                                        │
 │ -Y --pdf-browser    [xdg-open........] -P --file-pdf       [%P%f.pdf........] │
 │ -W --char-width     [0...............] -A --char-aspect    [3/5.............] │
 │ -S --paper-size     [A4..............] -Z --landscape       □                 │
 │ -L --left-margin    [2cm.............] -R --right-margin   [2cm.............] │
 │ -T --top-margin     [2cm.............] -B --bottom-margin  [2cm.............] │
 │ -C --correct-sizes   ○ n=no  ◎ d=default  ○ f=file    -K --fake-margins □     │
 │ text_file           [.......................................................] │
 │ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ │
 │ │   New    │ │   Open   │ │  Recent  │ │  Saveas  │ │   Help   │ │   Exit   │ │
 │ └──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────────┘ │
 │ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ │
 │ │   Edit   │ │  Format  │ │ Noformat │ │   Undo   │ │   Log    │ │  Correct │ │
 │ └──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────────┘ │
 └───────────────────────────────────────────────────────────────────────────────┘

These are the buttons in GUI Main window:

    • 4 buttons dedicated to the selection of the text file:
        • New button: create a new empty text file
        • Open button: browse the file system to select the text file
        • Recent button: browse the list of recent files to select the text file
        • Saveas button: clone current text file into a new target text file
    • Help button: browse the YAWP Manual through the PDF browser defined by -Y
    • Exit button: save current text file with its arguments and finish
    • 4 buttons dedicated to the processing of the text file:
        • Edit button: edit the text file through the text editor defined by -y
        • Format button: process the text file by formatting it
        • Noformat button: process the text file without formatting it
        • Undo button: restore the text file to its previous content
    • Log button: browse the log file through the text editor defined by -y
    • Correct button: manage the correction file (Edit Reset or Undo)

positional arguments:
  text_file             text file to be processed, ASCII or UTF8-encoded

options:
  -h, --help            show this help message and exit
  -H, --view-manual     browse the yawp-generated PDF Yawp Manual and exit
  -V, --version         show program's version number and exit
  -v, --verbose         write all messages on stderr (default: write errors
                        only)
  -M USAGE_MODE, --usage-mode USAGE_MODE
                        run yawp in this usage mode (default: 'g' = GUI, 'e' =
                        Edit, 'f' = Format, 'n' = Noformat, 'U' = undo)
  -y TEXT_EDITOR, --text-editor TEXT_EDITOR
                        editor for text files (default: 'idle')
  -g, --graphics        redraw '`'-segments and '^'-arrowheads
  -w CHARS_PER_LINE, --chars-per-line CHARS_PER_LINE
                        line width in characters per line (default: '0' =
                        automatic)
  -l, --just-left-only  justify text lines at left only (default: at left and
                        right)
  -c CONTENTS_TITLE, --contents-title CONTENTS_TITLE
                        title of contents chapter (default: 'contents')
  -i INDEX_TITLE, --index-title INDEX_TITLE
                        title of index chapter (default: 'index')
  -f FIGURES_TITLE, --figures-title FIGURES_TITLE
                        title of figures chapter (default: 'figures')
  -F CAPTION_PREFIX, --caption-prefix CAPTION_PREFIX
                        first word of figure captions (default: 'figure')
  -p PAGE_HEADERS, --page-headers PAGE_HEADERS
                        insert page headers (default: 'n' = no, 'f' = on full
                        page, 'p' = and on broken pictures, 'c' = and on
                        level-1 chapters)
  -e EVEN_LEFT, --even-left EVEN_LEFT
                        headers of even pages, left (default: '%n/%N')
  -E EVEN_RIGHT, --even-right EVEN_RIGHT
                        headers of even pages, right (default: '%F %Y-%m-%d')
  -o ODD_LEFT, --odd-left ODD_LEFT
                        headers of odd pages, left (default: '%c')
  -O ODD_RIGHT, --odd-right ODD_RIGHT
                        headers of odd pages, right (default: '%n/%N')
  -n PAGE_OFFSET, --page-offset PAGE_OFFSET
                        offset of page numbers (default: '0', min: '-3999', if
                        negative it is count of initial Roman numbers)
  -a, --all-pages-E-e   put in all page headers -E at left and -e at right
  -X, --export-view-pdf
                        after processing export and browse PDF file
  -Y PDF_BROWSER, --pdf-browser PDF_BROWSER
                        browser for PDF files (default: 'xdg-open')
  -P PDF_FILE, --pdf-file PDF_FILE
                        exported PDF file (default: '%f.pdf')
  -W CHAR_WIDTH, --char-width CHAR_WIDTH
                        character width (default: '0' = automatic, unit: 'pt'
                        'in' 'mm' or 'cm')
  -A CHAR_ASPECT, --char-aspect CHAR_ASPECT
                        character aspect ratio = char width / char height
                        (default: '3/5', '1' = square grid)
  -S PAPER_SIZE, --paper-size PAPER_SIZE
                        portrait paper size width x height (default: 'A4' =
                        '210x297mm', unit: 'pt' 'in' 'mm' or 'cm')
  -Z, --landscape       turn page by 90 degrees (default: portrait)
  -L LEFT_MARGIN, --left-margin LEFT_MARGIN
                        left margin (default: '2cm', unit: 'pt' 'in' 'mm' or
                        'cm')
  -R RIGHT_MARGIN, --right-margin RIGHT_MARGIN
                        right margin (default: '2cm', unit: 'pt' 'in' 'mm' or
                        'cm')
  -T TOP_MARGIN, --top-margin TOP_MARGIN
                        top margin (default: '2cm', unit: 'pt' 'in' 'mm' or
                        'cm')
  -B BOTTOM_MARGIN, --bottom-margin BOTTOM_MARGIN
                        bottom margin (default: '2cm', unit: 'pt' 'in' 'mm' or
                        'cm')
  -C CORRECT_SIZES, --correct-sizes CORRECT_SIZES
                        correct character size and page margins (default: 'd'
                        = by default values, 'n' = no, 'f' = by correction
                        file)
  -K, --fake-margins    get left margin by blanks and top margin by empty
                        lines
```

REM Usage: no.bat infile.txt "Title of PDF"

echo %1 %2
wc -w %1

no.py %1 > no-%1
wc -w no-%1

no.py -t %1 > no-x2-%1
wc -w no-x2-%1

echo "PDF:" no-%1
REM https://openbookproject.googlecode.com/svn/tangle/html2pdf/reportlab_2_1/reportlab/tools/py2pdf/py2pdf.py
py2pdf.py --fontSize 10 --mode mono --title "%2" no-%1

echo "PDF:" no-x2-%1
REM http://two.pairlist.net/pipermail/reportlab-users/2007-February/005791.html
REM http://two.pairlist.net/pipermail/reportlab-users/attachments/20070213/80c61e82/attachment.obj
txt2pdf.py no-x2-%1

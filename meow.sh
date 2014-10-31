# Usage: meow.sh infile.txt "Title of PDF"

echo $1 $2
wc -w $1

meow.py $1 > meow-$1
wc -w meow-$1

meow.py -t $1 > meow-x2-$1
wc -w meow-x2-$1

echo "PDF:" meow-$1
# https://openbookproject.googlecode.com/svn/tangle/html2pdf/reportlab_2_1/reportlab/tools/py2pdf/py2pdf.py
py2pdf.py --fontSize 10 --mode mono --title "$2" meow-$1

echo "PDF:" meow-x2-$1
# http://two.pairlist.net/pipermail/reportlab-users/2007-February/005791.html
# http://two.pairlist.net/pipermail/reportlab-users/attachments/20070213/80c61e82/attachment.obj
txt2pdf.py meow-x2-$1

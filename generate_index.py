# Outputs the index.html file, which has links to read-only ipython notebooks via nbviewer.
import glob

def get_nbviewer_url(ipynb_file):
    return "http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/{0}".format(ipynb_file)

def write_index(ipynb_files):
    f = open("PRESENTATION_INDEX.md","w")
    f.write("<html><body><h1>Presentation iPython Notebook:</h1><ol>\n")
    for nb in ipynb_files:
        ipynb_url = get_nbviewer_url(nb)
        f.write("<li><a href='{0}'>{1}</a></li>\n".format(ipynb_url, nb))
    f.write("</ol></body></html>")
    f.close()

write_index(glob.glob("*.ipynb"))


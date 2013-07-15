# Outputs the index.html file, which has links to read-only ipython notebooks via nbviewer.
import glob

def get_nbviewer_url(ipynb_file):
    return "http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/{0}".format(ipynb_file)

def generate_index():
    ipynb_files = glob.glob("*.ipynb")
    ipynb_files.sort()
    index_list = ["\n"]
    for nb in ipynb_files:
        index_list.append("* [{0}]({1})\n".format(nb, get_nbviewer_url(nb)))
    return index_list

def find_index_start_and_end(readme):
    start_index = -1
    end_index = -1
    for index, line in enumerate(readme):
        if line.strip() == "# Presentation Index":
            start_index = index + 1
        elif start_index >= 0 and line.strip() == "---":
            end_index = index - 1
            break
    return (start_index, end_index)

readme = ""
with open("README.md", "r") as infile:
    readme = infile.readlines()

(start, end) = find_index_start_and_end(readme)
new_readme = readme[0:start] + generate_index() + readme[end:]

with open("README.md", "w") as outfile:
    outfile.writelines(new_readme)



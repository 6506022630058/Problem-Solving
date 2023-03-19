import os
import webbrowser
import networkx as nx
from flask import Flask, render_template
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename
from wtforms import FileField, SubmitField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'
app.config['UPLOAD_TEMPORARY'] = 'temporary/'

class UploadFileForm(FlaskForm):
    file = FileField('File',validators=[InputRequired()])
    submit = SubmitField('Upload File')

@app.route('/',methods = ['GET','POST'])
@app.route('/home',methods = ['GET','POST'])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_TEMPORARY'],secure_filename(file.filename)))
        copyfile('temporary/'+listDir('temporary'),'static/files/'+listDir('temporary'))
        readfile(listDir('static/files'))
        os.remove('temporary/'+listDir('temporary'))
        return "File has been uploaded",p1html()
    return render_template('index.html',form = form)

def listDir(dir):
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        return fileName

def readfile(filename):
    global lisnod
    global lisedg
    if filename.endswith('.txt') == False:filename += '.txt'
    lisnod,lisedg = [],[]
    filer = open('temporary/'+filename,'r')
    line = filer.readline().rstrip('\n').lower()
    while line != '':
        if len(line.split()) == 2:lisedg.append(tuple(swap(line.split())))
        elif len(line.split()) == 1:lisnod.append(line)
        line = filer.readline().rstrip('\n').lower()
    filer.close()
    network.add_nodes_from(lisnod)
    network.add_edges_from(lisedg)
    lisnod = network.nodes()
    print(lisnod)
    print(lisedg)

def copyfile(src,des):
    f1,f2 = open(src,'r'),open(des,'w')
    f1_content = f1.read()
    for line in f1_content:f2.write(line)
    f1.close()
    f2.close()

def p1html():
    content = '''
    <html lang="en">
    <head>
    <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
    <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
    <py-env>
        - matplotlib
        - networkx
    </py-env>
    <title>Page1</title>
    </head>
    <body>
        <div>
        <button onclick="document.getElementById('console').innerHTML = {0}">Show all nodes</button>
        </div>
        <div>
        {1}
        </div>
        <button onclick="document.getElementById('console').innerHTML = 'findpath()'">Find path</button>
        <div class="displayconsole">
            <p id="console">Hello</p>
        </div>
        <div style="width: 300%;margin-left: 25%;">
        <py-script>  
            import matplotlib.pyplot as plt
            import networkx as nx

            fig, ax = plt.subplots()
            network = nx.DiGraph()
            
            network.add_nodes_from({2})
            network.add_edges_from({3})
            
            nx.draw(network,with_labels=True,arrows=True,arrowstyle='->',arrowsize=15,pos=nx.circular_layout(network),node_size=1000,font_size=9)
            fig
        </py-script>
        </div>
    </body>
    </html>'''
    content = content.format(lisnod,createdropdown(),lisnod,lisedg)
    htmlcontent = content.format(**locals())
    outfile = open('p1.html','w')
    outfile.write(htmlcontent)
    outfile.close()
    webbrowser.open('file:///'+os.path.abspath('p1.html'))

def createdropdown():
    res = """
    <form>
    <select name="src1" id="src1" onchange="relation()">
    <option value="no" selected="selected">---Choose one---</option>
    """
    end = """
    </select>
    </form>
    """
    for i in lisnod:
        text = '<option value="{0}">{1}</option>'
        text = text.format(i,i)
        res = res+text
    res = res+end
    return res

def findpath(src,des):return [path for path in nx.all_simple_paths(network, source=src, target=des)]
def swap(l):return[l[1],l[0]]

if __name__ == "__main__":
    network = nx.DiGraph()
    app.run(debug=True)
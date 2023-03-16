import asyncio
from pyodide import create_proxy
#
#
def Setup_File_Listener():
    file_event = create_proxy(Process_File)
    e = document.getElementById("fasta_1")
    e.addEventListener("change", file_event, False)
#
#
async def Process_File(event):
    fileList = event.target.files.to_py()

    for f in fileList:
        data = await f.text()
        show_data(data)     #  OR do something else with the data
#
#        
def show_data(data):
    document.getElementById("outMsg").innerHTML = data

#   -----------------------------------------------------
Setup_File_Listener()
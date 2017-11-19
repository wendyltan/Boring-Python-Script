'''
a script that can easily transfer ppt to image or pdf or doc to pdf

'''
import os
from comtypes.client import CreateObject

def PPTtoImage(path_to_ppt, path_to_folder):
    if not (os.path.isfile(path_to_ppt) and os.path.isdir(path_to_folder)):
        raise "Please give valid paths!"
    powerpoint = CreateObject("Powerpoint.Application")
    # Needed for script to work, though I don't see any reason why...
    powerpoint.Visible = True
    powerpoint.Presentations.Open(path_to_ppt)
    # Or some other image types
    powerpoint.ActivePresentation.Export(path_to_folder, "JPG")
    powerpoint.Presentations[1].Close()
    powerpoint.Quit()

def PPTtoPDF(path_to_source_file, transfer_name, formatType = 32):
    powerpoint = CreateObject("Powerpoint.Application")
    powerpoint.Visible = True
    if transfer_name[-3:] != 'pdf':
        transfer_name = transfer_name + ".pdf"
    deck = powerpoint.Presentations.Open(path_to_source_file)
    deck.SaveAs(transfer_name, formatType) # formatType = 32 for ppt to pdf
    deck.Close()
    powerpoint.Quit()

def docToPdf(path_to_doc, transfer_name, format_type = 17):

    word = CreateObject('Word.Application')
    doc = word.Documents.Open(path_to_doc)
    doc.SaveAs(transfer_name, format_type)
    doc.Close()
    word.Quit()

if __name__ == '__main__':
    current_directory = os.getcwd()
    filename = ''


    choice = input("Give me your choice(1 for ppt to image,2 for ppt to pdf,3 for doc to pdf)")
    if(choice=="1"):
        filename = r'pptImage'
    elif(choice=="2"):
        filename =  r'pptPdf'
    elif(choice=="3"):
        filename =  r'docPdf'
    final_directory = os.path.join(current_directory,filename)

    if not os.path.exists(final_directory):
        os.makedirs(final_directory)
        os.chdir(filename)
    print(os.getcwd())

    original = input("Please enter original file name and put your file under this directory:\n")
    original_path = os.path.abspath(original)
    print(original_path)

    if(choice=="1"):
        PPTtoImage(original_path, final_directory)
    elif(choice=="2"):
        PPTtoPDF(original_path,final_directory)
    elif(choice=="3"):
        docToPdf(original_path,final_directory)
    print("Transfer success!")
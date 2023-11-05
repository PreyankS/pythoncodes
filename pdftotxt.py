import PyPDF2

pdffileobj=open('pdffilename.pdf', 'rb')
pdfreader=PyPDF2.PdfReader(pdffileobj)
all_text=""
for page in pdfreader.pages:
    text=page.extract_text()
    all_text+=text
pdffileobj.close()

with open(r"C:\Users\Admin\OneDrive - fulllocationaddress\\all_text.txt","w",encoding='utf-8') as file1:
    file1.write(all_text)
#pdffilename is whatever is the name of the pdf file that you want to convert to text.
#fulllocationaddress is to remind that we must copy and paste here the location in which the txtfile is located, in which the converted pdf will be stored.

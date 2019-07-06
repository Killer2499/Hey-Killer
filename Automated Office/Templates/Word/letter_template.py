from docx import Document
from docx.shared import Inches
from datetime import date
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
from docx.shared import Pt


document=Document()

obj_styles = document.styles
obj_charstyle = obj_styles.add_style('CommentsStyle', WD_STYLE_TYPE.CHARACTER)
obj_font = obj_charstyle.font
obj_font.size = Pt(16)
obj_font.name = 'Times New Roman'

#From Address
from_input=raw_input("From address:")

from_split=from_input.split(',')
from_name=from_split[0]

data=''
for i in range(1,len(from_split)):
    data=data+from_split[i]+" . "
    
data=data[:-2]


from_title_name=document.add_paragraph()
from_title_name.add_run(from_name, style = 'CommentsStyle').bold = True
from_title_name.bold=True
from_title_name.alignment =1 #0-L ,1-C, 2-R

from_address=document.add_paragraph(data)
from_address.name = 'Times New Roman'
from_address.size = Pt(14)
from_address.alignment =1


#Date
date_today=str(date.today())
year=int(date_today.split('-')[0])
month=int(date_today.split('-')[1])
day=int(date_today.split('-')[2])
date_words=date(day=day, month=month, year=year).strftime('%d %B %Y')
date=document.add_paragraph(date_words)
document.add_page_break()

#To Address
to_input=raw_input("To address:")
to_address=document.add_paragraph(to_input)

#Greetings
greeting_input=raw_input("Greetings:")
greetings=document.add_paragraph(greeting_input)

#Body
body_input=raw_input("Body of the Letter")
body=document.add_paragraph(body_input)

#Closing
closing_input=raw_input("Closing Greeting")
closing=document.add_paragraph(closing_input)


#Signature
signature=raw_input("Signature Path:")
if(signature):
    document.add_picture(signature,width=Inches(2),height=Inches(1))
else:
    pass

document.add_page_break()

#Saving Document
#location=raw_input("Save Document as")
location="Letter2.docx"
document.save(location)







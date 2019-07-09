from docx import Document
from docx.shared import Inches
from datetime import date
from docx.shared import RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH,WD_BREAK
from docx.enum.style import WD_STYLE
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_LINE_SPACING
from docx.shared import Pt
  
def cv():
    document = Document()

    paragraph_styles = document.styles
    paragraph_styles = paragraph_styles.add_style('ParagraphStyle',WD_STYLE_TYPE.PARAGRAPH)
    paragraph_font = paragraph_styles.font
    paragraph_font.size = Pt(12)
    paragraph_font.name = 'Segoe UI Historic'

    title_styles=document.styles
    title_styles = title_styles.add_style('TitleStyle',WD_STYLE_TYPE.CHARACTER)
    title_font=title_styles.font
    title_font.color.rgb=RGBColor(247,93,93)
    title_font.bold=True
    title_font.size=Pt(25)
    title_font.name='Segoe UI Historic'

    heading_styles=document.styles
    heading_styles = heading_styles.add_style('HeadingStyle',WD_STYLE_TYPE.CHARACTER)
    heading_font=heading_styles.font
    heading_font.color.rgb=RGBColor(247,93,93)
    heading_font.bold=True
    heading_font.size=Pt(15)
    heading_font.name='Segoe UI Historic'

    
    #name=raw_input("Name:")
    name='Sanath Singavarapu'
    name_title=document.add_paragraph()
    name_title=name_title.add_run(name,style="TitleStyle")
    name_title.size=Pt(40)

   
    #email=raw_input("Email:")
    #phone=raw_input("Phone:")
    email='sanathsingavarapu99@gmail.com'
    phone='+91-8919142764'

    contact_info="Email: "+email+", Mobile: "+phone
    contact=document.add_paragraph(contact_info,style='ParagraphStyle')

    spacing = contact.add_run()
    spacing.add_break(WD_BREAK.LINE)

    

    #skills_info=raw_input("Skills:")
    skills_info='Html,Css,Js,Jquery,Php,Mysql,T-sql,U-sql,Python,C,C++,Bootstrap,PL/SQL,NO-SQL,Power Bi,Azure Data Factory,Azure Data Bricks,React Native,React Js,Arduino,Raspberry Pi,Adobe Photoshop'
    skills_header=document.add_paragraph().add_run("Skills",style="HeadingStyle")
    skills=document.add_paragraph(skills_info,style='ParagraphStyle')

    
    def add_experience(experience_count):
        if (experience_count==0):
            experience_header=document.add_paragraph().add_run("Experience",style="HeadingStyle")
    
        company_info=raw_input("Company Name")
        experience=document.add_paragraph()
        company=experience.add_run(company_info)
        
        spacing = experience.add_run()
        spacing.add_break(WD_BREAK.LINE)
        
        role_info=raw_input("Role:")
        role=experience.add_run(role_info)
        
        spacing = experience.add_run()
        spacing.add_break(WD_BREAK.LINE)
        
        time_period_info=raw_input("Time Period:")
        time_period=experience.add_run(time_period_info)

        experience_count+=1
        if(experience_count>=1):
            option=raw_input("Wanna Add More(y/n):")
            if option=='y' or option=='yes':
                add_experience(1)
            else:
                pass
    add_experience(0)
    document.save('cv.docx')



cv()

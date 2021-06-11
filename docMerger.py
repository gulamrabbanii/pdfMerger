rom docx import Document

doc1 = Document('1.docx')
doc2 = Document('2.docx')
for element in doc2.element.body:
    doc1.element.body.append(element)
doc1.save('new.docx')

from docxtpl import DocxTemplate


def create_training_sheet(
    class_name, subject_name, tpl_name="tpl.docx", *marks
):
    doc = DocxTemplate(tpl_name)
    context = {
        "class_name": class_name,
        "subject_name": subject_name,
        "marks": [
            {"num": num + 1, "fio": fio, "mark": mark}
            for num, (fio, mark) in enumerate(
                sorted(marks, key=lambda x: x[0])
            )
        ],
    }
    doc.render(context)
    doc.save("res.docx")

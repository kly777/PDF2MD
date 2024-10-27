from pypdf import PdfReader

reader = PdfReader("pho.pdf")
last_page = 0
def del_enter(text):
    processed_lines = text
    return processed_lines.replace(' \n', '').replace("\n", "\n\n")
def format_number(number):
    return str(number).zfill(3)
def out_md(title,content,page_number):
    number =format_number(page_number)
    with open(number+'-'+title+'.md', "w", encoding="utf-8") as f:
        print(content)
        f.writelines(content)
def get_page_content_from_to(start, end):
    print("-" * 40)
    content=""
    if start == end:
        end+=1
    for i in range(start, end):
        content+=del_enter(reader.pages[i].extract_text())
    return content

title='000'
def get_outlines(outline):
        global last_page,title
        for outline_item in outline:
            if isinstance(outline_item, list):
                get_outlines(outline_item)
            else:
                page_number = reader.get_destination_page_number(outline_item)

                content=get_page_content_from_to(last_page,page_number)

                out_md(title,content,page_number)
                # 打印大纲项的标题和对应的页码
                print(f"Title: {title}, Page Number: {page_number}")
                title = outline_item.title
                last_page = page_number

get_outlines(reader.outline)



import os
import markdown
from ebooklib import epub

def _convert_files(md_files, epub_file, book_id, book_title, book_author):
    book = epub.EpubBook()
    book.set_identifier(book_id)
    book.set_title(book_title)
    book.set_language('en')
    book.add_author(book_author)
    chap_num = 1
    chapters = []
    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        html_content = markdown.markdown(content)

        chapter = epub.EpubHtml(title=f'Chapter {chap_num}', file_name=f'chapter_{chap_num}.xhtml', lang='en')
        chapter.content = html_content
        chapters.append(chapter)
        chap_num += 1
        book.add_item(chapter)
    
    book.toc = (chapters)
    book.spine = ['nav'] + chapters
    
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    epub.write_epub(epub_file, book)





"""
Convert a Markdown file or all Markdown files in a folder to an EPUB file.

:param md_source: Path to a Markdown file or a folder containing Markdown files. Cannot be empty.
:param epub_file: Path where the resulting EPUB file will be saved.
:param book_id: Unique identifier for the book (optional).
:param book_title: Title of the book (optional).
:param book_author: Author of the book (optional).
"""
def convert(md_source, epub_file = None, book_id = None, book_title = None, book_author = None):
    if not md_source:
        raise ValueError("You must specify a Markdown file or a folder containing Markdown files.")

    file_list = []
    if os.path.isfile(md_source):
        file_path_no_ext = os.path.splitext(md_source)[0]
        if not epub_file:
            epub_file = file_path_no_ext + '.epub'
        if not book_title:
            book_title = os.path.basename(file_path_no_ext).capitalize()
    else:
        if not epub_file:
            epub_file = os.path.join(md_source, 'output.epub')
        if not book_title:
            book_title = os.path.basename(md_source).capitalize()
        for root, _, files in os.walk(md_source):
            for file in files:
                if file.endswith('.md'):
                    file_list.append(os.path.join(root, file))
    
    if not book_id:
        book_id = f'{book_title}-{os.urandom(4).hex()}'
    
    if not book_author:
        book_author = os.getenv('USER')
        if not book_author:
            book_author = os.getenv('USERNAME', 'Unknown Author')
    
    _convert_files(file_list, epub_file, book_id, book_title, book_author)
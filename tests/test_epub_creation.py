import md2epub
import os

def create_md_file(file_path, content = '**This is a test line**'):
    with open(file_path, 'w') as md_file:
        md_file.write(content)

def test_file_to_epub(tmp_path):
    md_file_path = f'{tmp_path}/input_md_file.md'
    create_md_file(md_file_path)
    md2epub.convert(md_file_path)
    assert os.path.exists(f'{tmp_path}/input_md_file.epub')


def create_md_dir(root_dir):
    md_dir_path = f'{root_dir}/md_folder'
    os.makedirs(md_dir_path)
    create_md_file(f'{md_dir_path}/md_file1.md', '**chapter1 content**')
    create_md_file(f'{md_dir_path}/md_file2.md', '**chapter2 content**')
    return md_dir_path

def test_dir_to_epub(tmp_path):
    md_dir_path = create_md_dir(tmp_path)
    md2epub.convert(md_dir_path);
    assert os.path.exists(f'{md_dir_path}/output.epub')


def test_file_to_epub_with_path(tmp_path):
    md_file_path = f'{tmp_path}/input_md_file.md'
    create_md_file(md_file_path)
    md2epub.convert(md_file_path, f'{tmp_path}/test.epub')
    assert os.path.exists(f'{tmp_path}/test.epub')

def test_dir_to_epub_with_path(tmp_path):
    md_dir_path = create_md_dir(tmp_path)
    op_path = f'{tmp_path}/mybook.epub'
    md2epub.convert(md_dir_path, op_path);
    assert os.path.exists(op_path)

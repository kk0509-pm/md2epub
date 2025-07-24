import argparse
from .main import convert

def main():
    parser = argparse.ArgumentParser(description="Convert Markdown files to EPUB books.")
    parser.add_argument('md_source', type=str, help='Path to input Markdown file or directory containing Markdown files.')
    parser.add_argument('-o', '--output', type=str, help='Path to output EPUB file.', required=False)

    args = parser.parse_args()

    print(f"Converting '{args.md_source}' ...")
    convert(md_source=args.md_source, epub_file=args.output)


if __name__ == "__main__":
    main()

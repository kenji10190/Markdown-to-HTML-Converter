import sys
import markdown

args = sys.argv

if len(args) != 4:
    print("コマンドが違うようです。例 python3 file-converter.py markdown xxx.md xxx.htmlのように入力してください。")
    sys.exit()

script, command, input_file, output_file = args

if command != "markdown":
    print("2番目の引数が違うようです。markdownと入力してください。")
    sys.exit()

if not input_file.endswith(".md"):
    print("3番目の引数にはMDファイルを指定してください。")
    sys.exit()

if not output_file.endswith(".html"):
    print("4番目の引数には作成したいhtmlファイルの名前を入力してください。例 index.html")
    sys.exit()

with open(input_file, encoding="utf-8") as f:
    contents = f.read()
    html = markdown.markdown(contents)

with open(output_file, 'w') as f:
    f.write(html)
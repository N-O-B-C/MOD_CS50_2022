import re

def main():
    print(parse(input("HTML: ")))

def parse(HTML):
    if re.search(r"<iframe(.)*><\/iframe>",HTML):
        url_patern = re.search(r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/([a-z_A-Z_0-9]+))",HTML)
        if url_patern:
            url_grouging = url_patern.groups()
            return "https://youtu.be/" + url_grouging[3]

if __name__ == "__main__":
    main()
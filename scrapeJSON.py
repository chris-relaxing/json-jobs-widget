#!/home/bluegala/virtualenv/cgi/3.6/bin/python

import requests
#  This script is for gathering the JSON available at the following API, cleaning
#  the data and delivering it to JavaScript.

def main():
    url = r'https://api.stagingjobshq.com/madgexWidgetJobs.php?callback=displayJobs&city=Moorhead&state=Minnesota'
    r = requests.get(url, verify=False)  # ssl, don't verify
    page_source = r.text.strip()

    # data needs to be cleaned for JavaScript JSON.parse:
    # 1. remove the function wrapping (displayJobs( ))
    # 2. replace all right and left quote characters (u"\u2018"|u"\u2019" --> \')

    page_source = page_source.replace(u"\u2018", "\\'").replace(u"\u2019", "\\'")
    page_source = page_source.replace('displayJobs(', '').rstrip(')').rstrip()

    print("Content-type: text/html\n\n")
    # print("length: ", len(page_source))
    print(page_source)
    return page_source


if __name__ == '__main__':
    main()

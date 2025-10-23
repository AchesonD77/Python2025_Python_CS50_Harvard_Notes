"""
Your job: from an HTML snippet, find a YouTube <iframe>’s src (in one of the embed URL forms)
and convert it to a short youtu.be link. If nothing is found, return None.

1) Why re (Regular Expressions)?
HTML is a structured string. You only need to find one pattern:
an <iframe> with a src that starts with http(s)://(www.)?youtube.com/embed/…. A small regex is perfect
(the assignment even suggests using re). For full-fledged HTML parsing you’d normally use an HTML parser (e.g., BeautifulSoup),
but the pset forbids extra libraries and the pattern is constrained.

2) The regex pattern (line by line)
pat = r'<iframe[^>]*\bsrc="https?://(?:www\.)?youtube\.com/embed/([^"]+)"'

<iframe[^>]* — start at an <iframe tag, then any attributes until we see src
\bsrc=" ... " — ensure we hit the src="..."
https?:// — http:// or https://
(?:www\.)? — optional www.
youtube\.com/embed/ — exactly that path
([^"]+) — capture everything that follows up to the closing double quote
→ that’s our “video part” (often just the ID, but could include ?rel=0 etc.)

3) Normalizing to youtu.be/<id>
Once we captured the “video part”, we trim off any query string (?…) or extra path (/…) just in case, then return https://youtu.be/<id>.

4) Return None when there’s no match
If the regex doesn’t find a match, we return None exactly as the spec asks.

====================================================================================

pat = r'<iframe[^>]*\bsrc="https?://(?:www\.)?youtube\.com/embed/([^"]+)"'
m = re.search(pat, s, flags=re.IGNORECASE)

if not m:
    return None

pat (Pattern): 这是前面我们解释过的正则表达式。它定义了要查找的 YouTube 嵌入式 <iframe> 标签的结构。

关键点： ([^"]+) 部分是一个捕获组 (Capture Group)，它的目的是捕获视频 ID 部分（即 youtube.com/embed/ 之后、下一个双引号之前的任何内容）。

re.search(pat, s, ...):

这是 re 模块中的搜索函数，用于在整个字符串 s 中查找与 pat 匹配的第一个位置。

s 是待搜索的源字符串（通常是 HTML 内容）。

flags=re.IGNORECASE: 这是一个标志位，告诉正则表达式引擎在匹配时忽略大小写。这意味着它可以匹配 YouTube.com、YOUTUBE.COM 或 youtube.com。

m: 如果找到匹配项，re.search 返回一个 Match Object（匹配对象）并赋值给 m；如果未找到，则返回 None。

if not m: return None: 如果没有找到匹配的 <iframe> 标签，函数立即返回 None，结束执行。

"""


import re


def main():
    html = input("HTML: ")
    print(parse(html))


def parse(s : str) -> str | None:
    """
    Accepts these forms (protocol + optional www):
      - http://youtube.com/embed/<id>
      - https://youtube.com/embed/<id>
      - https://www.youtube.com/embed/<id>

    Assumptions per spec:
      - The src value is wrapped in double quotes.
      - At most one such URL appears in the input.
    """

    # 1) Find an <iframe ... src="..."> whose src matches youtube.com/embed/<...>
    #    - <iframe[^>]*      : match an iframe tag, any attributes before src
    #    - \bsrc=" ... "     : find src=" ... " (double quotes as required)
    #    - https?://         : http or https
    #    - (?:www\.)?        : optional "www."
    #    - youtube\.com/embed/: literal domain/path
    #    - ([^"]+)           : capture everything up to the next quote (the video part)

    pat = r'<iframe[^>]*\bsrc="https?://(?:www\.)?youtube\.com/embed/([^"]*)"'
    m = re.search(pat, s, flags=re.IGNORECASE)
    if not m:
        return None

    # 2) extract
    raw = m.group(1)
    video_id = raw.split("?", 1)[0].split("/", 1)[0]
    if not video_id:
        return None

    # 3) Return short form
    return f"https://youtu.be/{video_id}"


if __name__ == "__main__":
    main()


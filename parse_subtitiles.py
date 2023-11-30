import srt
import re

with open('Her.srt') as file:
    subtitles = srt.parse(file.read())

ln = 0
le = 0
quotes = []


def clean_quote(raw_quote):
    quote = raw_quote.replace('\n', ' ').strip().lstrip("- ")
    return quote

# start from index 137
for subtitle in subtitles:
    if subtitle.index >= 137:
        if '<i>' in subtitle.content:
            # use regex to match what is in <i> tags (could include \n)
            pattern = re.compile(r'<i>(.*?)</i>', re.DOTALL)
            match = pattern.search(subtitle.content)
            if match:
                quote_piece = clean_quote(match.group(1))
                if (subtitle.index - ln == 1) and \
                    (subtitle.start.seconds - le <= 2):
                    quotes[-1] += f" {quote_piece}"
                else:
                    quotes.append(quote_piece)
                ln = subtitle.index
                le = subtitle.end.seconds

with open("fortunes/samantha", "w", encoding='utf-8') as f:
    f.write("\n%\n".join(quotes))

print("Quotes have been compiled in ./fortunes/samantha")

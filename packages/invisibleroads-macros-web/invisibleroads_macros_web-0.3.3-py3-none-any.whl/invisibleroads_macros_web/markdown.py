import re

from markdown2 import markdown


SINGLE_PARAGRAPH_PATTERN = re.compile(r'^<p>((?:(?!<p>).)*)</p>$', re.DOTALL)
EXTRAS = [
    'break-on-newline',
    'code-friendly',
    'cuddled-lists',
    'fenced-code-blocks',
    'footnotes',
    'markdown-in-html',
    'strike',
    'target-blank-links',
    'tables',
    'use-file-vars',
    'task_list']


def get_html_from_markdown(text, extras=EXTRAS):
    return markdown(text, extras=extras).strip()


def remove_single_paragraph(html):
    return SINGLE_PARAGRAPH_PATTERN.sub(r'\g<1>', html)


def remove_parent_paragraphs(html):
    return html.replace('<p><', '<').replace('></p>', '>')

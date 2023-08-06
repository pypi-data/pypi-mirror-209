import datetime
import random
import string
import codecs
import subprocess
import tempfile


DATE_FORMAT = '%Y-%m-%d'
DATE_TIME_SEPARATOR = 'T'
DT_FORMAT = '{}{}%H:%M:%S'.format(DATE_FORMAT, DATE_TIME_SEPARATOR)

# mapping of short ISO 639 language codes to their longer form
# which is the identifier used for tesseract OCR language packages
LANGUAGES = {
  'af': 'afr',
  'am': 'amh',
  'ar': 'ara',
  'as': 'asm',
  'az': 'aze',
  'aze_cyrl': 'aze_cyrl',
  'be': 'bel',
  'bn': 'ben',
  'bo': 'bod',
  'bs': 'bos',
  'br': 'bre',
  'bg': 'bul',
  'ca': 'cat',
  'ceb': 'ceb',
  'cs': 'ces',
  'cze': 'ces',
  'chi': 'chi_sim',
  'zh': 'chi_sim',
  'chi_tra': 'chi_tra',
  'chr': 'chr',
  'co': 'cos',
  'cy': 'cym',
  'da': 'dan',
  'de': 'deu',
  'ger': 'deu',
  'dv': 'div',
  'dz': 'dzo',
  'el': 'ell',
  'gre': 'ell',
  'en': 'eng',
  'enm': 'enm',
  'eo': 'epo',
  'equ': 'equ',
  'et': 'est',
  'eu': 'eus',
  'baq': 'eus',
  'fa': 'fas',
  'fo': 'fao',
  'fil': 'fil',
  'fi': 'fin',
  'fr': 'fra',
  'fre': 'fra',
  'frk': 'frk',
  'frm': 'frm',
  'fy': 'fry',
  'gd': 'gla',
  'ga': 'gle',
  'gl': 'glg',
  'grc': 'grc',
  'gu': 'guj',
  'ht': 'hat',
  'he': 'heb',
  'iw': 'heb',
  'hi': 'hin',
  'hr': 'hrv',
  'hu': 'hun',
  'hy': 'hye',
  'arm': 'hye',
  'iu': 'iku',
  'id': 'ind',
  'in': 'ind',
  'is': 'isl',
  'ice': 'isl',
  'it': 'ita',
  'ita_old': 'ita_old',
  'jv': 'jav',
  'ja': 'jpn',
  'kn': 'kan',
  'ka': 'kat',
  'geo': 'kat',
  'kat_old': 'kat_old',
  'kk': 'kaz',
  'km': 'khm',
  'ky': 'kir',
  'kmr': 'kmr',
  'ko': 'kor',
  'kor_vert': 'kor_vert',
  'lo': 'lao',
  'la': 'lat',
  'lv': 'lav',
  'lt': 'lit',
  'lb': 'ltz',
  'ml': 'mal',
  'mr': 'mar',
  'mk': 'mkd',
  'mac': 'mkd',
  'mt': 'mlt',
  'mn': 'mon',
  'mi': 'mri',
  'mao': 'mri',
  'ms': 'msa',
  'may': 'msa',
  'my': 'mya',
  'bur': 'mya',
  'ne': 'nep',
  'nl': 'nld',
  'dut': 'nld',
  'no': 'nor',
  'oc': 'oci',
  'or': 'ori',
  'osd': 'osd',
  'pa': 'pan',
  'pl': 'pol',
  'pt': 'por',
  'ps': 'pus',
  'qu': 'que',
  'ro': 'ron',
  'rum': 'ron',
  'ru': 'rus',
  'sa': 'san',
  'si': 'sin',
  'sk': 'slk',
  'slo': 'slk',
  'sl': 'slv',
  'sd': 'snd',
  'es': 'spa',
  'spa_old': 'spa_old',
  'sq': 'sqi',
  'alb': 'sqi',
  'sr': 'srp',
  'scc': 'srp',
  'srp_latn': 'srp_latn',
  'su': 'sun',
  'sw': 'swa',
  'sv': 'swe',
  'syr': 'syr',
  'ta': 'tam',
  'tt': 'tat',
  'te': 'tel',
  'tg': 'tgk',
  'th': 'tha',
  'ti': 'tir',
  'to': 'ton',
  'tr': 'tur',
  'ug': 'uig',
  'uk': 'ukr',
  'ur': 'urd',
  'uz': 'uzb',
  'uzb_cyrl': 'uzb_cyrl',
  'vi': 'vie',
  'yi': 'yid',
  'yo': 'yor',
}


def random_string(length=32, characters=None):
    if characters is None:
        characters = string.ascii_letters + string.digits + '.-_+/='
    return ''.join(random.choices(characters, k=length))


def random_id():
    return random_string(24, string.ascii_lowercase + string.digits)


def human_readable_size(size):
    rem = size
    units = ['', 'K', 'M', 'G', 'T']
    unit = 0

    while rem >= 1024:
        rem /= 1024.
        unit += 1

    return str(round(rem, 2)) + ' ' + units[unit] + 'b'


def date_from_str(text):
    return datetime.datetime.strptime(text, DATE_FORMAT).date()


def readable_code(code, sep=' '):
    groupsize = 2
    for gs in [4, 3, 5]:
        if len(code) % gs == 0:
            groupsize = gs
            break

    result = ''
    for idx, c in enumerate(code):
        if idx > 0 and idx % groupsize == 0:
            result += sep
        result += c
    return result


def parse_duration(text):
    if not text.startswith('P'):
        raise ValueError('Not a ISO 8601 duration')

    pos = 1
    value = ''
    days = 0
    seconds = 0

    while pos < len(text):
        if text[pos] == 'T':
            pass
        elif text[pos] in 'YDWHMS':
            if text[pos] == 'Y':
                days += int(value)*365  # this is weird
            elif text[pos] == 'W':
                days += int(value)*7
            elif text[pos] == 'D':
                days += int(value)
            elif text[pos] == 'H':
                seconds += int(value)*3600
            elif text[pos] == 'M':
                seconds += int(value)*60
            elif text[pos] == 'S':
                seconds += int(value)
            value = ''
        elif text[pos] in string.digits:
            value += text[pos]
        else:
            raise ValueError(f"{text} is not a ISO 8601 duration. First problem at '{text[pos]}'.")
        pos += 1

    return datetime.timedelta(days=days, seconds=seconds)


def parse_size(text, fallback=0):
    text = text.lower().strip()
    factor = 1
    try:
        for postfix, f_ in [('g', 1024*1024*1024), ('m', 1024*1024), ('k', 1024), ('b', 1)]:
            if text.endswith(postfix):
                text = text[:-1]
                factor = f_
                break
        return int(text)*factor
    except ValueError:
        return fallback


def to_utf8(raw):
    if isinstance(raw, str):
        return raw
    encoding = None
    strip_from = 1

    if raw.startswith(codecs.BOM_UTF8):
        encoding = 'utf-8'
    elif raw.startswith(codecs.BOM_UTF16_BE):
        encoding = 'utf-16-be'
    elif raw.startswith(codecs.BOM_UTF16_LE):
        encoding = 'utf-16-le'
    elif raw.startswith(codecs.BOM_UTF32_BE):
        encoding = 'utf-32-be'
    elif raw.startswith(codecs.BOM_UTF32_LE):
        encoding = 'utf-32-le'
    else:
        # just guessing
        encoding = 'utf-8'
        strip_from = 0

    try:
        text = str(raw, encoding=encoding).strip()
        return text[strip_from:]  # drop the BOM
    except UnicodeError:
        pass
    return None


def get_language_from_filename(fn):
    parts = fn.stem.rsplit('-', 1)
    if len(parts) != 2:
        return None
    lang = LANGUAGES.get(parts[1], parts[1])
    if lang not in LANGUAGES.values():
        return None
    return lang


def edit_fulltext_externally(version, program):
    to_edit = "\n".join([part.fulltext for part in version.parts])
    edited = to_edit

    with tempfile.NamedTemporaryFile('w+t', encoding='utf-8', newline="\n") as tf:
        tf.write(to_edit)
        tf.flush()
        subprocess.run(program + [tf.name])
        tf.seek(0)
        edited = tf.read()

    if edited != to_edit:
        for part in version.parts:
            part.technical.fulltext = ''
        version.parts[0].technical.fulltext = edited

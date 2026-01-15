import re
from urllib.parse import urlparse

URL_REGEX = re.compile(r"(https?://\S+|www\.\S+)", re.IGNORECASE)

SHORTENERS = {
    "bit.ly", "tinyurl.com", "t.co", "goo.gl", "ow.ly", "is.gd", "buff.ly", "cutt.ly"
}

def extract_urls(text: str):
    return URL_REGEX.findall(text or "")

def has_ip_url(url: str) -> int:
    # e.g. http://192.168.0.1/login
    return 1 if re.search(r"https?://\d{1,3}(\.\d{1,3}){3}", url) else 0

def suspicious_url_score(urls):
    score = 0
    for u in urls:
        uu = u if u.startswith("http") else "http://" + u
        parsed = urlparse(uu)
        domain = (parsed.netloc or "").lower()

        if "@" in u: score += 1
        if ".." in u: score += 1
        if u.count("//") > 1: score += 1
        if has_ip_url(uu): score += 2
        if any(s in domain for s in SHORTENERS): score += 2
        if "-" in domain: score += 1
        if len(u) > 75: score += 1
        if parsed.scheme not in ("http", "https"): score += 1

    return score

def extra_security_features(text: str):
    text = text or ""
    urls = extract_urls(text)

    feats = {
        "num_urls": len(urls),
        "suspicious_url_score": suspicious_url_score(urls),
        "has_urgent_words": int(bool(re.search(r"\burgent|immediately|act now|verify\b", text, re.I))),
        "has_threat_words": int(bool(re.search(r"\baccount will be closed|suspended|locked\b", text, re.I))),
        "has_money_words": int(bool(re.search(r"\bpayment|bank|invoice|transaction\b", text, re.I))),
        "has_login_words": int(bool(re.search(r"\blogin|sign in|password|credentials\b", text, re.I))),
        "has_attachment_words": int(bool(re.search(r"\battachment|attached|document\b", text, re.I))),
        "has_html_tags": int(bool(re.search(r"<html|<body|<a\s", text, re.I))),
    }
    return feats

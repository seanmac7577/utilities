import requests as _r

def curl_to_url_and_headers(cmd_raw):
    cmd = cmd_raw.strip()
    (base_cmd, quoted_url, header_section) = cmd.split(' ', 2)

    # URL
    assert quoted_url.startswith('"')
    assert quoted_url.endswith('"')
    url = quoted_url[1:-1]

    # headers
    prefix = '-H '
    assert header_section.startswith(prefix)
    raw_headers = header_section[len(prefix):].split(' ' + prefix)
    
    header_dict = {}
    
    for header in raw_headers:
        assert header.startswith('"')
        assert header.endswith('"')
        header_unquoted = header[1:-1]
        name, value = header_unquoted.split(': ')
        header_dict[name] = value

    return (url, header_dict)

def compare_dicts(a, b):
    keyset_a = set(a.keys())
    keyset_b = set(b.keys())

    if (keyset_a == keyset_b):
        print 'keys match'
    else:
        print 'keys only in left:', (keyset_a - keyset_b)
        print 'keys only in right:', (keyset_b - keyset_a)

url_b, h_b = curl_to_url_and_headers(open('req_b').read())
url_c, h_c = curl_to_url_and_headers(open('req_c').read())

#r = _r.get(url, headers=h)

compare_dicts(h_b, h_c)



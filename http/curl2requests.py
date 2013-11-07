import requests as _r

class HttpRequest:
    def __init__(self, cmd_raw):
        cmd = cmd_raw.strip()
        (base_cmd, quoted_url, header_section) = cmd.split(' ', 2)

        # URL
        assert quoted_url.startswith('"')
        assert quoted_url.endswith('"')
        self.url = quoted_url[1:-1]

        # headers
        prefix = '-H '
        assert header_section.startswith(prefix)
        raw_headers = header_section[len(prefix):].split(' ' + prefix)

        self.header_dict = {}

        for header in raw_headers:
            assert header.startswith('"')
            assert header.endswith('"')
            header_unquoted = header[1:-1]
            name, value = header_unquoted.split(': ')
            self.header_dict[name] = value

    def __repr__(self):
        s = ['{0}: {1}'.format(k, self.header_dict[k])
             for k in sorted(self.header_dict.keys())]
        return ('URL: {0}\n'.format(self.url) + '\n'.join(s))

def compare_dicts(a, b):
    keyset_a = set(a.keys())
    keyset_b = set(b.keys())

    if (keyset_a == keyset_b):
        print 'keys match'
    else:
        print 'keys only in left:', (keyset_a - keyset_b)
        print 'keys only in right:', (keyset_b - keyset_a)

req = HttpRequest(open('r0_alt').read())
print req
#url_c, h_c = curl_to_url_and_headers(open('req_c').read())

#r = _r.get(url_b, headers=h_b)
#compare_dicts(h_b, h_c)




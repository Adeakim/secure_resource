import re
def email_parser(email):
    handler=['username','domain']
    pattern=re.compile(r"(^[a-z]+[a-z+]+[a-z0-9]+@[a-z][a-z0-9]+\.com$)")
    val=pattern.search(email)
    if val:
        splitter=re.split('@',email)
        result={k:v for (k,v)in zip(handler,splitter)}
        return result
    else:
        return None
    

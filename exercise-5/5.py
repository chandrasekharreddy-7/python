''' Create a function shift that rotates the string left by acount and then right by
ccount.
Example
shift('NinjaHattori') -> 'NinjaHattori'
shift('NinjaHattori', acount=3) -> 'jaHattoriNin'
shift('NinjaHattori', ccount=3) -> 'oriNinjaHatt'
shift('NinjaHattori', ccount=3, acount=3) -> 'NinjaHattori'
shift('NinjaHattori', ccount=3, acount=6) -> 'jaHattoriNin'
shift('NinjaHattori', ccount=6, acount=3) -> 'oriNinjaHatt' '''
def shift(s,ccount,acount):
    s = s[acount:] + s[:acount]
    s = s[-ccount:] + s[:-ccount]
    return s
print(shift("NinjaHattori",0,3)) 
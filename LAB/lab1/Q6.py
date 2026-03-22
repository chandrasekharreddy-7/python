def shift(s, ccount, acount):
    s = s[acount:] + s[:acount]
    s = s[-ccount:] + s[:-ccount]
    return s
print(shift("NinjaHattori", 0, 3))
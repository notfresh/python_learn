from string import Template
template_string = '${who} likes ${what}'
s = Template(template_string)
d = {'who': 'Tim', 'what': 'kung pao'}
s2 =  s.substitute(d)
print(s2)

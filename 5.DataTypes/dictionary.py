colors = {
	'hruška': 'zelená',
    'jablko': 'červená',
    'meloun': 'zelená',
    'švestka': 'modrá',
    'ředkvička': 'červená',
    'zelí': 'zelená',
    'mrkev': 'červená',
}

week_colors = dict(colors)

for key in week_colors:
	week_colors[key] = 'černo-hnědo-' + week_colors[key]

print(colors)
print(colors['jablko'])
print(week_colors['jablko'])
print(week_colors)

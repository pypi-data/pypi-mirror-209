from jinja2 import Environment, FileSystemLoader


template = env.get_template('template.html')


html = template.render(tab_text='Data Quality Report', Some_heading='Data Quality Report')

with open('jinga_report.html', 'w') as f:
    f.write(html)


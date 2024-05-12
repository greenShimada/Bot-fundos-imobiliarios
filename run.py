import subprocess

with open("path.txt", "r") as file:
	path = file.read().strip()

subprocess.run(['scrapy', 'runspider', path, '-o', './output/result.json'])


#//scrapy runspider srpy_fundosImobil/srpy_fundosImobil/spiders/SpiderFundos.py -o output.json

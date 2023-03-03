
# pip install rpa
# apt install php

import rpa as r

r.init(chrome_browser=True)
import time
r.url('https://www.google.com')
time.sleep(5)
r.type('//*[@name="q"]', 'decentralisation[enter]')
print(r.read('result-stats'))
r.snap('page', 'results.png')
r.close()

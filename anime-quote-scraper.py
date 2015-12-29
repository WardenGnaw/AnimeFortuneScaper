import sys
import requests
import textwrap
import time
from bs4 import BeautifulSoup

def main():
   for i in range(0, 78):
      time.sleep(5) 
      response = requests.get("http://www.less-real.com/quotes?p=" + str(i) + "&s=popular&p_p=100&p_m=click&open_in=new_window")
      if int(response.status_code) == 200:
         bs = BeautifulSoup(response.content, "lxml")
         quotes = bs.findAll('div', {'class' : 'quote'})
         for quote in quotes:
            quoteText = quote.find('span', {'class' : 'quoteText'})
            quoteList = textwrap.wrap(quoteText.text.encode('utf-8').strip(), width=80)

            for q in quoteList:
               print q

            quoteData = quote.findAll('a')
            temp = True
            for data in quoteData: 
               if temp:
                  sys.stdout.write('          - ')
                  temp = False
               else:
                  sys.stdout.write(' ')
               sys.stdout.write(data.text.encode('utf-8').strip())
            print '\n%' 
   return 0

if __name__ == "__main__":
   sys.exit(main())

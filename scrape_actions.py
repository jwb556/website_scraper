import urllib2
from bs4 import BeautifulSoup
from scrape_data import * 

def main():
  ins = instructions_from_file_read()

  html_string = html_grab(ins[0]) 
  soup = BeautifulSoup(html_string, 'html.parser') 

  #soup_debug(soup)			#debugging

  tag = ins[1][:-1]
  attr_name = ins[2][:-1]
  attr_value = ins[3][:-1]

  attr_name2 = ins[4][:-1]
  attr_value2 = ins[5][:-1]

  attr_name3 = ins[6][:-1]
  attr_value3 = ins[7][:-1]

  soup_filtered1 = soup.find_all(tag, attrs={attr_name:attr_value})
  soup_filtered2 = soup.find_all(tag, attrs={attr_name2:attr_value2})
  soup_filtered3 = soup.find_all(tag, attrs={attr_name3:attr_value3})

  print tag
  print attr_name
  print attr_value

  field_list = []
  count = 0

  for elements in soup_filtered1:
    temp_field = field()
    temp_attrs = {'data-tn-element':'jobTitle'}
    temp_title = elements.find('a', attrs=temp_attrs).text
    temp_date = elements.find('span', attrs={'class':'date'}).text
    temp_location = elements.find('span', attrs={'class':'location'}).text
    temp_company = elements.find('a',
attrs={'data-tn-element':'companyName'}).text

    temp_field.set_text(temp_title)
    temp_field.set_date(temp_date)
    temp_field.set_location(temp_location)
    temp_field.set_company(temp_company)

    field_list.append(temp_field) 
    #print elements
    count = count+1

  for elements in soup_filtered2:
    temp_field = field()
    temp_attrs = {'data-tn-element':'jobTitle'}
    temp_title = elements.find('a', attrs=temp_attrs).text
    temp_date = elements.find('span', attrs={'class':'date'}).text
    temp_location = elements.find('span', attrs={'class':'location'}).text
    temp_company = elements.find('a',
attrs={'data-tn-element':'companyName'}).text

    temp_field.set_text(temp_title)
    temp_field.set_date(temp_date)
    temp_field.set_location(temp_location)
    temp_field.set_company(temp_company)

    field_list.append(temp_field) 
    #print elements
    count = count+1
  
  for elements in soup_filtered3:
    temp_field = field()
    temp_attrs = {'data-tn-element':'jobTitle'}
    temp_title = elements.find('a', attrs=temp_attrs).text
    temp_date = elements.find('span', attrs={'class':'date'}).text
    temp_location = elements.find('span', attrs={'class':'location'}).text
    temp_company = elements.find('a',
attrs={'data-tn-element':'companyName'}).text

    temp_field.set_text(temp_title)
    temp_field.set_date(temp_date)
    temp_field.set_location(temp_location)
    temp_field.set_company(temp_company)

    field_list.append(temp_field) 
    #print elements
    count = count+1
  
    print count

  for fields in field_list:
    print fields

def html_grab(website_string):		#open connection, grabs html
  html = urllib2.urlopen(website_string)
  return html

def soup_debug(soup):   		#helpful debugging by printing
  print soup.prettify()

def instructions_from_file_read():
  #1 website
  #2 tag
  #3 attributes key1
  #4 attributes value1
  #5 attributes key2
  #6 attributes value2
  #7 attributes key3
  #8 attributes value3
  #9 date class name
  #10

  instructions = []
  f=open("./instruct/input.txt",'r')
  for lines in f:
    instructions.append(lines)

  return instructions

if __name__ == "__main__":
  main()

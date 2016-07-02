import hashlib
import os
import sys

class field():
  def __init__(self):
    self.field_text = ""
    self.field_link = ""
    self.field_description = ""
    self.field_price = ""
    self.field_date = ""
    self.field_id = ""
    self.field_location = ""
    self.field_company = ""

  def __str__(self):		#what happens when you print object
    s = "Title: "+ self.field_text
    s = s + "\nLocation:" + self.field_location
    s = s + "\nDate:" + self.field_date
    s = s + "\nDescription:" + self.field_description
    return s  

  def __repr__(self):		#what happens when you call in interp.
    s = "Title: "+ self.field_text
    s = s + "\nLocation:" + self.field_location
    s = s + "\nDate:" + self.field_date
    s = s + "\nDescription:" + self.field_description
    return s 

  ################
  #print methods
  ################
  def print_text(self):
    print self.field_text 

  def print_link(self):
    print self.field_link 

  def print_price(self):
    print self.field_price 

  def print_date(self):
    print self.field_date 

  def print_location(self):
    print self.field_location 

  def print_company(self):
    print self.field_company 

  ###############
  #get methods
  ###############
  def get_price(self):
    return int(self.field_price)

  def get_text(self):
    return self.field_text

  def get_link(self):
    return self.field_link

  def get_date(self):
    return self.field_date

  def get_id(self):
    return self.field_id

  def get_location(self):
    return self.field_location

  def get_company(self):
    return self.field_company

  ###############
  #set methods
  ###############
  def set_price(self, inprice):
    self.field_price=inprice 
    self.id_calculate()

  def set_text(self, intext):
    self.field_text=intext 

  def set_link(self, inlink):
    self.field_link=inlink 

  def set_date(self, indate):
    self.field_date=indate 

  def set_location(self, inlocation):
    self.field_location=inlocation 

  def set_company(self, incompany):
    self.field_location=incompany 

  ###############
  #calculate ID
  ###############
  def id_calculate(self):
    h = hashlib.new("ripemd160")
    h = hashlib.update(self.field_id)
    self.field_id = h.hexdigest()


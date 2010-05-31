#!/usr/bin/env python

import sys, calendar

#Import the ZSI machinery
from ZSI import dispatch

CAL_NS = "http://uche.ogbuji.net/eg/ws/simple-cal"

#The actual implementations
def getMonth(year, month):
    return calendar.month(year, month)

def getYear(year):
  return calendar.calendar(year)

#Generic function to check the namespace
def _functionMap(name,mapping,*args):
  cb = dispatch.GetClientBinding()
  func = mapping.get(cb.GetNS())
  if func is None:
    raise TypeError, "Unimplemented method %s %s" % (cb.GetNS(),name)
  return apply(func,args)

#Publicly defined methods
getMonthMap = {CAL_NS:getMonth,
               }
getMonth = lambda year,month,_functionMap=_functionMap,map=getMonthMap:_functionMap
("getMonth",map,year,month)


getYearMap = {CAL_NS:getYear,
              }
getYear = lambda year,_functionMap=_functionMap,map=getYearMap:_functionMap("getYear",map,year)


#Delete this so it is not available as a service.
del _functionMap

# Run Server  
print "Starting server..."
dispatch.AsServer(port=8888)


while True:
   try:
      execfile("logger.py")
   except Exception as e:
      print "Exception occured: ", e

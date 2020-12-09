import sys
import time

time.sleep(1)

if len(sys.argv) > 2:
  if sys.argv[1] == '-f':
    try:
      with open(sys.argv[2]) as file:
        print(file.read(), end="")
    except:
      print("ERROR: couldn't read file")
  elif sys.argv[1] == '-w': # Write
    pass
  # Include more options
else:
  print('ERROR: many few args')
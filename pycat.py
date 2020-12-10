import sys
import time

time.sleep(1)

def parse_quotes(string):
  return string.replace("\"", "")


if len(sys.argv) > 2:
  option = sys.argv[1]
  if option == '-r' or option == '--read':
    try:
      with open(sys.argv[2]) as file:
        print(file.read(), end="")
    except:
      print("ERROR: couldn't read file")
  elif option == '-w' or '--write': # Write
    new_file = open(parse_quotes(sys.argv[2]), "w")
    new_file.write(sys.argv[3])
    new_file.close()
  # Include more options
else:
  print('ERROR: many few args')

# TODO: parse "" characters for text
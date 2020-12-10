import sys
import time

time.sleep(1)

def parse_quotes(string):
  return string.replace("\"", "")

if len(sys.argv) > 2:
  command = sys.argv[1]
  if command == 'read':
    try:
      with open(sys.argv[2]) as file:
        print(file.read(), end="")
    except EnvironmentError as err:
      print("ERROR: couldn't read file")
      print(err)
  elif command == 'concat': # Write
    file_to_be_concatenated = open(sys.argv[2], "a")
    file_to_be_concatenated.write(parse_quotes(sys.argv[3]))
    file_to_be_concatenated.close()
  elif command == 'make':
    pass
  # Include more options (INCLUDE -m OR --make TO CREATE FILES)
else:
  print('ERROR: many few args')

# TODO: parse "" characters for text
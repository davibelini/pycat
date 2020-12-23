import sys
import time

time.sleep(1)

def parse_quotes(string):
  return string.replace("\"", "")

if len(sys.argv) > 1:
  command = sys.argv[1]
  if command == 'read':
    try:
      with open(sys.argv[2]) as file:
        print(file.read(), end="")
    except EnvironmentError as err:
      print("ERROR: couldn't read file")
  elif command == 'write': # Write
    file_to_be_concatenated = open(sys.argv[2], "a")
    file_to_be_concatenated.write(parse_quotes(sys.argv[3]))
    file_to_be_concatenated.close()
  elif command == 'make':
    try:
      f = open(sys.argv[2],"a+")
      f.close()
    except:
      print("ERROR: Could not create file.")
  elif command == 'help' or command == '?' or command == "docs": 
    try:
      docs_file = open("docs.txt", "r")
      print(docs_file.read(), end="")
    except:
      print("ERROR: could not print docs file.")
    finally:
      docs_file.close()
  elif command == 'join':
    with open(sys.argv[2], "a") as f:
      f.write(open(sys.argv[3], "r").read())
  else:
    print(f"ERROR: option '{sys.argv[1]}' does not exist.")
else:
  print('ERROR: many few arguments')

# TODO: parse "" characters for text
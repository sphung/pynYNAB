from pynYNAB.ClientFactory import clientfromargs
from pynYNAB.__main__ import parser
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

print('test_sync')
args = parser.parse_known_args()[0]
client = clientfromargs(args)
client.sync()
print('OK')

from secret_handshake import *
from secret_handshake import _actions

print(_actions)

print(standardized_code('101'))
print(handshake('101'))

print standardized_hshk(['wink', 'sneeze'])
print code(['wink', 'sneeze'])


print standardized_hshk(['wink', 'double blink'])
print code(['wink', 'double blink'])

print code(handshake(27))

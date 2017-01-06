from rail_fence_cipher_ugly import RailFenceCipher

number_of_rails = 4
rcp = RailFenceCipher(number_of_rails)

plaintext = 'somerandomtexthere'
ciphertext = rcp.encode(plaintext)

print(rcp.defenced(ciphertext))

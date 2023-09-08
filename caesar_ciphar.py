alphabet = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ'

phrase = input('Digite a frase que deseja encriptar: ')
key = 0
while key <= 0:
  try:
    key = int(input('Entre com o valor da chave (deslocamento): '))
    if key <= 0:
      print('Opa! Digite um número inteiro positivo, por favor.')
  except ValueError:
    print('Opa! Digite um número inteiro positivo, por favor.')
print('Encriptando a frase... ')
encrypted_phrase = ''
for char in phrase:
  index = alphabet.find(char)
  if index == -1:
    encrypted_phrase += char
  else:
    new_index = index + key
    if new_index > len(alphabet):
      encrypted_phrase += alphabet[new_index - len(alphabet)]
    else:
      encrypted_phrase += alphabet[new_index]
print('A frase encriptada é: {}'.format(encrypted_phrase))

print('Decodificando a frase de volta... ')
decrypted_phrase = ''
for char in encrypted_phrase:
  index = alphabet.find(char)
  if index == -1:
    decrypted_phrase += char
  else:
    decrypted_phrase += alphabet[index - key]
print('Frase decodificada: {}'.format(decrypted_phrase))
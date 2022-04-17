import whois

print('''

____    __    ____  __    __    ______    __       _______.
\   \  /  \  /   / |  |  |  |  /  __  \  |  |     /       |
 \   \/    \/   /  |  |__|  | |  |  |  | |  |    |   (----`
  \            /   |   __   | |  |  |  | |  |     \   \    
   \    /\    /    |  |  |  | |  `--'  | |  | .----)   |   
    \__/  \__/     |__|  |__|  \______/  |__| |_______/    
                                                           
BY: Kriptonflavy

''')

dns = input("Digite o Endereço do site que Deseja fazer o whois: ")
w = whois.whois(dns)

print('-----COLETA COMPLETA-----')

print(w.text)

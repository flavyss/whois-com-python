import whois
w = whois.whois('webscraping.com')
w.expiration_date  # dates converted to datetime object

print(w)  	# print values of all found attributes

import twitter 
i=1
totalrt=0
while i <= 5:
    print ""
    
    
    cuenta = raw_input('Introduzca Cuenta de Twitter:')
    if ( len(cuenta) < 1 ) : break
    outfile = open('datos.txt', 'a') # Indicamos el valor 'w'.
    apiTwitter = twitter.Api(consumer_key="ZR0hWrHInaZflCjfte0fMhIhK", consumer_secret="KEgRblKZ8F7hI7v5OIlre1ivviZ2ZPemywriXQtzNFzdkKERAR", access_token_key="4821911859-PZd3d76qpiW1SaWpozrpgDMwpJZMTZ8Z5hDaN8b", access_token_secret="LncX4NiUKcCDCJP2tp8ixVEuSM7nC5eFd04kCYQMv8zmb")
    query = apiTwitter.GetSearch(cuenta)
    for result in query:
        outfile.write( 'Tweet: %s \n'%(result.text.encode("utf-8")) )
        outfile.write( 'Creation date: %s \n' %(result.created_at))
        outfile.write( 'Favs count: %d \n' %(result.favorite_count))
        outfile.write( 'location: %s \n' %(result.location))
        outfile.write( 'Retweets count: %d \n' %(result.retweet_count))
        totalrt=totalrt+(result.retweet_count)
        outfile.write( 'Account: %s \n' %( result.user.screen_name ))
        #outfile.write( 'listed_count: %d \n' %(result.listed_count))
        outfile.write( '\n')  
    i += 1
  
    outfile.close()  
    infile = open('datos.txt', 'r')
    print(infile.read())
    print 'total retwets: ',totalrt
    totalrt=0
    infile.close()


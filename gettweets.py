import sys
import json
import oauth2 as oauth
import urllib2 as urllib

#twitter access tokens & consumer keys
access_token_key = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""
_debug = 0
http_method = "GET"


oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

#request user tweets
def twitterreq(url, method, parameters):
    req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)    
    req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)
    headers = req.to_header()

    if http_method == "POST":
        encoded_post_data = req.to_postdata()
    else:
        encoded_post_data = None
        url = req.to_url()

    opener = urllib.OpenerDirector()
    opener.add_handler(http_handler)
    opener.add_handler(https_handler)
    response = opener.open(url, encoded_post_data)
    return response


def gettweets(screen_name = 'pinchofyum', interest = '', count = 150, directory = 'data'):
    print "Downloading tweets by " + screen_name
    f = open(directory + '/' + screen_name, 'w')
    f.write("tweet,screen,interest\n")
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    parameters = {'screen_name' : screen_name, 'count' : count, 'exclude_replies' : 'true'}
    response = twitterreq(url, "GET", parameters)
    
    for line in response:
        #tweet = json.loads(line.strip())[50]['text']
        #save tweets to file
        for i in range(0, count-1):
            try:
                tweet = json.loads(line.strip())[i]['text']
                tweet = tweet.encode('utf-8')
                f.write("\"{0}\",{1},{2}\n".format(tweet.replace('"', ''), screen_name, interest))
                #print tweet
            except:
                pass
                #print "no more tweets"
                
    #close the file        
    f.closed
    
    
    
if __name__ == '__main__':
    gettweets(sys.argv[1], sys.argv[2])








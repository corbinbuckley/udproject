import urllib

def read_text():
    quotes = open("/Users/corbinbuckley/Documents/Python/movie_quotes.txt")
    contents_of_file = quotes.read()
    #print (contents_of_file). #Dont need to the doc to print
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output = connection.read()
    #print (output).         # I would like to make an if false print this..
    connection.close()
#Prints the results in human talk.  This is what I wanted
    if "true" in output:
        print ("Profanity Alert!!")
    elif "false" in output:
        print ("This documnet has no curse words!")
    else:
        print ("Could not scan the document properly.")


read_text()

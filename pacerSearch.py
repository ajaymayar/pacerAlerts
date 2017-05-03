# pacerSearch
# by Ajay Mayar
# Case: 1:17-cv-10242-IT Government of Bermuda v. Lahey Clinic, Inc. et al
# TODO: change the case name -- cut the string so that it just looks for the party name or its number

import feedparser
import requests
import string

feed = feedparser.parse('https://ecf.mad.uscourts.gov/cgi-bin/rss_outside.pl')

#####                                       FUNCTIONS                                                             ######

def send_message(message):
    print "sending message" 
    return requests.post(
            "https://api.mailgun.net/v3/sandbox2382a0bb2e994e37a0140cecb2f0ff04.mailgun.org/messages",
            auth=("api", "key-37b8a84c8f0875803c167f24f0fc28dd"),
            data={"from": "Pacer Alert <postmaster@sandbox2382a0bb2e994e37a0140cecb2f0ff04.mailgun.org>",
                "to": "Ajay <ajaymayar96@gmail.com>",
                "subject": "PACER case update",
                "text": message })

def find_case(case):
    length = len(feed['items'])
    i = 0
    casenumber = get_case_number(case)
    while i < length:
        # if get_case_number of the title == get_case
        current = get_case_number(feed['items'][i]['title'])
        if current == casenumber: 
            print "found case"
            send_message(get_message(i))
            # print feed['items'][i]['title']
        i += 1

def get_message(index):
    var = "Case Name: " + feed['items'][index]['title'] + "\n \n"\
            + "Description: " + feed['items'][index]['description']\
            + "\n \n" + "Link: " + feed['items'][index]['link']\
            + "\n \n \n \n"

    return var

    

def get_case_number(case):
    length = len(case)
    cnumber = ""
    i = 0
    while i < length:
        if case[i] == " ": 
            break
        else:
            cnumber += case[i]
        i += 1

    j = i - 1
    while j > 0:
        if cnumber[j] == "-":
            break
        else:
            cnumber = cnumber[:-1]
        j -= 1

    return cnumber

def test_get_cnumber(case):
    print get_case_number(case)


caseTest = "1:16-cr-10157-1 USA v. Garland"

# test_get_cnumber(caseTest) 
find_case(caseTest)

########################################################################

#find_case(case)

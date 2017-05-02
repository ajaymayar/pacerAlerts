# pacerSearch
# by Ajay Mayar
# Case: 1:17-cv-10242-IT Government of Bermuda v. Lahey Clinic, Inc. et al

import feedparser
import requests

feed = feedparser.parse('https://ecf.mad.uscourts.gov/cgi-bin/rss_outside.pl')

########################################################################################################################
#####                                       FUNCTIONS                                                             ######

def send_message(message):
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
    while i < length:
        if feed['items'][i]['title'] == case: 
            send_message(get_message(i))
            # print feed['items'][i]['title']
        i += 1

def get_message(index):
    var = "Case Name: " + feed['items'][index]['title'] + "\n \n" + "Description: " + feed['items'][index]['description']\
            + "\n \n" + "Link: " + feed['items'][index]['link'] + "\n \n \n \n"\
            + "Alert system created by Ajay Mayar - for issues contact ajaymayar96@gmail.com"

    return var

########################################################################################################################

case = "1:16-cr-10096-6 USA v. Chisholm et al"
find_case(case)

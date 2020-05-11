import re
import csv

def check_suffix(tld, word):
    tld = tld + "$"
    return re.search(tld,word)

with open("tld_e.csv") as tld_list:
    tld_reader = csv.reader(tld_list,delimiter=',')
    for tld_row in tld_reader:
        with open("words.csv") as wordList:
            word_reader = csv.reader(wordList,delimiter=',')
            for word_row in word_reader:
                match = check_suffix(tld_row[0],word_row[1])
                if match:
                    match_pos = match.start()
                    URL = word_row[1][0:match_pos] + "." + tld_row[0]
                    print(URL)
                    with open("domain_haxNew.csv", "a") as output:
                        output_writer = csv.writer(output, delimiter=",")
                        output_writer.writerow([URL])

                

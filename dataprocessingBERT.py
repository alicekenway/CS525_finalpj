import json, csv, re, os

a = []
for k in os.walk("C:/Users/vamsi/PycharmProjects/irfin/CORD-19-research-challenge/"):

    if 'pdf_json' in k[0] and len(k[2]) > 0:
        print(len(k[2]), k[0])
        for z in k[2]:
            if z.endswith(".json"):

                loaded_json = json.load((open(k[0] + '/' + z, "r")))
                body_string = []

                title_string = re.sub('[^a-zA-Z0-9 \n\.]', '', loaded_json['metadata']['title'])
                for x in loaded_json["body_text"]:
                    body_string.append(re.sub('[^a-zA-Z0-9 \n\.]', '', x['text']))
                    # print()
                if 'abstract' in loaded_json and len(loaded_json['abstract']) > 0:
                    abstract_string = re.sub('[^a-zA-Z0-9 \n\.]', '', loaded_json['abstract'][0]['text'])
                else:
                    abstract_string = ''
                a.append((title_string, abstract_string, body_string))
csv_read = open("final.csv", "w")
for (i, j, k) in a:
    if i == a[0][0]:
        csv_read.write('"{}","{}","{}"'.format("title", "abstract", "paragraphs"))
        csv_read.write("\n")
    csv_read.write('"{}","{}","{}"'.format(i, j, k))
    csv_read.write("\n")
csv_read.close()


def add_one(number):
    return number + 1



def vcounts21(x):
    # Injesting the pandas dataframe
    wsources = list(x['SOURCEURLS'])
    # Bag of words
    data = ''.join(wsources)
    data = data.split("htt")

    # Cleaning

    data2 = []

    # Striping the headnews from the webaddress
    
    for line in data:
        line2 = pathlib.PurePath(line).name
        if not re.match(r"^article", line2):
            if not re.match(r'^[0-9].*', line2):
                data2.append(line2)
    # Removing tags
    clean_txt = []
    for lines in data2:
        desc = lines.lower()

        #remove punctuation
        desc = re.sub('[^a-zA-Z]', ' ', desc)

        #remove tags
        desc=re.sub("&lt;/?.*?&gt;"," &lt;&gt; ",desc)

        #remove digits and special chars
        desc=re.sub("(\\d|\\W)+"," ",desc)

        desc=desc.replace("-", ' ')
    
        desc=desc.replace("html", '')
        desc=desc.replace("<UDIV>", '')
        desc=desc.replace("udiv", '')
        clean_txt.append(desc)    
 
        # Deleting phrases
        for i in clean_txt[:]:
            if len(i) <= 25:
                clean_txt.remove(i)
        # A second whitespace removal
        data3=[]
        for i in clean_txt:
            data3.append(i.strip())
        
        # Removing duplicates
        data3 = remove_duplicates(data3)
    return data3

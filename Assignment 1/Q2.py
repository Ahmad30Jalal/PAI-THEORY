allPosts = [
    {'id': 1, 'text': 'I LOVE the new #GuiPhone! Battery life is amazing.'},
    {'id': 2, 'text': 'My #GuiPhone is a total disaster. The screen is already broken!'},
    {'id': 3, 'text': 'Worst customer service ever from @GuPhoneSupport. Avoid this.'},
    {'id': 4, 'text': 'The @GuPhoneSupport team was helpful and resolved my issue. Great service!'},
]

# Keywords and characters for processing
PUNCTUATION_CHARS = '!"#$%&\'()*+,-./::<=>?@[\\]^_`{|}~'
STOPWORDS_SET = {'i', 'me', 'my', 'a', 'an', 'the', 'is', 'am', 'was', 'and', 'but', 'if', 'on', 'to', 'of', 'at', 'by', 'for', 'with', 'this', 'that'}
POSITIVE_WORDS_SET = {'love', 'amazing', 'great', 'helpful', 'resolved'}
NEGATIVE_WORDS_SET = {'disaster', 'broken', 'worst', 'avoid', 'bad'}


def preProcessText(text, punctuationList, stopWordsSet):
    new_text = ""
    result_text = ""

    text = text.lower()

    for x in text:
        if x not in punctuationList:
            new_text += x

    words = new_text.split()

    for word in words:
        if word not in stopWordsSet:
            result_text += word
            result_text += " "

    return result_text

def analyzePosts(postsList, punctuation, stopwords, positive, negative):
    cleaned_posts = list(map(lambda post: preProcessText(post['text'], punctuation, stopwords), postsList))
    score = 0
    new_list = []

    for i in range(len(postsList)):
        text = cleaned_posts[i]
        words = text.split()
        score = 0

        for word in words:
            if word in positive:
                score += 1
            elif word in negative:
                score -= 1

        new_list.append({
            'id': postsList[i]['id'],
            'text': postsList[i]['text'],
            'processedText': text.strip(),  
            'score': score
        })
    return new_list

def getFlaggedPosts(scoredPosts, sentimentThreshold=-1):
    return [post for post in scoredPosts if post['score'] <= sentimentThreshold]

def findNegativePosts(flaggedPosts):
    posts = {}

    for post in flaggedPosts:
        text = post['text']

        for word in text.split():
            for ch in word:
                if ch == "@" or ch == "#":
                    if word not in posts:
                        posts[word] = 0     
                    posts[word] += 1       

    return posts

        
text = "PAI  is kesy !@ (prhen?"

result = preProcessText(text, PUNCTUATION_CHARS, STOPWORDS_SET)
print(result)

    
results = analyzePosts(allPosts, PUNCTUATION_CHARS, STOPWORDS_SET, POSITIVE_WORDS_SET, NEGATIVE_WORDS_SET)

for r in results:
    print(r)

fposts = getFlaggedPosts(results)

for f in fposts:
    print (f)

nposts = findNegativePosts(fposts)
print(nposts)


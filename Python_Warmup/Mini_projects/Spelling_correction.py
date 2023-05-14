from textblob import TextBlob

def correct_text(text):
    bolb = TextBlob(text)
    corrected_text = bolb.correct()
    return corrected_text

if __name__ == "__main__":
    text = '''Hello evryone I am shyam goli the great. Every hapy to meet you all. I faeling proud to be at this postion. Thnkyou all for coming here.'''
    corrected_text = correct_text(text)
    print(text)
    print(corrected_text)


# for sentence in blob.sentences:
#     print(sentence.sentiment.polarity)
#wap to detetect whether a  comment is scam or not.a comment should be treated a spam if it conatins  "make alot of money","buy now" , "subscribe this"
comment = input("Enter a comment: ")

if "make alot of money" in comment or "buy now" in comment or "subscribe this" in comment:
    print("Comment is Spam")
else:
    print("Comment is Not Spam")
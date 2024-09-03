# from preloaded import Like, Dislike, Nothing

def like_or_dislike(lst):
    status = 0

    if(lst == []):
        return "Nothing"
    else:
        for i in lst:
            if(i == "Like"):
                if(status == 0 or status == -1):
                    if(status == 0):
                        status = status + 1
                    elif(status == -1):
                        status = status + 2
                elif(status == 1):
                    status = status - 1
            elif(i == "Dislike"):
                if(status == 0 or status == 1):
                    if(status == 0):
                        status = status - 1
                    elif(status == 1):
                        status = status - 2
                elif(status == -1):
                    status = 0

    if(status == 0):
        return "Nothing"
    elif(status == 1):
        return "Like"
    elif(status == -1):
        return "Dislike"               

like_or_dislike(["Like", "Like", "Dislike"])

# Best Practice:
    # def like_or_dislike(lst):
    # 	state = 'Nothing'
    # 	for i in lst:
    # 		state = 'Nothing' if i == state else i
    # 	return state
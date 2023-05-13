# Like, Dislike, Nothing come from Preloaded
def like_or_dislike(lst):
    Like,Dislike = 0,0
    for el in lst:
        if el == 'Like':
            if Like == 0:
                Like = 1
                Dislike = 0
            elif Like == 1:
                Like,Dislike = 0,0
        elif el == 'Dislike':
            if Dislike == 0:
                Dislike = 1
                Like = 0
            elif Dislike == 1:
                Like,Dislike = 0,0
        elif el == 'Nothing':
            Dislike,Like = 0,0
    if Like == 1:
        return 'Like'
    elif Dislike == 1 :
        return 'Dislike'
    else:
        return 'Nothing'


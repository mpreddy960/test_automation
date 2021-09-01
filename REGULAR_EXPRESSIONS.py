import re
#using RE.finddall
str = "The Ball on the Wall"
find = re.findall("a",str)
print("print(find)   :",find)
#CHEAK GROUP OF CHARACTERS
d0c_find = re.findall("Wall",str)
print("print(d0c_find   :",d0c_find)
#CHEAK KNOW CHARCTERS
VOLUME = re.findall("hj",str)
print("print(VOLUME)   :",VOLUME)
#USING RE.SEARCH {it is return object}
search_replay = re.search("Wall",str)
print("print(search_replay)   :",search_replay)
#using start method {it is excute character or characters indexing
cheak_search = re.search("a",str)
print("print(cheak_search)  :",cheak_search)
cv = cheak_search.start()
print("print(cv)   :",cv)
#using span menthod {it is excute to range}
span_method = search_replay.span()
print("print(span_method)   :",span_method)
teddy = cheak_search.span()
print("print teddy   :",teddy)

got_draw = re.search("T",str)
print("print(got_draw) :",got_draw)
nm = got_draw.span()
print("print(nm)   :",nm)
#using string methods{it is excute total string}
blm = got_draw.string
print("print(blm)  :",blm)
#using split method
split_doc = "GATE wall is iron metal"
ganga = re.findall("G",split_doc)
print("print(ganga)  :",ganga)
split_string = re.split("l",split_doc)
print(split_string)
print("(re.split("",split_doc wall ))  :",re.split("wall",split_doc))
print("re.split(" ",split_doc one space)  :",re.split(" ",split_doc))
# pv = re.split("",split_doc)
# print(pv)
#USING MAX SPLIT
print("re.split(" ",maxium) :",re.split(" ",split_doc,1))

REDDY = "pot on the wall"
teddy = re.split(" ",REDDY)
print(REDDY)
flag = re.split("wall",REDDY)
print(flag)
GOT = re.split(" ",REDDY,1)
print(GOT)
#USING SUB METHOD
sun_method = "perfect man always help to others"
using_sub = re.sub("t","T",sun_method)
print("print(using_sub)  :",using_sub)
strenger = re.sub("e","E",sun_method)
print("print strenger  [e]  :",strenger)
xes = re.sub("e","E",sun_method,1)
print("PRINT CHANGE OLD TO NEW STRING :",xes)
drink = "Example for meta Character in Regular Expressions needed in python exeed"
drunk = re.findall("[a]",drink)
print("print(drunk)  :",drunk)
toy = re.findall("[in]",drink)
print("print(toy)   :",toy)
cap = re.findall("^Example",drink)
print("print(cap)  :",cap)
meta = re.findall("^meta",drink)
print("print(meta)   :",meta)
using_o = re.findall("meta$",drink)
print("print(using_o)   :",using_o)
court_0 = re.findall("exeed$",drink)
print("print(court_0  :",court_0)
exam_o = re.findall("Exam......",drink)
print("print(exam_o)  :",exam_o)
exam_o12 = re.findall("Exam..",drink)
print("print(exam_o12)  :",exam_o12)
exam_after_6dots = re.findall("Exam.......",drink)
print("print(exam_after_6dots)  :",exam_after_6dots)
exam_before_3dots = re.findall("...Exam",drink)
print("print(exam_before_3dots)  :",exam_before_3dots)
exam_before_2dots = re.findall("....ple",drink)
print("print(exam_before_2dots)   :",exam_before_2dots)
exam_dots_5 = re.findall("...r",drink)
print("print(exam_dots_5)   :",exam_dots_5)
using_star = re.findall("m*",drink)
print("print(using_star)   :",using_star)
using_adition = re.findall("m+",drink)
print("print(using_adition)    :",using_adition)
using_doble_character = re.findall("ee*",drink)
print("print(using_doble_character)   :",using_doble_character)
using_doble_character_adition = re.findall("ee+",drink)
print("print(using_doble_character_adition)  ",using_doble_character_adition)
other_characters = re.findall("ed*",drink)
print("print(other_characters)   :",other_characters)
other_charact = re.findall("ed+",drink)
print("print(other_charact)   :",other_charact)
exam_j = re.findall("ed{1}",drink)
print("print(exam_j)  :",exam_j)
curly = re.findall("e{1}",drink)
print("print(curly)",curly)
braces = re.findall("e{2}",drink)
print("print(braces)  :",braces)
speaces = re.findall("\s",drink)
print("print(speaces)   :",speaces)
capital_S = re.findall( "\S",drink)
print("print(capital_S)  :",capital_S)
ink = "12,4,653,in the WALL"
small_d = re.findall("\d",ink)
print("print(small_d)   :",small_d)
CAPITAL_D = re.findall("\D",ink)
print("print(CAPITAL_D)   :",CAPITAL_D)
small_w = re.findall("\w",ink)
print("print(small_w)  :",small_w)
CAPITAL_W = re.findall("\W",ink)
print("print(CAPITAL_W)   :",CAPITAL_W)
one_using = re.findall("[123]",ink)
print("print(one_using)   :",one_using)
ra_using_cap = re.findall("[^123]", ink)
print("print(ra_using_cap)   :",ra_using_cap)
range_using_cap = re.findall("[0-9]", ink)
print("print(range_using_cap)  :",range_using_cap)
three_using_cap = re.findall("[0-9][0-9][0-9]",ink)
print("print(three_using_cap)  :",three_using_cap)
characters = re.findall("[a-z]",ink)
print("print(characters)  :",characters)
tree = re.findall("[A-Z]",ink)
print("print(tree)   :",tree)
KING = "A, VELL cow"
small_t = re.findall("\A",KING)
print(small_t)

small_time = re.findall("\n",KING)
print(small_time)

#Character(s)	What it does
# .	A period. Matches any single character except the newline character.
# ^	A caret. Matches a pattern at the start of the string.
# \A	Uppercase A. Matches only at the start of the string.
# $	Dollar sign. Matches the end of the string.
# \Z	Uppercase Z. Matches only at the end of the string.
# [ ]	Matches the set of characters you specify within it.
# \	∙ If the character following the backslash is a recognized escape character, then the special meaning of the term is taken.
# ∙ Else the backslash () is treated like any other character and passed through.
# ∙ It can be used in front of all the metacharacters to remove their special meaning.
# \w	Lowercase w. Matches any single letter, digit, or underscore.
# \W	Uppercase W. Matches any character not part of \w (lowercase w).
# \s	Lowercase s. Matches a single whitespace character like: space, newline, tab, return.
# \S	Uppercase S. Matches any character not part of \s (lowercase s).
# \d	Lowercase d. Matches decimal digit 0-9.
# \D	Uppercase D. Matches any character that is not a decimal digit.
# \t	Lowercase t. Matches tab.
# \n	Lowercase n. Matches newline.
# \r	Lowercase r. Matches return.
# \b	Lowercase b. Matches only the beginning or end of the word.
# +	Checks if the preceding character appears one or more times.
# *	Checks if the preceding character appears zero or more times.
# ?	∙ Checks if the preceding character appears exactly zero or one time.
# ∙ Specifies a non-greedy version of +, *
# { }	Checks for an explicit number of times.
# ( )	Creates a group when performing matches.
# < >	Creates a named group when performing matches.





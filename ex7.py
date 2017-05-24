print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 10
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

formatter = "%r %r %r %r"

print formatter
print formatter % ('a', 'b', 'c', 'd')
print formatter % (formatter, formatter, formatter, formatter)
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months

print """
There's something going on there.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5 or 6. """

while True:
    for i in ["/", "-", "|", "\\", "|"]:
        print "%s\r" % i

print "How old are you?"
age = raw_input()
print "how tall are you?"
height = raw_input()
print "How much do you weigh?"
weight = raw_input()
print "So, you're %r old, %r tall and %r heavey." % (age, height, weight)





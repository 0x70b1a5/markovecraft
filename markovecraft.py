# combines arbitrary corpa in a markov chain.
# usage:
# python markovecraft.py [1.txt ... n.txt] [x1,...,xn]
#   where x1...xn is a comma-separated (no spaces) list of number weights
import markovify
import sys

files = sys.argv[1:-1]
weights = [float(num) for num in sys.argv[-1].split(",")]
print(weights)
models = []
print("chaining %s" % str(files))
for filename in files:
    f = open(filename)
    models.append(markovify.Text(f.read(),  state_size=3))

model = markovify.combine(models, weights)
while True:
    length = input("Input sentence length: ")
    if (length != ''):
        print (model.make_short_sentence(int(length)))
    else:
        print (model.make_short_sentence(140))

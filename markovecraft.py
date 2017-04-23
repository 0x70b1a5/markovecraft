# combines arbitrary corpa in a markov chain.
# usage:
# python markovecraft.py [1.txt ... n.txt] [x1,...,xn]
#   where x1...xn is a comma-separated (no spaces) list of number weights
import markovify
import sys

state_size = int(sys.argv[1])
files = sys.argv[2:-1]
try:
    weights = [float(num) for num in sys.argv[-1].split(",")]
except Exception:
    files.append(sys.argv[-1])
    weights = [1.0 for f in range(0,len(files))]

print(weights)
models = []
print("chaining %s" % str(files))
for filename in files:
    f = open(filename)
    models.append(markovify.Text(f.read(),  state_size=state_size))

model = markovify.combine(models, weights)
while True:
    length = input("Input sentence length: ")
    if (length != ''):
        sen = model.make_short_sentence(int(length))
    else:
        sen = model.make_short_sentence(140)
    for f in files:
        for line in f:
            if sen in line:
                print("NOT UNIQUE: sentence found in %s" % f)
    print(sen)

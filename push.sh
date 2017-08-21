PREFIX=$(cd "$(dirname "$0")"; pwd)
cd $PREFIX
hg ci -m '.'
hg fe
hg bookmark -f master
hg push

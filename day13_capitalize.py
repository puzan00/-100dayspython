#hacker rank capitlize problem
# in order to capitalize each first letter of the word we use 'Title'

name="ram shrestha"
print(name.title())

# so this is the solution for the problem
def solve(s):
    return ' '.join(i.capitalize() for i in s.split(' ')) #first join the words with capitalize and split them 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()



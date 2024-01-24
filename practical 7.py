num=input('enter the input:')
fh=open('ram 7.txt','w')
reverse=num[::-1]
if (num == reverse):
    print('Palindrome')
    fh.write(f'the given string {num} is a palindrome')
else:
    print('not')
    fh.write(f'the given string {num} is a not palindrome')

fh.close()
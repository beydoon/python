#          zyxwvutsrqponmlkjihgfedcba
#          54321098765432109876543210
#          01234567890123456789012345
#          abcdefghijklmnopqrstuvwxyz
letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[25:0:-1]
print(backwards)

backwards = letters[25::-1]
print(backwards)

backwards = letters[::-1]
print(backwards)

print()
print()
# create a slice that produces the characters qpo
print(letters[16:13:-1])

# slice the string to produce edcba
print(letters[4::-1])

# slice the string to produce the last 8 characters, in reverse order
print(letters[25:17:-1])
# or
print(letters[:-9:-1])

print()

# get last 4 letters
print(letters[-4:])
print(letters[-1:])
print(letters[:1])
print(letters[0])
line = 'nobody:*:-2:-2:Up user:/var/empty:/user/bin/false'
user, *file, homedir, sh = line.split(':')

print(user)
print(homedir)
print(sh)


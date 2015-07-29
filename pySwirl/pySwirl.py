def hello(): 
    name = raw_input('Welcome to pySwirl! What shall I call you?: ')
    print "Hello, %s!" % name
    print 'You can exit pySwirl by typing quit() at any time.'
    print 'Available courses:  1. Python programming basics'
    num = raw_input('Select a course to follow: ')
    if num == 1:
      basics()


def basics():
  print 'learn python basics here'

def main():
  print "this is pySwirl's main menu"

def info():
  print 'helpful pySwirl user info'
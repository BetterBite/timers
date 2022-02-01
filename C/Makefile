# Find the OS platform using the uname command.
Linux := $(findstring Linux, $(shell uname -s))
MacOS := $(findstring Darwin, $(shell uname -s))
Windows := $(findstring NT, $(shell uname -s))

# Specify what typing 'make' on its own will compile
default: test

# For Native Windows only, add the .exe extension
ifdef Windows

%: %.c
	clang -std=c11 -Wall -pedantic -g $@.c -o ./compiled/$@.exe

# For Linux/MacOS, include the advanced debugging options
else

%: %.c
	clang -std=c11 -Wall -pedantic -g $@.c -o ./compiled/$@ \
	    -fsanitize=undefined -fsanitize=address

endif

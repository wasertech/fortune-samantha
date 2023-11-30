MAKEFLAGS += -r
UNAME := $(shell uname)

ifeq ($(UNAME), Darwin)
	# Homebrew-installed fortune path
	fortunesdir=/opt/homebrew/opt/share/fortune
else
	fortunesdir=/usr/share/fortune
endif

wd=./fortunes

srcfiles := $(filter-out $(wildcard $(wd)/*.dat), $(wildcard $(wd)/*))
datfiles := $(srcfiles:=.dat)

buildtool=strfile
rm=rm -f

.PHONY:
all: $(datfiles)

$(wd)/samantha.dat: $(wd)/samantha
	$(buildtool) $^ $@

.PHONY:
install: all
	cp $(wd)/* $(fortunesdir)

.PHONY:
clean:
	$(rm) $(datfiles)
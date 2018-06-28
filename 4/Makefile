# Sources:
SRCS:=fork.c
OBJS:=$(SRCS:.c=.o)

# Config:
CC:=gcc
CFLAGS:= -c
LD:=gcc

# Targets:

all: run

clean:
	@echo Cleaning.
	@rm -f *.o
	@rm -f run

run: $(OBJS)
	@echo $@
	@$(LD) -o $@ $^
	@rm -f *.o


%.o:%.c
	@echo $@
	@ $(CC) $(CFLAGS) -o $@ $<

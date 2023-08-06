all: monty barrett base

CFLAGS=-DMUL=MUL_TOOM_COOK -DSQR=MUL_TOOM_COOK

monty: test.c
	gcc $(CFLAGS) -DREDUCTION=RED_MONTGOMERY -g -I../tommath/ bn.c test.c ../tommath/libtommath-HOST.a -o monty

barrett: test.c
	gcc $(CFLAGS) -DREDUCTION=RED_BARRETT -g -I../tommath/ bn.c test.c ../tommath/libtommath-HOST.a -o barrett

base: test.c
	gcc $(CFLAGS) -DREDUCTION=RED_BASE -g -I../tommath/ bn.c test.c ../tommath/libtommath-HOST.a -o base

clean:
	rm monty barrett base
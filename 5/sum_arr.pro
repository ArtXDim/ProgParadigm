domains
	l  = integer* 
predicates
	nondeterm sum(l, integer)
	nondeterm sum(l, integer, integer)
clauses
	sum(L,     Len)		:- 
		sum(L, 0,      Len).
	sum([],    Len,    Len)	:- 
		!.
	sum([H|T], Buf,    Len)	:- 
		NewBuf = Buf + H,
		sum(T, NewBuf, Len).
goal
	sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], Res).
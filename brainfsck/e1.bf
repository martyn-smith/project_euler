
Find the sum of all the multiples of 3 below 100

memory layout:

i  x  mod  sum  tmp0  tmp1

create i (10*10) with tmp0 as countera then align on i
>>>> ++++++++++ [<<<<++++++++++>>>>-] <<<<

loop i 100 to 0
[-
  move i to x and tmp0 move tmp0 to i then align on x
  [>+>>>+<<<<-] >>>> [<<<<+>>>>-] <<<

  move x to mod using tmp0 then align on x
  [>+>>+<<<-] >>> [<<<+>>>-] <<<

  then do modulus loop then align on mod
  this currently fails due to underflow
  [->---<] >

  we want a value that is 1 is mod is 0 and 0 otherwise
  copy mod to tmp1 then align on mod
  [>>+>+<<<-] >> [<<+>>-] <<

  if mod is 0 add one to tmp0 and subtract tmp1 from mod then align on tmp0
  [+ >>> [<<<->>>-] ] <

  tmp0 is now a sentinel value
  if tmp0 is 0 align on i
  [<<<<
    copy i to x via tmp1 then align on x
    [>+>>>>+<<<<<-] >>>>> [<<<<< + >>>>> -] <<<<
    addition loop x to sum
    [>>+<<-]
  align on tmp0 and decrement
  >>>-] 
  align on i
  <<<<

]

print ASCII 48 plus sum
>>>++++++++++++++++++++++++++++++++++++++++++++++++.
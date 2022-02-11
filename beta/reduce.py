#BETA REDUCTION FOR SK CALCULUS
from pyparsing import nestedExpr

SREDUCTOR = (lambda x:
  (lambda y:
    (lambda z:
      [x,z,[y,z]]
    )
  )
)

KREDUCTOR = (lambda x:
  (lambda _:
    [x]
  )
)

def DFS(l):
  if isinstance(l, str):
    return l
  newL = []
  for i in l:
    newL.append(DFS(i))
  while (len(newL)>0) and (not isinstance(newL[0], str)):
    if not isinstance(newL[0], list):
      newL = l[1:]
    else:
      newL = newL[0]+newL[1:]
  if (newL[0] == 'S') and (len(newL) >= 4):
    newL = DFS(SREDUCTOR(DFS(newL[1]))(DFS(newL[2]))(DFS(newL[3])) + newL[4:])
  elif (newL[0] == 'K') and (len(newL) >= 3):
    newL = DFS(KREDUCTOR(DFS(newL[1]))(DFS(newL[2])) + newL[3:])
  return newL

def rDFS(l):
  if not isinstance(l, list):
    if not isinstance(l, str):
      print('Unexpected token: ', l)
    return str(l)
  if len(l) == 0:
    return ''
  newL = rDFS(l[0])
  for i in l[1:]:
    newL += f'({rDFS(i)})'
  return newL

#ONLY APPLY REDUCE FUNCTION ON SINGLE EXPRESSIONS WITH NO STRINGS OR COMMENTS
def REDUCE(s):
  tokens = nestedExpr('(',')').parseString(f'({s})').asList()
  cleaned = DFS(tokens)
  return rDFS(cleaned)
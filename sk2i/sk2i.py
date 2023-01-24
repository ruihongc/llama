#SK combinator to iota combinator
from tokenize import generate_tokens, untokenize, TokenInfo
from io import StringIO

i = (lambda f:
  f(lambda a:
    (lambda b:
      (lambda c:
        a(
          c
        )(
          b(
            c
          )
        )
      )
    )
  )
  (lambda d:
    (lambda e:
      d
    )
  )
)

WORDS = (lambda x:
  list(
    generate_tokens(
      StringIO(
        x
      )
      .readline
    )
  )
)

RED = {
  'S': 'i(i(i(i(i))))',
  'K': 'i(i(i(i)))'
}

SK2I = (lambda x:
  untokenize(
    REPLACE(y)
    for y in WORDS(x)
  )
)

REPLACE = (lambda x:
  TokenInfo(
    x.type,
    RED[
      x.string
    ],
    x.start,
    x.end,
    x.line,
  )
  if x.string in RED
  else x
)
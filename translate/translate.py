#TRANSLATION FUNCTION
from tokenize import generate_tokens, untokenize, TokenInfo
from io import StringIO

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

REPLACE = (lambda RED:
  (lambda x:
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
)

APPLY = (lambda w:
  (lambda x:
    (lambda y:
      (lambda z:
        w
        if w == x
        else z(
          w
        )
      )
    )
  )
)

TRANSLATE = (lambda RED:
  (lambda x:
    APPLY(
      untokenize(
        REPLACE(RED)(y)
        for y in WORDS(x)
      )
    )(
      x
    )(
      RED
    )(
      TRANSLATE
    )
  )
)

RUN = (lambda RED:
  (lambda x:
    eval(
      TRANSLATE(
        RED
      )(
        x
      )
    )
  )
)
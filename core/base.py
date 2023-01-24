#BASE FUNCTIONS
S = (lambda x:
  (lambda y:
    (lambda z:
      x(
        z
      )(
        y(
          z
        )
      )
    )
  )
)

K = (lambda x:
  (lambda _:
    x
  )
)

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
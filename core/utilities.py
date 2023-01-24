I2C = (
  (lambda x:
	  (lambda y:
      x(lambda z:
        y(
          y
        )(
          z
        )
      )
    )
		(lambda y:
      x(lambda z:
        y(
          y
        )(
          z
        )
      )
    )
  )
  (lambda w:
    (lambda x:
      (lambda y:
        (lambda z:
          (
            [lambda:
              z
            ][
              x:
            ]+[lambda:
              y(
                w(
                  x-1
                )(
                  y
                )(
                  z
                )
              )
            ]
          )[
            0
          ]
          ()
        )
      )
    )
  )
)

C2I = (lambda x:
  x(lambda y:
    y + 1
  )(
    0
  )
)

ISTRUE = (lambda x:
  x(
    True
  )(
    False
  )
)

ISFALSE = (lambda x:
  x(
    False
  )(
    True
  )
)
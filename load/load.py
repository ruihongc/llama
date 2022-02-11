LOAD = (lambda RED:
  (
    exec(f'{C} = {RED[C]}') for C in RED
  )
)

LOADSAFE = (lambda TRANSLATE:
  (lambda RED:
    (
      exec(f'{C} = {TRANSLATE(RED[C])}') for C in RED if C not in ('Y', 'Θ')
    )
  )
)
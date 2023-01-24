#FUNCTION TO APPLY AS ARGUMENT TO HELP IN DEBUGGING
HELPER = (lambda x: 
  list(
    setattr(
      f,
      '__name__',
      x
    ) or f
    for f in (
      (lambda y:
        print(
          f'''{
            x
          }({
            y.__name__
            if y.__name__ != '<lambda>'
            else y
          })''',
          flush=True
        ) or HELPER(
          x.split(
            '-'
          ) [
            0
          ] + '-' + str(
            int(
              (
                x.split(
                  '-'
                ) [
                  1:
                ] or [
                  0
                ]
              ) [
                0
              ]
            ) + 1
          )
        ),
      )
    )
  ) [
    0
  ]
)
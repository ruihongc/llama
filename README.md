# llama

Write, evaluate, reduce and run lambda calculus and combinator functions in python. Comes with a number of predefined combinator birds and other utility functions.

Available functions:
 - WORDS: tokenizer (mainly used internally)
 - REPLACE: substitute with dictionary equivalent (mainly used internally)
 - APPLY: run a function again (mainly used internally)
 - TRANSLATE: translate into SK combinators based on a translation dictionary
 - RUN: run combinator code based on a translation dictionary
 - SK2I: translate SK combinators to i combinator
 - S, K, i: Starling, Kestrel and iota combinators respectively
 - I2C, C2I: natural number to church, church to natural number
 - ISTRUE, ISFALSE: Kestrel and Kite to True and False
 - LOAD, LOADSAFE: load combinator functions of translation dictionary into current namespace
 - HELPER: function to feed as input parameter in combinators to help with debugging
 - REDUCE: beta reduction on the output of TRANSLATE
 - ALL_, BIRDNAMES_, BIRDS_, BOOL_, EXTRABIRDS_, LIST_, MATH_, PAIR_: translation dictionaries to feed into functions 

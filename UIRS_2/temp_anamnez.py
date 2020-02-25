from yargy import rule
from yargy.interpretation import fact
from yargy.predicates import eq, normalized, gram
from consts import *


T_anamnez = fact(
    'T_anamnez'
    ['Temp']
)

T_ANAMNEZ = TEMP.interpretation(
    T_anamnez.Temp
)

ANAMNEZ = rule(
    normalized('анамнез'),
    NOUN.optional(),
    EOL,
    VERB.repeatable.optional(),
    NOUN.repeatable.optional(),

    )

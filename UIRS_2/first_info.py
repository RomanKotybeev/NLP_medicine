from yargy import rule
from yargy.interpretation import fact
from consts import *
"""
FIRST_INFO
"""
#from natasha.grammars import date

First_info = fact(
    'First_info',
    ['N_patient', 'Sex', 'Birth_date']
)

N_PATIENT = INT.interpretation(
    First_info.N_patient.custom(int)
)

SEX = or_(
    SEX_M,
    SEX_F
).interpretation(
    First_info.Sex.normalized()
)

BIRTH_DATE = DATE.interpretation(
    First_info.Birth_date
)

FIRST_INFO = rule(
    N_PATIENT,
    COMMA,
    SEX,
    COMMA,
    BIRTH_DATE
).interpretation(
    First_info
)
from consts import TIME, DATE, PREP
from yargy.interpretation import fact
from yargy import rule
from yargy.predicates import eq, normalized, gram



Date_begin_disease = fact(
    'Date_begin_disease',
    ['date', 'time']
)

DATE_DISEASE = DATE.interpretation(
    Date_begin_disease.date
)

TIME_DISEASE = TIME.interpretation(
    Date_begin_disease.time
)

SICK = rule(
    normalized('заболеть'), 
    PREP.optional()
)

DATE_BEGIN_DISEASE = rule(
    SICK,
    TIME_DISEASE.optional(),
    DATE_DISEASE,
    TIME.optional()
).interpretation(
    Date_begin_disease
)


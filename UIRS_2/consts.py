from yargy import or_, rule, not_
from yargy.pipelines import morph_pipeline
from yargy.predicates import eq, in_, gram, normalized, type as type_
from yargy.interpretation import fact

""" CONSTS"""
INT = type_('INT')
NOUN = gram('NOUN')
VERB = gram('VERB')
PREP = gram('PREP')
EOL = gram('EOL')

DOT = eq('.')
COMMA = eq(',')
SYMBOLS = type_('PUNCT')

SEX_M = morph_pipeline([
    'мужской',
    'муж',
])

SEX_F = morph_pipeline([
    'женский',
    'жен',
])

DATE = rule(
    INT,
    DOT,
    INT,
    DOT,
    INT
)

TIME = rule(
    INT,
    in_(':.'),
    INT
)

# temperature
TEMP = rule(
    normalized('температура'),
    VERB.optional(),
    PREP.optional()
)
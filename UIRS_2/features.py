from yargy import rule
from yargy.interpretation import fact
from consts import *
from yargy import and_, not_
from yargy.pipelines import morph_pipeline

"""
'chils', озноб
'weakness', слабость
'lethargy', вялость
'headache', головная боль
'sleep_disturbance', нарушение сна
'dec_appetite', снижение аппетита
'aches', ломота в теле
'nausea', тошнота
'unconscious', Сознания нарушения
'cramps', Судороги
'paresthesia', Парестезии
'erythema', Появление  эритемы
'clear_boundaries', с четкими границами
'fractur', краевой валика
'edema', отек
'hard_begin', Острое начало
hyperemia, гиперемия
lymphangitis, лимфангоит
"""

NONE = not_(eq(morph_pipeline([
    'отсутсвует',
    'нет',
    'без',
])))

Features = fact(
    'Features',
    ['chils', 'weakness', 'lethargy', 
    'headache', 'sleep_disturbance', 'dec_appetite',
    'aches', 'nausea', 'unconscious',
    'cramps', 'paresthesia', 'erythema',
    'clear_boundaries', 'fractur', 'edema',
    'hard_begin', 'hyperemia', 'lymphangitis',

    ]
)

chils = rule(
    NONE.optional(),
    normalized('озноб'),
    NONE.optional()
).interpretation(
    Features.chils
)

weakness = rule(
    NONE.optional(),
    normalized('слабость'),
    NONE.optional()
).interpretation(
    Features.weakness
)

lethargy = rule(
    NONE.optional(),
    normalized('вялость'),
    NONE.optional()
).interpretation(
    Features.lethargy
)

headache = rule(
    NONE.optional(),
    morph_pipeline([
        'головная боль'
    ]),
    NONE.optional()
).interpretation(
    Features.headache
)

sleep_disturbance = rule(
    NONE.optional(),
    morph_pipeline([
        'нарушение сна'
    ]),
    NONE.optional()
).interpretation(
    Features.headache
)

dec_appetite = morph_pipeline([
    'пропасть',
     'аппетит',
     'снизился'
]).interpretation(
    Features.dec_appetite
)

aches = rule(
    NONE.optional(),
    normalized('ломота'),
    NONE.optional()
).interpretation(
    Features.aches
)

nausea = rule(
    NONE.optional(),
    morph_pipeline([
        'тошнота',
        'рвота'
    ]),
    NONE.optional()
)

unconscious = rule(
    normalized('нарушение'),
    normalized('сознание')
)

cramps = rule(
    NONE.optional(),
    normalized('судорога'),
    NONE.optional()
)

paresthesia = rule(
    NONE.optional(),
    morph_pipeline([
        'парестезия', 
        'чувство распирание',
        'жжение', 
        'неинтенсивный боль', 
        'покраснение область кожа',
        'краснота'
    ]),
    NONE.optional(),
)

erythema = rule(
    NONE.optional(),
    'эритема',
    NONE.optional(),
)

clear_boundaries = rule(
    NONE.optional(),
    morph_pipeline([
        'чёткий граница'
    ]),
    NONE.optional(),
)

fractur = rule(
    NONE.optional(),
    morph_pipeline([
        'неровный край'
    ]),
    NONE.optional(),
)

edema = rule(
    NONE.optional(),
    normalized('отёк'),
    NONE.optional()
)

#hard_begin = 

hyperemia = rule(
    NONE.optional(),
    normalized('гиперемия'),
    NONE.optional()
)

lymphangitis = rule(
    NONE.optional(),
    normalized('лимфангоит'),
    NONE.optional()
)

FEATURES = or_(
    chils, 
    weakness,
    lethargy,
    headache,
    sleep_disturbance,
    dec_appetite,
    aches,
    nausea,
    unconscious,
    cramps,
    paresthesia,
    erythema,
    clear_boundaries,
    fractur,
    edema,
    #hard_beginб
    hyperemia,
    lymphangitis

).interpretation(
    Features
)
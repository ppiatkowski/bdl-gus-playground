#!/usr/bin/python3


class Unit:
    bydgoszcz = "040410661011"
    warszawa = "071412865011"
    krakow = "011212161011"
    lodz = "051011661011"
    wroclaw = "030210564011"
    poznan = "023016264011"
    gdansk = "042214361011"
    szczecin = "023216562011"
    lublin = "060611163011"
    bialystok = "062013761011"
    katowice = "012414869011"


class Variable:
    class Population:
        total = 72305
        male = 72300
        female = 72295
        male0_4 = 72301
        male5_9 = 72302
        male10_14 = 72303
        male15_19 = 72304
        male20_24 = 47711
        male25_29 = 47736
        male30_34 = 47724
        male35_39 = 47712
        male40_44 = 47725
        male45_49 = 47728
        male50_54 = 47706
        male55_59 = 47715
        male60_64 = 47721
        male65_69 = 72243
        maleOver70 = 72238
        female0_4 = 72296
        female5_9 = 72297
        female10_14 = 72298
        female15_19 = 72299
        female20_24 = 47738
        female25_29 = 47696
        female30_34 = 47695
        female35_39 = 47716
        female40_44 = 47698
        female45_49 = 47727
        female50_54 = 47723
        female55_59 = 47702
        female60_64 = 47693
        female65_69 = 72241
        femaleOver70 = 72242


CITIES_10 = [
    Unit.bydgoszcz,
    Unit.warszawa,
    Unit.krakow,
    Unit.lodz,
    Unit.wroclaw,
    Unit.poznan,
    Unit.gdansk,
    Unit.szczecin,
    Unit.lublin,
    Unit.bialystok,
    Unit.katowice,
]

MALES_0_19 = [
    Variable.Population.male0_4,
    Variable.Population.male5_9,
    Variable.Population.male10_14,
    Variable.Population.male15_19,
]
MALES_20_39 = [
    Variable.Population.male20_24,
    Variable.Population.male25_29,
    Variable.Population.male30_34,
    Variable.Population.male35_39,
]

MALES_40_and_over = [
    Variable.Population.male40_44,
    Variable.Population.male45_49,
    Variable.Population.male50_54,
    Variable.Population.male55_59,
    Variable.Population.male60_64,
    Variable.Population.male65_69,
    Variable.Population.maleOver70
]

MALES = MALES_0_19 + MALES_20_39 + MALES_40_and_over

FEMALES_0_19 = [
    Variable.Population.female0_4,
    Variable.Population.female5_9,
    Variable.Population.female10_14,
    Variable.Population.female15_19,
]
FEMALES_20_39 = [
    Variable.Population.female20_24,
    Variable.Population.female25_29,
    Variable.Population.female30_34,
    Variable.Population.female35_39,
]

FEMALES_40_and_over = [
    Variable.Population.female40_44,
    Variable.Population.female45_49,
    Variable.Population.female50_54,
    Variable.Population.female55_59,
    Variable.Population.female60_64,
    Variable.Population.female65_69,
    Variable.Population.femaleOver70
]

FEMALES = FEMALES_0_19 + FEMALES_20_39 + FEMALES_40_and_over

ALL_0_19 = MALES_0_19 + FEMALES_0_19
ALL_20_39 = MALES_20_39 + FEMALES_20_39

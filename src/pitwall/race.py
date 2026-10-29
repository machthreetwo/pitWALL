# Chapter 3 - see the book. Replace each NotImplementedError with a real body.
"""Chapter 3: control flow and loops - running a stint lap by lap."""


def tyre_life(compound: str) -> int:
    """Laps until the tyre falls off the cliff. 0 for an unknown compound."""
    match compound:
        case "soft":
            return 18
        case "medium":
            return 28
        case "hard":
            return 40
        case _:
            return 0
    


def tyre_state(age_laps: int, compound: str) -> str:
    """Classify a tyre: 'unknown', 'fresh', 'ok', 'worn' or 'cliff'.

    fresh: age <= 3; cliff: age >= life; worn: age >= 70% of life; else ok.
    """
    if tyre_life(compound)==0:
        return "unknown"
    if age_laps<=3:
        return "fresh"
    if age_laps>=tyre_life(compound):
        return "cliff"
    if age_laps>=0.7*tyre_life(compound):
        return "worn"
    
    return "ok"


def stint_laptimes(base_ms: int, laps: int, deg_ms_per_lap: int) -> list[int]:#stint = stretch  of laps a car runs on 1 set of tyres
    """Lap times for a stint where each lap is deg_ms_per_lap slower than the last."""
    stint=[]
    for i in range(laps):
        stint.append(base_ms+i*deg_ms_per_lap)

    return stint #finds out how much time is taken when tyre degrades


def first_lap_over(laptimes: list[int], threshold_ms: int) -> int:
    """1-based number of the first lap slower than threshold, or -1 if none."""
    for number,lap_ms in enumerate(laptimes, start=1):
        if lap_ms>threshold_ms:
            return number
        
    return -1 #indentation error printed -1 everytime


def laps_until_cliff(compound: str, age_laps: int) -> int:
    """Laps left before the cliff (never negative). Uses a while loop on purpose."""
    life=tyre_life(compound) #finds out the tyre life by compound using tyrelife function
    remaining=0
    while(age_laps+remaining<life):
        remaining+=1
    return remaining


def count_in_window(laptimes: list[int], low_ms: int, high_ms: int) -> int:
    """How many laps fall inside [low_ms, high_ms] inclusive."""
    count=0
    for i in range(len(laptimes)):
        if (low_ms<=laptimes[i]<=high_ms):
            count+=1
    return count


    

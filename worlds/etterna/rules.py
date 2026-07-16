from __future__ import annotations

from worlds.generic.Rules import set_rule


def has(state, player: int, item: str, count: int = 1) -> bool:
    return state.has(item, player, count)


def set_rules(world) -> None:
    player = world.player
    mw = world.multiworld

    mw.get_entrance("Menu -> Profile Setup", player).access_rule = lambda state: has(state, player, "Score Tracker")
    mw.get_entrance("Menu -> Community Packs", player).access_rule = lambda state: has(state, player, "Community Pack Access")
    mw.get_entrance("Menu -> Daily Challenges", player).access_rule = lambda state: has(state, player, "Daily Challenge Board")
    mw.get_entrance("Menu -> Replay Lab", player).access_rule = lambda state: has(state, player, "Replay Lab Access")
    mw.get_entrance("Menu -> Beginner Packs", player).access_rule = lambda state: has(state, player, "Beginner Pack Access")
    mw.get_entrance("Beginner Packs -> Standard Packs", player).access_rule = lambda state: has(state, player, "Standard Pack Access")
    mw.get_entrance("Standard Packs -> Advanced Packs", player).access_rule = lambda state: has(state, player, "Advanced Pack Access")
    mw.get_entrance("Advanced Packs -> Expert Packs", player).access_rule = lambda state: has(state, player, "Expert Pack Access")
    mw.get_entrance("Expert Packs -> Challenge Packs", player).access_rule = lambda state: has(state, player, "Challenge Pack Access")
    mw.get_entrance("Expert Packs -> Marathon", player).access_rule = lambda state: has(state, player, "Marathon Pack Access")
    mw.get_entrance("Challenge Packs -> Marathon", player).access_rule = lambda state: has(state, player, "Marathon Pack Access")
    mw.get_entrance("Skillsets -> Marathon", player).access_rule = lambda state: has(state, player, "Marathon Pack Access")
    mw.get_entrance("Modifiers -> Marathon", player).access_rule = lambda state: has(state, player, "Marathon Pack Access")

    if world.options.include_veteran_checks.value:
        mw.get_entrance("Challenge Packs -> Veteran Packs", player).access_rule = lambda state: has(state, player, "Veteran Pack Access")
        mw.get_entrance("Veteran Packs -> Elite Packs", player).access_rule = lambda state: has(state, player, "Elite Pack Access")
        mw.get_entrance("Elite Packs -> Legend Packs", player).access_rule = lambda state: has(state, player, "Legend Pack Access")
        mw.get_entrance("Veteran Packs -> Marathon", player).access_rule = lambda state: has(state, player, "Marathon Pack Access")
        mw.get_entrance("Elite Packs -> Marathon", player).access_rule = lambda state: has(state, player, "Marathon Pack Access")
        mw.get_entrance("Legend Packs -> Marathon", player).access_rule = lambda state: has(state, player, "Marathon Pack Access")

    stream = lambda state: has(state, player, "Stream License")
    jumpstream = lambda state: has(state, player, "Jumpstream License")
    handstream = lambda state: has(state, player, "Handstream License")
    stamina = lambda state: has(state, player, "Stamina License")
    jack = lambda state: has(state, player, "Jack License")
    chordjack = lambda state: has(state, player, "Chordjack License")
    technical = lambda state: has(state, player, "Technical License")
    chordstream = lambda state: has(state, player, "Chordstream License")
    strict = lambda state: has(state, player, "Strict Judgment Unlock")
    rate = lambda state: has(state, player, "Rate Mod Unlock")
    veteran = lambda state: has(state, player, "Veteran MSD License")
    elite = lambda state: has(state, player, "Elite MSD License")
    legend = lambda state: has(state, player, "Legend MSD License")
    setlist_10 = lambda state: has(state, player, "Progressive Setlist Length", 1)
    setlist_20 = lambda state: has(state, player, "Progressive Setlist Length", 2)
    setlist_30 = lambda state: has(state, player, "Progressive Setlist Length", 3)

    rules_by_location = {
        "Earn 3 AAA Grades": strict,
        "Earn 10 Expert AAA Grades": strict,
        "Earn a AAAA Grade": strict,
        "Hit 96 Wife Percent on Expert": strict,
        "Hit 97 Wife Percent on Challenge": strict,
        "Pass 1.1x Rate on Advanced Chart": rate,
        "Pass 1.2x Rate on Expert Chart": rate,
        "Pass a 1.3x Rate Chart": rate,
        "Pass an 18 Meter Chart": rate,
        "Pass a 20 Meter Chart": lambda state: rate(state) and stamina(state),
        "Pass a 22 Meter Chart": lambda state: rate(state) and stamina(state),
        "Reach Stream Skillset 10": stream,
        "Reach Stream Skillset 15": stream,
        "Reach Jumpstream Skillset 10": jumpstream,
        "Reach Jumpstream Skillset 15": jumpstream,
        "Reach Handstream Skillset 10": handstream,
        "Reach Handstream Skillset 15": handstream,
        "Reach Stamina Skillset 10": stamina,
        "Reach Stamina Skillset 15": stamina,
        "Reach Jack Skillset 10": jack,
        "Reach Chordjack Skillset 10": chordjack,
        "Reach Technical Skillset 10": technical,
        "Reach Technical Skillset 15": technical,
        "Reach Chordstream Skillset 10": chordstream,
        "Upload First Score": lambda state: has(state, player, "Score Tracker"),
        "Save First Replay": lambda state: has(state, player, "Replay Lab Access"),
        "Set a Personal Best": lambda state: has(state, player, "Score Tracker"),
        "Clear a Tournament Pack": lambda state: has(state, player, "Challenge Pack Access"),
        "Clear a Stamina-Focused Pack": stamina,
        "Clear a Technical-Focused Pack": technical,
        "Earn AA Across a Community Pack": strict,
        "Complete a Daily Rate Goal": rate,
        "Complete a Daily Wife Percent Goal": strict,
        "Complete a Daily Skillset Goal": technical,
        "Review a Replay": lambda state: has(state, player, "Replay Review"),
        "Improve a Replay by 1 Percent": lambda state: has(state, player, "Replay Review"),
        "Improve a Replay by 2 Percent": lambda state: has(state, player, "Replay Review") and strict(state),
        "Fix an Offset and Reclear": lambda state: has(state, player, "Offset Helper"),
        "Reclear a Failed Chart": lambda state: has(state, player, "Replay Review"),
        "Convert a B Grade to an A Grade": lambda state: has(state, player, "Replay Review"),
        "Pass a Chart with Mirror": lambda state: has(state, player, "Mirror Unlock"),
        "Pass a Chart with Shuffle": lambda state: has(state, player, "Shuffle Unlock"),
        "Pass a Chart with No Mines": lambda state: has(state, player, "No Mines Unlock"),
        "Pass a Chart with CMod": lambda state: has(state, player, "CMod/MMod Unlock"),
        "Pass a Chart with MMod": lambda state: has(state, player, "CMod/MMod Unlock"),
        "Pass a Chart on Strict Judge": strict,
        "Survive Immediate Fail": lambda state: has(state, player, "Fail Type Options"),
        "Clear a 10 Minute Setlist": setlist_10,
        "Clear a 20 Minute Setlist": lambda state: setlist_20(state) and stamina(state),
        "Clear a 30 Minute Setlist": lambda state: setlist_30(state) and stamina(state),
        "Clear a 45 Minute Setlist": lambda state: setlist_30(state) and stamina(state) and rate(state),
        "Complete Endgame Gauntlet": lambda state: setlist_30(state) and stamina(state) and strict(state) and rate(state),
        "The Etterna Finale": lambda state: state.has("Goal Fragment", player, world.options.goal_fragments_required.value)
        and has(state, player, "Finale Access")
        and has(state, player, "Marathon Pack Access")
        and setlist_30(state)
        and stamina(state),
    }

    if world.options.include_veteran_checks.value:
        rules_by_location.update(
            {
                "Pass a 23 MSD Chart": lambda state: veteran(state) and stamina(state),
                "Pass a 25 MSD Chart": lambda state: veteran(state) and stamina(state) and rate(state),
                "Hit 98 Wife Percent on Veteran": lambda state: veteran(state) and strict(state),
                "Pass a 1.4x Rate Chart": lambda state: veteran(state) and rate(state),
                "Pass a 28 MSD Chart": lambda state: elite(state) and stamina(state),
                "Pass a 30 MSD Chart": lambda state: elite(state) and stamina(state) and rate(state),
                "Earn 5 Elite AAAA Grades": lambda state: elite(state) and strict(state),
                "Pass a 1.5x Rate Chart": lambda state: elite(state) and rate(state),
                "Pass a 32 MSD Chart": lambda state: legend(state) and stamina(state),
                "Pass a 35 MSD Chart": lambda state: legend(state) and stamina(state) and rate(state),
                "Hit 99 Wife Percent on Legend": lambda state: legend(state) and strict(state),
                "Complete Legend Gauntlet": lambda state: legend(state) and stamina(state) and strict(state) and rate(state),
            }
        )

    if world.options.include_hard_checks.value:
        rules_by_location.update(
            {
                "Earn 10 AAAA Grades": strict,
                "Pass a 24 Meter Chart": lambda state: rate(state) and stamina(state),
                "Pass a 26 MSD Chart": lambda state: rate(state) and stamina(state),
                "Reach Any Skillset 20": lambda state: technical(state) and stamina(state),
                "Clear a Sightread Gauntlet": lambda state: strict(state) and rate(state),
            }
        )

    for location_name, rule in rules_by_location.items():
        set_rule(mw.get_location(location_name, player), rule)

    mw.completion_condition[player] = lambda state: state.can_reach("The Etterna Finale", "Location", player)

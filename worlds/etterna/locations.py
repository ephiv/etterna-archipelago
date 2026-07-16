from __future__ import annotations

from BaseClasses import Location

BASE_ID = 557700000

LOCATION_GROUPS = {
    "Menu": [
        "Sync Machine Profile",
        "Calibrate Global Offset",
    ],
    "Profile Setup": [
        "Upload First Score",
        "Save First Replay",
        "Create Favorites Folder",
        "Complete Input Consistency Check",
        "Set a Personal Best",
    ],
    "Beginner Packs": [
        "Clear 5 Beginner Charts",
        "Clear 1 Beginner Pack",
        "Clear 3 Beginner Packs",
        "Earn 3 A Grades",
        "Earn 5 Beginner AA Grades",
        "Hit 90 Wife Percent on Beginner",
        "Pass a 6 Meter Chart",
        "Pass a 8 Meter Chart",
    ],
    "Standard Packs": [
        "Clear 10 Standard Charts",
        "Clear 1 Standard Pack",
        "Clear 3 Standard Packs",
        "Earn 5 AA Grades",
        "Earn 5 Standard AAA Grades",
        "Hit 93 Wife Percent on Standard",
        "Pass a 10 Meter Chart",
        "Pass a 12 Meter Chart",
    ],
    "Advanced Packs": [
        "Clear 15 Advanced Charts",
        "Clear 1 Advanced Pack",
        "Clear 3 Advanced Packs",
        "Earn 8 AA Grades",
        "Earn 5 Advanced AAA Grades",
        "Hit 95 Wife Percent on Advanced",
        "Pass a 14 Meter Chart",
        "Pass a 16 Meter Chart",
        "Pass 1.1x Rate on Advanced Chart",
    ],
    "Expert Packs": [
        "Clear 20 Expert Charts",
        "Clear 1 Expert Pack",
        "Clear 3 Expert Packs",
        "Earn 3 AAA Grades",
        "Earn 10 Expert AAA Grades",
        "Hit 96 Wife Percent on Expert",
        "Pass an 18 Meter Chart",
        "Pass a 20 Meter Chart",
        "Pass 1.2x Rate on Expert Chart",
    ],
    "Challenge Packs": [
        "Clear 1 Challenge Pack",
        "Clear 3 Challenge Packs",
        "Earn a AAAA Grade",
        "Pass a 22 Meter Chart",
        "Hit 97 Wife Percent on Challenge",
        "Pass a 1.3x Rate Chart",
    ],

    "Veteran Packs": [
        "Clear 1 Veteran Pack",
        "Clear 3 Veteran Packs",
        "Pass a 23 MSD Chart",
        "Pass a 25 MSD Chart",
        "Hit 98 Wife Percent on Veteran",
        "Pass a 1.4x Rate Chart",
    ],
    "Elite Packs": [
        "Clear 1 Elite Pack",
        "Clear 3 Elite Packs",
        "Pass a 28 MSD Chart",
        "Pass a 30 MSD Chart",
        "Earn 5 Elite AAAA Grades",
        "Pass a 1.5x Rate Chart",
    ],
    "Legend Packs": [
        "Clear 1 Legend Pack",
        "Pass a 32 MSD Chart",
        "Pass a 35 MSD Chart",
        "Hit 99 Wife Percent on Legend",
        "Complete Legend Gauntlet",
    ],

    "Community Packs": [
        "Clear a Curated Community Pack",
        "Clear 3 Curated Community Packs",
        "Clear a Tournament Pack",
        "Clear a Stamina-Focused Pack",
        "Clear a Technical-Focused Pack",
        "Earn AA Across a Community Pack",
    ],
    "Daily Challenges": [
        "Complete a Daily Chart Goal",
        "Complete 3 Daily Chart Goals",
        "Complete a Daily Rate Goal",
        "Complete a Daily Wife Percent Goal",
        "Complete a Daily Skillset Goal",
    ],
    "Replay Lab": [
        "Review a Replay",
        "Improve a Replay by 1 Percent",
        "Improve a Replay by 2 Percent",
        "Fix an Offset and Reclear",
        "Reclear a Failed Chart",
        "Convert a B Grade to an A Grade",
    ],
    "Skillsets": [
        "Reach Stream Skillset 10",
        "Reach Stream Skillset 15",
        "Reach Jumpstream Skillset 10",
        "Reach Jumpstream Skillset 15",
        "Reach Handstream Skillset 10",
        "Reach Handstream Skillset 15",
        "Reach Stamina Skillset 10",
        "Reach Stamina Skillset 15",
        "Reach Jack Skillset 10",
        "Reach Chordjack Skillset 10",
        "Reach Technical Skillset 10",
        "Reach Technical Skillset 15",
        "Reach Chordstream Skillset 10",
    ],
    "Modifiers": [
        "Pass a Chart with Mirror",
        "Pass a Chart with Shuffle",
        "Pass a Chart with No Mines",
        "Pass a Chart with CMod",
        "Pass a Chart with MMod",
        "Pass a Chart on Strict Judge",
        "Survive Immediate Fail",
    ],
    "Marathon": [
        "Clear a 10 Minute Setlist",
        "Clear a 20 Minute Setlist",
        "Clear a 30 Minute Setlist",
        "Clear a 45 Minute Setlist",
        "Complete Endgame Gauntlet",
        "The Etterna Finale",
    ],
}
HARD_LOCATIONS = [
    "Earn 10 AAAA Grades",
    "Pass a 24 Meter Chart",
    "Pass a 26 MSD Chart",
    "Reach Any Skillset 20",
    "Clear a Sightread Gauntlet",
]

ALL_LOCATION_NAMES = [name for names in LOCATION_GROUPS.values() for name in names] + HARD_LOCATIONS
LOCATION_NAME_TO_ID = {name: BASE_ID + index for index, name in enumerate(ALL_LOCATION_NAMES)}


class EtternaLocation(Location):
    game = "Etterna"

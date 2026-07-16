from dataclasses import dataclass

from Options import Choice, PerGameCommonOptions, Range, Toggle


class GoalFragmentsRequired(Range):
    """Goal Fragments required before the finale check is in logic."""

    display_name = "Goal Fragments Required"
    range_start = 1
    range_end = 18
    default = 12


class IncludeHardChecks(Toggle):
    """Adds higher-meter and AAA-grade checks for experienced Etterna players."""

    display_name = "Include Hard Checks"


class IncludeVeteranChecks(Toggle):
    """Adds post-Challenge MSD checks for veteran Etterna players."""

    display_name = "Include Veteran Checks"


class StartingPackTier(Choice):
    """Initial pack tier available before receiving pack unlocks."""

    display_name = "Starting Pack Tier"
    option_beginner = 0
    option_standard = 1
    default = 0


class TrapChance(Range):
    """Percent chance that generated filler is a Minefield Trap."""

    display_name = "Trap Chance"
    range_start = 0
    range_end = 100
    default = 10


@dataclass
class EtternaOptions(PerGameCommonOptions):
    goal_fragments_required: GoalFragmentsRequired
    include_hard_checks: IncludeHardChecks
    include_veteran_checks: IncludeVeteranChecks
    starting_pack_tier: StartingPackTier
    trap_chance: TrapChance

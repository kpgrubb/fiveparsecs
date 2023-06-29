# Relevant modules
import random


class Dice:
    # We use this dice throughout the program

    def __init__(self, sides=6, rolls=1):
        self.sides = sides
        self.rolls = rolls

    def roll_dice(self):
        results = []
        for _ in range(self.rolls):
            result = random.randint(1, self.sides)
            results.append(result)
        return results


d100 = Dice(100, 1)
d6 = Dice(6, 1)

# key objects that will be referenced regularly through program
credits = 0
patrons = 0
rivals = 0
quest_rumors = 0
story_points = 0
crew = []


# Member class creates template for individual crew members
class Member:
    # creates an individual character with necessary attributes and methods supporting gameplay management

    # initializes the core statistics for each crew member; default baseline human
    def __init__(self, name="John Doe", reactions=1, combat=0, speed=4, toughness=3, savvy=0, luck=0, race="Human",
                 weapons=None, equipment=None, xp=0, special=None, background=None, motivation=None, classtype=None):
        self.name = name
        self.reactions = reactions
        self.combat = combat
        self.speed = speed
        self.toughness = toughness
        self.savvy = savvy
        self.luck = luck
        self.race = race
        self.weapons = weapons if weapons else []
        self.equipment = equipment if equipment else []
        self.xp = xp
        self.special = special if special else []
        self.background = background if background else []
        self.motivation = motivation
        self.classtype = classtype

    def __str__(self):
        # creates a default representation of the Crew Member

        member_attributes = (
            f"Name: {self.name}, Race: {self.race} \n"
            f"Combat: {self.combat} Reactions: {self.reactions} "
            f"Speed: {self.speed}, Toughness: {self.toughness} "
            f"Savvy: {self.savvy}, Luck: {self.luck} \n"
            f"XP: {self.xp} \n"
            f"Background: {self.background} \n"
            f"Motivation: {self.motivation} \n"
            f"Class: {self.classtype} \n"
        )

        member_equipment = "Weapons:\n" + "\n".join(str(weapon) for weapon in self.weapons) + "\n"
        member_equipment += "Equipment:\n" + "\n".join(str(item) for item in self.equipment) + "\n"

        member_special = "Special:\n" + "\n".join(str(quality) for quality in self.special) + "\n"

        return member_attributes + member_equipment + member_special


class Weapon:
    def __init__(self, name, type, range, shots, damage, traits=None):
        self.name = name
        self.type = type
        self.range = range
        self.shots = shots
        self.damage = damage
        self.traits = traits if traits else []

    def __str__(self):
        weapon_info = (
            f"Name: {self.name}, Type: {self.type}, Range: {self.range}, "
            f"Shots: {self.shots}, Damage: {self.damage}"
        )
        trait_info = "Trait(s):\n".join(str(trait) for trait in self.traits)

        return weapon_info + ("\n" + trait_info if self.traits else "")

class Equipment:
    def __init__(self, name="thing", type=None, effect=None):
        self.name = name
        self.type = type
        self.effect = effect

    def __str__(self):
        return f"Name: {self.name}, Type: {self.type}, Effect: {self.effect}"

class Trait:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"


# Weapon Traits

trait_area = Trait("Area", "Resolve all shots against the initial target. They cannot be spread. Then resolve one "
                           "bonus shot against every figure within two inches")
trait_clumsy = Trait("Clumsy", "-1 to Brawling rolls, if opponent has higher Speed")
trait_critical = Trait("Critical", "A natural 6 on the to Hit roll will inflict 2 Hits on target")
trait_elegant = Trait("Elegant", "When Brawling, the fighter may reroll the die. Enemies will always reroll if they "
                                 "have a lower total than their opponent, and can improve the result.")
trait_focused = Trait("Focused", "All shots must be against a single target.")
trait_heavy = Trait("Heavy", "-1 penalty to Hit if the firer moved this round.")
trait_impact = Trait("Impact", "If target is Stunned, place a second Stun marker.")
trait_melee = Trait("Melee", "+2 to Brawling rolls.")
trait_piercing = Trait("Piercing", "Ignore Armor saving throws")
trait_pistol = Trait("Pistol", "+1 to Brawling rolls")
trait_singleuse = Trait("Single use", "The item can be used only once and must be deducted from the available supply. "
                                      "The Panic Fire rule (p.46) can be used with Single use weapons.")
trait_snapshot = Trait("Snap shot", "+1 to Hit within 6 inches")
trait_stun = Trait("Stun", "All targets are automatically Stunned. No damage rolls take place.")
trait_terrifying = Trait("Terrifying", "Any target hit must retreat 1D6 inches away from the firer")

# Weapons
#note that infantry laser is muliti-class

weap_autorifle = Weapon("Auto rifle", "military", 24, 2, 0, traits=None)
weap_beampistol = Weapon("Beam pistol", "hi-tech", 10, 1,1, traits=[trait_pistol,trait_critical])
weap_blade = Weapon("Blade", "low-tech", "Brawl", None, 0, traits=trait_melee)
weap_blastpistol = Weapon("Blast pistol", 'hi-tech', 8, 1, 1, traits=trait_pistol)
weap_blastrifle = Weapon("Blast rifle", "hi-tech", 16, 1, 1, traits=None)
weap_boardingsaber = Weapon("Boarding Saber", "military", "Brawl", 0, 1, traits=[trait_melee, trait_elegant])
weap_brutalmeleeweapon = Weapon("Brutal melee weapon", "low-tech", "Brawl", 0, 1, traits=[trait_melee, trait_clumsy])
weap_clingfirepistol = Weapon("Cling fire pistol", None, 12, 2, 1, traits=[trait_focused, trait_terrifying])
weap_colonyrifle = Weapon("Colony Rifle", "low-tech", 18, 1, 0, traits=None)
weap_dazzlegrenade = Weapon("Dazzle Grenade", None, 6, 1, None, traits=[trait_area, trait_stun, trait_singleuse])
weap_duelingpistol = Weapon("Dueling Pistol", "hi-tech", 8, 1, 0, traits=[trait_pistol,trait_critical])
weap_flakgun = Weapon("Flak gun", None, 8, 2, 1, traits=[trait_focused, trait_critical])
weap_frakkgrenade = Weapon("Frakk grenade", None, 6, 2, 0, traits=[trait_area, trait_heavy, trait_singleuse])
weap_furyrifle = Weapon("Fury rifle", None, 24, 1, 2, traits=[trait_heavy, trait_piercing])
weap_glaresword = Weapon("Glare sword", "hi-tech", "Brawl", None, 0, traits=[trait_melee, trait_elegant, trait_piercing])
weap_handcannon = Weapon("Hand cannon", "hi-tech", 8, 1, 2, traits=trait_pistol)
weap_handflamer = Weapon("Hand flamer", None, 12, 2, 1, traits=[trait_focused, trait_area])
weap_handlaser = Weapon("Hand laser", "hi-tech", 12, 1, 0, traits=[trait_snapshot, trait_pistol])
weap_handgun = Weapon("Hand gun", "low-tech", 12, 1, 0, traits=trait_pistol)
weap_holdoutpistol = Weapon("Holdout pistol", None, 4, 1, 0, traits=[trait_pistol, trait_melee])
weap_huntingrifle = Weapon("Hunting rifle", "low-tech", 30, 1, 1, traits=trait_heavy)
weap_hyperblaster = Weapon("Hyper blaster", None, 24, 3, 1, traits=None)
weap_infantrylaser = Weapon("Infantry laser", ["hi-tech","military"], 30, 1, 0, traits=trait_snapshot)
weap_machinepistol = Weapon("Machine pistol", "low-tech", 8, 2, 0, traits=[trait_pistol, trait_focused])
weap_marksmansrifle = Weapon("Marksman rifle", "military", 36, 1, 0, traits=trait_heavy)
weap_militaryrifle = Weapon("Military rifle", "military", 24, 1, 0, traits=None)
weap_needlerifle = Weapon("Needle rifle", "military", 18, 2, 0, traits=trait_critical)
weap_plasmarifle = Weapon("Plasma rifle", "hi-tech", 20, 2, 1, traits=[trait_focused, trait_piercing])
weap_powerclaw = Weapon("Power claw", None, "Brawl", None, 3, traits=[trait_melee, trait_clumsy])
weap_rattlegun = Weapon("Rattle gun", "military", 24, 3, 0, traits=trait_heavy)
weap_rippersword = Weapon("Ripper sword", "type", "Brawl", None, 1, traits=trait_melee)
weap_scrappistol = Weapon("Scrap pistol", "type", 9, 1, 0, traits=trait_pistol)
weap_shatteraxe = Weapon("Shatter axe", "military", "Brawl", None, 2, traits=trait_melee)
weap_shellgun = Weapon("Shell gun", None, 30, 2, 0, traits=[trait_heavy, trait_area])
weap_shotgun = Weapon("Shotgun", "low-tech", 12, 2, 1, traits=trait_heavy)
weap_suppressionmaul = Weapon("Suppression maul", "type", "Brawl", None, 1, traits=[trait_melee, trait_impact])

# Equipment

eq_assaultblade = Equipment("Assault Blade", "Gear", "The weapon gains the Melee trait. Damage +1, and wins combat on "
                                                     "a Draw. Non-Pistol only.")
eq_beamlight = Equipment("Beam Light", "Gear", "When using the weapon in conditions of reduced visibility, increase "
                                               "visibility by +3 inches.")
eq_bipod = Equipment("Bipod", "Gear", "The weapon receives +1 to Hit at ranges over 8” when Aiming or when firing "
                                      "from Cover. Non-Pistol only.")
eq_boosterpills = Equipment("Bipod", "Gear", "When taken, the character removes all Stun markers. They may move at "
                                             "double normal Speed this round.")
eq_camocloak = Equipment("Camo Cloak", "Gear", "If character is within 2” of Cover, they are counted as being in "
                                               "Cover. Does not apply if the shooter is within 4 inches.")
eq_combatarmor = Equipment("Combat Armor", "Gear", "Saving Throw 5+.")
eq_communicator = Equipment("Communicator", "Gear", "When making the Reaction roll each round, you may roll one "
                                                    "additional die, then choose a die to discard.")
eq_concealedblade = Equipment("Concealed Blade", "Gear", "If the character begins their round within 2 inches of an "
                                                         "opponent, they may throw the blade as a Free Action before "
                                                         "doing anything else. Roll to Hit normally, resolving the "
                                                         "Hit with Damage +0. The blade can be used once per battle, "
                                                         "and is replaced afterwards for free.")
eq_fakeid = Equipment("Fake ID", "Gear", "Add +1 to all attempts to obtain a license or other legal document")
eq_fixer = Equipment("Fixer", "Gear", "One piece of damaged or destroyed personal equipment can be repaired "
                                      "automatically, and at no cost. Single-use")
eq_fragvest = Equipment("Frag Vest", "Gear", "The wearer receives a 6+ Saving Throw, improved to 5+ against any Area "
                                             "attack.")
eq_grapplelauncher = Equipment("Grapple Launcher", "Gear", "As a Combat Action, the character may use the launcher to "
                                                           "scale a terrain feature within 1 inch. The character can "
                                                           "ascend up to 12 inches but must reach a surface they can "
                                                           "stand on")
eq_hazardsuit = Equipment("Hazard Suit", "Gear", "If the character takes a Hit from an environmental hazard, "
                                                 "they receive a 5+ Saving Throw.")
eq_lasersight = Equipment("Laser Sight", "Gear", "The weapon receives the Snap Shot trait. Pistol only.")
eq_loadeddice = Equipment("Load Dice", "Gear", "Each campaign turn, one crew member may gamble on the side. Roll 1D6. "
                                               "On a 1-4, earn that many credits. On a 5, earn nothing. On a 6, "
                                               "the locals don’t take kindly to losing: The dice are lost and the "
                                               "crew member must roll on the postbattle Injury Table.")
eq_medpatch = Equipment("Med-patch", "Gear", "A character recovering from an Injury may subtract one campaign turn "
                                             "from the recovery duration required. If this reduces the time to zero "
                                             "turns, they may act normally this campaign turn. Single-use.")
eq_nanodoc = Equipment("Nano-doc", "Gear", "Prevent one roll on the post-battle Injury Table, no matter the source of "
                                           "the injury. You must decide before rolling the dice. Single-use.")
eq_purifier = Equipment("Purifier", "Gear", "Each campaign turn, the Purifier can be used to generate clean water "
                                            "which can be sold off for 1 credit. This does not require a crew member "
                                            "to operate, but only one Purifier may be used at a time")
eq_scannerbot_gadget = Equipment("Scanner Bot", "Gadget", "The crew adds +1 to all Seize the Initiative rolls")
eq_sectorpermit = Equipment("Sector Permit", "Gear", "Whenever you arrive at a planet where a license is required, "
                                                     "roll 1D6. On a 4+, the Sector Permit is accepted. You must roll"
                                                     " for each license type, on each planet.")
eq_steelboots = Equipment("Steel Bots", "Gear", "If the character rolls a natural 5 or 6 in a Brawl and wins the "
                                                "Brawl, they may opt to kick instead of striking normally. This hits "
                                                "with Damage +0 and knocks them 1D3 inches directly backwards. If the "
                                                "opponent is kicked into another character, that character is knocked "
                                                "1D3 inches in a random direction")
eq_trackersight = Equipment("Track Sight", "Gear", "+1 to Hit if you fired at the same target during your previous "
                                                   "round.")
eq_aicompanion = Equipment("AI Companion", "Gadget", "When making Savvy rolls, the character may roll twice and pick "
                                                     "the better score")
eq_analyzer = Equipment("Analyzer", "Gadget", "Add +1 when rolling to see if Rumors result in a Quest and when "
                                              "rolling for Quest resolution.")
eq_battlevisor = Equipment("Battle Visor", "Gadget", "When shooting, the character may reroll any 1s on the firing dice")
eq_boostedarm = Equipment("Boosted Arm", "Gadget", "Increase Grenade range by +2 inches. If the character ends their "
                                                   "Move in contact with an obstacle that is no taller than the "
                                                   "miniature, they may pull themselves up on top (but not cross) as "
                                                   "a Free Action")
eq_boostedleg = Equipment("Boosted Leg", "Gadget", "Increase base move and Dash speed by +1 inch each. ")
eq_cyberhand = Equipment("Cyber Hand", "Gadget", "The character may take any one Pistol they own and build it into "
                                                 "their hand. Range is reduced to half, but the weapon always shoots "
                                                 "with +1 to Hit and an additional +1 bonus when Brawling.")
eq_displacer = Equipment("Displacer", "Gadget", "Usable once per mission instead of Moving. Aim anywhere in sight. "
                                                "The character teleports to a point 1D6 inches away in a random "
                                                "direction. If the teleport would end up within a solid obstacle, "
                                                "the device fails and must be Repaired before it can used again. The "
                                                "character emerges on the same height as the aiming point, "
                                                "which may cause them to fall if they emerge in open air. The "
                                                "character may take a Combat Action after teleporting. If used by a "
                                                "Precursor character, you may establish two “landing points”, "
                                                "and select to use either")
eq_distractionbot = Equipment("Distraction Bot", "Gadget", "Usable once per battle as a Combat Action. Select an "
                                                           "enemy within 12 inches. Next time they would become "
                                                           "active, they are unable to act, though they remove Stun "
                                                           "markers as normal. Use a small marker to remember")
eq_duplicator = Equipment("Duplicator", "Gadget", "Create a perfect copy of any one item in your inventory. A "
                                                  "Duplicator cannot copy a Duplicator, due to the same proprietary "
                                                  "nano-bot lock-out codes that makes your printer say it’s out of "
                                                  "ink after printing 17 pages. Single-use.")
eq_instawall = Equipment("Insta-Wall", "Gadget", "May be used once per mission as a Combat Action. Place a marker "
                                                 "within 3 inches, then place a 2 inches long force wall oriented any "
                                                 "way you like, as long as it touches the marker. The wall is "
                                                 "man-height and impenetrable to attacks (but does not block sight or "
                                                 "mental abilities). At the start of each subsequent round, "
                                                 "a D6 is rolled. On a 6, the wall dissipates.")
eq_jumpbelt = Equipment("Jump Belt", "Gadget", "Instead of Moving normally, the character may jump up to 9 inches "
                                               "directly forward and 3 inches upwards. The character may take a "
                                               "Combat Action normally after landing.")
eq_nerveadjuster = Equipment("Nerve Adjuster", "Gadget", "Whenever the character is Stunned for any reason, "
                                                         "they receive a 5+ Saving Throw to avoid the Stun.")
eq_repairbot = Equipment("Repair Bot", "Gadget", "+1 to all Repair attempts.")
eq_scannerbot_gear = Equipment("Scanner Bot", "Gadget", "The crew adds +1 to all Seize the Initiative rolls")
eq_screengenerator = Equipment("Screen Generator", "Gadget", "Receives a 5+ Saving Throw against gunfire. No effect "
                                                             "against Area or Melee attacks.")
eq_seekersight = Equipment("Seeker Sight", "Gadget", "The weapon receives +1 to Hit if the shooter did not Move this "
                                                     "round.")
eq_shockattachment = Equipment("Shock Attachment", "Gadget", "The weapon receives the Impact trait against targets "
                                                             "within 8”.")
eq_snooperbot = Equipment("Snooper Bot", "Gadget", "May be deployed before a battle, if the Seize the Initiative roll "
                                                   "would be penalized or negated. The penalty can be ignored, "
                                                   "but the Bot is Damaged on a D6 roll of a 1.")
eq_sonicemitter = Equipment("Sonic Emitter", "Gadget", "Any enemy within 5 inches suffers -1 to all Hit rolls when "
                                                       "shooting.")
eq_stabilizer = Equipment("Stabilizer", "Gadget", "Weapon may ignore Heavy trait")
eq_stealthgear = Equipment("Stealth Gear", "Gadget", "Enemies firing from a range over 9” are -1 to Hit")
eq_stimpack = Equipment("Stim-pack", "Gadget", "If a character would become a casualty, they remain on the table with "
                                               "a single Stun marker. This item can be used reflexively upon becoming"
                                               " a casualty. It does not require an action")


# Loot Functions

def get_random_weapon(type):
    weapon_dict = {
        "low-tech": {
            (1, 15): weap_handgun,
            (16, 35): weap_scrappistol,
            (36, 40): weap_machinepistol,
            (41, 65): weap_colonyrifle,
            (66, 75): weap_shotgun,
            (76, 80): weap_huntingrifle,
            (81, 95): weap_blade,
            (96, 100): weap_brutalmeleeweapon
        },
        "military": {
            (1, 25): weap_militaryrifle,
            (26, 45): weap_infantrylaser,
            (46, 50): weap_marksmansrifle,
            (51, 60): weap_needlerifle,
            (61, 75): weap_autorifle,
            (76, 80): weap_rattlegun,
            (81, 95): weap_boardingsaber,
            (96, 100): weap_shatteraxe
        },
        "hi-tech": {
            (1, 5): weap_duelingpistol,
            (6, 15): weap_handcannon,
            (16, 30): weap_handlaser,
            (31, 45): weap_beampistol,
            (46, 55): weap_infantrylaser,
            (56, 70): weap_blastpistol,
            (71, 80): weap_blastrifle,
            (81, 85): weap_plasmarifle,
            (86, 100): weap_glaresword
        }
    }

    weapon_type_dict = weapon_dict.get(type)
    if weapon_type_dict:
        roll = random.randint(1, 100)
        for roll_range, weapon_instance in weapon_type_dict.items():
            if roll in range(roll_range[0], roll_range[1] + 1):
                return weapon_instance

    return None

#Can I adjust the Scanner bot to be a single instance?
def get_random_equipment(type):
    weapon_dict = {
        "gear": {
            (1, 4): eq_assaultblade,
            (5, 10): eq_beamlight,
            (11, 15): eq_bipod,
            (16, 20): eq_boosterpills,
            (21, 24): eq_camocloak,
            (25, 28): eq_combatarmor,
            (29, 33): eq_communicator,
            (34, 37): eq_concealedblade,
            (38, 42): eq_fakeid,
            (43, 46): eq_fixer,
            (47, 52): eq_fragvest,
            (53, 57): eq_grapplelauncher,
            (58, 61): eq_hazardsuit,
            (62, 65): eq_lasersight,
            (66, 69): eq_loadeddice,
            (70, 75): eq_medpatch,
            (76, 81): eq_nanodoc,
            (82, 85): eq_purifier,
            (86, 89): eq_scannerbot_gear,
            (90, 92): eq_sectorpermit,
            (93, 96): eq_steelboots,
            (97, 100): eq_trackersight
        },
        "gadget": {
            (1, 4): eq_aicompanion,
            (5, 9): eq_analyzer,
            (10, 13): eq_battlevisor,
            (14, 17): eq_boostedarm,
            (18, 21): eq_boostedleg,
            (22, 24): eq_cyberhand,
            (25, 27): eq_displacer,
            (28, 31): eq_distractionbot,
            (32, 36): eq_duplicator,
            (37, 41): eq_instawall,
            (42, 46): eq_jumpbelt,
            (47, 50): eq_nerveadjuster,
            (51, 55): eq_repairbot,
            (56, 60): eq_scannerbot_gadget,
            (61, 65): eq_screengenerator,
            (66, 69): eq_seekersight,
            (70, 73): eq_shockattachment,
            (74, 79): eq_snooperbot,
            (80, 83): eq_sonicemitter,
            (84, 89): eq_stabilizer,
            (90, 93): eq_stealthgear,
            (94, 100): eq_stimpack
        }
    }

    equipment_type_dict = weapon_dict.get(type)
    if equipment_type_dict:
        roll = random.randint(1, 100)
        for roll_range, equipment_instance in equipment_type_dict.items():
            if roll in range(roll_range[0], roll_range[1] + 1):
                return equipment_instance

    return None

def generate_character():
    global credits
    global patrons
    global quest_rumors
    global story_points
    new_character = Member()
    new_character.name = input("Enter your character name.")
    print(f"Let's define {new_character.name}'s race.")
    print("Rolling...")
    # note that the default roll result is a list, the index of 0 is needed to get the right integer
    roll_result = d100.roll_dice()[0]
    print(f"Rolled a {roll_result}.")
    if roll_result <= 60:
        new_character.race = "Human"
        print("Generating a human character...")
        new_character.special.append("Humans can exceed one point of luck.")
    elif 61 <= roll_result <= 80:
        print("Generating Primary Alien Race...")
        new_roll = d100.roll_dice()[0]
        if new_roll <= 20:
            new_character.race = "Engineer"
            print("Generating an Engineer character...")
            new_character.toughness = 2
            new_character.savvy = 1
            new_character.special.append("+1 to roll for repairing a damaged item")
            new_character.special.append("Toughness can never exceed 4 (even with equipment)")
        elif 21 <= new_roll <= 40:
            new_character.race = "K'Erin"
            print("Generating an K'Erin character...")
            new_character.toughness = 4
            new_character.special.append("When brawling, roll twice.")
            new_character.special.append(
                "If you begin your round within base movement speed of enemy, "
                "you must move to engage them in brawling combat"
            )
        elif 41 <= new_roll <= 55:
            new_character.race = "Soulless"
            print("Generating an Soulless character...")
            new_character.toughness = 4
            new_character.savvy = 1
            new_character.special.append("6+ Armor Saving Throw")
            new_character.special.append("Cannot use consumables or receive implants; use Bot Injury Table")
            new_character.special.append("May receive Bot Upgrades, but cost is 1.5x")
        elif 56 <= new_roll <= 70:
            new_character.race = "Precursor"
            print("Generating an Precursor character...")
            new_character.speed = 5
            new_character.toughness = 2
            new_character.special.append(
                "Roll 2x on Character Event Table and pick. Or spend 1 Story Point to skip."
            )
        elif 71 <= new_roll <= 90:
            new_character.race = "Feral"
            print("Generating a Feral character...")
            new_character.special.append("Enemy imposed penalties to Seize the Initiative rolls ignored")
            new_character.special.append(
                "When making a Reaction Roll at start of battle round, if the dice only score a single 1"
                "it must be given to Feral crew member, if possible."
            )
        else:
            new_character.race = "Swift"
            print("Generating a Swift character...")
            new_character.speed = 5
            new_character.special.append(
                "May glide down to a lower position. Horizontal distance = Height Diff.")
            new_character.special.append(
                "Can leap gaps 4 inches wide; can jump down from any height without dmg.")
            new_character.special.append(
                "When firing a weapon with multiple shots,"
                "all shots must be directed towards the same target"
            )
    elif 81 <= roll_result <= 90:
        new_character.race = "Bot"
        print("Generating a Bot character...")
        new_character.reactions = 0
        new_character.toughness = 4
        new_character.combat = 1
        new_character.special.append("6+ Armor Saving Throw")
        new_character.special.append("Do not earn XP; use credits to upgrade")
        new_character.special.append("Do not benefit from implants or use of consumables")
        new_character.special.append("Cannot be subject to Character Event")
        new_character.special.append("Do not roll on character creation table")
        new_character.special.append("Note separate injury table")
    else:
        print("Generating Strange Character")
        new_roll = d100.roll_dice()[0]
        print(f"Rolled a {new_roll}")
        if new_roll <= 2:
            new_character.race = "Special: De-Converted"
            new_character.special.append("6+ Armor Saving Throw")
            new_character.special.append("Can fit 3 implants")
            new_character.special.append("Savvy never improved")
            new_character.special.append("Motivation is always revenge")
        elif 3 <= new_roll <= 8:
            new_character.race = "Special: Unity Agent"
            new_character.reactions = 2
            new_character.special.append(
                "Call in a Favor: Each campaign turn, you may roll 2d6"
                "On 10-12, you can remove a Rival, gain a Quest Rumor or gain a Patron"
                "On 2-4, you must travel to next planet immediately; if unable, lose trait permanently"
            )
            new_character.special.append("Motivation is always Order.")
        elif 9 <= new_roll <= 17:
            new_character.race = "Special: Mysterious Past"
            new_character.special.append(
                "Roll 2x on Background Table; apply both results."
                "Ignore bonus story points"
            )
        elif 18 <= new_roll <= 22:
            new_character.race = "Special: Hakshan"
            new_character.special.append("Automatically has Truth Motivation")
        elif 23 <= new_roll <= 27:
            new_character.race = "Special: Stalker"
            new_character.special.append(
                "May teleport 1d6 as alternative movement option"
                "4XP can buy 1 inch of distance"
            )
        elif 28 <= new_roll <= 34:
            new_character.race = "Special: Hulker"
            new_character.toughness = 5
            new_character.combat = 1
            new_character.special.append("When shooting, combat skill is always 0")
            new_character.special.append("Ignore Clumsy and Heavy traits on weapons")
            new_character.special.append("Any technician, scientist or hacker result is treated as Primative "
                                         "instead")
        elif 35 <= new_roll <= 41:
            new_character.race = "Special: Hopeful Rookie"
            new_character.luck = 1
            new_character.special.append("+1 XP for every game where they do not become a casualty")
            new_character.special.append(
                "First time they become a casualty, lose all Luck and never receive luck again"
                "No longer receives XP bonus either"
            )
        elif 42 <= new_roll <= 47:
            new_character.race = "Special: Genetic Uplift"
            new_character.reactions = 2
            new_character.speed = 5
            new_character.toughness = 4
            new_character.combat = 1
            new_character.special.append(
                "Background rolls that would result in additional credits are ignored."
                "The crew receives 1 additional Rival."
            )
        elif 48 <= new_roll <= 53:
            new_character.race = "Special: Mutant"
            new_character.special.append("Cannot perform Recruit or Find Patron Tasks.")
            new_character.special.append("Background is always Lower classes of megacity")
        elif 54 <= new_roll <= 58:
            new_character.race = "Special: Assault Bot"
            new_character.reactions = 0
            new_character.toughness = 4
            new_character.combat = 1
            new_character.special.append("5+ Armor Saving Throw")
            new_character.special.append("Do not earn XP; use credits to upgrade")
            new_character.special.append("Do not benefit from implants or use of consumables")
            new_character.special.append("Cannot be subject to Character Event")
            new_character.special.append("Do not roll on character creation table")
            new_character.special.append("Note separate injury table")
            new_character.special.append("Ignores Clumsy and Heavy traits on weapons")
        elif 59 <= new_roll <= 62:
            new_character.race = "Special: Manipulator"
            new_character.reactions = 2
            new_character.savvy = 1
            new_character.special.append("Cannot voluntarily enter Brawl")
            new_character.special.append("Use tentacles to fire 2 pistols in same round. May choose 2 targets")
            new_character.special.append(
                "Whenever the crew earns Story Points, roll 1d6 per Manipulator"
                "Each 6 grants a Bonus Story Point"
            )
            new_character.special.append("Background is always Bureaucrat.")
        elif 63 <= new_roll <= 67:
            new_character.race = "Special: Primitive"
            new_character.special.append("Cannot benefit from gun sights or fire above 8 inch range.")
            new_character.special.append("All Melee weapons count as Elegant.")
            new_character.special.append("Background is always Primitive or Regressed World.")
        elif 68 <= new_roll <= 73:
            new_character.race = "Special: Feeler"
            new_character.special.append(
                "Roll twice on Motivation Table and receive benefits of both rolls."
                "If crew member ever ends up in a fight with another crew member, they leave forever, "
                "immediately"
            )
        elif 74 <= new_roll <= 79:
            new_character.race = "Special: Emo-suppressed"
            new_character.special.append("Character will never voluntarily leave for any reason")
            new_character.special.append("Never receives Luck points")
            new_character.special.append("Motivation is always survival")
        elif 80 <= new_roll <= 85:
            new_character.race = "Special: Minor Alien"
            new_character.special.append("If Background, Motivation or Class Table results would grant bonus "
                                         "credits or bonus story points, reduce the final increase by 1")
            minor_alien_bonus = d6
            if minor_alien_bonus == 1:
                new_character.special.append("Reduce Reaction XP cost by 1")
            elif minor_alien_bonus == 2 or minor_alien_bonus == 3:
                new_character.special.append("Reduce Speed XP cost by 1")
            elif minor_alien_bonus == 4:
                new_character.special.append("Reduce Combat XP cost by 1")
            elif minor_alien_bonus == 5:
                new_character.special.append("Reduce Toughness XP cost by 1")
            else:
                new_character.special.append("Reduce Savvy XP cost by 1")
        elif 86 <= new_roll <= 87:
            new_character.race = "Special: Traveler"
            new_character.reactions = 3
            new_character.savvy = 2
            new_character.special.append("+2 Story Points")
            new_character.special.append("+2 Quest Rumors")
            new_character.special.append("+2 Speed if moving directly away from a visible enemy")
            new_character.special.append("After every battle, roll 2d6: On a 2, they disappear, never to be "
                                         "seen again. Claim 2 Story Points. On a 11-12, the crew immediately "
                                         "receives a Quest.")
            new_character.special.append("Motivation is always Truth")
        elif 88 <= new_roll <= 93:
            new_character.race = "Special: Empath"
            new_character.special.append("+1 to roll to Recruit or Find a Patron. Cannot be given implants "
                                         "without losing this .")
        else:
            new_character.race = "Special: Bio-Upgrade"
            new_character.special.append(
                "May have up to 4 implants and can benefit from 2 of the same implant.")
            new_character.special.append("If Background, Motivation or Class rolls produce bonus credits, "
                                         "receive 2 less.")
    print(f"Generated a {new_character.race}")
    print(f"Now generating background, motivation, and class.")
    bmc_gen = True
    while bmc_gen:
        if new_character.race == "Bot" or new_character.race == "Special:Assault Bot":
            print(f"Character is a {new_character.race}. No rolls necessary")
            bmc_gen = False
        else:
            print("Generating character background...")
            background_credits = 0
            if new_character.race == "Special: Mutant":
                print("Mutant always has 'Lower Megacity Class' background.")
                new_character.background = "Lower Megacity Class"
                print("+1 Low-Tech Weapon")
                background_weapon = get_random_weapon('low-tech')
                print(f"Received {background_weapon.name}.")
                new_character.weapons.append(background_weapon)
            elif new_character.race == "Special: Manipulator":
                print("Manipulator always has 'Bureaucrat' background.")
                new_character.background = "Special: Bureaucrat"
                background_credits = d6.roll_dice()[0]
                print(f"Earned {background_credits} additional credits.")
            elif new_character.race == "Special: Primitive":
                print("Primitive always has 'Primitive or Regressed World' background.")
                new_character.background = "Primitive or Regressed World"
                print("+1 Toughness")
                new_character.toughness += 1
                print("+1 Low Tech Weapon")
                background_weapon = get_random_weapon('low-tech')
                print(f"Received {background_weapon.name}.")
                new_character.weapons.append(background_weapon)
            else:
                print("Rolling d100 for background")
                background_roll = d100.roll_dice()[0]
                print(f"Rolled a {background_roll}...")
                if background_roll <= 4:
                    print("Peaceful, High-Tech Colony background selected")
                    new_character.background = "Peaceful, High-Tech Colony"
                    new_character.savvy += 1
                    background_credits = d6.roll_dice()[0]
                    print("+1 Savvy")
                elif 5 <= background_roll <= 9:
                    print("Giant, Overcrowded, Dystopian City background selected")
                    new_character.background = "Giant, Overcrowded, Dystopian City"
                    new_character.speed += 1
                    print("+1 Speed")
                elif 10 <= background_roll <= 13:
                    print("Low-Tech Colony background selected")
                    new_character.background = "Low-Tech Colony"
                    print("+1 Low-Tech Weapon")
                    background_weapon = get_random_weapon('low-tech')
                    print(f"Received {background_weapon.name}.")
                    new_character.weapons.append(background_weapon)
                elif 14 <= background_roll <= 17:
                    print("Mining Colony background selected")
                    new_character.background = "Mining Colony"
                    new_character.toughness += 1
                    print("+1 Toughness")
                elif 18 <= background_roll <= 21:
                    print("Military Brat background selected")
                    new_character.background = "Military Brat"
                    new_character.combat += 1
                    print("+1 Combat Skill")
                elif 22 <= background_roll <= 25:
                    print("Space Station background selected")
                    new_character.background = "Space Station"
                    print("+1 Gear")
                    background_equipment = get_random_equipment('gear')
                    print(f"Received {background_equipment.name}.")
                    new_character.equipment.append(background_equipment)
                elif 26 <= background_roll <= 29:
                    print("Military Outpost background selected")
                    new_character.background = "Military Outpost"
                    new_character.reactions += 1
                    print("+1 Reactions")
                elif 30 <= background_roll <= 34:
                    print("Drifter background selected")
                    new_character.background = "Drifter"
                    print("+1 Gear")
                    background_equipment = get_random_equipment('gear')
                    print(f"Received {background_equipment.name}.")
                    new_character.equipment.append(background_equipment)
                elif 35 <= background_roll <= 39:
                    print("Lower Megacity Class background selected")
                    new_character.background = "Lower Megacity Class"
                    print("+1 Low-Tech Weapon")
                    background_weapon = get_random_weapon('low-tech')
                    print(f"Received {background_weapon.name}.")
                    new_character.weapons.append(background_weapon)
                elif 40 <= background_roll <= 42:
                    print("Wealthy Merchant Family background selected")
                    new_character.background = "Wealthy Merchant Family"
                    background_credits = d6.roll_dice()[0] + d6.roll_dice()[0]
                elif 43 <= background_roll <= 46:
                    print("Frontier Gang background selected")
                    new_character.background = "Frontier Gang"
                    new_character.combat += 1
                    print("+1 Combat Skill")
                elif 47 <= background_roll <= 49:
                    print("Religious Cult background selected")
                    new_character.background = "Religious Cult"
                    patrons += 1
                    story_points += 1
                    print("+1 Patrons")
                    print("+1 Story Points")
                elif 50 <= background_roll <= 52:
                    print("War-Torn Hell-Hole background selected")
                    new_character.background = "War-Torn Hell-Hole"
                    new_character.reactions += 1
                    print("+1 Reactions")
                    print("+1 Military Weapon")
                    background_weapon = get_random_weapon('military')
                    print(f"Received {background_weapon.name}.")
                    new_character.weapons.append(background_weapon)
                elif 53 <= background_roll <= 55:
                    print("Tech Guild background selected")
                    new_character.background = "Tech Guild"
                    new_character.savvy += 1
                    background_credits = d6.roll_dice()[0]
                    print("+1 Savvy")
                    print("+1 High-tech Weapon")
                    background_weapon = get_random_weapon('hi-tech')
                    print(f"Received {background_weapon.name}.")
                    new_character.weapons.append(background_weapon)
                elif 56 <= background_roll <= 59:
                    print("Subjugated Colony on Alien World background selected")
                    new_character.background = "Subjugated Colony on Alien World"
                    print("+1 Gadget")
                    background_equipment = get_random_equipment('gadget')
                    print(f"Received {background_equipment.name}.")
                    new_character.equipment.append(background_equipment)
                elif 60 <= background_roll <= 64:
                    print("Long-Term Space Mission background selected")
                    new_character.background = "Long-Term Space Mission"
                    new_character.savvy += 1
                    print("+1 Savvy")
                elif 65 <= background_roll <= 68:
                    print("Research Outpost background selected")
                    new_character.background = "Research Outpost"
                    new_character.savvy += 1
                    print("+1 Savvy")
                    print("+1 Gadget")
                    background_equipment = get_random_equipment('gadget')
                    print(f"Received {background_equipment.name}.")
                    new_character.equipment.append(background_equipment)
                elif 69 <= background_roll <= 72:
                    print("Primitive or Regressed World background selected")
                    new_character.background = "Primitive or Regressed World"
                    new_character.toughness += 1
                    print("+1 Toughness")
                    print("+1 Low-Tech Weapon")
                    background_weapon = get_random_weapon('low-tech')
                    print(f"Received {background_weapon.name}.")
                    new_character.weapons.append(background_weapon)
                elif 73 <= background_roll <= 76:
                    print("Orphan Utility Program background selected")
                    new_character.background = "Orphan Utility Program"
                    patrons += 1
                    story_points += 1
                    print("+1 Patron")
                    print("+1 Story Point")
                elif 77 <= background_roll <= 80:
                    print("Isolationist Enclave background selected")
                    new_character.background = "Isolationist Enclave"
                    quest_rumors += 2
                    print("+2 Quest Rumors")
                elif 81 <= background_roll <= 84:
                    print("Comfortable Megacity Class background selected")
                    new_character.background = "Comfortable Megacity Class"
                    background_credits = d6.roll_dice()[0]
                elif 85 <= background_roll <= 89:
                    print("Industrial World Class selected")
                    new_character.background = "Industrial World"
                    print("+1 Gear")
                    background_equipment = get_random_equipment('gear')
                    print(f"Received {background_equipment.name}.")
                    new_character.equipment.append(background_equipment)
                elif 90 <= background_roll <= 93:
                    print("Bureaucrat background selected")
                    new_character.background = "Bureaucrat"
                    background_credits = d6.roll_dice()[0]
                elif 94 <= background_roll <= 97:
                    print("Wasteland Nomads background selected")
                    new_character.background = "Wasteland Nomads"
                    new_character.reactions += 1
                    print("+1 Reactions")
                    print("+1 Low-tech Weapon")
                    background_weapon = get_random_weapon('low-tech')
                    print(f"Received {background_weapon.name}.")
                    new_character.weapons.append(background_weapon)
                else:
                    print("Alien Culture background selected")
                    new_character.background = "Alien Culture"
                    print("+1 High-Tech Weapon")
                    background_weapon = get_random_weapon('hi-tech')
                    print(f"Received {background_weapon.name}.")
                    new_character.weapons.append(background_weapon)
                if new_character.race == "Special: Bio-Upgrade":
                    background_credits -= 2
                    print("Race subject to credit reduction")
                    if background_credits <= 0:
                        background_credits = 0
                        print("No credits earned.")
                if new_character.race == "Special: Minor Alien":
                    background_credits -= 1
                    print("Race subject to credit reduction")
                    if background_credits <= 0:
                        background_credits = 0
                        print("No credits earned.")
                if new_character.race == "Special: Genetic Uplift":
                    background_credits = 0
                    print("Race subject to credit reduction")
                    print("No credits earned.")
                print(f"{background_credits} credits earned from background")
                credits += background_credits
            bmc_gen = False
    print(f"Crew member added to crew.")
    crew.append(new_character)

print("Welcome to the Five Parsecs from Home companion application.")
program_active = True
while program_active == True:
    print("[1] Create Characters")
    print("[2] View / Manage Team")
    print("[3] Quit")

    try:
        response = int(input("Select your action"))
        if response == 1:
            generate_character()

        elif response == 2:
            # manages crew composition
            team_management = True
            while team_management:
                print("Here's your team:")
                for index, member in enumerate(crew):
                    print(f"[{index + 1}] {member}")
                print(f"Credits: {credits}")
                print(f"Rumors: {quest_rumors}")
                print(f"Patrons: {patrons}")
                print(f"Rivals: {rivals}")
                print("[1] Delete Crew Member")
                print("[2] Return to Program Menu")
                team_manage_response = int(input("Select your action."))
                try:
                    if team_manage_response == 1:
                        try:
                            deleted_member = int(input("Select the number for the team member you want to remove."))
                            print(f"Are you sure you want to remove {crew[deleted_member - 1].name.upper()} from the "
                                  f"crew? This action cannot be undone.")
                            confirmation = input("Type 'y' to confirm. Any other key to cancel")
                            if confirmation == 'y':
                                del crew[deleted_member - 1]
                            else:
                                print("Deletion cancelled.")
                                break
                        except ValueError:
                            break
                    else:
                        break
                except ValueError:
                    break

        elif response == 3:
            # exits program
            program_active = False
            print("Goodbye; thank you for playing.")
        else:
            print("Invalid input. Try again.")

    except ValueError:
        print("Invalid input. Please enter a number.")

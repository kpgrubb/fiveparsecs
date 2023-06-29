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
        trait_info = "\n".join(str(trait) for trait in self.traits)

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

weap_autorifle = Weapon("Auto rifle", "military", 24, 2, 0, traits=None)
weap_beampistol = Weapon("Beam pistol", "hi-tech", 10, 1,1, traits=[trait_pistol,trait_critical])
weap_blade = Weapon("Blade", "low-tech", "Brawl", None, 0, traits=trait_melee)
weap_blastpistol = Weapon("Blast pistol", 'hi-tech', 8, 1, 1, traits=trait_pistol)
weap_blastrifle = Weapon("Blaster rifle", "type", 0, 0, 0, traits=None)
weap_boardingsaber = Weapon("Name", "type", 0, 0, 0, traits=None)
weap_brutalmeleeweapon = Weapon("Name", "type", 0, 0, 0, traits=None)
weap_clingfirepistol = Weapon("Name", "type", 0, 0, 0, traits=None)
weap_colonyrifle = Weapon("Name", "type", 0, 0, 0, traits=None)
weap_dazzlegrenade = Weapon("Name", "type", 0, 0, 0, traits=None)
weap_duelingpistol = Weapon("Name", "type", 0, 0, 0, traits=None)
weap_flakgun = Weapon("Name", "type", 0, 0, 0, traits=None)
weap_frakkgrenade = Weapon("Name", "type", 0, 0, 0, traits=None)
weap_furyrifle = Weapon("Name", "type", 0, 0, 0, traits=None)
weap_glaresword = Weapon("Name", "type", 0, 0, 0, traits=None)
weap_handcannon = Weapon("Name", "type", 0, 0, 0, traits=None)
weap_handflamer = Weapon("Name", "type", 0, 0, 0, traits=None)
weap_handlaser = Weapon("Name", "type", 0, 0, 0, traits=None)
weap_handgun = Weapon("Name", "type", 0, 0, 0, traits=None)
weap_holdoutpistol = Weapon("Name", "type", 0, 0, 0, traits=None)
weap_huntingrifle = Weapon("Name", "type", 0, 0, 0, traits=None)
weap_hyperblaster = Weapon("Name", "type", 0, 0, 0, traits=None)
weap_infantrylaser = Weapon("Name", "type", 0, 0, 0, traits=None)
weap_machinepistol = Weapon("Name", "type", 0, 0, 0, traits=None)
weap_marksmansrifle = Weapon("Name", "type", 0, 0, 0, traits=None)
weap_militaryrifle = Weapon("Name", "type", 0, 0, 0, traits=None)
weap_needlerifle = Weapon("Name", "type", 0, 0, 0, traits=None)
weap_plasmarifle = Weapon("Name", "type", 0, 0, 0, traits=None)
weap_plasmasword = Weapon("Name", "type", 0, 0, 0, traits=None)
weap_powerclaw = Weapon("Name", "type", 0, 0, 0, traits=None)
weap_rattlegun = Weapon("Name", "type", 0, 0, 0, traits=None)
weap_rippersword = Weapon("Name", "type", 0, 0, 0, traits=None)
weap_scrappistol = Weapon("Name", "type", 0, 0, 0, traits=None)
weap_shatteraxe = Weapon("Name", "type", 0, 0, 0, traits=None)
weap_shellgun = Weapon("Name", "type", 0, 0, 0, traits=None)
weap_shotgun = Weapon("Name", "type", 0, 0, 0, traits=None)
weap_suppressionmaul = Weapon("Name", "type", 0, 0, 0, traits=None)

# Equipment

eq_assaultblade = Equipment("Assault Blade", "Gear", "XXX")
eq_beamlight = Equipment("Beam Light", "Gear", "XXX")
eq_bipod = Equipment("Bipod", "Gear", "XXX")
eq_boosterpills = Equipment("Bipod", "Gear", "XXX")
eq_camocloak = Equipment("Camo Cloak", "Gear", "XXX")
eq_combatarmor = Equipment("Combat Armor", "Gear", "XXX")
eq_communicator = Equipment("Communicator", "Gear", "XXX")
eq_concealedblade = Equipment("Concealed Blade", "Gear", "XXX")
eq_fakeid = Equipment("Fake ID", "Gear", "XXX")
eq_fixer = Equipment("Fixer", "Gear", "XXX")
eq_fragvest = Equipment("Frag Vest", "Gear", "XXX")
eq_grapplelauncher = Equipment("Grapple Launcher", "Gear", "XXX")
eq_hazardsuit = Equipment("Hazard Suit", "Gear", "XXX")
eq_lasersight = Equipment("Laser Sight", "Gear", "XXX")
eq_loadeddice = Equipment("Load Dice", "Gear", "XXX")
eq_medpatch = Equipment("Med-patch", "Gear", "XXX")
eq_nanodoc = Equipment("Nano-doc", "Gear", "XXX")
eq_purifier = Equipment("Purifier", "Gear", "XXX")
eq_scannerbot_gadget = Equipment("Scanner Bot", "Gear", "XXX")
eq_sectorpermit = Equipment("Sector Permit", "Gear", "XXX")
eq_steelboots = Equipment("Steel Bots", "Gear", "XXX")
eq_trackersight = Equipment("Track Sight", "Gear", "XXX")
eq_aicompanion = Equipment("AI Companion", "Gadget", "XXX")
eq_analyzer = Equipment("Analyzer", "Gadget", "XXX")
eq_battlevisor = Equipment("Battle Visor", "Gadget", "XXX")
eq_boostedarm = Equipment("Boosted Arm", "Gadget", "XXX")
eq_boostedleg = Equipment("Boosted Leg", "Gadget", "XXX")
eq_cyberhand = Equipment("Cyber Hand", "Gadget", "XXX")
eq_displacer = Equipment("Displacer", "Gadget", "XXX")
eq_distractionbot = Equipment("Distraction Bot", "Gadget", "XXX")
eq_duplicator = Equipment("Duplicator", "Gadget", "XXX")
eq_instawall = Equipment("Insta-Wall", "Gadget", "XXX")
eq_jumpbelt = Equipment("Jump Belt", "Gadget", "XXX")
eq_nerveadjuster = Equipment("Nerve Adjuster", "Gadget", "XXX")
eq_repairbot = Equipment("Repair Bot", "Gadget", "XXX")
eq_scannerbot_gear = Equipment("Scanner Bot", "Gadget", "XXX")
eq_screengenerator = Equipment("Screen Generator", "Gadget", "XXX")
eq_seekersight = Equipment("Seeker Sight", "Gadget", "XXX")
eq_shockattachment = Equipment("Shock Attachment", "Gadget", "XXX")
eq_snooperbot = Equipment("Snooper Bot", "Gadget", "XXX")
eq_sonicemitter = Equipment("Sonic Emitter", "Gadget", "XXX")
eq_stabilizer = Equipment("Stabilizer", "Gadget", "XXX")
eq_stealthgear = Equipment("Stealth Gear", "Gadget", "XXX")
eq_stimpack = Equipment("Stim-pack", "Gadget", "XXX")


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
            (46, 55): weap_blastpistol,
            (56, 70): weap_blastrifle,
            (71, 80): weap_plasmarifle,
            (81, 85): weap_plasmasword,
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

def get_random_equipment(type):
    weapon_dict = {
        "gear": {
            (1, 15): weap_handgun,
            (16, 35): weap_scrappistol,
            (36, 40): weap_machinepistol,
            (41, 65): weap_colonyrifle,
            (66, 75): weap_shotgun,
            (76, 80): weap_huntingrifle,
            (81, 95): weap_blade,
            (96, 100): weap_brutalmeleeweapon
        },
        "gadget": {
            (1, 25): weap_militaryrifle,
            (26, 45): weap_infantrylaser,
            (46, 50): weap_marksmansrifle,
            (51, 60): weap_needlerifle,
            (61, 75): weap_autorifle,
            (76, 80): weap_rattlegun,
            (81, 95): weap_boardingsaber,
            (96, 100): weap_shatteraxe
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
                print("PENDING FEATURE")
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
                print("PENDING FEATURE")
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
                    print("FEATURE PENDING")
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
                    print("FEATURE PENDING")
                elif 26 <= background_roll <= 29:
                    print("Military Outpost background selected")
                    new_character.background = "Military Outpost"
                    new_character.reactions += 1
                    print("+1 Reactions")
                elif 30 <= background_roll <= 34:
                    print("Drifter background selected")
                    new_character.background = "Drifter"
                    print("+1 Gear")
                    print("FEATURE PENDING")
                elif 35 <= background_roll <= 39:
                    print("Lower Megacity Class background selected")
                    new_character.background = "Lower Megacity Class"
                    print("+1 Low-Tech Weapon")
                    print("PENDING FEATURE")
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
                    print("FEATURE PENDING")
                elif 53 <= background_roll <= 55:
                    print("Tech Guild background selected")
                    new_character.background = "Tech Guild"
                    new_character.savvy += 1
                    background_credits = d6.roll_dice()[0]
                    print("+1 Savvy")
                    print("+1 High-tech Weapon")
                    print("FEATURE PENDING")
                elif 56 <= background_roll <= 59:
                    print("Subjugated Colony on Alien World background selected")
                    new_character.background = "Subjugated Colony on Alien World"
                    print("+1 Gadget")
                    print("FEATURE PENDING")
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
                    print("FEATURE PENDING")
                elif 69 <= background_roll <= 72:
                    print("Primitive or Regressed World background selected")
                    new_character.background = "Primitive or Regressed World"
                    new_character.toughness += 1
                    print("+1 Toughness")
                    print("+1 Low-Tech Weapon")
                    print("FEATURE PENDING")
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
                    print("FEATURE PENDING")
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
                    print("FEATURE PENDING")
                else:
                    print("Alien Culture background selected")
                    new_character.background = "Alien Culture"
                    print("+1 High-Tech Weapon")
                    print("FEATURE PENDING")
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

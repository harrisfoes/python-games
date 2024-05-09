def get_punched(health, armor=0):
    return health - (50 - armor)

def get_slashed(health, armor=0):
    return health - (100 - armor) 

# Don't Touch


def test(health, armor):
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after punch: {get_punched(health,armor)}")
    print("====")
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after slash: {get_slashed(health,armor)}\n")
    print("====")
    print(f"Health: {health}, Armor: no armor!") 
    print(f"Health after slash: {get_slashed(health)}\n")
    print("====")
    print(f"Health: {health}, Armor: no armor!") 
    print(f"Health after punch: {get_punched(health)}")
    print("====")

test(400, 5)
test(300, 3)
test(200, 1)

from app.KNIGHTS import KNIGHTS
from app.KnightStats import Knight


def battle(knights: dict) -> dict:

    lancelot = Knight(knights["lancelot"])
    arthur = Knight(knights["arthur"])
    mordred = Knight(knights["mordred"])
    red_knight = Knight(knights["red_knight"])

    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection

    arthur.hp -= red_knight.power - arthur.protection
    red_knight.hp -= arthur.power - red_knight.protection

    if lancelot.hp < 0:
        lancelot.hp = 0

    if mordred.hp < 0:
        mordred.hp = 0

    if arthur.hp < 0:
        arthur.hp = 0

    if red_knight.hp < 0:
        red_knight.hp = 0

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }


print(battle(KNIGHTS))

#main
import intro
from fight import Fight
import story
from Player import Player
import Inventory
import enemies
from text_tempo import pause

#story_1=story.Story()
#story_1.chapter_1_intro()
player=Player()

# player.player_stats_intro()
# fight_1=Fight(player, enemies.guard_1, enemies.guard_2, enemies.guard_3)
# # story.chapter_1_intro()
# fight_1.fight_start()
# fight_1.speed_check()
# if player.health <= 0:
#     player.health = 1
# pause()
# story.chapter_1_after_intro_fight()
# pause()
# story.chapter_1_year_later()
player.player_stats_normal()
# m1,m2,m3 = enemies.spawn("Mercenary", 3)
# fight_2=Fight(player, m1, m2, m3 )
# fight_2.fight_start()
# fight_2.speed_check()
# healer = enemies.spawn("Healer")
# m2, m3 = enemies.spawn("Mercenary", 2)
# fight_x=Fight(player, healer, m2,m3)
# fight_x.fight_start()
# fight_x.speed_check()
story.village_orphans_event(player)

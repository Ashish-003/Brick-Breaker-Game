import signal, os, time
from colorama import Fore, Back, Style

end = [list("      ___           ___           ___           ___                    ___                         ___           ___     "),
       list("     /\__\         /\  \         /\  \         /\__\                  /\  \          ___          /\__\         /\  \    "), 
       list("    /:/ _/_       /::\  \       |::\  \       /:/ _/_                /::\  \        /\  \        /:/ _/_       /::\  \   "), 
       list("   /:/ /\  \     /:/\:\  \      |:|:\  \     /:/ /\__\              /:/\:\  \       \:\  \      /:/ /\__\     /:/\:\__\  "),
       list("  /:/ /::\  \   /:/ /::\  \   __|:|\:\  \   /:/ /:/ _/_            /:/  \:\  \       \:\  \    /:/ /:/ _/_   /:/ /:/  /  "),
       list(" /:/__\/\:\__\ /:/_/:/\:\__\ /::::|_\:\__\ /:/_/:/ /\__\          /:/__/ \:\__\  ___  \:\__\  /:/_/:/ /\__\ /:/_/:/__/___"),
       list(" \:\  \ /:/  / \:\/:/  \/__/ \:\~~\  \/__/ \:\/:/ /:/  /          \:\  \ /:/  / /\  \ |:|  |  \:\/:/ /:/  / \:\/:::::/  /"),
       list("  \:\  /:/  /   \::/__/       \:\  \        \::/_/:/  /            \:\  /:/  /  \:\  \|:|  |   \::/_/:/  /   \::/~~/~~~~ "),
       list("   \:\/:/  /     \:\  \        \:\  \        \:\/:/  /              \:\/:/  /    \:\__|:|__|    \:\/:/  /     \:\~~\     "),
       list("    \::/  /       \:\__\        \:\__\        \::/  /                \::/  /      \::::/__/      \::/  /       \:\__\    "),
       list("     \/__/         \/__/         \/__/         \/__/                  \/__/        ~~~~           \/__/         \/__/    ")]
win = [list("                  ___           ___                    ___                       ___     "),
       list("                 /\  \         /\  \                  /\  \                     /\  \    "),
       list("      ___       /::\  \        \:\  \                _\:\  \       ___          \:\  \   "),
       list("     /|  |     /:/\:\  \        \:\  \              /\ \:\  \     /\__\          \:\  \  "),
       list("    |:|  |    /:/  \:\  \   ___  \:\  \            _\:\ \:\  \   /:/__/      _____\:\  \ "),
       list("    |:|  |   /:/__/ \:\__\ /\  \  \:\__\          /\ \:\ \:\__\ /::\  \     /::::::::\__\\"),
       list("  __|:|__|   \:\  \ /:/  / \:\  \ /:/  /          \:\ \:\/:/  / \/\:\  \__  \:\~~\~~\/__/"),
       list(" /::::\  \    \:\  /:/  /   \:\  /:/  /            \:\ \::/  /   ~~\:\/\__\  \:\  \      "),
       list(" ~~~~\:\  \    \:\/:/  /     \:\/:/  /              \:\/:/  /       \::/  /   \:\  \     "),
       list("      \:\__\    \::/  /       \::/  /                \::/  /        /:/  /     \:\__\    "),
       list("       \/__/     \/__/         \/__/                  \/__/         \/__/       \/__/    ")]
def loss_game():
    os.system('clear')
    for i in range(0, len(end)):
            for j in range(0, len(end[0])):
                print(Fore.WHITE + end[i][j] + Fore.RESET, end='')
            print()
    os.system("aplay sounds/gameover.wav -q &")
    time.sleep(3)
    
def win_game():
    os.system('clear')
    for i in range(0, len(win)):
            for j in range(0, len(win[0])):
                print(Fore.WHITE + win[i][j] + Fore.RESET, end='')
            print()
    os.system("aplay sounds/gameover.wav -q &")
    time.sleep(3)
    
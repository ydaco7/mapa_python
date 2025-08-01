import os
import keyboard


map = { 
    "level 1": [
    ["#","#","#","#","#","#"],
    ["#",".",".","#","f","#"],
    ["#",".",".","a",".","#"],
    ["#",".","#",".","#","#"],
    ["#",".","f",".","f","#"],
    ["#","#","#","#","#","#"],
],
    "level 2": [
    ["#","#","#","#","#","#"],
    ["#","f",".","#","f","#"],
    ["#",".",".",".",".","#"],
    ["#",".","#",".","#","#"],
    ["#","a",".",".","f","#"],
    ["#","#","#","#","#","#"],
    ],
    "level 3": [
    ["#","#","#","#","#","#"],
    ["#",".",".","f",".","#"],
    ["#",".","#",".","#","#"],
    ["#",".","f",".",".","#"],
    ["#","a",".",".","f","#"],
    ["#","#","#","#","#","#"],
],
}


size_rows = 5
size_cols = 5
avatar_y = 2
avatar_x = 1
counting_cerezas = 0
counting_beer = 0
limit = 20
level = ["level 1", "level 2", "level 3"]
next = 0

def fn_clear_map():
    os.system("cls" if os.name == "nt" else "clear")

def fn_render_map():
    # map = [level[next]]
    fn_clear_map()
    for rows in map[level[next]]:
        tiles = []
        for cols in rows:
            if cols == ".":
               tiles.append("⬜")
            if cols == "#":
               tiles.append("🧱")
            if cols == "@":
               tiles.append("😃")
            if cols == "f":
               tiles.append("🍒")
            if cols == "g":
               tiles.append("🎁")
            if cols == "a":
               tiles.append("🍺")    

        print(" ".join(tiles))
    print(f"total cerezas: {counting_cerezas}")
    print (f"total cervezas: {counting_beer}")
    print ("limite de intentos: ", limit) 

def fn_move_avatar():
    global avatar_x, avatar_y, counting_cerezas, counting_beer, limit, next
    new_x = avatar_x
    new_y = avatar_y

    while True:
        event = keyboard.read_event(suppress=True)
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == "w":
                new_y -= 1
                limit -= 1

            elif event.name == "s":
                new_y += 1
                limit -= 1

            elif event.name == "a":
                new_x -= 1
                limit -= 1

            elif event.name == "d":
                new_x += 1
                limit -= 1

            elif event.name == "q":
                print("Saliendo del juego...")
                break

            if limit <= 0:
                print("¡Te quedaste sin intentos! Fin del juego.")
                break
            
            fn_clear_map()

            if (0 <= new_x < len(map[level[next]][0]) and 0 <= new_y < len(map[level[next]]) and map[level[next]][new_y][new_x] != "#"):
                map[level[next]][avatar_y][avatar_x] = "."
                avatar_x = new_x
                avatar_y = new_y
                if map[level[next]][avatar_y][avatar_x] == "f":
                    counting_cerezas += 1

                if counting_cerezas == 3:
                    fn_render_map()

                if map[level[next]][avatar_y][avatar_x] == "a":
                    counting_beer += 1

                if counting_beer == 1:
                    fn_render_map()

                if counting_cerezas == 3 and counting_beer == 1:
                    print("Ganaste")
                    next += 1
                    if next < len(level):
                        avatar_x = 1
                        avatar_y = 2
                        new_x = avatar_x  
                        new_y = avatar_y   
                        counting_cerezas = 0
                        counting_beer = 0
                        limit = 20
                        fn_render_map()
                        continue  
                    else:
                        print("¡Completaste todos los niveles!")
                        break

                map[level[next]][avatar_y][avatar_x] = "@"
            else:
                new_x = avatar_x
                new_y = avatar_y
            fn_render_map()

if __name__ == "__main__":
    fn_render_map()
    fn_move_avatar()
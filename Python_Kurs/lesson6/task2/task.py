hello_world = "Hallo, Welt!"

for ch in hello_world:    # gibt jedes Zeichen von hello_world aus
    print(ch)

length = 0      # setzt die Variable length

for _ in hello_world:
    length += 1     # addiert length mit 1

print(len(hello_world) == length)

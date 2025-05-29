#print(f'пример 1')
#for x in 0, 1:
    #for y in 0, 1:
    #    for z in 0, 1:
    #        for w in 0,1:
   #             f = (x or y) and not (y == z) and not (w)
  #              if f == 1:
 #                   print(x, y, z, w, f)


#print(f'(a, b, c) = not (a or b) and c')
#for a in 0, 1:
#    for b in 0, 1:
#        for c in 0, 1:
#            for w in 0,1:
#                f = (x or y) and not (y == z) and not (w)
#                if f == 1:
#                    print(x, y, z, w, f)


print(f'(x, y, z) = not x and not y => z')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0,1:
                f = (x or y) and not (y == z) and not (w)
                if f == 1:
                    print(x, y, z, w, f)

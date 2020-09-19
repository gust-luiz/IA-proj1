from sys import maxsize

from utils import get_named_route, get_total_distance

best = {
    'dist': maxsize,
    'route': []
}
route = []
cnt = 0

for i0 in range(9):
    route.append(i0)

    for i1 in range(9):
        if i1 in route:
            continue
        route.append(i1)

        for i2 in range(9):
            if i2 in route:
                continue
            route.append(i2)

            for i3 in range(9):
                if i3 in route:
                    continue
                route.append(i3)

                for i4 in range(9):
                    if i4 in route:
                        continue
                    route.append(i4)

                    for i5 in range(9):
                        if i5 in route:
                            continue
                        route.append(i5)

                        for i6 in range(9):
                            if i6 in route:
                                continue
                            route.append(i6)

                            for i7 in range(9):
                                if i7 in route:
                                    continue
                                route.append(i7)

                                for i8 in range(9):
                                    if i8 in route:
                                        continue
                                    route.append(i8)

                                    route.insert(0, 9)
                                    dist = get_total_distance(''.join(list(map(str, route))))

                                    if dist < best['dist']:
                                        best['dist'] = dist
                                        best['route'] = [route.copy()]
                                    elif dist == best['dist']:
                                        best['route'].append(route.copy())

                                    print('tested:', cnt, end='\r')
                                    cnt += 1

                                    route.pop()
                                    route.pop(0)

                                route.pop()

                            route.pop()

                        route.pop()

                    route.pop()

                route.pop()

            route.pop()

        route.pop()

    route.pop()
    route.clear()

print('\nbest.dist:', best['dist'])
print('best.routes:')
for route in best['route']:
    print('\troute', route)
    print('\tnamed_route', get_named_route(''.join(list(map(str, route)))))
    print()

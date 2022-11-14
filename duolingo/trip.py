def sightseeing(trail, attraction):
    start, end = "Parking Lot", "Campsite"

    new_trail = []
    for t in trail:
        fst, sec = t[0], t[1]
        new_trail.append((fst, sec))
    trail = new_trail


    q = [(start, set(), set(attraction))]
    while q:
        cur, is_visited, cur_attr_remaining = q.pop(0)
        # print(cur, is_visited, cur_attr_remaining)
        if cur_attr_remaining == set() and cur == end:
            return True
        for i, t in enumerate(trail):
            if (i, t) in is_visited or (t[0] != cur and t[1] != cur):
                continue
            fst, sec = t
            if fst == cur:
                if sec in attraction:
                    q.append((sec, is_visited.union({(i, t)}), cur_attr_remaining - set({sec})))
                else:
                    q.append((sec, is_visited.union({(i, t)}), cur_attr_remaining))
            elif sec == cur:
                if fst in attraction:
                    q.append((fst, is_visited.union({(i, t)}), cur_attr_remaining - set({fst})))
                else:
                    q.append((fst, is_visited.union({(i, t)}), cur_attr_remaining))
    return False


if __name__ == '__main__':
    trails1 = [
      ["Beaver Dam", "Frozen Ocean"],  # First trail between Beaver Dam/Frozen Ocean
      ["Beaver Dam", "Frozen Ocean"],  # Second trail between Beaver Dam/Frozen Ocean
      ["Parking Lot", "Beaver Dam"],
      ["Parking Lot", "Liberty Lake"],
      ["Beaver Dam", "Campsite"],
      ["Eel Weir", "Campsite"],
      ["Eel Weir", "Campsite"],
    ]
    attractions1_1 = ["Frozen Ocean"] #True
    attractions1_2 = ["Liberty Lake", "Beaver Dam"] #False
    attractions1_3 = ["Eel Weir"] #True

    trails2 = [
      ["Mason's Cabin", "Liberty Lake"],
      ["Parking Lot", "Mill Falls"],
      ["Mason's Cabin", "Jeremy's Bay"],
      ["Eel Weir", "Hardwood Forest"],
      ["Outdoor Theater", "Campsite"],
      ["Jeremy's Bay", "Horseshoe Falls"],
      ["Mason's Cabin", "Parking Lot"],
      ["Mason's Cabin", "Liberty Lake"],
      ["Mill Falls", "Horseshoe Falls"],
      ["Mill Falls", "Eel Weir"],
      ["Hardwood Forest", "Campsite"],
      ["Eel Weir", "Outdoor Theater"],
      ["Liberty Lake", "Mason's Cabin"]
    ]

    attractions2_1 = ["Jeremy's Bay", "Mason's Cabin", "Outdoor Theater"]  # => True
    attractions2_2 = ["Outdoor Theater", "Eel Weir", "Hardwood Forest"]  # => False
    attractions2_3 = ["Liberty Lake"]  # => True
    attractions2_4 = ["Horseshoe Falls", "Eel Weir"]  # => True

    print(sightseeing(trails1, attractions1_1)) #True
    print(sightseeing(trails1, attractions1_2)) #Fals
    print(sightseeing(trails1, attractions1_3)) #True
    #
    print(sightseeing(trails2, attractions2_1))# => True
    print(sightseeing(trails2, attractions2_2))# => False
    print(sightseeing(trails2, attractions2_3))# => True
    print(sightseeing(trails2, attractions2_4))  # => True
    # Path: Parking
    # Lot->Beaver
    # Dam->Frozen
    # Ocean->Beaver
    # Dam->Campsite
    # attractions1_2 = ["Liberty Lake", "Beaver Dam"] = > False
    # It is not possible
    # to
    # return
    # from Liberty Lake
    # 
    # so
    # this
    # path is not possible.
    # attractions1_3 = ["Eel Weir"] = > True
    # Path: Parking
    # Lot->Beaver
    # Dam->Campsite->Eel
    # Weir->Campsite
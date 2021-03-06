
IMG_HEIGHT = 416
IMG_WIDTH = 416

CLASS_NUM = 2

# ANCHORS_GROUP = {
#     13: [[116,90], [156,198], [373,326]],
#     26: [[30,61], [62,45], [59,119]],
#     52: [[10,13], [16,30], [33,23]]
# }
ANCHORS_GROUP = {
    13:[[83,83]],
    26:[[21,21],[21,20],[19,22]],
    52:[[4,16],[15,3]]
}

ANCHORS_GROUP_AREA = {
    13: [x * y for x, y in ANCHORS_GROUP[13]],
    26: [x * y for x, y in ANCHORS_GROUP[26]],
    52: [x * y for x, y in ANCHORS_GROUP[52]],
}

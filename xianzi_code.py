data = ["0", "8", "9", "5", "6"]

"""
右手使用， 手小
可能重复的 6890
"""


def make_code():
    f = open("code.txt", "w", encoding="utf-8")

    code_str = ""
    for _1 in data:
        for _2 in data:
            for _3 in data:
                for _4 in data:
                    for _5 in data:
                        for _6 in data:
                            code_str = f"{_1}{_2}{_3}{_4}{_5}{_6}"
                            f.write(code_str + "\n")

    f.close()


bad_list = ['868508',
            '858699',
            '085699',
            '085966',
            '858605',
            '858608',
            '085866',
            '860599',
            '086966',
            '085996',
            '085685',
            '086599',
            '083599',
            '058669',
            '080586',
            '058599',
            '850566',
            '058685',
            '058586',
            '056995',
            '085696',
            '058666',
            '086995',
            '085399',
            '085686',
            '080566',
            '058699',
            '050886',
            '089653'
]


def score_code():
    f_new = open("code_new.txt", "w", encoding="utf-8")
    data = open("code.txt", "r", encoding="utf-8").read()
    data = data.splitlines()
    items = []

    for dat in data:
        # print(dat)
        dat, score = filter_bad_code(dat)
        if score == -1:
            dat, score = score_code_str(dat)
        if score > 2:
            print(dat, score)
            items.append((dat, score))
    # for item in items:
    #     print(item)
    items = sorted(items, key=lambda x: x[1], reverse=True)
    for item in items:
        f_new.write(item[0] + "\t" + str(item[1]) + "\n")
    f_new.close()


def filter_bad_code(dat):
    if dat in bad_list:
        return dat, 0
    else:
        return dat, -1


def score_code_str(dat):
    score = 0
    if dat.endswith("66"):
        score += 1
    elif dat.endswith("99"):
        score += 1
    else:
        score = 0
    if dat.startswith("08"):
        score += 2
    elif dat.startswith("05"):
        score += 1
    else:
        score = 0

    if dat[2:4].count(dat[2]) == 2:
        score = 0
    if dat[2] == "8":
        score = 0
    # if not dat.endswith("99"):
    #     score = 0
    # elif not dat.endswith("66"):
    #     score = 0

    # score = 0
    # # 规则一
    # if dat.startswith("08") or dat.startswith("05"):
    #     score += 2
    # elif dat.startswith("09") or dat.startswith("06"):
    #     score += 1
    # else:
    #     pass
    # # 规则二和规则三
    # if dat.endswith("66") or dat.endswith("99"):
    #     score += 1
    # elif dat.endswith("6") or dat.endswith("9"):
    #     score += 2
    # else:
    #     pass
    # # 规则四和规则五
    # if dat.count("8") < 3 or dat.count("0") < 3 or dat.count("5")< 3 or dat.count("6") < 3 or dat.count("9") < 3:
    #     score += 1
    # else:
    #     pass
    #
    # if dat.count("0") >= 3 or dat.count("8") >= 3 or dat.count("6") >= 4 or dat.count("9") >= 4 or dat.count("5") >= 3:
    #     score -= 1
    # # 规则六和规则七
    if "000" in dat or "555" in dat or "666" in dat or "888" in dat or "999" in dat:
        score = 0
    return dat, score


# 规则1 08 05 加二分  09 06 加一分
# 规则2 尾数66 尾数99 加一分
# 规则3 尾数6 尾数9 加一分
# 规则4 8和0重复但是不挨着 加一分
# 规则5 默认重复次数最大为2
# 规则6 三联 666 888 999 555 000 不存在
# 规则7 去除脏数据


if __name__ == '__main__':
    make_code()
    score_code()

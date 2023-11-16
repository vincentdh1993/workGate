special_clothes = []  # 모자, 털모자, 넥타이,스카프,수영복
symbol_list = ["물세탁"]  # 물세탁, 드라이, 손세탁
material_list = ["레이온","마","면"]  # 천연가죽, 고어텍스, 인조가죽, 울, 견, 레이온, 마, 아크릴, 면, 나일론, 폴리에스터, 폴리우레탄
special_material = ["충전재","물빠짐의류","의류패턴"]  # 충전재,의류패턴,물빠짐의류
shrink_list = ["꽈배기원단","소재강도"]  # 수축요인 >> 비닐형태, 꽈배기원단, 트위드, 코듀로이/벨벳, 안감(폴리), 고무소재, 수축/팽창, 스크래치, 소재강도
status_list = ["탈색진행"]  # 세탁불가, 손상진행, 탈색진행, 이염발생
stain_list = ["일반오염","지용성"]  # 일반오염, 찌든오염, 수용성,지용성,복합오염
design_list = []  # 접착물, 부착물, 프린트, 페인트, 큐빅,비즈,메탈,패치, 반짝이, 레이스, 시스루, 올풀림


def level1_2(special_clothes, symbol_list, material_list):
    result = []
    # 특수의류 일 때
    if "털모자" in special_clothes:
        result.append("드라이")
        result.append("일반건조")
    elif "모자" in special_clothes:
        result.append("손세탁")
        result.append("송풍건조")
    elif "넥타이" in special_clothes or "스카프" in special_clothes:
        result.append("드라이")
        result.append("송풍건조")
    elif "수영복" in special_clothes:
        result.append("손세탁")
        result.append("송풍건조")
    # 특수의류 아닐때
    else:
        # 물세탁 부호가 있을때
        if "물세탁" in symbol_list:
            # 드라이 부호도 있을때
            if "드라이" in symbol_list:
                if "천연가죽" in material_list:
                    result.append("전문점")
                elif "고어텍스" in material_list:
                    result.append("손세탁")
                    result.append("송풍건조")
                elif "인조가죽" in material_list:
                    result.append("단독세탁")
                    result.append("손세탁")
                    result.append("송풍건조")
                elif "울" in material_list or "견" in material_list:
                    result.append("#1")
                elif "레이온" in material_list or "마" in material_list or "아크릴" in material_list:
                    # 단일소재일때
                    if len(material_list) == 1:
                        result.append("#1")
                    # 복합소재일때
                    else:
                        if "충전재" in special_material:
                            result.append("#6")
                        else:
                            result.append("#2")
                else:
                    if "충전재" in special_material:
                        result.append("#6")
                    else:
                        result.append("#4")

            # 드라이 부호가 없을때
            else:
                if "인조가죽" in material_list:
                    result.append("단독세탁")
                    result.append("손세탁")
                    result.append("송풍건조")
                elif "천연가죽" in material_list:
                    result.append("전문점")
                elif "고어텍스" in material_list:
                    result.append("손세탁")
                    result.append("송풍건조")
                elif "울" in material_list or "견" in material_list:
                    result.append("#1")
                elif "레이온" in material_list or "마" in material_list or "아크릴" in material_list:
                    # 단일소재
                    if len(material_list) == 1:
                        result.append("#1")
                    # 복합소재
                    else:
                        if "충전재" in special_material:
                            result.append("#6")
                        else:
                            result.append("#2")
                elif "면" in material_list and len(material_list) == 1:
                    result.append("#4")
                else:
                    if "충전재" in special_material:
                        result.append("#6")
                    else:
                        result.append("#5")

        # 손세탁
        elif "손세탁" in symbol_list:
            # 드라이도 있을 때
            if "드라이" in symbol_list:
                if "천연가죽" in material_list:
                    result.append("전문점")
                elif "울" in material_list or "견" in material_list:
                    result.append("#1")
                elif "레이온" in material_list or "마" in material_list or "아크릴" in material_list:
                    # 단일소재
                    if len(material_list) == 1:
                        result.append("#1")
                    # 복합소재
                    else:
                        if "충전재" in special_material:
                            result.append("#4")
                        else:
                            result.append("#2")
                else:
                    if "충전재" in special_material:
                        result.append("#4")
                    else:
                        result.append("#2")
            # 손세탁만 있고 드라이는 없을때
            else:
                if "천연가죽" in material_list:
                    result.append("전문점")
                elif "울" in material_list or "견" in material_list:
                    result.append("#1")
                elif "레이온" in material_list or "마" in material_list or "아크릴" in material_list:
                    # 단일소재
                    if len(material_list) == 1:
                        result.append("#1")
                    else:
                        result.append("#2")
                elif "면" in material_list and len(material_list) == 1:
                    result.append("#2")
                else:
                    if "충전재" in special_material:
                        result.append("#5")
                    else:
                        result.append("#3")
        # 드라이
        elif "드라이" in symbol_list:
            if "인조가죽" in material_list:
                result.append("단독세탁")
                result.append("손세탁")
                result.append("송풍건조")
            elif "천연가죽" in material_list:
                result.append("전문점")
            elif "폴리우레탄" in material_list and len(material_list) == 1:
                result.append("단독세탁")
                result.append("손세탁")
                result.append("송풍건조")
            elif "고어텍스" in material_list:
                result.append("손세탁")
                result.append("송풍건조")
            elif "울" in material_list or "견" in material_list or "아크릴" in material_list or "레이온" in material_list or "마" in material_list:
                result.append("#1")
            else:
                result.append("#2")
        else:
            result.append("세탁불가 / 전문점")

    return result


def level3(level1_result, symbol_list, material_list, shrink_list, status_list, special_material):
    result = []
    if "#1" in level1_result:
        if "세탁불가" in status_list:
            result.append("의류반환(세탁불가)")
        else:
            result.append("#1")
    elif "#2" in level1_result:
        if "손상진행" in status_list:
            if "세탁불가" in status_list:
                result.append("의류반환(세탁불가)")
            else:
                result.append("단독세탁")
                result.append("손세탁")
                result.append("드라이")
                result.append("송풍건조")
        elif "비닐형태" in shrink_list:
            result.append("#3")
        elif "꽈배기원단" in shrink_list:
            result.append("#1")
        elif "트위드" in shrink_list:
            result.append("#1")
        elif "코듀로이/벨벳" in shrink_list:
            result.append("#2")
        elif "안감(폴리)" in shrink_list:
            result.append("#1")
        elif "고무소재" in shrink_list:
            result.append("#3")
        elif "수축/팽창" in shrink_list:
            result.append("#2")
        elif "스크래치" in shrink_list:
            result.append("#1")
        elif "소재강도" in shrink_list:
            result.append("#5")
        else:
            result.append("#2")

    elif "#3" in level1_result:
        if "손상진행" in status_list:
            if "세탁불가" in status_list:
                result.append("의류반환(세탁불가)")
            else:
                result.append("단독세탁")
                result.append("손세탁")
                result.append("드라이")
                result.append("송풍건조")
        elif "비닐형태" in shrink_list:
            result.append("#3")
        elif "꽈배기원단" in shrink_list:
            result.append("#2")
        elif "트위드" in shrink_list:
            result.append("#1")
        elif "코듀로이/벨벳" in shrink_list:
            result.append("#2")
        elif "안감(폴리)" in shrink_list:
            result.append("#1")
        elif "고무소재" in shrink_list:
            result.append("#3")
        elif "수축/팽창" in shrink_list:
            result.append("#2")
        elif "스크래치" in shrink_list:
            result.append("#3")
        elif "소재강도" in shrink_list:
            result.append("#5")
        else:
            result.append("#3")

    elif "#4" in level1_result:
        if "손상진행" in status_list:
            if "세탁불가" in status_list:
                result.append("의류반환(세탁불가)")
            else:
                result.append("단독세탁")
                result.append("손세탁")
                result.append("드라이")
                result.append("송풍건조")
        elif "비닐형태" in shrink_list:
            result.append("#3")
        elif "꽈배기원단" in shrink_list:
            result.append("#1")
        elif "트위드" in shrink_list:
            result.append("#1")
        elif "코듀로이/벨벳" in shrink_list:
            result.append("#2")
        elif "안감(폴리)" in shrink_list:
            result.append("#1")
        elif "고무소재" in shrink_list:
            result.append("#3")
        elif "수축/팽창" in shrink_list:
            result.append("#1")
        elif "스크래치" in shrink_list:
            result.append("#1")
        elif "소재강도" in shrink_list:
            result.append("#5")
        else:
            result.append("#4")

    elif "#5" in level1_result:
        if "손상진행" in status_list:
            if "세탁불가" in status_list:
                result.append("의류반환(세탁불가)")
            else:
                result.append("단독세탁")
                result.append("손세탁")
                result.append("송풍건조")
        elif "비닐형태" in shrink_list:
            result.append("#3")
        elif "꽈배기원단" in shrink_list:
            result.append("#2")
        elif "트위드" in shrink_list:
            result.append("#1")
        elif "코듀로이/벨벳" in shrink_list:
            result.append("#3")
        elif "안감(폴리)" in shrink_list:
            result.append("#1")
        elif "고무소재" in shrink_list:
            result.append("#3")
        elif "수축/팽창" in shrink_list:
            result.append("#2")
        elif "스크래치" in shrink_list:
            result.append("#3")
        elif "소재강도" in shrink_list:
            result.append("#5")
        else:
            result.append("#5")

    elif "#6" in level1_result:
        if "손상진행" in status_list:
            if "세탁불가" in status_list:
                result.append("의류반환(세탁불가)")
            else:
                result.append("단독세탁")
                result.append("손세탁")
                result.append("송풍건조")
        elif "물세탁" in symbol_list:
            result.append("#6")
        else:
            result.append("#2")

    return result


def level4(level3_result, symbol_list, material_list, shrink_list, status_list, special_material):
    result = []
    if "#1" in level3_result:
        if "세탁불가" in status_list:
            result.append("의류반환(세탁불가)")
        else:
            result.append("#1")
    elif "#2" in level3_result:
        if "탈색진행" in status_list:
            if "세탁불가" in status_list:
                result.append("의류반환(세탁불가)")
            else:
                result.append("단독세탁")
                result.append("손세탁")
                result.append("드라이")
                result.append("송풍건조")
        elif "의류패턴" in special_material:
            if "물세탁" in symbol_list:
                if "물빠짐의류" in special_material:
                    result.append("#2")
                else:
                    if "이염발생" in status_list:
                        result.append("#2")
                    else:
                        result.append("#2")
            else:
                result.append("#2")
        else:
            result.append("#2")


    elif "#3" in level3_result:
        if "탈색진행" in status_list:
            if "세탁불가" in status_list:
                result.append("의류반환(세탁불가)")
            else:
                result.append("단독세탁")
                result.append("손세탁")
                result.append("송풍건조")
        elif "의류패턴" in special_material:
            if "물세탁" in symbol_list:
                if "물빠짐의류" in special_material:
                    result.append("#3")
                else:
                    if "이염발생" in status_list:
                        result.append("#3")
                    else:
                        result.append("#3")
            else:
                result.append("#3")
        else:
            result.append("#3")


    elif "#4" in level3_result:
        if "탈색진행" in status_list:
            if "세탁불가" in status_list:
                result.append("의류반환(세탁불가)")
            else:
                result.append("단독세탁")
                result.append("손세탁")
                result.append("드라이")
                result.append("송풍건조")
        elif "의류패턴" in special_material:
            if "물세탁" in symbol_list:
                if "물빠짐의류" in special_material:
                    result.append("#2")
                else:
                    if "이염발생" in status_list:
                        result.append("#2")
                    else:
                        result.append("#4")
            else:
                result.append("#4")
        else:
            result.append("#4")

    elif "#5" in level3_result:
        if "탈색진행" in status_list:
            if "세탁불가" in status_list:
                result.append("의류반환(세탁불가)")
            else:
                result.append("단독세탁")
                result.append("손세탁")
                result.append("송풍건조")
        elif "의류패턴" in special_material:
            if "물세탁" in symbol_list:
                if "물빠짐의류" in special_material:
                    result.append("#3")
                else:
                    if "이염발생" in status_list:
                        result.append("#3")
                    else:
                        result.append("#5")
            else:
                result.append("#5")
        else:
            result.append("#5")


    elif "#6" in level3_result:
        if "탈색진행" in status_list:
            if "세탁불가" in status_list:
                result.append("의류반환(세탁불가)")
            else:
                result.append("단독세탁")
                result.append("손세탁")
                result.append("송풍건조")
        elif "의류패턴" in special_material:
            if "물세탁" in symbol_list:
                if "물빠짐의류" in special_material:
                    result.append("#2")
                else:
                    if "이염발생" in status_list:
                        result.append("#2")
                    else:
                        result.append("#6")
            else:
                result.append("#6")
        else:
            result.append("#6")

    return result


def level5(level4_result, symbol_list, material_list, shrink_list, status_list, special_material, stain_list):
    result = []
    if "#1" in level4_result:
        if "찌든오염" in stain_list:
            result.append("손세탁")
            result.append("송풍건조")
        elif "수용성" in stain_list:
            if "지용성" in stain_list:
                result.append("전처리")
                result.append("드라이")
                result.append("일반건조")
            elif "수용성" in stain_list:
                result.append("전처리")
                result.append("드라이")
                result.append("일반건조")
        elif "지용성" in stain_list:
            result.append("드라이")
            result.append("일반건조")
        else:
            result.append("드라이")
            result.append("일반건조")

    elif "#2" in level4_result:
        if "찌든오염" in stain_list:
            result.append("물세탁")
            result.append("자연건조")
        elif "수용성" in stain_list:
            if "지용성" in stain_list:
                result.append("전처리")
                result.append("손세탁/송풍건조")
                result.append("또는")
                result.append("드라이/일반건조")
            elif "수용성" in stain_list:
                result.append("전처리")
                result.append("손세탁/송풍건조")
                result.append("또는")
                result.append("드라이/일반건조")
        elif "지용성" in stain_list:
            result.append("손세탁/송풍건조")
            result.append("또는")
            result.append("드라이/일반건조")
        else:
            result.append("손세탁/송풍건조")
            result.append("또는")
            result.append("드라이/일반건조")

    elif "#3" in level4_result:
        if "찌든오염" in stain_list:
            result.append("물세탁")
            result.append("송풍건조")
        elif "수용성" in stain_list:
            if "지용성" in stain_list:
                result.append("손세탁")
                result.append("송풍건조")
            elif "수용성" in stain_list:
                result.append("손세탁")
                result.append("송풍건조")
        elif "지용성" in stain_list:
            result.append("손세탁")
            result.append("송풍건조")
        else:
            result.append("손세탁")
            result.append("송풍건조")

    elif "#4" in level4_result:
        if "찌든오염" in stain_list:
            result.append("물세탁")
            result.append("송풍건조")
        elif "수용성" in stain_list:
            if "지용성" in stain_list:
                result.append("전처리")
                result.append("물세탁/일반건조")
                result.append("또는")
                result.append("드라이/일반건조")
            elif "수용성" in stain_list:
                result.append("전처리")
                result.append("물세탁/일반건조")
                result.append("또는")
                result.append("드라이/일반건조")
        elif "지용성" in stain_list:
            result.append("전처리")
            result.append("물세탁/일반건조")
            result.append("또는")
            result.append("드라이/일반건조")
        else:
            result.append("물세탁/일반건조")
            result.append("또는")
            result.append("드라이/일반건조")

    elif "#5" in level4_result:
        if "찌든오염" in stain_list:
            result.append("물세탁")
            result.append("송풍건조")


        elif "수용성" in stain_list:
            if "지용성" in stain_list:
                result.append("전처리")
                result.append("물세탁")
                result.append("일반건조")
            elif "수용성" in stain_list:
                result.append("물세탁")
                result.append("일반건조")
        elif "지용성" in stain_list:
            result.append("전처리")
            result.append("물세탁")
            result.append("일반건조")
        else:
            result.append("물세탁")
            result.append("일반건조")

    elif "#6" in level4_result:
        if "찌든오염" in stain_list:
            result.append("물세탁")
            result.append("송풍건조")

        elif "수용성" in stain_list:
            if "지용성" in stain_list:
                result.append("전처리")
                result.append("물세탁")
                result.append("일반건조")
            elif "수용성" in stain_list:
                result.append("물세탁")
                result.append("일반건조")
        elif "지용성" in stain_list:
            result.append("전처리")
            result.append("물세탁")
            result.append("일반건조")
        else:
            result.append("물세탁")
            result.append("일반건조")
    return result


def level6(level4_result, symbol_list, material_list, shrink_list, status_list, special_material, design_list):
    result = []
    if "접착물" in design_list:
        if "프린트" in design_list or "페인트" in design_list:
            if "레이스" in design_list or "시스루" in design_list or "올풀림" in design_list:
                result.append("세탁망")
            else:
                result.append("뒤집어서")
        elif "큐빅" in design_list or "비즈" in design_list or "메탈" in design_list or "패치" in design_list:
            if "레이스" in design_list or "시스루" in design_list or "올풀림" in design_list:
                result.append("세탁망")
            else:
                result.append("세탁망/보호캡")
        elif "반짝이" in design_list:
            if "레이스" in design_list or "시스루" in design_list or "올풀림" in design_list:
                result.append("세탁망")
            else:
                result.append("세탁망/뒤집어서")
    elif "부착물" in design_list:
        if "큐빅" in design_list or "비즈" in design_list or "메탈" in design_list or "패치" in design_list:
            if "레이스" in design_list or "시스루" in design_list or "올풀림" in design_list:
                result.append("세탁망")
            else:
                result.append("뒤집어서")
        else:
            if "레이스" in design_list or "시스루" in design_list or "올풀림" in design_list:
                result.append("세탁망")
            else:
                result.append("세탁망/보호캡")
    else:
        if "레이스" in design_list or "시스루" in design_list or "올풀림" in design_list:
            result.append("세탁망")
        else:
            result.append("없음")

    return result


level1_result = level1_2(special_clothes, symbol_list, material_list)
# print(level1_result)
level3_result = level3(level1_result, symbol_list, material_list, shrink_list, status_list, special_material)
# print(level3_result)
level4_result = level4(level3_result, symbol_list, material_list, shrink_list, status_list, special_material)
# print(level4_result)
level5_result = level5(level3_result, symbol_list, material_list, shrink_list, status_list, special_material,stain_list)
# print(level5_result)
level6_result = level6(level4_result, symbol_list, material_list, shrink_list, status_list, special_material,design_list)
# print(level6_result)

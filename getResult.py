

#0150741271
#소재 (단일소재, 혼합소재)
material_list = []
#세탁부호 (물세탁 드라이)
symbol = []
#얼룩 (수용성 지용성)
stain = []
#오염범위 (국부)
stain_area = []

#염색/이염 : 원색계열, 흰색+a 타입, 인디고염료, 다색조합
#탈색 : 탈색
#손상 : 시스루, 레이스, 시어서커, 플리츠, 트위드, 스티치, 올풀림 디자인,
#수축 : 코듀로이(골덴), 벨벳, 기모
#찌든때 : 찌든때
caution = []

#악세사리
#큐빅,프린트,페인트비즈,인조가죽패치,메탈류,지퍼/심,큐빅단추
#접착물,부착물
accessories = []
#특수기능
#충전재, 발수코팅, 아웃도어
special = []
#색상 #검정,#흰색,#빨강
color = []
#세탁법 결과
result = []

def getFirst(result,material_list, symbol, stain, stain_area,caution,accessories,special,color):
    if len(material_list) == 1: #단일소재
        if material_list[0] == "면":
            if symbol[0] == "물세탁": #물세탁
                if stain[0] == "수용성": #수용성
                    if stain_area[0] == "국부":
                        result.append("전처리")
                        result.append("물세탁")
                    elif stain_area[0] == "광범위":
                        result.append("물세탁")
                elif stain[0] == "지용성": #지용성
                    if stain_area[0] == "국부":
                        result.append("전처리")
                        result.append("물세탁")
                    elif stain_area[0] == "광범위":
                        result.append("드라이1")
                else: #얼룩 없음
                    result.append("물세탁")
            else: #드라이
                if stain[0] == "수용성":  # 수용성
                    if stain_area[0] == "국부":
                        result.append("전처리")
                        result.append("드라이1")
                    elif stain_area[0] == "광범위":
                        result.append("드라이1")
                elif stain[0] == "지용성":  # 지용성
                    if stain_area[0] == "국부":
                        result.append("전처리")
                        result.append("드라이1")
                    elif stain_area[0] == "광범위":
                        result.append("드라이1")
                else:  # 얼룩 없음
                    result.append("드라이1")

        elif material_list[0] == "폴리에스터" or material_list[0] == "나일론":
            if symbol[0] == "물세탁":  # 물세탁
                if stain[0] == "수용성":  # 수용성
                    if stain_area[0] == "국부":
                        result.append("물세탁")
                    elif stain_area[0] == "광범위":
                        result.append("전처리")
                        result.append("물세탁")
                elif stain[0] == "지용성":  # 지용성
                    result.append("전처리")
                    result.append("물세탁")
                else:  # 얼룩 없음
                    result.append("물세탁")
            else:  # 드라이
                if stain[0] == "수용성":  # 수용성
                    if stain_area[0] == "국부":
                        result.append("전처리")
                        result.append("드라이1")
                    elif stain_area[0] == "광범위":
                        result.append("전처리")
                        result.append("물세탁")
                elif stain[0] == "지용성":  # 지용성
                    result.append("드라이1")
                else:  # 얼룩 없음
                    result.append("드라이1")

        elif material_list[0] == "레이온" or material_list[0] == "아크릴" or material_list[0] == "마":
            if symbol[0] == "드라이":  # 물세탁
                if stain[0] == "수용성":  # 수용성
                    if stain_area[0] == "국부":
                        result.append("전처리")
                        result.append("드라이2")
                    elif stain_area[0] == "광범위":
                        result.append("손세탁/약한세탁")
                elif stain[0] == "지용성":  # 지용성
                    result.append("드라이2")
                else:  # 얼룩 없음
                    result.append("드라이2")
            else:  # 드라이
                if stain_area[0] == "국부":
                    result.append("전처리")
                    result.append("드라이2")
                else:
                    result.append("손세탁/약한세탁")

        elif material_list[0] == "울" or material_list[0] == "견":

            result.append("드라이3")

        elif material_list[0] == "폴리우레탄":
            result.append("단독세탁")
            result.append("손세탁/약한세탁")
            result.append("자연건조")
            result.append("끝")

        elif material_list[0] == "인조가죽":
            result.append("다벌세탁")
            result.append("손세탁/약한세탁")
            result.append("자연건조")
            result.append("끝")
        elif material_list[0] == "천연가죽":
            result.append("전문점")
            result.append("끝")

    else: #복합소재
        if "울" in material_list or "견" in material_list:
            result.append("드라이3")

        elif "레이온" in material_list or "마" in material_list or "아크릴" in material_list:
            if symbol[0] == "드라이":  # 물세탁
                if stain[0] == "수용성":  # 수용성
                    if stain_area[0] == "국부":
                        result.append("전처리")
                        result.append("드라이2")
                    elif stain_area[0] == "광범위":
                        result.append("손세탁/약한세탁")
                elif stain[0] == "지용성":  # 지용성
                    result.append("드라이2")
                else:  # 얼룩 없음
                    result.append("드라이2")
            else:  # 드라이
                if stain_area[0] == "국부":
                    result.append("전처리")
                    result.append("드라이2")
                # elif stain_area[0] == "광범위":
                #     result.append("손세탁/약한세탁")
                else:
                    result.append("손세탁/약한세탁")
        elif "폴리에스터" in material_list or "나일론" in material_list or "폴리우레탄" in material_list:
            if symbol[0] == "물세탁":  # 물세탁
                if stain[0] == "수용성":  # 수용성
                    if stain_area[0] == "국부":
                        result.append("물세탁")
                    elif stain_area[0] == "광범위":
                        result.append("전처리")
                        result.append("물세탁")
                elif stain[0] == "지용성":  # 지용성
                    result.append("전처리")
                    result.append("물세탁")
                else:  # 얼룩 없음
                    result.append("물세탁")
            else:  # 드라이
                if stain[0] == "수용성":  # 수용성
                    if stain_area[0] == "국부":
                        result.append("전처리")
                        result.append("드라이1")
                    elif stain_area[0] == "광범위":
                        result.append("전처리")
                        result.append("물세탁")
                elif stain[0] == "지용성":  # 지용성
                    result.append("드라이1")
                else:  # 얼룩 없음
                    result.append("드라이1")
    return result

def getSecond(result,material_list, symbol, stain, stain_area,caution,accessories,special,color):
    new_result = []
    if "끝" in result:
        new_result = result[:-1]
    #드라이1
    elif "드라이1" in result:
        if "원색계열" in caution or "흰색+a" in caution or "인디고염료" in caution or "다색조합" in caution or "탈색" in caution:
            if "큐빅" in accessories or "프린트" in accessories or "페인트비즈" in accessories or "인조가죽패치" in accessories or "메탈류" in accessories or "지퍼/심" in accessories or "큐빅단추" in accessories:
                if "접착물" in accessories:
                    if "충전재" in special:
                        new_result.append("단독세탁")
                        new_result.append("의류뒤집기")
                        new_result.append("약한세탁")
                        new_result.append("반건조&송풍건조")
                    elif "발수코팅" in accessories:
                        new_result.append("단독세탁")
                        new_result.append("의류뒤집기")
                        new_result.append("약한세탁")
                        new_result.append("송풍건조&자연건조")
                    else:
                        new_result.append("단독세탁")
                        new_result.append("의류뒤집기")
                        new_result.append("약한세탁")
                        new_result.append("송풍건조&자연건조")
                elif "부착물" in accessories:
                    if "충전재" in special:
                        new_result.append("단독세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("약한세탁")
                        new_result.append("반건조&송풍건조")
                    elif "발수코팅" in accessories:
                        new_result.append("단독세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("약한세탁")
                        new_result.append("송풍건조&송풍건조")
                    else:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망")
                        new_result.append("드라이")
                        new_result.append("일반건조")
            else:
                if "충전재" in special:
                    new_result.append("단독세탁")
                    new_result.append("세탁망/보호구")
                    new_result.append("약한세탁")
                    new_result.append("반건조&송풍건조")
                elif "발수코팅" in accessories:
                    new_result.append("단독세탁")
                    new_result.append("세탁망/보호구")
                    new_result.append("약한세탁")
                    new_result.append("송풍건조&송풍건조")
                else:
                    new_result.append("다벌세탁")
                    new_result.append("세탁망")
                    new_result.append("드라이")
                    new_result.append("일반건조")
        elif "시스루" in caution or "레이스" in caution or "시어서커" in caution or "플리츠" in caution or "트위드" in caution or "스티치" in caution or "올풀림" in caution or "코듀로이" in caution or "벨벳" in caution or "기모" in caution:
            if "큐빅" in accessories or "프린트" in accessories or "페인트비즈" in accessories or "인조가죽패치" in accessories or "메탈류" in accessories or "지퍼/심" in accessories or "큐빅단추" in accessories:
                if "접착물" in accessories:
                    if "충전재" in special:
                        new_result.append("다벌세탁")
                        new_result.append("의류뒤집기")
                        new_result.append("손세탁")
                        new_result.append("반건조&송풍건조")
                    elif "발수코팅" in accessories:
                        new_result.append("다벌세탁")
                        new_result.append("의류 뒤집기")
                        new_result.append("손세탁")
                        new_result.append("송풍건조&자연건조")
                    else:
                        new_result.append("다벌세탁")
                        new_result.append("의류뒤집기")
                        new_result.append("손세탁")
                        new_result.append("송풍건조&자연건조")
                elif "부착물" in accessories:
                    if "충전재" in special:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("손세탁")
                        new_result.append("반건조&송풍건조")
                    elif "발수코팅" in accessories:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("손세탁")
                        new_result.append("송풍건조&송풍건조")
                    else:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망")
                        new_result.append("드라이")
                        new_result.append("일반건조")
                else:
                    if "충전재" in special:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("손세탁")
                        new_result.append("반건조&송풍건조")
                    elif "발수코팅" in accessories:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("손세탁")
                        new_result.append("송풍건조&송풍건조")
                    else:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망")
                        new_result.append("드라이")
                        new_result.append("일반건조")
            else:
                if "충전재" in special:
                    new_result.append("다벌세탁")
                    new_result.append("세탁망/보호구")
                    new_result.append("손세탁")
                    new_result.append("반건조&송풍건조")
                elif "발수코팅" in accessories:
                    new_result.append("다벌세탁")
                    new_result.append("세탁망/보호구")
                    new_result.append("손세탁")
                    new_result.append("송풍건조&송풍건조")
                else:
                    new_result.append("다벌세탁")
                    new_result.append("세탁망")
                    new_result.append("드라이")
                    new_result.append("일반건조")
        elif "찌든때" in caution:
            new_result.append("다벌세탁")
            new_result.append("담금세탁")
            new_result.append("송풍건조&자연건조")
        else:
            new_result.append("다벌세탁")
            new_result.append("드라이")
            new_result.append("일반건조")
    #물세탁
    elif "물세탁" in result:
        #이염탈색
        if "원색계열" in caution or "흰색+a" in caution or "인디고염료" in caution or "다색조합" in caution or "탈색" in caution:
            #악세사리
            if "큐빅" in accessories or "프린트" in accessories or "페인트비즈" in accessories or "인조가죽패치" in accessories or "메탈류" in accessories or "지퍼/심" in accessories or "큐빅단추" in accessories:
                if "접착물" in accessories:
                    if "충전재" in special:
                        new_result.append("단독세탁")
                        new_result.append("의류뒤집기")
                        new_result.append("약한세탁")
                        new_result.append("반건조&송풍건조")
                    elif "발수코팅" in accessories:
                        new_result.append("단독세탁")
                        new_result.append("의류뒤집기")
                        new_result.append("약한세탁")
                        new_result.append("송풍건조&자연건조")
                    else:
                        new_result.append("단독세탁")
                        new_result.append("의류뒤집기")
                        new_result.append("약한세탁")
                        new_result.append("송풍건조&자연건조")
                elif "부착물" in accessories:
                    if "충전재" in special:
                        new_result.append("단독세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("약한세탁")
                        new_result.append("반건조&송풍건조")
                    elif "발수코팅" in accessories:
                        new_result.append("단독세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("약한세탁")
                        new_result.append("송풍건조&자연건조")
                    else:
                        new_result.append("단독세탁")
                        new_result.append("약한세탁")
                        new_result.append("송풍건조&자연건조")
                else:
                    if "충전재" in special:
                        new_result.append("단독세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("약한세탁")
                        new_result.append("반건조&송풍건조")
                    elif "발수코팅" in accessories:
                        new_result.append("단독세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("약한세탁")
                        new_result.append("송풍건조&자연건조")
                    else:
                        new_result.append("단독세탁")
                        new_result.append("약한세탁")
                        new_result.append("송풍건조&자연건조")
            else:
                if "충전재" in special:
                    new_result.append("단독세탁")
                    new_result.append("세탁망/보호구")
                    new_result.append("약한세탁")
                    new_result.append("반건조&송풍건조")
                elif "발수코팅" in accessories:
                    new_result.append("단독세탁")
                    new_result.append("세탁망/보호구")
                    new_result.append("약한세탁")
                    new_result.append("송풍건조&자연건조")
                else:
                    new_result.append("단독세탁")
                    new_result.append("약한세탁")
                    new_result.append("송풍건조&자연건조")
        #손상/수축
        elif "시스루" in caution or "레이스" in caution or "시어서커" in caution or "플리츠" in caution or "트위드" in caution or "스티치" in caution or "올풀림" in caution or "코듀로이" in caution or "벨벳" in caution or "기모" in caution:
            if "큐빅" in accessories or "프린트" in accessories or "페인트비즈" in accessories or "인조가죽패치" in accessories or "메탈류" in accessories or "지퍼/심" in accessories or "큐빅단추" in accessories:
                if "접착물" in accessories:
                    if "충전재" in special:
                        new_result.append("다벌세탁")
                        new_result.append("의류뒤집기")
                        new_result.append("손세탁")
                        new_result.append("반건조")
                    elif "발수코팅" in accessories:
                        new_result.append("다벌세탁")
                        new_result.append("의류뒤집기")
                        new_result.append("손세탁")
                        new_result.append("송풍건조&자연건조")
                    else:
                        new_result.append("다벌세탁")
                        new_result.append("의류뒤집기")
                        new_result.append("손세탁")
                        new_result.append("송풍건조&자연건조")
                elif "부착물" in accessories:
                    if "충전재" in special:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("손세탁")
                        new_result.append("반건조")
                    elif "발수코팅" in accessories:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("손세탁")
                        new_result.append("송풍건조&자연건조")
                    else:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망")
                        new_result.append("손세탁")
                        new_result.append("송풍건조%자연건조")
                else:
                    if "충전재" in special:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("손세탁")
                        new_result.append("반건조")
                    elif "발수코팅" in accessories:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("손세탁")
                        new_result.append("송풍건조&자연건조")
                    else:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망")
                        new_result.append("손세탁")
                        new_result.append("송풍건조%자연건조")
            else:
                if "충전재" in special:
                    new_result.append("다벌세탁")
                    new_result.append("세탁망/보호구")
                    new_result.append("손세탁")
                    new_result.append("반건조")
                elif "발수코팅" in accessories:
                    new_result.append("다벌세탁")
                    new_result.append("세탁망/보호구")
                    new_result.append("손세탁")
                    new_result.append("송풍건조&자연건조")
                else:
                    new_result.append("다벌세탁")
                    new_result.append("세탁망")
                    new_result.append("손세탁")
                    new_result.append("송풍건조%자연건조")
        elif "찌든때" in caution:
            new_result.append("다벌세탁")
            new_result.append("담금세탁")
            new_result.append("송풍건조&자연건조")
        else:
            new_result.append("다벌세탁")
            new_result.append("일반세탁")
            new_result.append("일반건조")
    #드라이2
    elif "드라이2" in result:
        # 이염탈색
        if "원색계열" in caution or "흰색+a" in caution or "인디고염료" in caution or "다색조합" in caution or "탈색" in caution:
            # 악세사리
            if "큐빅" in accessories or "프린트" in accessories or "페인트비즈" in accessories or "인조가죽패치" in accessories or "메탈류" in accessories or "지퍼/심" in accessories or "큐빅단추" in accessories:
                if "접착물" in accessories:
                    if "충전재" in special:
                        new_result.append("다벌세탁")
                        new_result.append("의류뒤집기")
                        new_result.append("드라이")
                        new_result.append("송풍건조&자연건조")
                    elif "발수코팅" in accessories:
                        new_result.append("단독세탁")
                        new_result.append("의류뒤집기")
                        new_result.append("약한세탁")
                        new_result.append("송풍건조&자연건조")
                    else:
                        new_result.append("다벌세탁")
                        new_result.append("의류뒤집기")
                        new_result.append("드라이")
                        new_result.append("송풍건조&자연건조")
                elif "부착물" in accessories:
                    if "충전재" in special:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("드라이")
                        new_result.append("일반건조")
                    elif "발수코팅" in accessories:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("약한세탁")
                        new_result.append("송풍건조&자연건조")
                    else:
                        new_result.append("다벌세탁")
                        new_result.append("드라이")
                        new_result.append("일반건조")
                else:
                    if "충전재" in special:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("드라이")
                        new_result.append("일반건조")
                    elif "발수코팅" in accessories:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("약한세탁")
                        new_result.append("송풍건조&자연건조")
                    else:
                        new_result.append("다벌세탁")
                        new_result.append("드라이")
                        new_result.append("일반건조")
            else:
                if "충전재" in special:
                    new_result.append("다벌세탁")
                    new_result.append("세탁망/보호구")
                    new_result.append("드라이")
                    new_result.append("일반건조")
                elif "발수코팅" in accessories:
                    new_result.append("다벌세탁")
                    new_result.append("세탁망/보호구")
                    new_result.append("약한세탁")
                    new_result.append("송풍건조&자연건조")
                else:
                    new_result.append("다벌세탁")
                    new_result.append("드라이")
                    new_result.append("일반건조")
        # 손상/수축
        elif "시스루" in caution or "레이스" in caution or "시어서커" in caution or "플리츠" in caution or "트위드" in caution or "스티치" in caution or "올풀림" in caution or "코듀로이" in caution or "벨벳" in caution or "기모" in caution:
            if "큐빅" in accessories or "프린트" in accessories or "페인트비즈" in accessories or "인조가죽패치" in accessories or "메탈류" in accessories or "지퍼/심" in accessories or "큐빅단추" in accessories:
                if "접착물" in accessories:
                    if "충전재" in special:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("드라이")
                        new_result.append("송풍건조&자연건조")
                    elif "발수코팅" in accessories:
                        new_result.append("다벌세탁")
                        new_result.append("의류뒤집기")
                        new_result.append("손세탁")
                        new_result.append("송풍건조&자연건조")
                    else:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("드라이")
                        new_result.append("송풍건조&자연건조")
                elif "부착물" in accessories:
                    if "충전재" in special:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("드라이")
                        new_result.append("일반건조")
                    elif "발수코팅" in accessories:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("손세탁")
                        new_result.append("송풍건조&자연건조")
                    else:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("드라이")
                        new_result.append("일반건조")
                else:
                    if "충전재" in special:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("드라이")
                        new_result.append("일반건조")
                    elif "발수코팅" in accessories:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("손세탁")
                        new_result.append("송풍건조&자연건조")
                    else:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("드라이")
                        new_result.append("일반건조")
            else:
                if "충전재" in special:
                    new_result.append("다벌세탁")
                    new_result.append("세탁망/보호구")
                    new_result.append("드라이")
                    new_result.append("일반건조")
                elif "발수코팅" in accessories:
                    new_result.append("다벌세탁")
                    new_result.append("세탁망/보호구")
                    new_result.append("손세탁")
                    new_result.append("송풍건조&자연건조")
                else:
                    new_result.append("다벌세탁")
                    new_result.append("세탁망/보호구")
                    new_result.append("드라이")
                    new_result.append("일반건조")
        else:
            new_result.append("다벌세탁")
            new_result.append("드라이")
            new_result.append("일반건조")
    #손세탁/약한세탁
    elif "손세탁/약한세탁" in result:
        # 이염탈색
        if "원색계열" in caution or "흰색+a" in caution or "인디고염료" in caution or "다색조합" in caution or "탈색" in caution:
            # 악세사리
            if "큐빅" in accessories or "프린트" in accessories or "페인트비즈" in accessories or "인조가죽패치" in accessories or "메탈류" in accessories or "지퍼/심" in accessories or "큐빅단추" in accessories:
                if "접착물" in accessories:
                    if "충전재" in special:
                        new_result.append("단독세탁")
                        new_result.append("의류뒤집기")
                        new_result.append("약한세탁")
                        new_result.append("송풍건조&자연건조")
                    elif "발수코팅" in accessories:
                        new_result.append("단독세탁")
                        new_result.append("의류뒤집기")
                        new_result.append("약한세탁")
                        new_result.append("송풍건조&자연건조")
                    else:
                        new_result.append("단독세탁")
                        new_result.append("의류뒤집기")
                        new_result.append("드라이")
                        new_result.append("송풍건조&자연건조")
                elif "부착물" in accessories:
                    if "충전재" in special:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("약한세탁")
                        new_result.append("일반건조")
                    elif "발수코팅" in accessories:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("약한세탁")
                        new_result.append("송풍건조&자연건조")
                    else:
                        new_result.append("다벌세탁")
                        new_result.append("드라이")
                        new_result.append("일반건조")
                else:
                    if "충전재" in special:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("약한세탁")
                        new_result.append("일반건조")
                    elif "발수코팅" in accessories:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("약한세탁")
                        new_result.append("송풍건조&자연건조")
                    else:
                        new_result.append("다벌세탁")
                        new_result.append("드라이")
                        new_result.append("일반건조")
            else:
                if "충전재" in special:
                    new_result.append("다벌세탁")
                    new_result.append("세탁망/보호구")
                    new_result.append("약한세탁")
                    new_result.append("일반건조")
                elif "발수코팅" in accessories:
                    new_result.append("다벌세탁")
                    new_result.append("세탁망/보호구")
                    new_result.append("약한세탁")
                    new_result.append("송풍건조&자연건조")
                else:
                    new_result.append("다벌세탁")
                    new_result.append("드라이")
                    new_result.append("일반건조")
        # 손상/수축
        elif "시스루" in caution or "레이스" in caution or "시어서커" in caution or "플리츠" in caution or "트위드" in caution or "스티치" in caution or "올풀림" in caution or "코듀로이" in caution or "벨벳" in caution or "기모" in caution:
            if "큐빅" in accessories or "프린트" in accessories or "페인트비즈" in accessories or "인조가죽패치" in accessories or "메탈류" in accessories or "지퍼/심" in accessories or "큐빅단추" in accessories:
                if "접착물" in accessories:
                    if "충전재" in special:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("드라이")
                        new_result.append("송풍건조&자연건조")
                    elif "발수코팅" in accessories:
                        new_result.append("다벌세탁")
                        new_result.append("의류뒤집기")
                        new_result.append("약한세탁")
                        new_result.append("송풍건조&자연건조")
                    else:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("드라이")
                        new_result.append("송풍건조&자연건조")
                elif "부착물" in accessories:
                    if "충전재" in special:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("드라이")
                        new_result.append("일반건조")
                    elif "발수코팅" in accessories:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("약한세탁")
                        new_result.append("송풍건조&자연건조")
                    else:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("드라이")
                        new_result.append("일반건조")
                else:
                    if "충전재" in special:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("드라이")
                        new_result.append("일반건조")
                    elif "발수코팅" in accessories:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("약한세탁")
                        new_result.append("송풍건조&자연건조")
                    else:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("드라이")
                        new_result.append("일반건조")
            else:
                if "충전재" in special:
                    new_result.append("다벌세탁")
                    new_result.append("세탁망/보호구")
                    new_result.append("드라이")
                    new_result.append("일반건조")
                elif "발수코팅" in accessories:
                    new_result.append("다벌세탁")
                    new_result.append("세탁망/보호구")
                    new_result.append("약한세탁")
                    new_result.append("송풍건조&자연건조")
                else:
                    new_result.append("다벌세탁")
                    new_result.append("세탁망/보호구")
                    new_result.append("드라이")
                    new_result.append("일반건조")
        else:
            new_result.append("다벌세탁")
            new_result.append("드라이")
            new_result.append("일반건조")
    #드라이3
    elif "드라이3" in result:
        # 이염탈색
        if "원색계열" in caution or "흰색+a" in caution or "인디고염료" in caution or "다색조합" in caution or "탈색" in caution:
            # 악세사리
            if "큐빅" in accessories or "프린트" in accessories or "페인트비즈" in accessories or "인조가죽패치" in accessories or "메탈류" in accessories or "지퍼/심" in accessories or "큐빅단추" in accessories:
                if "접착물" in accessories:
                    if "충전재" in special:
                        new_result.append("다벌세탁")
                        new_result.append("의류뒤집기")
                        new_result.append("드라이")
                        new_result.append("송풍건조&자연건조")
                    elif "발수코팅" in accessories:
                        new_result.append("단독세탁")
                        new_result.append("의류뒤집기")
                        new_result.append("약한세탁")
                        new_result.append("송풍건조&자연건조")
                    else:
                        new_result.append("다벌세탁")
                        new_result.append("의류뒤집기")
                        new_result.append("드라이")
                        new_result.append("송풍건조&자연건조")
                elif "부착물" in accessories:
                    if "충전재" in special:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("드라이")
                        new_result.append("일반건조")
                    elif "발수코팅" in accessories:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("약한세탁")
                        new_result.append("송풍건조&자연건조")
                    else:
                        new_result.append("다벌세탁")
                        new_result.append("드라이")
                        new_result.append("일반건조")
                else:
                    if "충전재" in special:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("드라이")
                        new_result.append("일반건조")
                    elif "발수코팅" in accessories:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("약한세탁")
                        new_result.append("송풍건조&자연건조")
                    else:
                        new_result.append("다벌세탁")
                        new_result.append("드라이")
                        new_result.append("일반건조")
            else:
                if "충전재" in special:
                    new_result.append("다벌세탁")
                    new_result.append("세탁망/보호구")
                    new_result.append("드라이")
                    new_result.append("일반건조")
                elif "발수코팅" in accessories:
                    new_result.append("다벌세탁")
                    new_result.append("세탁망/보호구")
                    new_result.append("약한세탁")
                    new_result.append("송풍건조&자연건조")
                else:
                    new_result.append("다벌세탁")
                    new_result.append("드라이")
                    new_result.append("일반건조")
        # 손상/수축
        elif "시스루" in caution or "레이스" in caution or "시어서커" in caution or "플리츠" in caution or "트위드" in caution or "스티치" in caution or "올풀림" in caution or "코듀로이" in caution or "벨벳" in caution or "기모" in caution:
            if "큐빅" in accessories or "프린트" in accessories or "페인트비즈" in accessories or "인조가죽패치" in accessories or "메탈류" in accessories or "지퍼/심" in accessories or "큐빅단추" in accessories:
                if "접착물" in accessories:
                    if "충전재" in special:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("드라이")
                        new_result.append("송풍건조&자연건조")
                    elif "발수코팅" in accessories:
                        new_result.append("다벌세탁")
                        new_result.append("의류뒤집기")
                        new_result.append("손세탁")
                        new_result.append("송풍건조&자연건조")
                    else:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("드라이")
                        new_result.append("송풍건조&자연건조")
                elif "부착물" in accessories:
                    if "충전재" in special:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("드라이")
                        new_result.append("일반건조")
                    elif "발수코팅" in accessories:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("손세탁")
                        new_result.append("송풍건조&자연건조")
                    else:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("드라이")
                        new_result.append("일반건조")
                else:
                    if "충전재" in special:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("드라이")
                        new_result.append("일반건조")
                    elif "발수코팅" in accessories:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("손세탁")
                        new_result.append("송풍건조&자연건조")
                    else:
                        new_result.append("다벌세탁")
                        new_result.append("세탁망/보호구")
                        new_result.append("드라이")
                        new_result.append("일반건조")
            else:
                if "충전재" in special:
                    new_result.append("다벌세탁")
                    new_result.append("세탁망/보호구")
                    new_result.append("드라이")
                    new_result.append("일반건조")
                elif "발수코팅" in accessories:
                    new_result.append("다벌세탁")
                    new_result.append("세탁망/보호구")
                    new_result.append("손세탁")
                    new_result.append("송풍건조&자연건조")
                else:
                    new_result.append("다벌세탁")
                    new_result.append("세탁망/보호구")
                    new_result.append("드라이")
                    new_result.append("일반건조")
        else:
            new_result.append("다벌세탁")
            new_result.append("드라이")
            new_result.append("일반건조")
    return new_result

def getColor(result,color):
    if "검정" in color:
        # result[-2] = result[-2]+"_검정"
        result.append("검정")
    elif "흰색" in color:
        # result[-2] = result[-2]+"_흰색"
        result.append("흰색")
    elif "빨강" in color:
        # result[-2] = result[-2]+"_빨강"
        result.append("빨강")
    return result


# first = getFirst()
# second = getSecond(first)
# result = getColor(second)
# print(first)
# print(second)
# print(result)
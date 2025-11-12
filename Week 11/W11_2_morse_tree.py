"""
날짜: 2025-11-12
이름: 박용성
프로그램명: 모스 코드 결정 트리 알고리즘
프로그램 설명: 모스 코드의 인코딩 및 디코딩을 위한 결정 트리 알고리즘
"""

# ==========================================
# - 트리 구성: make_morse_tree()
# - 인코딩: encode(ch)  -> 알파벳 → 모스 코드
# - 디코딩: decode(root, code) -> 모스 코드 → 알파벳
# - 테스트: 입력 문자열을 모스 코드로 변환 후, 다시 디코딩
# ==========================================


# 트리 노드 정의
class TNode:
    def __init__(self, elem, left=None, right=None):
        self.data = elem
        self.left = left
        self.right = right


# (알파벳, 모스코드) 테이블: A(.-) ~ Z(--..)
table = [
    ("A", ".-"),
    ("B", "-..."),
    ("C", "-.-."),
    ("D", "-.."),
    ("E", "."),
    ("F", "..-."),
    ("G", "--."),
    ("H", "...."),
    ("I", ".."),
    ("J", ".---"),
    ("K", "-.-"),
    ("L", ".-.."),
    ("M", "--"),
    ("N", "-."),
    ("O", "---"),
    ("P", ".--."),
    ("Q", "--.-"),
    ("R", ".-."),
    ("S", "..."),
    ("T", "-"),
    ("U", "..-"),
    ("V", "...-"),
    ("W", ".--"),
    ("X", "-..-"),
    ("Y", "-.--"),
    ("Z", "--.."),
]


def make_morse_tree():
    """모스 코드 결정 트리를 구성한다."""
    root = TNode(None, None, None)  # 모스 트리의 루트(비어 있음)
    for tp in table:
        code = tp[1]  # 모스 코드
        node = root
        # 맨 마지막 문자 이전까지 → 좌/우로 이동하며 노드 확보
        for c in code:
            if c == ".":  # '.' 이면 왼쪽으로 이동
                if node.left is None:  # 비었으면 빈 노드 만들기
                    node.left = TNode(None, None, None)
                node = node.left  # 그쪽으로 이동
            elif c == "-":  # '-' 이면 오른쪽으로 이동
                if node.right is None:  # 비었으면 빈 노드 만들기
                    node.right = TNode(None, None, None)
                node = node.right  # 그쪽으로 이동
        node.data = tp[0]  # 코드의 알파벳 저장
    return root


def encode(ch):
    """알파벳 대문자 ch → 모스 코드 문자열로 인코딩."""
    idx = ord(ch) - ord("A")  # 'A'를 0으로 정렬
    if 0 <= idx < len(table):
        return table[idx][1]
    raise ValueError(f"Unsupported char for encode: {ch!r}")


def decode(root, code):
    """모스 코드 문자열 code → 알파벳 한 글자로 디코딩."""
    node = root
    for c in code:
        if c == ".":
            node = node.left
        elif c == "-":
            node = node.right
        else:
            raise ValueError(f"Invalid morse token: {c!r}")
        if node is None:
            raise ValueError(f"Code not found in tree: {code!r}")
    return node.data


# ==========================================
# 테스트 프로그램
# ==========================================
if __name__ == "__main__":
    morseCodeTree = make_morse_tree()

    # 입력을 받아 대문자/알파벳만 사용 (공백·숫자·기타 문자는 무시 또는 오류 처리 가능)
    s = input("입력 문장 : ").strip().upper()
    # 알파벳만 남기고 필터링 (원본 강의 예시와 동일한 단순 버전)
    s = "".join(ch for ch in s if "A" <= ch <= "Z")

    mlist = []
    for ch in s:
        code = encode(ch)
        mlist.append(code)

    print("Morse Code : ", mlist)
    print("Decoding   : ", end="")
    for code in mlist:
        ch = decode(morseCodeTree, code)
        print(ch, end="")
    print()

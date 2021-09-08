from typing import List


def solution(files: List[str]):
    answer = []
    for file in files:
        head, number, tail = '', '', ''
        number_flag = False
        for i, f in enumerate(file):
            if f.isdigit():
                number += f
                number_flag = True
            elif not number_flag:
                head += f
            else:
                tail = file[i:]
                break
        answer.append((head, number, tail))

    answer.sort(key=lambda x: (x[0].lower(), int(x[1])))
    return [''.join(file) for file in answer]


if __name__ == '__main__':
    files_lst = [
        ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF",
         "img2.JPG"],
        ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II",
         "F-14 Tomcat"]
    ]

    for files in files_lst:
        print(solution(files))

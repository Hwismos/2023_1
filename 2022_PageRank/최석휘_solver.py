directory_location = 'C:\\Users\\최석휘\\Desktop\\3-2\\22년_겨울방학_공학연구인턴십\\Assignment\\Assignment#1\\inputs\\'

class FileReader:
    def __init__(self, dir, dm):
        self.f = open(dir, 'r')
        self.document = []
        self.dangling_mode = dm

    def parsing(self):
        while True:
            line = self.f.readline().strip().replace('   ', ',')  # 한 줄씩 읽어서 공백을 ,(comma)로 변환
            self.document.append(line)
            if not line:  # 빈 문자열을 읽으면 break
                break
        self.f.close()
        self.document.pop()  # 마지막 개행 제거
        return self.document

    def check_dangling(self):
        return self.dangling_mode

class FileWriter:
    def __init__(self, dir, dm, pr):
        self.dangling_mode = dm
        self.page_rank = pr
        self.directory = dir

    def write_file(self):
        if self.dangling_mode == 0:  # out_a.txt
            f = open(self.directory + 'out_a.txt', 'w')
            for node, rank in enumerate(self.page_rank):
                f.write(str(node) + ': ' + str(rank) + '\n')
            f.close()
        else:  # out_b.txt
            f = open(self.directory + 'out_b.txt', 'w')
            for node, rank in enumerate(self.page_rank):
                f.write(str(node) + ': ' + str(rank) + '\n')
            f.close()
class PageRank:
    def __init__(self, arg, dm):
        self.argument = arg
        self.dangling_mode = dm
        self.graph = None
        self.node_num = None
        self.initial_node_points = None
        self.previous_node_points = None
        self.updated_node_points = None

    # 그래프 생성
    def make_graph(self):
        node_num = int(self.argument.pop(0))
        graph = [[] for _ in range(node_num)]
        for element in self.argument:
            from_node, to_node = element.split(',')
            graph[int(from_node)].append(int(to_node))
        self.graph = graph
        self.node_num = len(graph)

    # 노드별 랭크 값 초기화
    def initialize_node_points(self):
        initial_node_points = [1 / self.node_num for _ in range(self.node_num)]
        self.initial_node_points = initial_node_points
        self.previous_node_points = self.initial_node_points

    # 랭크 값 1회 업데이트
    def update_node_points(self):
        self.updated_node_points = [0 for _ in range(self.node_num)]
        for node_index in range(self.node_num):
            if len(self.graph[node_index]) == 0:
                self.updated_node_points[node_index] += self.previous_node_points[node_index]
            else:
                share = self.previous_node_points[node_index] / len(self.graph[node_index])
                for each_reference in self.graph[node_index]:
                    self.updated_node_points[each_reference] += share

    # 모든 노드들의 랭크 값들이 수렴할 때까지 반복
    def keep_updating_until_converge(self):
        convergence_value = 0.00001
        while True:
            self.update_node_points()

            if self.dangling_mode == 1:
                for i in range(self.node_num):
                    self.updated_node_points[i] *= 0.85
                for i in range(self.node_num):
                    self.updated_node_points[i] += 0.15 / self.node_num

            for index in range(self.node_num):
                if abs(self.updated_node_points[index] - self.previous_node_points[index]) > convergence_value:
                    break
            else:
                return self.updated_node_points
            self.previous_node_points = self.updated_node_points

import sys

def main():
    # 인자 입력
    if len(sys.argv) != 3:
        sys.exit()
    arg1 = sys.argv[1]
    arg2 = int(sys.argv[2])

    fr = FileReader(directory_location + arg1, arg2)  # 파일 읽기

    # 페이지 랭크 리스트 생성
    pr = PageRank(fr.parsing(), fr.check_dangling())
    pr.make_graph()
    pr.initialize_node_points()
    page_ranks = pr.keep_updating_until_converge()

    # 생성된 페이지 랭크 리스트를 파일에 쓰기
    fw = FileWriter(directory_location, fr.check_dangling(), page_ranks)
    fw.write_file()

if __name__ == "__main__":
    print('Doing...\n')
    main()
    print('\nDone!!!')
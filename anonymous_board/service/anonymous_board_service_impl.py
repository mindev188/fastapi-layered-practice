from anonymous_board.repository.anonymous_board_repository_impl import AnonymousBoardRepositoryImpl
from anonymous_board.service.anonymous_board_service import AnonymousBoardService


# python으로 싱글톤 만드는 패턴
class AnonymousBoardServiceImpl(AnonymousBoardService):
    # python 에는 특이한 문법 구조를 가지고 있음
    # '_' 가 없으면 public
    # '_' 가 1개 있으면 protected
    # '__' 가 2개 있으면 private를 의미한다.
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.anonymous_board_repository = (

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    # 보편적으로 Spring 코드를 작성 할 때 아래와 같은 작업을 많이 한다.
    # 1번째 패턴
    # @Autowired
    # AnonymousBoardService anonymousBoardService;

    # 2번째 패턴
    # @RequiredArgsConstructor
    # final AnonymousBoardService anonymousBoardService;

    # 3번째 패턴
    # 생성자에서 직접 주입
    # 문제 해결 시 항상 final로 의존성을 추가하니까
    # 몇 십개를 추가해도 저항이 없었음.
    # 일종의 경고 신호가 필요함

    def create(self, title: str, content: str):
        return self.anonymous_board_repository.create(title, content)

    def list(self):
        return self.anonymous_board_repository.find_all()

    def get(self, board_id: str):
        read_board = self.anonymous_board_repository.find_by_id(board_id)
        if not read_board:
            raise ValueError("Not Found Board")

        return read_board

class StateManager:
    def __init__(self, start_state: int = 1, final_state: int = 6) -> None:
        self.__state = start_state
        self.__final_state = final_state

    def next_state(self) -> None:
        self.__state += 1

    def is_final_state(self) -> bool:
        return self.__state == self.__final_state
    
    def get_state(self) -> int:
        return self.__state
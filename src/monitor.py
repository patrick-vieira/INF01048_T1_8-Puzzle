from time import perf_counter_ns


class Monitor:
    def __init__(self, explored_nodes: set, frontier_nodes):
        self.start_time = None
        self.end_time = None
        self.expansions = 0

        self.X = explored_nodes
        self.F = frontier_nodes

    def start(self):
        self.start_time = perf_counter_ns()

    def finish(self):
        self.end_time = perf_counter_ns()

    def count(self):
        self.expansions += 1
        # print(self.expansions)

    def get_execution_time_in_seconds(self):
        return (self.end_time - self.start_time) / 1e9

    def get_results(self):
        if self.get_execution_time_in_seconds() > 0.01:
            message = "Execution time: " + str(self.get_execution_time_in_seconds()) + " seconds"
        else:
            message = "Execution time: " + str(self.get_execution_time_in_seconds() * 1000) + " milliseconds"

        message = "#Fronteira: " + str(len(self.F)) + "\n" + message
        message = "#Explorados: " + str(len(self.X)) + "\n" + message

        return "\n" + message

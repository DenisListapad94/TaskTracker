from django.test import TestCase, Client

# from task_tracker.models import TaskQueue
from task_tracker.models import TaskQueue, Task


class Queue:
    FIFO = "FIFO"
    LIFO = "LIFO"
    STRATEGIES = [FIFO, LIFO]

    def __init__(self, strategy):
        if strategy not in self.STRATEGIES:
            raise TypeError
        self.strategy = strategy
        # self.queue = TaskQueue()

    def add(self, value):
        if self.strategy == self.FIFO:
            # self.storage.append(value)
            TaskQueue.objects.create(value=value)

    def pop(self):
        elem = TaskQueue.objects.order_by('id').first()
        if not elem:
            raise NotImplementedError
        if self.strategy == self.FIFO:
            TaskQueue.objects.filter(id=elem.id).delete()

            return elem.value


# TDD

"""
очередь для добавления задач. Это будет класс. 
Стратегии только FIFO и LIFO остальное TypeError
FIFO first in first out
LIFO last in first out
добваить методы добавления в очередь и удалиние из очереди

"""


# class TestStringMethods(unittest.TestCase):
#
#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')
#
#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())
#
#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)

# class TestQueue(TestCase):
#     # def SetUp(self):
#     #     self.q = Queue()
#
#     def setUp(self):
#         strategy = "FIFO"
#         self.q = Queue(strategy)
#     def test_non_real_strategy(self):
#         with self.assertRaises(TypeError):
#             self.q = Queue("FIFA")
#
#     def test_strategy_exist(self):
#         self.assertEqual(self.q.strategy, "FIFO", msg="Проверка существования стратегии FIFO")
#
#     # def test_storage_exist(self):
#     #     self.assertIs(self.q.queue, TaskQueue())
#
#     def test_add_elem_into_queue(self):
#         first_test_number = 5
#         self.q.add(first_test_number)
#         first_elem = self.q.pop()
#         self.assertEqual(first_elem, first_test_number)
#
#     def test_add_elem_multi_elem_into_queue(self):
#         first_test_number = 5
#         second_test_number = 2
#         third_test_number = 3
#         self.q.add(first_test_number)
#         self.q.add(second_test_number)
#         self.q.add(third_test_number)
#         # import pdb;pdb.set_trace()
#         first_elem = self.q.pop()
#         second_elem = self.q.pop()
#         third_elem = self.q.pop()
#         self.assertEqual(first_elem, first_test_number)
#         self.assertEqual(second_elem, second_test_number)
#         self.assertEqual(third_elem, third_test_number)
#
#     def test_add_many_solt_elem_into_queue(self):
#         first_test_number = 5
#         self.q.add(first_test_number)
#         for i in range(10):
#             random_test_number = random.randint(10, 20)
#             self.q.add(random_test_number)
#         first_elem = self.q.pop()
#         self.assertEqual(first_elem, first_test_number)
#
#     def test_empty_storage(self):
#         with self.assertRaises(NotImplementedError):
#             elem = self.q.pop()
#
#     def tearDown(self):
#         del self.q
#
# if __name__ == '__main__':
#     unittest.main()


class TestTask(TestCase):
    def SetUp(self):
        self.client = Client()

    def test_view_task(self):
        self.title = "first_test_task"
        self.description = "first_test_description"

        Task.objects.create(
            title=self.title,
            description=self.description
        )

        url = "/tasks/"

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        tasks = response.context_data["task_list"]

        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].title, self.title)
        self.assertEqual(tasks[0].description, self.description)

    def test_create_task(self):
        self.title = "first_test_task"
        self.description = "first_test_description"

        url = "/tasks/create"

        response = self.client.post(
            url,
            data={
                "title": self.title,
                "description": self.description
            }
        )

        self.assertEqual(response.status_code, 302)

        task = Task.objects.first()

        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, self.title)
        self.assertEqual(task.description, self.description)

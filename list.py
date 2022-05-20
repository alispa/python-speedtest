from time import time

"""
Just run the file in command line
"""

def python_speed_test():
    def _fastest_way_to_create_a_list():
        print()
        print("TESTING - list creating...")
        rang = 10000000
        start_creating_li1 = time()
        lis1 = [i for i in range(rang)]
        end_creating_li1 = time()
        print(f"List 1 created [for loop], with {rang:,} items")
        start_creating_li2 = time()
        lis2 = list(i for i in range(rang))
        end_creating_li2 = time()
        print(f"List 2 created list(for loop), with {rang:,} items")
        start_creating_li00 = time()
        lis00 = [i for i in range(rang)]
        end_creating_li00 = time()
        print(f"List last created, with {rang:,} items")

        print()
        print("RESULTS - list creating ({rang:,} items):")
        time_in_millis = end_creating_li1 - start_creating_li1
        print(f"List 1 [for loop]: {time_in_millis} ms")
        time_in_millis = end_creating_li2 - start_creating_li2
        print(f"List 2 list(for loop): {time_in_millis} ms")
        time_in_millis = end_creating_li00 - start_creating_li00
        print(f"List recheck 1 [for loop]: {time_in_millis} ms")
        print()

        # RESULTS:
        # List 1 [for loop]: 1.6439995765686035 ms
        # List 2 list(for loop): 1.9490056037902832 ms
        # List recheck 1 [for loop]: 1.3829975128173828 ms

    def _fastest_way_to__copy_a_list():
        print()
        print("TESTING - list copying...")
        rang = 100000000
        main_list = [i for i in range(rang)]
        print(f"Mail list created, with {rang:,} items")
        start_copying_li1 = time()
        lis1 = main_list.copy()
        end_copying_li1 = time()
        print(f"List 1 copied .copy(), with {rang:,} items")
        start_creating_li2 = time()
        lis2 = main_list[:]
        end_creating_li2 = time()
        print(f"List 2 copied [:], with {rang:,} items")

        print()
        print("RESULTS - list copying ({rang:,} items):")
        time_in_millis = end_copying_li1 - start_copying_li1
        print(f"List 1 .copy(): {time_in_millis} ms")
        time_in_millis = end_creating_li2 - start_creating_li2
        print(f"List 2 [:]: {time_in_millis} ms")
        print()

        # RESULTS:
        # List 1 .copy(): 4.349000453948975 ms
        # List 2 [:]: 15.618998289108276 ms

    _fastest_way_to_create_a_list()
    _fastest_way_to__copy_a_list()


python_speed_test()
